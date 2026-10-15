# The AI run: fixed prompt and rules

Every email gets the **same prompt**, in a **fresh chat**, with the **same evidence pack** I triaged from. The test only means something if nothing changes between runs.

## Rules

1. **Triage it myself first.** Finish the case file before the AI sees the email.
2. **Fresh chat each time.** Memory/personalization off, no project or custom instructions, web browsing off. The AI judges only the evidence pack, the way a Tier 1 analyst judges an alert before enrichment.
3. **Paste only the redacted evidence pack** (`cases/PHISH-00X-evidence.txt`). Never my notes or verdict.
4. **First answer only.** No follow-ups, no hints, no "are you sure?". Re-runs go in as separate runs, and I grade each one.
5. **Save the response verbatim** to `ai-runs/PHISH-00X-run1.md`, with the header below.

## Run log header

```
Model:        <!-- e.g. the exact model name shown in the app -->
Date/time:    <!-- -->
Browsing:     off
Memory:       off
Evidence:     cases/PHISH-00X-evidence.txt
Response time: <!-- seconds, roughly -->
```

## The prompt

```
You are a Tier 1 SOC analyst triaging a user-reported suspicious email.
Below is the extracted evidence: headers, the Received chain (oldest hop first),
defanged URLs, attachment metadata, and body text. You cannot browse or look
anything up. Judge only from what is here.

Answer in exactly this format:

1. Verdict: Malicious / Suspicious / Benign (spam) / Benign (legitimate)
2. Confidence: High / Medium / Low
3. Type: Credential harvest / Malware delivery / BEC-invoice fraud / Scam / Extortion / Marketing spam / Other
4. Key evidence: up to 5 bullets, each quoting the exact header line or text you rely on
5. Email authentication: SPF, DKIM and DMARC results, and what they mean for this email
6. Impersonated brand or sender (if any)
7. MITRE ATT&CK technique(s)
8. Recommended SOC actions
9. What you would verify before closing this ticket

EVIDENCE:
<paste the evidence pack here>
```

## Optional round B: AI with enrichment

If I have time, run each email a second time and add my urlscan.io / VirusTotal / AbuseIPDB results under the evidence. Does enrichment fix the AI's misses? That's the "AI plus SOAR enrichment" question in miniature.
