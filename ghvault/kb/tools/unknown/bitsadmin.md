---
parsed_by: focuslocust
source: mitre
type: generated
---
# BITSAdmin

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0190` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

BITSAdmin is a command line tool used to create and manage BITS Jobs.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/bitsadmin.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1048.003 - Exfiltration Over Unencrypted Non-C2 Protocol](../../attack/techniques/T1048.003-exfiltration-over-unencrypted-non-c2-protocol.md) | explicit | source | [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload files from a compromised host.(Citation: Microsoft BITSAdmin) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload and/or download files.(Citation: Microsoft BITSAdmin) |
| [T1197 - BITS Jobs](../../attack/techniques/T1197-bits-jobs.md) | explicit | source | [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to launch a malicious process.(Citation: TrendMicro Tropic Trooper Mar 2018) |
| [T1570 - Lateral Tool Transfer](../../attack/techniques/T1570-lateral-tool-transfer.md) | explicit | source | [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload and/or download files from SMB file servers.(Citation: Microsoft About BITS) |

## Source Verification

[source record](../../sources/mitre/bitsadmin.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS
Jobs](https://attack.mitre.org/techniques/T1197). (Citation: Microsoft BITSAdmin)'
external_references:
- external_id: S0190
source_name: mitre-attack
url: https://attack.mitre.org/software/S0190
```
