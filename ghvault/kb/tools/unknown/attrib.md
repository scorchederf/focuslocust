---
parsed_by: focuslocust
source: mitre
type: generated
---
# attrib

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1176` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

attrib is a Windows utility used to display, set or remove attributes assigned to files or directories.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/attrib.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1564.001 - Hidden Files and Directories](../../attack/techniques/T1564.001-hidden-files-and-directories.md) | explicit | source | [attrib](https://attack.mitre.org/software/S1176) can be used to make files or directories hidden.(Citation: Microsoft attrib 2023)(Citation: gbhackers Darkgate Malware 2024)(Citation: LogRhythm WannaCry)(Citation: Checkpoint WannaCry 2017)(Citation: Unit42 ComboJack 2018)  |

## Source Verification

[source record](../../sources/mitre/attrib.md)

## Evidence Excerpt

```text
created: '2024-12-04T15:47:07.382Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[attrib](https://attack.mitre.org/software/S1176) is a Windows utility used to display, set or remove attributes
assigned to files or directories.(Citation: Microsoft attrib 2023) '
external_references:
- external_id: S1176
source_name: mitre-attack
url: https://attack.mitre.org/software/S1176
```
