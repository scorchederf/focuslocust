---
parsed_by: focuslocust
source: mitre
type: generated
---
# Windows Credential Editor

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Credential Editor is a password dumping tool.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/windows-credential-editor.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | [Windows Credential Editor](https://attack.mitre.org/software/S0005) can dump credentials.(Citation: Amplia WCE) |

## Source Verification

[source record](../../sources/mitre/windows-credential-editor.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:32:12.684Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Windows Credential Editor](https://attack.mitre.org/software/S0005) is a password dumping tool. (Citation:
Amplia WCE)'
external_references:
- external_id: S0005
source_name: mitre-attack
url: https://attack.mitre.org/software/S0005
```
