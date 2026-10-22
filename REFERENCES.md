# OSINT & References

Sources I used during triage: tools, standards and documentation. Each entry notes what it is, where I used it, and what it told me.

---

## Standards (RFCs)

### RFC 5322: Internet Message Format
- **Link:** https://www.rfc-editor.org/rfc/rfc5322#section-3.6.4
- **What it is:** The standard that defines how email headers are formatted, including `Message-ID`.
- **What it says about Message-ID (§3.6.4):**
  - A Message-ID **must be globally unique** for each message.
  - Format is `<left-side@right-side>`.
  - It's **recommended** that the right side be a domain identifying the sender's host, and the left side a unique value such as a date/time stamp.
- **Used in:** PHISH-001 (Header analysis → Message-ID)
- **What it told me:** PHISH-001's Message-ID is `<689869637-689869637@689869637.com>`. It's technically valid syntax, but it doesn't follow the RFC's recommended practice. The right side is a number-only domain that has nothing to do with the sender, and the left side is the same number repeated instead of a unique value. That number also appears in the malformed `Date:` header, which suggests it came from a spam tool's template rather than a real mail system.

### RFC 5322: Date field
- **Link:** https://www.rfc-editor.org/rfc/rfc5322#section-3.6.1 (format defined in [§3.3](https://www.rfc-editor.org/rfc/rfc5322#section-3.3))
- **What it says:**
  - Every message **must** have exactly one `Date:` field (§3.6).
  - Its value **must** be a date-time in the defined format, e.g. `Fri, 16 Oct 2026 03:34:54 -0700` (§3.3, §3.6.1).
- **Used in:** PHISH-001 (Header analysis → Message-ID)
- **What it told me:** PHISH-001's Date field is `_smtpDate . 689869637`, an unfilled template placeholder rather than a date. Unlike the Message-ID, this is an actual **violation** of RFC 5322. Real mail systems fill in the date automatically, so a broken placeholder points to bulk spam software. The real send time comes from Gmail's Received stamp: `Fri, 16 Oct 2026 03:34:54 -0700 (PDT)`.

---

## OSINT tools

### AbuseIPDB
- **Link:** https://www.abuseipdb.com
- **What it is:** A community database of IP addresses reported for abuse (spam, hacking, scanning). Shows ISP, usage type, country and report count.
- **Used in:** PHISH-001 (Header analysis → Originating IP)
- **What it told me:** `141.94.53.209` belongs to OVH SAS, a data center/web hosting provider in France, with 0 reports. 0 reports doesn't mean clean, since spammers rotate through fresh IPs.

### VirusTotal
- **Link:** https://www.virustotal.com
- **What it is:** Checks IPs, domains, URLs and file hashes against dozens of security vendors.
- **Used in:** PHISH-001 (Header analysis → Originating IP)
- **What it told me:** <!-- add vendor count, e.g. 0/94 -->

---

## Frameworks

### MITRE ATT&CK: T1566 Phishing
- **Link:** https://attack.mitre.org/techniques/T1566/
- **What it is:** The industry-standard catalog of attacker techniques.
- **Sub-techniques I'm using:**
  - T1566.001 Spearphishing Attachment
  - T1566.002 Spearphishing Link
- **Used in:** All cases (Section 6), and the no-attachments note in `JOURNAL.md`
