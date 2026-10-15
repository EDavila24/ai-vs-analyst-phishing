# Grading: AI vs. my triage

My completed case file is the answer key. Grade the AI's **first** answer only.

## Labels

| Label | Meaning |
|-------|---------|
| ✅ Correct | Matches my finding, with valid evidence |
| 🟡 Partial | Right direction, but incomplete or imprecise |
| ❌ Wrong | Contradicts what the evidence shows |
| 👻 Hallucinated | Cites a header, value or text that isn't in the evidence pack |
| ⚠️ Right answer, wrong reasoning | Correct conclusion, but the evidence it cites doesn't support it |

## Confidence calibration

| AI confidence | AI was right | AI was wrong |
|---------------|--------------|--------------|
| **High** | Calibrated | **Overconfident** ← the headline finding |
| **Medium / Low** | Under-confident | Appropriately cautious |

## Per-email scorecard

| Case | Verdict | Type | Evidence cited | Auth (SPF/DKIM/DMARC) | Actions | Confidence → calibration | My time | AI time |
|------|---------|------|----------------|-----------------------|---------|--------------------------|---------|---------|
| PHISH-001 | | | | | | | | |
| PHISH-002 | | | | | | | | |
| PHISH-003 | | | | | | | | |
| PHISH-004 | | | | | | | | |
| PHISH-005 | | | | | | | | |

## Totals

| Field | ✅ | 🟡 | ❌ | 👻 | ⚠️ |
|-------|----|----|----|----|----|
| Verdict | | | | | |
| Type | | | | | |
| Evidence cited | | | | | |
| Auth reading | | | | | |
| Actions | | | | | |

**Overconfident answers (High + wrong):** <!-- count -->
**Hallucinated evidence:** <!-- count -->
**Average triage time:** me <!-- min --> vs. AI <!-- sec -->

## Notes on misses

<!-- For each ❌ / 👻 / ⚠️: what the AI said, what the evidence actually shows (quote the line), and why an analyst who trusted it would have made the wrong call. The best 2-3 go in the README. -->
