---
parsed_by: focuslocust
source: lolbas
type: generated
---
# write.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `write.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/write.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [write.exe](../../tools/windows/write.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | write.exe |
| name | write.exe |
| type | tool |
| source | lolbas |
| url | https://gist.github.com/mblzk/b8c5ff7c2bd0fb2b385cc2fdd119874b |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: Michal Belzak
Author: Michal Belzak
Commands:
- Category: Execute
  Command: write.exe
  Description: Executes a binary provided in default value of `HKCU\Software\Microsoft\Windows\CurrentVersion\App Paths\wordpad.exe`.
  MitreID: T1218
  OperatingSystem: Windows 10, Windows 11 (before 24H2)
  Privileges: User
  Tags:
  - Execute: EXE
  - Requires: Registry Change
  Usecase: Execute binary through legitimate proxy. This might be utilized to confuse detection solutions that rely on parent-child
    relationships.
Created: 2025-06-17
Description: Windows Write
Detection:
- IOC: Changes to HKCU:\Software\Microsoft\Windows\CurrentVersion\App Paths\wordpad.exe
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_app_paths.yml
Full_Path:
- Path: C:\Windows\write.exe
- Path: C:\Windows\System32\write.exe
- Path: C:\Windows\SysWOW64\write.exe
Name: write.exe
Resources:
- Link: https://gist.github.com/mblzk/b8c5ff7c2bd0fb2b385cc2fdd119874b
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/write.yml
```

## Detection / Analysis Notes

```text
IOC: Changes to HKCU:\Software\Microsoft\Windows\CurrentVersion\App Paths\wordpad.exe
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_app_paths.yml
```

```text
- IOC: Changes to HKCU:\Software\Microsoft\Windows\CurrentVersion\App Paths\wordpad.exe
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_app_paths.yml
```
