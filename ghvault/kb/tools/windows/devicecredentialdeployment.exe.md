---
parsed_by: focuslocust
source: lolbas
type: generated
---
# DeviceCredentialDeployment.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `devicecredentialdeployment.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/DeviceCredentialDeployment.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Device Credential Deployment

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/devicecredentialdeployment.md)
- Source verification: [source record](../../sources/lolbas/devicecredentialdeployment.exe.md)

## Aliases

- `DeviceCredentialDeployment.exe`
- `devicecredentialdeployment.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1564 - Hide Artifacts](../../attack/techniques/T1564-hide-artifacts.md) | explicit | source | Command metadata lists T1564: DeviceCredentialDeployment |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/devicecredentialdeployment.exe.md)

## Source Verification

[source record](../../sources/lolbas/devicecredentialdeployment.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@elliotkillick'
Person: Elliot Killick
Author: Elliot Killick
Commands:
- Category: Conceal
Command: DeviceCredentialDeployment
Description: Grab the console window handle and set it to hidden
```
