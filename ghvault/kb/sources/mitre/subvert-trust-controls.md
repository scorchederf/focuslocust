---
parsed_by: focuslocust
source: mitre
type: generated
---
# Subvert Trust Controls

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1553` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Subvert Trust Controls](../../attack/techniques/T1553-subvert-trust-controls.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1553 |
| name | Subvert Trust Controls |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1553 |

## Preserved Source Material

```yaml
created: '2020-02-05T14:54:07.588Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may undermine security controls that will either warn users of untrusted activity or prevent execution
  of untrusted programs. Operating systems and security products may contain mechanisms to identify programs or websites as
  possessing some level of trust. Examples of such features would include a program being allowed to run because it is signed
  by a valid code signing certificate, a program prompting the user with a warning because it has an attribute set from being
  downloaded from the Internet, or getting an indication that you are about to connect to an untrusted site.


  Adversaries may attempt to subvert these trust mechanisms. The method adversaries use will depend on the specific mechanism
  they seek to subvert. Adversaries may conduct [File and Directory Permissions Modification](https://attack.mitre.org/techniques/T1222)
  or [Modify Registry](https://attack.mitre.org/techniques/T1112) in support of subverting these controls.(Citation: SpectorOps
  Subverting Trust Sept 2017) Adversaries may also create or steal code signing certificates to acquire trust on target systems.(Citation:
  Securelist Digital Certificates)(Citation: Symantec Digital Certificates) '
external_references:
- external_id: T1553
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1553
- description: Graeber, M. (2017, September). Subverting Trust in Windows. Retrieved January 31, 2018.
  source_name: SpectorOps Subverting Trust Sept 2017
  url: https://specterops.io/assets/resources/SpecterOps_Subverting_Trust_in_Windows.pdf
- description: Ladikov, A. (2015, January 29). Why You Shouldn’t Completely Trust Files Signed with Digital Certificates.
    Retrieved March 31, 2016.
  source_name: Securelist Digital Certificates
  url: https://securelist.com/why-you-shouldnt-completely-trust-files-signed-with-digital-certificates/68593/
- description: Shinotsuka, H. (2013, February 22). How Attackers Steal Private Keys from Digital Certificates. Retrieved March
    31, 2016.
  source_name: Symantec Digital Certificates
  url: http://www.symantec.com/connect/blogs/how-attackers-steal-private-keys-digital-certificates
id: attack-pattern--b83e166d-13d7-4b52-8677-dff90c548fd7
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:53.101Z'
name: Subvert Trust Controls
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
