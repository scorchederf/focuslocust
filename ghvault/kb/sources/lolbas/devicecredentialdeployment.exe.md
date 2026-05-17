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

## Generated Concept Page

- [DeviceCredentialDeployment.exe](../../tools/windows/devicecredentialdeployment.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | devicecredentialdeployment.exe |
| name | DeviceCredentialDeployment.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@elliotkillick'
  Person: Elliot Killick
Author: Elliot Killick
Commands:
- Category: Conceal
  Command: DeviceCredentialDeployment
  Description: Grab the console window handle and set it to hidden
  MitreID: T1564
  OperatingSystem: Windows 10
  Privileges: User
  Usecase: Can be used to stealthily run a console application (e.g. cmd.exe) in the background
Created: 2021-08-16
Description: Device Credential Deployment
Detection:
- IOC: DeviceCredentialDeployment.exe should not be run on a normal workstation
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_device_credential_deployment.yml
Full_Path:
- Path: C:\Windows\System32\DeviceCredentialDeployment.exe
Name: DeviceCredentialDeployment.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/DeviceCredentialDeployment.yml
```

## Detection / Analysis Notes

```text
IOC: DeviceCredentialDeployment.exe should not be run on a normal workstation
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_device_credential_deployment.yml
```

```text
- IOC: DeviceCredentialDeployment.exe should not be run on a normal workstation
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_device_credential_deployment.yml
```
