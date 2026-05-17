---
parsed_by: focuslocust
source: mitre
type: generated
---
# Out-of-Band Communications Channel

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1060` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Out-of-Band Communications Channel](../../attack/mitigations/M1060-out-of-band-communications-channel.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1060 |
| name | Out-of-Band Communications Channel |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1060 |

## Preserved Source Material

```yaml
created: '2024-08-30T13:08:10.349Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Establish secure out-of-band communication channels to ensure the continuity of critical communications during
  security incidents, data integrity attacks, or in-network communication failures. Out-of-band communication refers to using
  an alternative, separate communication path that is not dependent on the potentially compromised primary network infrastructure.
  This method can include secure messaging apps, encrypted phone lines, satellite communications, or dedicated emergency communication
  systems. Leveraging these alternative channels reduces the risk of adversaries intercepting, disrupting, or tampering with
  sensitive communications and helps coordinate an effective incident response.(Citation: TrustedSec OOB Communications)(Citation:
  NIST Special Publication 800-53 Revision 5)'
external_references:
- external_id: M1060
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1060
- description: National Institute of Standards and Technology. (2020, September). Security and Privacy Controlsfor Information
    Systems and Organizations. Retrieved August 30, 2024.
  source_name: NIST Special Publication 800-53 Revision 5
  url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf
- description: 'Tyler Hudak. (2022, December 29). To OOB, or Not to OOB?: Why Out-of-Band Communications are Essential for
    Incident Response. Retrieved August 30, 2024.'
  source_name: TrustedSec OOB Communications
  url: https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response
id: course-of-action--80a0e940-f683-4fbd-ac00-e9f935f2f808
modified: '2024-10-12T15:34:54.912Z'
name: Out-of-Band Communications Channel
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: course-of-action
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '1.0'
```
