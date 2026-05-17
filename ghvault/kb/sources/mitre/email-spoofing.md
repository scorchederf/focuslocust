---
parsed_by: focuslocust
source: mitre
type: generated
---
# Email Spoofing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1684.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Email Spoofing](../../attack/techniques/T1684.002-email-spoofing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1684.002 |
| name | Email Spoofing |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1684/002 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:54:01.539Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may fake, or spoof, a sender’s identity by modifying the value of relevant email headers in order\
  \ to establish contact with victims under false pretenses.(Citation: Proofpoint TA427 April 2024) In addition to actual\
  \ email content, email headers (such as the FROM header, which contains the email address of the sender) may also be modified.\
  \ Email clients display these headers when emails appear in a victim's inbox, which may cause modified emails to appear\
  \ as if they were from the spoofed entity.\n\nEnterprise environments can use Domain-based Message Authentication, Reporting,\
  \ and Conformance (DMARC) as an email authentication protocol that references results of the Sender Policy Framework (SPF)\
  \ and DomainKeys Identified Mail (DKIM) configurations. SPF and DKIM are configured separately in DNS: SPF verifies that\
  \ the sending server is authorized for the domain, while DKIM uses a digital signature to verify email integrity and domain\
  \ authentication. Together, they validate email authenticity and specify how receiving servers should handle authentication\
  \ failures. Without enforced identity authentication, adversaries may compromise the integrity of an authentication check\
  \ with altered headers that would not have otherwise passed.(Citation: Cloudflare DMARC, DKIM, and SPF)(Citation: DMARC-overview)(Citation:\
  \ Proofpoint-DMARC)\n\nAn example of a weak or absent DMARC policy is `v=DMARC1; p=none; fo=1;`. The `p=none`. The `p=none`\
  \ indicates no action should be taken, and therefore no filtering action will take place, even if an email fails authentication\
  \ checks (i.e., SPF and/or DKIM fail). When a DMARC policy indicates no action, the email will still be delivered to the\
  \ victim’s inbox.(Citation: ic3-dprk) \n\nAdversaries have abused weak or absent DMARC policies to circumvent authentication\
  \ checks and conceal social engineering attempts. Adversaries can alter email headers to include legitimate domain names\
  \ with fake usernames or impersonate legitimate users via [Impersonation](https://attack.mitre.org/techniques/T1684/001)\
  \ for [Phishing](https://attack.mitre.org/techniques/T1566). Additionally, adversaries may abuse Microsoft 365’s Direct\
  \ Send functionality to spoof internal users by using internal devices like printers to send emails without authentication.(Citation:\
  \ Barnea DirectSend)"
external_references:
- external_id: T1684.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1684/002
- description: Cloudflare. (n.d.). What are DMARC, DKIM, and SPF?. Retrieved April 8, 2025.
  source_name: Cloudflare DMARC, DKIM, and SPF
  url: https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/
- description: DMARC. (n.d.). Retrieved March 24, 2025.
  source_name: DMARC-overview
  url: https://dmarc.org/overview
- description: FBI, State Department, NSA. (2024, May 2). North Korean Actors Exploit Weak DMARC Security Policies to Mask
    Spearphishing Efforts. Retrieved April 2, 2025.
  source_name: ic3-dprk
  url: https://www.ic3.gov/CSA/2024/240502.pdf
- description: 'Lesnewich, G. et al. (2024, April 16). From Social Engineering to DMARC Abuse: TA427’s Art of Information
    Gathering. Retrieved May 3, 2024.'
  source_name: Proofpoint TA427 April 2024
  url: https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering
- description: Proofpoint. (n.d.). Retrieved March 24, 2025.
  source_name: Proofpoint-DMARC
  url: https://www.proofpoint.com/us/threat-reference/dmarc
- description: Tom Barnea. (2025, September 9). Ongoing Campaign Abuses Microsoft 365’s Direct Send to Deliver Phishing Emails.
    Retrieved September 24, 2025.
  source_name: Barnea DirectSend
  url: https://www.varonis.com/blog/direct-send-exploit
id: attack-pattern--fcf5bccf-be7a-48ff-b7a7-8d6019279301
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-22T15:49:23.425Z'
name: Email Spoofing
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Office Suite
- Windows
x_mitre_version: '1.0'
```
