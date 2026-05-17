---
parsed_by: focuslocust
source: mitre
type: generated
---
# Email Bombing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1667` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Email Bombing](../../attack/techniques/T1667-email-bombing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1667 |
| name | Email Bombing |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1667 |

## Preserved Source Material

```yaml
created: '2025-01-31T14:39:58.478Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may flood targeted email addresses with an overwhelming volume of messages. This may bury legitimate
  emails in a flood of spam and disrupt business operations.(Citation: sophos-bombing)(Citation: krebs-email-bombing)


  An adversary may accomplish email bombing by leveraging an automated bot to register a targeted address for e-mail lists
  that do not validate new signups, such as online newsletters. The result can be a wave of thousands of e-mails that effectively
  overloads the victim’s inbox.(Citation: krebs-email-bombing)(Citation: hhs-email-bombing)


  By sending hundreds or thousands of e-mails in quick succession, adversaries may successfully divert attention away from
  and bury legitimate messages including security alerts, daily business processes like help desk tickets and client correspondence,
  or ongoing scams.(Citation: hhs-email-bombing) This behavior can also be used as a tool of harassment.(Citation: krebs-email-bombing)


  This behavior may be a precursor for [Spearphishing Voice](https://attack.mitre.org/techniques/T1566/004). For example,
  an adversary may email bomb a target and then follow up with a phone call to fraudulently offer assistance. This social
  engineering may lead to the use of [Remote Access Software](https://attack.mitre.org/techniques/T1663) to steal credentials,
  deploy ransomware, conduct [Financial Theft](https://attack.mitre.org/techniques/T1657)(Citation: sophos-bombing), or engage
  in other malicious activity.(Citation: rapid7-email-bombing)

  '
external_references:
- external_id: T1667
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1667
- description: Brian Krebs. (2016, August 18). Massive Email Bombs Target .Gov Addresses. Retrieved January 31, 2025.
  source_name: krebs-email-bombing
  url: https://krebsonsecurity.com/2016/08/massive-email-bombs-target-gov-addresses/
- description: Mark Parsons, Colin Cowie, Daniel Souter, Hunter Neal, Anthony Bradshaw, Sean Gallagher. (2025, January 21).
    Sophos MDR tracks two ransomware campaigns using “email bombing,” Microsoft Teams “vishing”. Retrieved January 31, 2025.
  source_name: sophos-bombing
  url: https://news.sophos.com/en-us/2025/01/21/sophos-mdr-tracks-two-ransomware-campaigns-using-email-bombing-microsoft-teams-vishing/
- description: Tyler McGraw, Thomas Elkins, and Evan McCann. (2024, May 10). Ongoing Social Engineering Campaign Linked to
    Black Basta Ransomware Operators. Retrieved January 31, 2025.
  source_name: rapid7-email-bombing
  url: https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators
- description: U.S. Department of Health and Human Services. (2024, March 12). Defense and Mitigations from E-mail Bombing.
    Retrieved January 31, 2025.
  source_name: hhs-email-bombing
  url: https://www.hhs.gov/sites/default/files/email-bombing-sector-alert-tlpclear.pdf
id: attack-pattern--bed81616-3dde-4685-be6e-ba9820f9a7ed
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2025-04-15T19:59:03.350Z'
name: Email Bombing
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Ryan Perez
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Availability
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- Office Suite
- Windows
- macOS
x_mitre_version: '1.0'
```
