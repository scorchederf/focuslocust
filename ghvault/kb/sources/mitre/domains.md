---
parsed_by: focuslocust
source: mitre
type: generated
---
# Domains

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1584.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Domains](../../attack/techniques/T1584.001-domains.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1584.001 |
| name | Domains |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1584/001 |

## Preserved Source Material

```yaml
created: '2020-10-01T00:51:28.513Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may hijack domains and/or subdomains that can be used during targeting. Domain registration hijacking
  is the act of changing the registration of a domain name without the permission of the original registrant.(Citation: ICANNDomainNameHijacking)
  Adversaries may gain access to an email account for the person listed as the owner of the domain. The adversary can then
  claim that they forgot their password in order to make changes to the domain registration. Other possibilities include social
  engineering a domain registration help desk to gain access to an account, taking advantage of renewal process gaps, or compromising
  a cloud service that enables managing domains (e.g., AWS Route53).(Citation: Krebs DNS Hijack 2019)


  Subdomain hijacking can occur when organizations have DNS entries that point to non-existent or deprovisioned resources.
  In such cases, an adversary may take control of a subdomain to conduct operations with the benefit of the trust associated
  with that domain.(Citation: Microsoft Sub Takeover 2020)


  Adversaries who compromise a domain may also engage in domain shadowing by creating malicious subdomains under their control
  while keeping any existing DNS records. As service will not be disrupted, the malicious subdomains may go unnoticed for
  long periods of time.(Citation: Palo Alto Unit 42 Domain Shadowing 2022)'
external_references:
- external_id: T1584.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1584/001
- description: Brian Krebs. (2019, February 18). A Deep Dive on the Recent Widespread DNS Hijacking Attacks. Retrieved February
    14, 2022.
  source_name: Krebs DNS Hijack 2019
  url: https://krebsonsecurity.com/2019/02/a-deep-dive-on-the-recent-widespread-dns-hijacking-attacks/
- description: 'ICANN Security and Stability Advisory Committee. (2005, July 12). Domain Name Hijacking: Incidents, Threats,
    Risks and Remediation. Retrieved November 17, 2024.'
  source_name: ICANNDomainNameHijacking
  url: https://www.icann.org/en/ssac/registration-services/documents/sac-007-domain-name-hijacking-incidents-threats-risks-and-remediation-12-07-2005-en
- description: 'Janos Szurdi, Rebekah Houser and Daiping Liu. (2022, September 21). Domain Shadowing: A Stealthy Use of DNS
    Compromise for Cybercrime. Retrieved March 7, 2023.'
  source_name: Palo Alto Unit 42 Domain Shadowing 2022
  url: https://unit42.paloaltonetworks.com/domain-shadowing/
- description: Microsoft. (2020, September 29). Prevent dangling DNS entries and avoid subdomain takeover. Retrieved October
    12, 2020.
  source_name: Microsoft Sub Takeover 2020
  url: https://docs.microsoft.com/en-us/azure/security/fundamentals/subdomain-takeover
id: attack-pattern--f9cc4d06-775f-4ee1-b401-4e2cc0da30ba
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-10-24T17:49:38.448Z'
name: Domains
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Jeremy Galloway
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.4'
```
