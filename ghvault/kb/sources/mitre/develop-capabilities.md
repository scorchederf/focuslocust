---
parsed_by: focuslocust
source: mitre
type: generated
---
# Develop Capabilities

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1587` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Develop Capabilities](../../attack/techniques/T1587-develop-capabilities.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1587 |
| name | Develop Capabilities |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1587 |

## Preserved Source Material

```yaml
created: '2020-10-01T01:30:00.877Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may build capabilities that can be used during targeting. Rather than purchasing, freely downloading,
  or stealing capabilities, adversaries may develop their own capabilities in-house. This is the process of identifying development
  requirements and building solutions such as malware, exploits, and self-signed certificates. Adversaries may develop capabilities
  to support their operations throughout numerous phases of the adversary lifecycle.(Citation: Mandiant APT1)(Citation: Kaspersky
  Sofacy)(Citation: Bitdefender StrongPity June 2020)(Citation: Talos Promethium June 2020)


  As with legitimate development efforts, different skill sets may be required for developing capabilities. The skills needed
  may be located in-house, or may need to be contracted out. Use of a contractor may be considered an extension of that adversary''s
  development capabilities, provided the adversary plays a role in shaping requirements and maintains a degree of exclusivity
  to the capability.'
external_references:
- external_id: T1587
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1587
- description: Kaspersky Lab's Global Research and Analysis Team. (2015, December 4). Sofacy APT hits high profile targets
    with updated toolset. Retrieved December 10, 2015.
  source_name: Kaspersky Sofacy
  url: https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/
- description: Kovar, R. (2017, December 11). Tall Tales of Hunting with TLS/SSL Certificates. Retrieved October 16, 2020.
  source_name: Splunk Kovar Certificates 2017
  url: https://www.splunk.com/en_us/blog/security/tall-tales-of-hunting-with-tls-ssl-certificates.html
- description: Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.
  source_name: Mandiant APT1
  url: https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf
- description: Mercer, W. et al. (2020, June 29). PROMETHIUM extends global reach with StrongPity3 APT. Retrieved July 20,
    2020.
  source_name: Talos Promethium June 2020
  url: https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html
- description: Tudorica, R. et al. (2020, June 30). StrongPity APT - Revealing Trojanized Tools, Working Hours and Infrastructure.
    Retrieved July 20, 2020.
  source_name: Bitdefender StrongPity June 2020
  url: https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf
id: attack-pattern--edadea33-549c-4ed1-9783-8f5a5853cbdf
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-10-24T17:49:34.675Z'
name: Develop Capabilities
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.1'
```
