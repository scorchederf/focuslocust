---
parsed_by: focuslocust
source: mitre
type: generated
---
# Expand

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0361` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Expand is a Windows utility used to expand one or more compressed CAB files. It has been used by BBSRAT to decompress a CAB file into executable content.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/expand.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1140 - Deobfuscate／Decode Files or Information](../../attack/techniques/T1140-deobfuscate-decode-files-or-information.md) | explicit | source | [Expand](https://attack.mitre.org/software/S0361) can be used to decompress a local or remote CAB file into an executable.(Citation: Microsoft Expand Utility) |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | [Expand](https://attack.mitre.org/software/S0361) can be used to download or copy a file into an alternate data stream.(Citation: LOLBAS Expand) |
| [T1570 - Lateral Tool Transfer](../../attack/techniques/T1570-lateral-tool-transfer.md) | explicit | source | [Expand](https://attack.mitre.org/software/S0361) can be used to download or upload a file over a network share.(Citation: LOLBAS Expand) |

## Source Verification

[source record](../../sources/mitre/expand.md)

## Evidence Excerpt

```text
created: '2019-02-19T19:17:14.971Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Expand](https://attack.mitre.org/software/S0361) is a Windows utility used to expand one or more compressed
CAB files.(Citation: Microsoft Expand Utility) It has been used by [BBSRAT](https://attack.mitre.org/software/S0127) to
decompress a CAB file into executable content.(Citation: Palo Alto Networks BBSRAT)'
external_references:
- external_id: S0361
source_name: mitre-attack
```
