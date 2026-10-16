#!/usr/bin/env python3
"""Pull headers, URLs, attachment hashes and body text out of a .eml file
without opening it in a mail client. Nothing is fetched, clicked or executed.

The output is the "evidence pack": I triage from it, and the AI gets the
exact same text, so the comparison is fair.

Usage:
    python3 -I extract_iocs.py raw/PHISH-001.eml > cases/PHISH-001-evidence.txt
"""
import email
import hashlib
import html
import re
import sys
from email import policy

URL_RE = re.compile(r"https?://[^\s\"'<>)\]]+", re.IGNORECASE)
TAG_RE = re.compile(r"<[^>]+>")
STYLE_RE = re.compile(r"<(style|script)\b.*?</\1>", re.IGNORECASE | re.DOTALL)
HEADERS = [
    "From", "Reply-To", "Return-Path", "To", "Subject", "Date", "Message-ID",
    "Authentication-Results", "Received-SPF", "DKIM-Signature", "X-Mailer",
]
BODY_LIMIT = 4000


def defang(url):
    return url.replace("http", "hxxp", 1).replace(".", "[.]")


def decode_text(part):
    payload = part.get_payload(decode=True) or b""
    try:
        return payload.decode(part.get_content_charset() or "utf-8", "replace")
    except LookupError:
        return payload.decode("utf-8", "replace")


def header_values(msg, name):
    """Parsed header values, falling back to the raw text when a header is
    malformed (spammers often send broken Date or From headers on purpose)."""
    try:
        return [str(v) for v in msg.get_all(name, [])]
    except Exception:
        raw = [str(v) for k, v in msg.raw_items() if k.lower() == name.lower()]
        return [f"{v}  [MALFORMED - could not be parsed]" for v in raw]


def main(path):
    with open(path, "rb") as f:
        msg = email.message_from_binary_file(f, policy=policy.default)

    print("## Headers")
    for name in HEADERS:
        for value in header_values(msg, name):
            print(f"{name}: {' '.join(value.split())}")

    print("\n## Received chain (oldest hop first)")
    for i, hop in enumerate(reversed(header_values(msg, "Received")), 1):
        print(f"{i}. {' '.join(str(hop).split())}")

    urls, attachments, plain, rendered = set(), [], "", ""
    for part in msg.walk():
        if part.is_multipart():
            continue
        filename = part.get_filename()
        ctype = part.get_content_type()
        if filename:
            data = part.get_payload(decode=True) or b""
            attachments.append((filename, ctype, len(data), hashlib.sha256(data).hexdigest()))
        elif ctype in ("text/plain", "text/html"):
            text = html.unescape(decode_text(part))
            urls.update(URL_RE.findall(text))
            if ctype == "text/plain" and not plain:
                plain = text
            elif ctype == "text/html" and not rendered:
                rendered = TAG_RE.sub(" ", STYLE_RE.sub(" ", text))

    print("\n## URLs (defanged)")
    for url in sorted(urls) or ["(none)"]:
        print(f"- {defang(url) if url != '(none)' else url}")

    print("\n## Attachments")
    if not attachments:
        print("- (none)")
    for filename, ctype, size, sha256 in attachments:
        print(f"- {filename} | {ctype} | {size} bytes | SHA256 {sha256}")

    body = URL_RE.sub(lambda m: defang(m.group()), " ".join((plain or rendered).split()))
    print(f"\n## Body text (first {BODY_LIMIT} chars)")
    print(body[:BODY_LIMIT] or "(empty)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
