---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Diskshadow.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `diskshadow.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Diskshadow.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Diskshadow.exe](../../tools/windows/diskshadow.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | diskshadow.exe |
| name | Diskshadow.exe |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2018/03/26/diskshadow-the-return-of-vss-evasion-persistence-and-active-directory-database-extraction/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@bohops'
  Person: Jimmy
Author: Oddvar Moe
Commands:
- Category: Dump
  Command: diskshadow.exe /s {PATH:.txt}
  Description: Execute commands using diskshadow.exe from a prepared diskshadow script.
  MitreID: T1003.003
  OperatingSystem: Windows server
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Use diskshadow to exfiltrate data from VSS such as NTDS.dit
- Category: Execute
  Command: diskshadow> exec {PATH:.exe}
  Description: Execute commands using diskshadow.exe to spawn child process
  MitreID: T1202
  OperatingSystem: Windows server
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Use diskshadow to bypass defensive counter measures
Created: 2018-05-25
Description: Diskshadow.exe is a tool that exposes the functionality offered by the volume shadow copy Service (VSS).
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diskshadow.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_shadow_copies_deletion.yml
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- IOC: Child process from diskshadow.exe
Full_Path:
- Path: C:\Windows\System32\diskshadow.exe
- Path: C:\Windows\SysWOW64\diskshadow.exe
Name: Diskshadow.exe
Resources:
- Link: https://bohops.com/2018/03/26/diskshadow-the-return-of-vss-evasion-persistence-and-active-directory-database-extraction/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Diskshadow.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
```

```text
IOC: Child process from diskshadow.exe
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diskshadow.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_shadow_copies_deletion.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diskshadow.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_shadow_copies_deletion.yml
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- IOC: Child process from diskshadow.exe
```
