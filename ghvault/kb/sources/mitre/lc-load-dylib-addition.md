---
parsed_by: focuslocust
source: mitre
type: generated
---
# LC_LOAD_DYLIB Addition

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1546.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [LC_LOAD_DYLIB Addition](../../attack/techniques/T1546.006-lc-load-dylib-addition.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1546.006 |
| name | LC_LOAD_DYLIB Addition |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1546/006 |

## Preserved Source Material

```yaml
created: '2020-01-24T14:21:52.750Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may establish persistence by executing malicious content triggered by the execution of tainted binaries.
  Mach-O binaries have a series of headers that are used to perform certain operations when a binary is loaded. The LC_LOAD_DYLIB
  header in a Mach-O binary tells macOS and OS X which dynamic libraries (dylibs) to load during execution time. These can
  be added ad-hoc to the compiled binary as long as adjustments are made to the rest of the fields and dependencies.(Citation:
  Writing Bad Malware for OSX) There are tools available to perform these changes.


  Adversaries may modify Mach-O binary headers to load and execute malicious dylibs every time the binary is executed. Although
  any changes will invalidate digital signatures on binaries because the binary is being modified, this can be remediated
  by simply removing the LC_CODE_SIGNATURE command from the binary so that the signature isn’t checked at load time.(Citation:
  Malware Persistence on OS X)'
external_references:
- external_id: T1546.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1546/006
- description: Patrick Wardle. (2015). Malware Persistence on OS X Yosemite. Retrieved July 10, 2017.
  source_name: Malware Persistence on OS X
  url: https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf
- description: Patrick Wardle. (2015). Writing Bad @$$ Malware for OS X. Retrieved July 10, 2017.
  source_name: Writing Bad Malware for OSX
  url: https://www.blackhat.com/docs/us-15/materials/us-15-Wardle-Writing-Bad-A-Malware-For-OS-X.pdf
id: attack-pattern--10ff21b9-5a01-4268-a1b5-3b55015f1847
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:48:25.182Z'
name: LC_LOAD_DYLIB Addition
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
- macOS
x_mitre_version: '1.1'
```
