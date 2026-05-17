---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Dxcap.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dxcap.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dxcap.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Dxcap.exe](../../tools/windows/dxcap.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dxcap.exe |
| name | Dxcap.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/harr0ey/status/992008180904419328 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@harr0ey'
  Person: Matt harr0ey
- Handle: '@vikas891'
  Person: Vikas Singh
- Handle: '@ghosts621'
  Person: Naor Evgi
Author: Oddvar Moe
Code_Sample:
- Code: https://gist.github.com/ghosts621/1d0e0f43f7288c826035d5d011b6ca51
Commands:
- Category: Execute
  Command: Dxcap.exe -c {PATH_ABSOLUTE:.exe}
  Description: Launch specified executable as a subprocess of dxcap.exe. Note that you should have write permissions in the
    current working directory for the command to succeed; alternatively, add '-file c:\path\to\writable\location.ext' as first
    argument.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Local execution of a process as a subprocess of dxcap.exe
- Category: Execute
  Command: dxcap.exe -usage
  Description: Once executed, `dxcap.exe` will execute `xperf.exe` in the same folder. Thus, if `dxcap.exe` is copied to a
    folder and an arbitrary executable is renamed to `xperf.exe`, `dxcap.exe` will spawn it.
  MitreID: T1127
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  - Requires: Rename
  Usecase: Execute an arbitrary executable via trusted system executable.
Created: 2018-05-25
Description: DirectX diagnostics/debugger included with Visual Studio.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_susp_dxcap.yml
- IOC: dxcap.exe executing from outside of System32/SysWOW64
- IOC: dxcap.exe spawning Xperf.exe
- IOC: Xperf.exe executing from unusual directories (if not running from ADK path)
Full_Path:
- Path: C:\Windows\System32\dxcap.exe
- Path: C:\Windows\SysWOW64\dxcap.exe
Name: Dxcap.exe
Resources:
- Link: https://twitter.com/harr0ey/status/992008180904419328
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dxcap.yml
```

## Detection / Analysis Notes

```text
IOC: Xperf.exe executing from unusual directories (if not running from ADK path)
```

```text
IOC: dxcap.exe executing from outside of System32/SysWOW64
```

```text
IOC: dxcap.exe spawning Xperf.exe
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_susp_dxcap.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_susp_dxcap.yml
- IOC: dxcap.exe executing from outside of System32/SysWOW64
- IOC: dxcap.exe spawning Xperf.exe
- IOC: Xperf.exe executing from unusual directories (if not running from ADK path)
```
