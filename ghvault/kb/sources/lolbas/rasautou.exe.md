---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Rasautou.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `rasautou.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rasautou.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Rasautou.exe](../../tools/windows/rasautou.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rasautou.exe |
| name | Rasautou.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/fireeye/DueDLLigence |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@FireEye'
  Person: FireEye
Author: Tony Lambert
Commands:
- Category: Execute
  Command: rasautou -d {PATH:.dll} -p export_name -a a -e e
  Description: Loads the target .DLL specified in -d and executes the export specified in -p. Options removed in Windows 10.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1
  Privileges: User, Administrator in Windows 8
  Tags:
  - Execute: DLL
  Usecase: Execute DLL code
Created: 2020-01-10
Description: Windows Remote Access Dialer
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/08ca62cc8860f4660e945805d0dd615ce75258c1/rules/windows/process_creation/win_rasautou_dll_execution.yml
- IOC: rasautou.exe command line containing -d and -p
Full_Path:
- Path: C:\Windows\System32\rasautou.exe
Name: Rasautou.exe
Resources:
- Link: https://github.com/fireeye/DueDLLigence
- Link: https://www.fireeye.com/blog/threat-research/2019/10/staying-hidden-on-the-endpoint-evading-detection-with-shellcode.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rasautou.yml
```

## Detection / Analysis Notes

```text
IOC: rasautou.exe command line containing -d and -p
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/08ca62cc8860f4660e945805d0dd615ce75258c1/rules/windows/process_creation/win_rasautou_dll_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/08ca62cc8860f4660e945805d0dd615ce75258c1/rules/windows/process_creation/win_rasautou_dll_execution.yml
- IOC: rasautou.exe command line containing -d and -p
```
