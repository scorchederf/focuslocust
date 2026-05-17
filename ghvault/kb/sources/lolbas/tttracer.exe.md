---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Tttracer.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `tttracer.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Tttracer.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Tttracer.exe](../../tools/windows/tttracer.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tttracer.exe |
| name | Tttracer.exe |
| type | tool |
| source | lolbas |
| url | https://lists.samba.org/archive/cifs-protocol/2016-April/002877.html |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@oulusoyum'
  Person: Onur Ulusoy
- Handle: '@mattifestation'
  Person: Matt Graeber
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: tttracer.exe {PATH_ABSOLUTE:.exe}
  Description: Execute specified executable from tttracer.exe. Requires administrator privileges.
  MitreID: T1127
  OperatingSystem: Windows 10 1809 and newer, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: EXE
  Usecase: Spawn process using other binary
- Category: Dump
  Command: TTTracer.exe -dumpFull -attach {PID}
  Description: Dumps process using tttracer.exe. Requires administrator privileges
  MitreID: T1003
  OperatingSystem: Windows 10 1809 and newer, Windows 11
  Privileges: Administrator
  Usecase: Dump process by PID
Created: 2019-11-05
Description: Used by Windows 1809 and newer to Debug Time Travel
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_tttracer_mod_load.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/image_load/image_load_tttracer_mod_load.yml
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- IOC: Parent child relationship. Tttracer parent for executed command
Full_Path:
- Path: C:\Windows\System32\tttracer.exe
- Path: C:\Windows\SysWOW64\tttracer.exe
Name: Tttracer.exe
Resources:
- Link: https://twitter.com/oulusoyum/status/1191329746069655553
- Link: https://twitter.com/mattifestation/status/1196390321783025666
- Link: https://lists.samba.org/archive/cifs-protocol/2016-April/002877.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Tttracer.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
```

```text
IOC: Parent child relationship. Tttracer parent for executed command
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/image_load/image_load_tttracer_mod_load.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_tttracer_mod_load.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_tttracer_mod_load.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/image_load/image_load_tttracer_mod_load.yml
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- IOC: Parent child relationship. Tttracer parent for executed command
```
