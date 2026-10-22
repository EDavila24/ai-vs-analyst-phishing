# PHISH-001-yeti: Fake Tractor Supply "Yeti bundle" prize

> Copy this file to `cases/PHISH-00X.md` for each email. Fill it in **before** running the AI on the same email.

| Field                     | Value                              |
| ------------------------- | ---------------------------------- |
| **Collected from**        | Gmail spam folder                  |
| **Date received**         | 10/16/26 @  6:34am                 |
| **Raw file**              | raw/PHISH-001-yeti.eml             |
| **Evidence pack**         | cases/PHISH-001-yeti-evidence.md   |
| **Time I spent triaging** | <!-- minutes, start to verdict --> |

## Safe handling

- [x] Saved as `.eml` ("Show original" → Download), never opened in a mail client with images on
- [x] Ran `python3 -I extract_iocs.py raw/PHISH-001-yeti.eml` and worked from the output
- [x] Did **not** click any link or open any attachment
- [ ] Stripped my unique tracking IDs (anything after `?` that looks per-recipient) before any lookup
- [ ] urlscan.io scans set to **Unlisted or Private**, never Public
- [x] Attachments: none in this email (N/A)

## 1. Header analysis

| Check                                | Value                                                                                                                                                                                                                                                                                   | What it tells me                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| From (display name + address)        | Claim-Your Bonus `<laNJBWJE@xQuTjrDxt.us>`                                                                                                                                                                                                                                              | suspicious address with "reward bait" type of title. Display name doesn't look like it correlates with the address (random numbers are red flags) or with "Tractor Supply" mentioned in the body whatsoever                                                                                                                                              |
| Reply-To                             | None                                                                                                                                                                                                                                                                                    | Most emails don't have, so the email will reply to the address on the "From" part. Attacker seems to wants the recipient to interact with the link rather than reply                                                                                                                                                                                     |
| Return-Path                          | `<return4362@131....rdbroadband.com>`                                                                                                                                                                                                                                                   | The return path domain has nothing to do with 'From' Domain or Tractor Supply. Also notice the same IP address that's shown from Auth-Results and Received-SPF (**client-ip=141.94.53.209**)                                                                                                                                                             |
| SPF                                  | spf=pass with domain from (rdbroadband.com) , designates **ip:141.94.53.209** as permitted sender on this domains guest list                                                                                                                                                            | SPF passed BUT was checked against `rdbroadband.com` a domain the scammer seems to control. Proves nothing about Tractor Supply or From address                                                                                                                                                                                                          |
| DKIM                                 | none                                                                                                                                                                                                                                                                                    | Since there's no digital signature this raises more of a red flag since most companies sign basically all their mail to validate that it came from the domain that signed it and wasn't changed along the way.                                                                                                                                           |
| DMARC                                | none                                                                                                                                                                                                                                                                                    | No DMARC check happened, so nothing tied SPF/DKIM to the From domain. That gap lets a scammer/attacker pass SPF on their own domain while showing a different From. Since Real Tractor Supply probably has a DMARC policy that would've blocked it, they only put Tractor Supply in the body text.                                                       |
| Originating IP (oldest Received hop) | IP= 141.94.53.209 (from `hardpearl.com`)<br>Looked up on abuseipdb.com <br>-ISP: OVH SAS<br>-Usage Type: Data Center/Web hosting <br>-Country: France<br>-Times Reported: 0 (doesn't clear it since attackers can rotate IPs)<br>Looked on VirusTotal.com<br>-0 vendors flagged this IP | Rented out hosting server (OVH) in France. This usage type of hosting is popular for spammers. Server "claimed" to be `hardpearl.com` , but the reverse DNS shows a generic OVH hosting name that doesn't match Tractor Supply/claimed name.                                                                                                             |
| Message-ID domain                    | yet a different domain `68986937...@689869637.com` with repeating numbers<br>Also noticed the same numbers within the 'Date' field and 'smtpdate'                                                                                                                                       | Number-only domain that matches none of the other domains (From, Return-Path, and HELO) or Tractor Supply. <br>With the standard (RFC 5322): The value of the domain matching the 'Date', suggest a possible scripted/templated generation. AND the 'smtpdate' looks like a failed placeholder that was suppose to be for the date. (see REFERENCES.md ) |

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
