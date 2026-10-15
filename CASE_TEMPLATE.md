# PHISH-<!-- 000 -->: <!-- Short title, e.g. "Fake Microsoft 365 password expiry" -->

> Copy this file to `cases/PHISH-00X.md` for each email. Fill it in **before** running the AI on the same email.

| Field | Value |
|-------|-------|
| **Collected from** | <!-- Gmail spam / old account / etc. --> |
| **Date received** | |
| **Raw file** | `raw/PHISH-<!-- 000 -->.eml` (never committed) |
| **Evidence pack** | `cases/PHISH-<!-- 000 -->-evidence.txt` (redacted) |
| **Time I spent triaging** | <!-- minutes, start to verdict --> |

## Safe handling

- [ ] Saved as `.eml` ("Show original" → Download), never opened in a mail client with images on
- [ ] Ran `python3 -I extract_iocs.py raw/PHISH-000.eml` and worked from the output
- [ ] Did **not** click any link or open any attachment
- [ ] Stripped my unique tracking IDs (anything after `?` that looks per-recipient) before any lookup
- [ ] urlscan.io scans set to **Unlisted or Private**, never Public
- [ ] Attachments: looked up the **hash** in VirusTotal, never uploaded the file

## 1. Header analysis

| Check | Value | What it tells me |
|-------|-------|------------------|
| From (display name + address) | | |
| Reply-To | | <!-- Different from From? Classic BEC/scam tell --> |
| Return-Path | | <!-- Matches From domain? --> |
| SPF | <!-- pass / fail / softfail / none --> | |
| DKIM | <!-- pass / fail / none; signing domain d= --> | <!-- Does d= match the From domain? --> |
| DMARC | <!-- pass / fail / none --> | |
| Originating IP (oldest Received hop) | | <!-- AbuseIPDB / VirusTotal result --> |
| Message-ID domain | | <!-- Matches the sender? --> |

## 2. URLs

| # | URL (defanged) | Link text shown to user | urlscan.io | VirusTotal | Verdict |
|---|----------------|-------------------------|------------|------------|---------|
| 1 | | | | | |

## 3. Attachments

| File name | Type | SHA256 | VirusTotal | Verdict |
|-----------|------|--------|------------|---------|
| | | | | |

## 4. Content / social engineering

- [ ] Urgency or threat ("account suspended", "within 24 hours")
- [ ] Brand impersonation: <!-- which brand -->
- [ ] Link text doesn't match the real destination
- [ ] Generic greeting ("Dear user")
- [ ] Asks for credentials, payment, gift cards or a reply
- [ ] Other: <!-- -->

## 5. Verdict

| Field | My answer |
|-------|-----------|
| **Verdict** | <!-- Malicious / Suspicious / Benign (spam) / Benign (legitimate) --> |
| **Confidence** | <!-- High / Medium / Low --> |
| **Type** | <!-- Credential harvest / Malware delivery / BEC-invoice fraud / Scam / Extortion / Marketing spam / Other --> |
| **Impersonated brand/sender** | |
| **Severity** | <!-- Low / Medium / High --> |

**Summary (what my shift lead reads):**
<!-- 2-3 sentences: what it is, how I know, what's at risk. -->

## 6. MITRE ATT&CK

| Technique | Why |
|-----------|-----|
| <!-- T1566.001 Spearphishing Attachment / T1566.002 Spearphishing Link / T1598 Phishing for Information --> | |

## 7. Recommended actions

1. <!-- e.g. Block sender domain + URL at the email gateway -->
2. <!-- e.g. Search for and purge the same message from other mailboxes -->
3. <!-- e.g. If anyone clicked: reset password, revoke sessions, check sign-in logs -->

## 8. Before committing (redaction)

- [ ] My email address, name and any other recipient details replaced with `[REDACTED]`
- [ ] Per-recipient tracking IDs removed from URLs
- [ ] No raw `.eml` or attachment files staged (`git status` is clean of `raw/`)
