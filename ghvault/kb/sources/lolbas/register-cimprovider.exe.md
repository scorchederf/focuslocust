---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Register-cimprovider.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `register-cimprovider.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Register-cimprovider.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Register-cimprovider.exe](../../tools/windows/register-cimprovider.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | register-cimprovider.exe |
| name | Register-cimprovider.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/PhilipTsukerman/status/992021361106268161 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@PhilipTsukerman'
  Person: Philip Tsukerman
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: Register-cimprovider -path {PATH_ABSOLUTE:.dll}
  Description: Load the target .DLL.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Execute code within dll file
Created: 2018-05-25
Description: Used to register new wmi providers
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/35a7244c62820fbc5a832e50b1e224ac3a1935da/rules/windows/process_creation/proc_creation_win_susp_register_cimprovider.yml
- IOC: Register-cimprovider.exe execution and cmdline DLL load may be supsicious
Full_Path:
- Path: C:\Windows\System32\Register-cimprovider.exe
- Path: C:\Windows\SysWOW64\Register-cimprovider.exe
Name: Register-cimprovider.exe
Resources:
- Link: https://twitter.com/PhilipTsukerman/status/992021361106268161
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Register-cimprovider.yml
```

## Detection / Analysis Notes

```text
IOC: Register-cimprovider.exe execution and cmdline DLL load may be supsicious
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/35a7244c62820fbc5a832e50b1e224ac3a1935da/rules/windows/process_creation/proc_creation_win_susp_register_cimprovider.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/35a7244c62820fbc5a832e50b1e224ac3a1935da/rules/windows/process_creation/proc_creation_win_susp_register_cimprovider.yml
- IOC: Register-cimprovider.exe execution and cmdline DLL load may be supsicious
```
