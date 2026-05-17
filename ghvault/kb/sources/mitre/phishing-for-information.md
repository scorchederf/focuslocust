---
parsed_by: focuslocust
source: mitre
type: generated
---
# Phishing for Information

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1598` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Phishing for Information](../../attack/techniques/T1598-phishing-for-information.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1598 |
| name | Phishing for Information |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1598 |

## Preserved Source Material

```yaml
created: '2020-10-02T17:07:01.502Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may send phishing messages to elicit sensitive information that can be used during targeting. Phishing\
  \ for information is an attempt to trick targets into divulging information, frequently credentials or other actionable\
  \ information. Phishing for information is different from [Phishing](https://attack.mitre.org/techniques/T1566) in that\
  \ the objective is gathering data from the victim rather than executing malicious code.\n\nAll forms of phishing are electronically\
  \ delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual,\
  \ company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing,\
  \ such as in mass credential harvesting campaigns.\n\nAdversaries may also try to obtain information directly through the\
  \ exchange of emails, instant messages, or other electronic conversation means.(Citation: ThreatPost Social Media Phishing)(Citation:\
  \ TrendMictro Phishing)(Citation: PCMag FakeLogin)(Citation: Sophos Attachment)(Citation: GitHub Phishery) Victims may also\
  \ receive phishing messages that direct them to call a phone number where the adversary attempts to collect confidential\
  \ information.(Citation: Avertium callback phishing)\n\nPhishing for information frequently involves social engineering\
  \ techniques, such as posing as a source with a reason to collect information (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585)\
  \ or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)) and/or sending multiple, seemingly urgent messages.\
  \ Another way to accomplish this is by [Email Spoofing](https://attack.mitre.org/techniques/T1684/002)(Citation: Proofpoint-spoof)\
  \ the identity of the sender, which can be used to fool both the human recipient as well as automated security tools.(Citation:\
  \ cyberproof-double-bounce) \n\nPhishing for information may also involve evasive techniques, such as removing or manipulating\
  \ emails or metadata/headers from compromised accounts being abused to send messages (e.g., [Email Hiding Rules](https://attack.mitre.org/techniques/T1564/008)).(Citation:\
  \ Microsoft OAuth Spam 2022)(Citation: Palo Alto Unit 42 VBA Infostealer 2014)"
external_references:
- external_id: T1598
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1598
- description: Avertium. (n.d.). EVERYTHING YOU NEED TO KNOW ABOUT CALLBACK PHISHING. Retrieved February 2, 2023.
  source_name: Avertium callback phishing
  url: https://www.avertium.com/resources/threat-reports/everything-you-need-to-know-about-callback-phishing
- description: Babon, P. (2020, September 3). Tricky 'Forms' of Phishing. Retrieved October 20, 2020.
  source_name: TrendMictro Phishing
  url: https://www.trendmicro.com/en_us/research/20/i/tricky-forms-of-phishing.html
- description: 'Ducklin, P. (2020, October 2). Serious Security: Phishing without links – when phishers bring along their
    own web pages. Retrieved October 20, 2020.'
  source_name: Sophos Attachment
  url: https://nakedsecurity.sophos.com/2020/10/02/serious-security-phishing-without-links-when-phishers-bring-along-their-own-web-pages/
- description: Itkin, Liora. (2022, September 1). Double-bounced attacks with email spoofing . Retrieved February 24, 2023.
  source_name: cyberproof-double-bounce
  url: https://blog.cyberproof.com/blog/double-bounced-attacks-with-email-spoofing-2022-trends
- description: Kan, M. (2019, October 24). Hackers Try to Phish United Nations Staffers With Fake Login Pages. Retrieved October
    20, 2020.
  source_name: PCMag FakeLogin
  url: https://www.pcmag.com/news/hackers-try-to-phish-united-nations-staffers-with-fake-login-pages
- description: Microsoft. (2023, September 22). Malicious OAuth applications abuse cloud email services to spread spam. Retrieved
    March 13, 2023.
  source_name: Microsoft OAuth Spam 2022
  url: https://www.microsoft.com/en-us/security/blog/2022/09/22/malicious-oauth-applications-used-to-compromise-email-servers-and-spread-spam/
- description: 'O''Donnell, L. (2020, October 20). Facebook: A Top Launching Pad For Phishing Attacks. Retrieved October 20,
    2020.'
  source_name: ThreatPost Social Media Phishing
  url: https://threatpost.com/facebook-launching-pad-phishing-attacks/160351/
- description: Proofpoint. (n.d.). What Is Email Spoofing?. Retrieved February 24, 2023.
  source_name: Proofpoint-spoof
  url: https://www.proofpoint.com/us/threat-reference/email-spoofing
- description: Ryan Hanson. (2016, September 24). phishery. Retrieved October 23, 2020.
  source_name: GitHub Phishery
  url: https://github.com/ryhanson/phishery
- description: Vicky Ray and Rob Downs. (2014, October 29). Examining a VBA-Initiated Infostealer Campaign. Retrieved March
    13, 2023.
  source_name: Palo Alto Unit 42 VBA Infostealer 2014
  url: https://unit42.paloaltonetworks.com/examining-vba-initiated-infostealer-campaign/
id: attack-pattern--cca0ccb6-a068-4574-a722-b1556f86833a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2026-04-17T16:15:21.344Z'
name: Phishing for Information
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Philip Winther
- Sebastian Salla, McAfee
- Robert Simmons, @MalwareUtkonos
- Ohad Zaidenberg, @ohad_mz
- Liora Itkin
- Liran Ravich, CardinalOps
- Scott Cook, Capital One
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.4'
```
