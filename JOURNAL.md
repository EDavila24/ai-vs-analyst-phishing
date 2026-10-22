# Project Journal

A dated, step-by-step log of how I built this project: what I did, what I found, and what tripped me up. Newest entries at the top.

---

## 2026-10-22: Picking back up + journal

**Did**
- Reviewed where the project stands and started this journal so every step is documented in both Obsidian and GitHub.

**Next**
- PHISH-001: finish the last safe-handling checkboxes, then Section 1 (header analysis).

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
