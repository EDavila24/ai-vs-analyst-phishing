# AI vs. Analyst: Phishing Triage on Real Spam

> I pulled real phishing emails out of my own spam folder, triaged each one as a Tier 1 SOC analyst, then had an AI triage the same evidence blind and graded it against my answers.

**TL;DR:** <!-- One sentence with the numbers. e.g. "The AI got the verdict right on X of Y emails, but was confidently wrong on Z and invented evidence on W." This line is the BSides opener. -->

**Author:** Ethan Davila · [LinkedIn](https://www.linkedin.com/in/ethan-davila-a05579378/) · [GitHub](https://github.com/EDavila24)
**Certifications:** CompTIA Security+ · Google Cybersecurity · TryHackMe SAL1 (in progress)
**Status:** 🟡 In progress

**Related work:** [Dagon Locker ransomware investigation (CTF)](https://github.com/EDavila24/scanned-document-468-dagon-locker-investigation)

---

## Why I did this

<!-- 2-3 sentences, your words. e.g. "SOCs are starting to hand Tier 1 triage to AI. I wanted to see for myself where that works and where an analyst still has to check the work, using the alert type L1s see most: phishing." -->

## Method

1. **Collection:** <!-- N --> suspicious emails from my spam folder, saved as raw `.eml` in `raw/`. Raw files stay local and are never committed (see [`.gitignore`](.gitignore)).
2. **Evidence pack:** [`extract_iocs.py`](extract_iocs.py) pulls headers, the Received chain, defanged URLs, attachment hashes and body text without opening the email. I triage from this, and the AI gets the exact same text (redacted).
3. **My triage:** headers (SPF/DKIM/DMARC, Return-Path, Reply-To), URL and hash reputation (urlscan.io, VirusTotal, AbuseIPDB), social-engineering cues, verdict, MITRE ATT&CK and actions. Case files are in [`cases/`](cases/), built from [`CASE_TEMPLATE.md`](CASE_TEMPLATE.md).
4. **AI run:** fresh chat, browsing and memory off, one fixed prompt ([`PROMPT.md`](PROMPT.md)), first answer only. Model: <!-- name -->, run on <!-- date -->. Raw responses are in [`ai-runs/`](ai-runs/).
5. **Grading:** field-by-field against my case files using [`GRADING.md`](GRADING.md), including whether the AI's confidence matched reality.

## Results

| Case | Lure | My verdict | AI verdict | AI confidence | Grade |
|------|------|------------|------------|---------------|-------|
| PHISH-001 | | | | | |

<!-- Paste the Totals table from GRADING.md here too. -->

## What the AI got wrong (and why it matters)

### 1. <!-- Short title -->
<!-- What the AI said · what the evidence actually shows (quote the header line / screenshot) · what would have happened if an analyst trusted it. -->

### 2.

## How I'd actually use AI on a Tier 1 shift

| Hand it to the AI | Always verify myself |
|-------------------|----------------------|
| <!-- e.g. summarizing the email and pulling IOCs --> | <!-- e.g. anything it claims a header says --> |
| | |

## Limitations

- <!-- N --> emails from one inbox, one model, one date. Results will differ for other models and versions.
- The AI had no enrichment (browsing off). I had urlscan/VirusTotal, so this tests judgment from evidence, not lookup access.
- My own triage is the answer key, so my mistakes would count against the AI.

## Files

| Path | What it is |
|------|------------|
| [`extract_iocs.py`](extract_iocs.py) | Builds the evidence pack from a `.eml` |
| [`CASE_TEMPLATE.md`](CASE_TEMPLATE.md) | My per-email triage checklist |
| [`PROMPT.md`](PROMPT.md) | The fixed AI prompt and run rules |
| [`GRADING.md`](GRADING.md) | Rubric and full scorecard |
| [`cases/`](cases/) | Completed case files and redacted evidence packs |
| [`ai-runs/`](ai-runs/) | Verbatim AI responses |
| [`JOURNAL.md`](JOURNAL.md) | Dated step-by-step log of how I built this |
