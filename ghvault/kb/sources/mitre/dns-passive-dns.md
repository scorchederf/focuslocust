---
parsed_by: focuslocust
source: mitre
type: generated
---
# DNS／Passive DNS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1596.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DNS／Passive DNS](../../attack/techniques/T1596.001-dns-passive-dns.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1596.001 |
| name | DNS／Passive DNS |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1596/001 |

## Preserved Source Material

```yaml
created: '2020-10-02T16:57:45.044Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search DNS data for information about victims that can be used during targeting. DNS information
  may include a variety of details, including registered name servers as well as records that outline addressing for a target’s
  subdomains, mail servers, and other hosts.


  Adversaries may search DNS data to gather actionable information. Threat actors can query nameservers for a target organization
  directly, or search through centralized repositories of logged DNS query responses (known as passive DNS).(Citation: DNS
  Dumpster)(Citation: Circl Passive DNS) Adversaries may also seek and target DNS misconfigurations/leaks that reveal information
  about internal networks. Information from these sources may reveal opportunities for other forms of reconnaissance (ex:
  [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)),
  establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise
  Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)
  or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).'
external_references:
- external_id: T1596.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1596/001
- description: CIRCL Computer Incident Response Center. (n.d.). Passive DNS. Retrieved October 20, 2020.
  source_name: Circl Passive DNS
  url: https://www.circl.lu/services/passive-dns/
- description: Hacker Target. (n.d.). DNS Dumpster. Retrieved October 20, 2020.
  source_name: DNS Dumpster
  url: https://dnsdumpster.com/
id: attack-pattern--17fd695c-b88c-455a-a3d1-43b6cb728532
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:48:27.172Z'
name: DNS/Passive DNS
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.0'
```
