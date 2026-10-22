# Project Journal

A dated, step-by-step log of how I built this project: what I did, what I found, and what tripped me up. Newest entries at the top.

---

## 2026-10-22: Picking back up + journal

**Did**
- Reviewed where the project stands and started this journal so every step is documented in both Obsidian and GitHub.
- PHISH-001: fixed the file name in the safe-handling checklist and marked attachments as N/A.
- PHISH-001: **completed Section 1 (header analysis)**, all 8 rows. Key findings: four unrelated domains in one email (From, Return-Path, HELO, Message-ID), none of them Tractor Supply; SPF passed only for the scammer's own domain; no DKIM or DMARC; sent from a rented OVH server in France; and an unfilled `_smtpDate` template placeholder that points to bulk spam software.
- Started `REFERENCES.md` to cite the OSINT tools and standards (RFC 5322, AbuseIPDB, VirusTotal, MITRE ATT&CK) behind my findings.

**Side note: no attachments in any of my samples**

While checking PHISH-001 for attachments, I realized it didn't have any. Then I noticed none of my 5 samples do. Every one of them is link-based. That turns out to be normal for modern phishing:

- **Gmail already scans attachments hard** and blocks risky file types, so file-based phishing gets caught more often.
- **Scammers can change where a link goes after the email is sent.** The page can look harmless when a scanner checks it and get swapped for the malicious one later.
- **No attachment often points to credential harvesting.** The goal is to get me onto a fake page where I type in a login or card info, and a link is all that takes.

This matters for my MITRE mapping (link-based phishing is T1566.002, attachment-based is T1566.001) and belongs in the README's Limitations section, since my dataset doesn't test how the AI handles malicious files.

**Lesson learned: SPF pass doesn't mean safe**

PHISH-001 showed `spf=pass`, and at first glance that looks like a good sign. It isn't. SPF only checks whether the sending IP is on the guest list of the **Return-Path domain**, not the From domain I see in my inbox. Here, that domain was `rdbroadband.com`, which the scammer appears to control. So the scammer's server passed the scammer's own guest list.

That "pass" proves nothing about Tractor Supply (the brand being impersonated) or the From address. It's easy to see the word "pass" and treat the email as normal, which is exactly why it's dangerous. A rushed analyst or an AI could make that mistake, and I want to watch for it when I grade the AI's answers.

**Takeaway:** authentication results only matter in context. Always check **which domain** passed, and whether that domain has anything to do with who the email claims to be from.

**Lesson learned: reading a Received line (legit vs. phishing)**

A Received line has three parts from two different sources:
- **Name after `from`:** what the sending server *said* it was (HELO greeting). Self-reported, unverified.
- **Name in parentheses:** what the receiving server looked up for that IP (reverse DNS). More trustworthy.
- **IP in brackets:** the IP the receiving server actually saw. Hardest to fake.

Comparing a legit Gmail line to PHISH-001 made the difference obvious:
```
Legit:    from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
PHISH-001: from hardpearl.com (ip209.ip-141-94-53.eu. [141.94.53.209])
```
In the legit one, both names match and belong to the sender. In the phishing one, the server claimed `hardpearl.com`, but reverse DNS shows a generic OVH hosting name built from the IP itself. Neither has anything to do with Tractor Supply.

**Takeaway:** trust what the receiving server wrote over what the sender claimed. A generic hosting name isn't suspicious alone, but a HELO that doesn't match reverse DNS, on rented hosting, from a "brand" email adds up.

**Next**
- PHISH-001: Section 2 (URLs). Strip tracking IDs before any lookup and keep urlscan.io scans private.

---

## 2026-10-16: Evidence packs + first case started

**Did**
- Collected 5 phishing emails from my Gmail spam folder and saved them as raw `.eml` files (kept local in `raw/`, never committed):
  - PHISH-001: fake Tractor Supply "Yeti bundle" prize
  - PHISH-002: Cash App
  - PHISH-003: Cyclops
  - PHISH-004: cloud storage
  - PHISH-005: Geek Squad
- Ran `extract_iocs.py` on each one to build a text evidence pack, so I never have to open the email itself.
- Fixed the extractor to handle malformed headers and skip CSS/script junk in the body text.
- Switched evidence packs from `.txt` to `.md` so they open in Obsidian.
- Started the PHISH-001 case file: filled in the top table and the first safe-handling checks.

**Learned / tripped me up**
- Obsidian only shows `.md` files by default, so the `.txt` evidence files were invisible until I renamed them.
- Working side by side (evidence on the left, case file on the right) makes it much easier to fill in the template.

---

## 2026-10-15: Project setup

**Did**
- Created the repo with the case template, the fixed AI prompt, the grading rubric and the IOC extractor script.
- Added a `.gitignore` so raw emails (which may contain my address and live malware) can never be committed.

**Why**
- SOCs are starting to hand Tier 1 triage to AI. I want to test where that works and where an analyst still has to check the work, using real phishing emails.
