---
parsed_by: focuslocust
source: mitre
type: generated
---
# DNS Server

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1584.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DNS Server](../../attack/techniques/T1584.002-dns-server.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1584.002 |
| name | DNS Server |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1584/002 |

## Preserved Source Material

```yaml
created: '2020-10-01T00:54:30.869Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may compromise third-party DNS servers that can be used during targeting. During post-compromise
  activity, adversaries may utilize DNS traffic for various tasks, including for Command and Control (ex: [Application Layer
  Protocol](https://attack.mitre.org/techniques/T1071)). Instead of setting up their own DNS servers, adversaries may compromise
  third-party DNS servers in support of operations.


  By compromising DNS servers, adversaries can alter DNS records. Such control can allow for redirection of an organization''s
  traffic, facilitating Collection and Credential Access efforts for the adversary.(Citation: Talos DNSpionage Nov 2018)(Citation:
  FireEye DNS Hijack 2019)  Additionally, adversaries may leverage such control in conjunction with [Digital Certificates](https://attack.mitre.org/techniques/T1588/004)
  to redirect traffic to adversary-controlled infrastructure, mimicking normal trusted network communications.(Citation: FireEye
  DNS Hijack 2019)(Citation: Crowdstrike DNS Hijack 2019) Alternatively, they may be able to prove ownership of a domain to
  a SaaS service in order to assert control of the service or create a new administrative [Cloud Account](https://attack.mitre.org/techniques/T1136/003).(Citation:
  CyberCX SaaS Domain Hijacking 2025) Adversaries may also be able to silently create subdomains pointed at malicious servers
  without tipping off the actual owner of the DNS server.(Citation: CiscoAngler)(Citation: Proofpoint Domain Shadowing)'
external_references:
- external_id: T1584.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1584/002
- description: 'Hirani, M., Jones, S., Read, B. (2019, January 10). Global DNS Hijacking Campaign: DNS Record Manipulation
    at Scale. Retrieved October 9, 2020.'
  source_name: FireEye DNS Hijack 2019
  url: https://www.fireeye.com/blog/threat-research/2019/01/global-dns-hijacking-campaign-dns-record-manipulation-at-scale.html
- description: Matt Dahl. (2019, January 25). Widespread DNS Hijacking Activity Targets Multiple Sectors. Retrieved February
    14, 2022.
  source_name: Crowdstrike DNS Hijack 2019
  url: https://www.crowdstrike.com/blog/widespread-dns-hijacking-activity-targets-multiple-sectors/
- description: Mercer, W., Rascagneres, P. (2018, November 27). DNSpionage Campaign Targets Middle East. Retrieved October
    9, 2020.
  source_name: Talos DNSpionage Nov 2018
  url: https://blog.talosintelligence.com/2018/11/dnspionage-campaign-targets-middle-east.html
- description: 'Nick Biasini. (2015, March 3). Threat Spotlight: Angler Lurking in the Domain Shadows. Retrieved March 6,
    2017.'
  source_name: CiscoAngler
  url: https://blogs.cisco.com/security/talos/angler-domain-shadowing
- description: 'Proofpoint Staff. (2015, December 15). The shadow knows: Malvertising campaigns use domain shadowing to pull
    in Angler EK. Retrieved October 16, 2020.'
  source_name: Proofpoint Domain Shadowing
  url: https://www.proofpoint.com/us/threat-insight/post/The-Shadow-Knows
- description: Tony Mau. (2025, May 29). Keys to the (SaaS) kingdom. Retrieved May 30, 2025.
  source_name: CyberCX SaaS Domain Hijacking 2025
  url: https://cybercx.com.au/blog/keys-to-the-saas-kingdom/
id: attack-pattern--c2f59d25-87fe-44aa-8f83-e8e59d077bf5
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-10-24T17:49:20.486Z'
name: DNS Server
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Jeremy Galloway
- Menachem Goldstein
- Tony Mau (CyberCX)
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.3'
```
