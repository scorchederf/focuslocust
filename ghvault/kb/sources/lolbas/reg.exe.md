---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Reg.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `reg.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Reg.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Reg.exe](../../tools/windows/reg.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | reg.exe |
| name | Reg.exe |
| type | tool |
| source | lolbas |
| url | https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: ADS
  Command: reg export HKLM\SOFTWARE\Microsoft\Evilreg {PATH_ABSOLUTE}:evilreg.reg
  Description: Export the target Registry key and save it to the specified .REG file within an Alternate data stream.
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Hide/plant registry information in Alternate data stream for later use
- Category: Credentials
  Command: reg save HKLM\SECURITY {PATH_ABSOLUTE:.1.bak} && reg save HKLM\SYSTEM {PATH_ABSOLUTE:.2.bak} && reg save HKLM\SAM
    {PATH_ABSOLUTE:.3.bak}
  Description: Dump registry hives (SAM, SYSTEM, SECURITY) to retrieve password hashes and key material
  MitreID: T1003.002
  OperatingSystem: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: Administrator
  Usecase: Dump credentials from the Security Account Manager (SAM)
Created: 2018-05-25
Description: Used to manipulate the registry
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regedit_import_keys.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_reg_dumping_sensitive_hives.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/attempted_credential_dump_from_registry_via_reg_exe.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f6421d8c534f295518a2c945f530e8afc4c8ad1b/rules/windows/credential_access_dump_registry_hives.toml
- IOC: reg.exe writing to an ADS
Full_Path:
- Path: C:\Windows\System32\reg.exe
- Path: C:\Windows\SysWOW64\reg.exe
Name: Reg.exe
Resources:
- Link: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- Link: https://pure.security/dumping-windows-credentials/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Reg.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/f6421d8c534f295518a2c945f530e8afc4c8ad1b/rules/windows/credential_access_dump_registry_hives.toml
```

```text
IOC: reg.exe writing to an ADS
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_reg_dumping_sensitive_hives.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regedit_import_keys.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/attempted_credential_dump_from_registry_via_reg_exe.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regedit_import_keys.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_reg_dumping_sensitive_hives.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/attempted_credential_dump_from_registry_via_reg_exe.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f6421d8c534f295518a2c945f530e8afc4c8ad1b/rules/windows/credential_access_dump_registry_hives.toml
- IOC: reg.exe writing to an ADS
```
