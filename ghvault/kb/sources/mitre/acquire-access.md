---
parsed_by: focuslocust
source: mitre
type: generated
---
# Acquire Access

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1650` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Acquire Access](../../attack/techniques/T1650-acquire-access.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1650 |
| name | Acquire Access |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1650 |

## Preserved Source Material

```yaml
created: '2023-03-10T15:37:21.782Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may purchase or otherwise acquire an existing access to a target system or network. A variety of
  online services and initial access broker networks are available to sell access to previously compromised systems.(Citation:
  Microsoft Ransomware as a Service)(Citation: CrowdStrike Access Brokers)(Citation: Krebs Access Brokers Fortune 500) In
  some cases, adversary groups may form partnerships to share compromised systems with each other.(Citation: CISA Karakurt
  2022)


  Footholds to compromised systems may take a variety of forms, such as access to planted backdoors (e.g., [Web Shell](https://attack.mitre.org/techniques/T1505/003))
  or established access via [External Remote Services](https://attack.mitre.org/techniques/T1133). In some cases, access brokers
  will implant compromised systems with a “load” that can be used to install additional malware for paying customers.(Citation:
  Microsoft Ransomware as a Service)


  By leveraging existing access broker networks rather than developing or obtaining their own initial access capabilities,
  an adversary can potentially reduce the resources required to gain a foothold on a target network and focus their efforts
  on later stages of compromise. Adversaries may prioritize acquiring access to systems that have been determined to lack
  security monitoring or that have high privileges, or systems that belong to organizations in a particular sector.(Citation:
  Microsoft Ransomware as a Service)(Citation: CrowdStrike Access Brokers)


  In some cases, purchasing access to an organization in sectors such as IT contracting, software development, or telecommunications
  may allow an adversary to compromise additional victims via a [Trusted Relationship](https://attack.mitre.org/techniques/T1199),
  [Multi-Factor Authentication Interception](https://attack.mitre.org/techniques/T1111), or even [Supply Chain Compromise](https://attack.mitre.org/techniques/T1195).


  **Note:** while this technique is distinct from other behaviors such as [Purchase Technical Data](https://attack.mitre.org/techniques/T1597/002)
  and [Credentials](https://attack.mitre.org/techniques/T1589/001), they may often be used in conjunction (especially where
  the acquired foothold requires [Valid Accounts](https://attack.mitre.org/techniques/T1078)).'
external_references:
- external_id: T1650
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1650
- description: Brian Krebs. (2012, October 22). Service Sells Access to Fortune 500 Firms. Retrieved March 10, 2023.
  source_name: Krebs Access Brokers Fortune 500
  url: https://krebsonsecurity.com/2012/10/service-sells-access-to-fortune-500-firms/
- description: 'CrowdStrike Intelligence Team. (2022, February 23). Access Brokers: Who Are the Targets, and What Are They
    Worth?. Retrieved March 10, 2023.'
  source_name: CrowdStrike Access Brokers
  url: https://www.crowdstrike.com/blog/access-brokers-targets-and-worth/
- description: Cybersecurity Infrastructure and Defense Agency. (2022, June 2). Karakurt Data Extortion Group. Retrieved March
    10, 2023.
  source_name: CISA Karakurt 2022
  url: https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-152a
- description: 'Microsoft. (2022, May 9). Ransomware as a service: Understanding the cybercrime gig economy and how to protect
    yourself. Retrieved March 10, 2023.'
  source_name: Microsoft Ransomware as a Service
  url: https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/
id: attack-pattern--d21bb61f-08ad-4dc1-b001-81ca6cb79954
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-10-24T17:49:25.997Z'
name: Acquire Access
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Jeremy Kennelly
- Jeffrey Barto
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.0'
```
