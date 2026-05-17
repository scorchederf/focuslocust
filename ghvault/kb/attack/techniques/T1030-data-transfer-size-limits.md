---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1030 - Data Transfer Size Limits

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1030` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certain thresholds. This approach may be used to avoid triggering network data transfer threshold alerts.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Mythic](../../tools/unknown/mythic.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) supports custom chunk sizes used to upload/download files.(Citation: Mythc Documentation)	 |
| [Rclone](../../tools/unknown/rclone.md) | explicit | source | The [Rclone](https://attack.mitre.org/software/S1040) "chunker" overlay supports splitting large files in smaller chunks during upload to circumvent size limits.(Citation: Rclone)(Citation: DFIR Conti Bazar Nov 2021) |

## Source Verification

[source record](../../sources/mitre/data-transfer-size-limits.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:34.523Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certain
thresholds. This approach may be used to avoid triggering network data transfer threshold alerts.
external_references:
- external_id: T1030
source_name: mitre-attack
url: https://attack.mitre.org/techniques/T1030
```
