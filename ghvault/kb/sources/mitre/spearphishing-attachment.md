---
parsed_by: focuslocust
source: mitre
type: generated
---
# Spearphishing Attachment

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1598.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Spearphishing Attachment](../../attack/techniques/T1598.002-spearphishing-attachment.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1598.002 |
| name | Spearphishing Attachment |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1598/002 |

## Preserved Source Material

```yaml
created: '2020-10-02T17:08:57.386Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may send spearphishing messages with a malicious attachment to elicit sensitive information that
  can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently
  credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques,
  such as posing as a source with a reason to collect information (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585)
  or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)) and/or sending multiple, seemingly urgent messages.


  All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or
  industry. In this scenario, adversaries attach a file to the spearphishing email. In some cases, they may rely upon the
  recipient populating information, then returning the file.(Citation: Sophos Attachment)(Citation: GitHub Phishery) The text
  of the spearphishing email usually tries to give a plausible reason why the file should be filled-in, such as a request
  for information from a business associate. In other cases, adversaries may leverage techniques such as [HTML Smuggling](https://attack.mitre.org/techniques/T1027/006)
  to harvest user credentials via fake login portals.(Citation: Huntress HTML Smuggling 2024)


  Adversaries may also use information from previous reconnaissance efforts (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)
  or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)) to craft persuasive and believable lures.'
external_references:
- external_id: T1598.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1598/002
- description: Australian Cyber Security Centre. (2012, December). Mitigating Spoofed Emails Using Sender Policy Framework.
    Retrieved November 17, 2024.
  source_name: ACSC Email Spoofing
  url: https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf
- description: 'Ducklin, P. (2020, October 2). Serious Security: Phishing without links – when phishers bring along their
    own web pages. Retrieved October 20, 2020.'
  source_name: Sophos Attachment
  url: https://nakedsecurity.sophos.com/2020/10/02/serious-security-phishing-without-links-when-phishers-bring-along-their-own-web-pages/
- description: 'Matt Kiely. (2024, July 5). Smuggler’s Gambit: Uncovering HTML Smuggling Adversary in the Middle Tradecraft.
    Retrieved March 18, 2025.'
  source_name: Huntress HTML Smuggling 2024
  url: https://www.huntress.com/blog/smugglers-gambit-uncovering-html-smuggling-adversary-in-the-middle-tradecraft
- description: Microsoft. (2020, October 13). Anti-spoofing protection in EOP. Retrieved October 19, 2020.
  source_name: Microsoft Anti Spoofing
  url: https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide
- description: Ryan Hanson. (2016, September 24). phishery. Retrieved October 23, 2020.
  source_name: GitHub Phishery
  url: https://github.com/ryhanson/phishery
id: attack-pattern--8982a661-d84c-48c0-b4ec-1db29c6cf3bc
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:49:04.751Z'
name: Spearphishing Attachment
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Philip Winther
- Sebastian Salla, McAfee
- Robert Simmons, @MalwareUtkonos
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.2'
```
