---
parsed_by: focuslocust
source: mitre
type: generated
---
# DCRAT

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S9017` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

DCRAT is a variant of the open-source AsyncRAT developed in C# with additional capabilities such as patching Microsoft’s Antimalware Scan Interface (AMSI).

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/dcrat.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1027.013 - Encrypted／Encoded File](../../attack/techniques/T1027.013-encrypted-encoded-file.md) | explicit | source | The [DCRAT](https://attack.mitre.org/software/S9017) configuration file is encrypted using AES-256.(Citation: Zscaler BlindEagle DEC 2025) |
| [T1056.001 - Keylogging](../../attack/techniques/T1056.001-keylogging.md) | explicit | source | [DCRAT](https://attack.mitre.org/software/S9017) can log keystrokes on targeted systems.(Citation: Zscaler BlindEagle DEC 2025) |
| [T1573.002 - Asymmetric Cryptography](../../attack/techniques/T1573.002-asymmetric-cryptography.md) | explicit | source | [DCRAT](https://attack.mitre.org/software/S9017) can use certificate-based authentication for C2 servers.(Citation: Zscaler BlindEagle DEC 2025)<br> |
| [T1685 - Disable or Modify Tools](../../attack/techniques/T1685-disable-or-modify-tools.md) | explicit | source | [DCRAT](https://attack.mitre.org/software/S9017) can patch Microsoft’s Antimalware Scan Interface (AMSI) to evade detection.(Citation: Zscaler BlindEagle DEC 2025) |

## Source Verification

[source record](../../sources/mitre/dcrat.md)

## Evidence Excerpt

```text
created: '2026-04-16T18:23:44.020Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[DCRAT](https://attack.mitre.org/software/S9017) is a variant of the open-source [AsyncRAT](https://attack.mitre.org/software/S1087)
developed in C# with additional capabilities such as patching Microsoft’s Antimalware Scan Interface (AMSI).(Citation: Zscaler
BlindEagle DEC 2025)'
external_references:
- external_id: S9017
source_name: mitre-attack
```
