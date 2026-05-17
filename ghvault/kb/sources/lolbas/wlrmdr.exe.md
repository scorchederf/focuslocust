---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Wlrmdr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wlrmdr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wlrmdr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Wlrmdr.exe](../../tools/windows/wlrmdr.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wlrmdr.exe |
| name | Wlrmdr.exe |
| type | tool |
| source | lolbas |
| url | https://docs.microsoft.com/en-us/windows/win32/api/shellapi/ns-shellapi-notifyicondataw |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@0gtweet'
  Person: Grzegorz Tworek
- Handle: '@Oddvarmoe'
  Person: Oddvar Moe
- Handle: '@falsneg'
  Person: Freddy
Author: Moshe Kaplan
Commands:
- Category: Execute
  Command: wlrmdr.exe -s 3600 -f 0 -t _ -m _ -a 11 -u {PATH:.exe}
  Description: Execute executable with wlrmdr.exe as parent process
  MitreID: T1202
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Use wlrmdr as a proxy binary to evade defensive countermeasures
Created: 2022-02-16
Description: Windows Logon Reminder executable
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_wlrmdr.yml
- IOC: wlrmdr.exe spawning any new processes
Full_Path:
- Path: c:\windows\system32\wlrmdr.exe
Name: Wlrmdr.exe
Resources:
- Link: https://twitter.com/0gtweet/status/1493963591745220608
- Link: https://twitter.com/Oddvarmoe/status/927437787242090496
- Link: https://twitter.com/falsneg/status/1461625526640992260
- Link: https://docs.microsoft.com/en-us/windows/win32/api/shellapi/ns-shellapi-notifyicondataw
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wlrmdr.yml
```

## Detection / Analysis Notes

```text
IOC: wlrmdr.exe spawning any new processes
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_wlrmdr.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_wlrmdr.yml
- IOC: wlrmdr.exe spawning any new processes
```
