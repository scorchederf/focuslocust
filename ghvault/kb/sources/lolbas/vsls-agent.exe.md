---
parsed_by: focuslocust
source: lolbas
type: generated
---
# vsls-agent.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vsls-agent.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/vsls-agent.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [vsls-agent.exe](../../tools/windows/vsls-agent.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | vsls-agent.exe |
| name | vsls-agent.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/bohops/status/1583916360404729857 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@bohops'
  Person: Jimmy
Author: Jimmy (@bohops)
Commands:
- Category: Execute
  Command: vsls-agent.exe --agentExtensionPath {PATH_ABSOLUTE:.dll}
  Description: Load a library payload using the --agentExtensionPath parameter (32-bit)
  MitreID: T1218
  OperatingSystem: Windows 10 21H2 (likely previous and newer versions with modern versions of Visual Studio installed)
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Execute proxied payload with Microsoft signed binary
Created: 2022-11-01
Description: Agent for Visual Studio Live Share (Code Collaboration)
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_vslsagent_agentextensionpath_load.yml
Full_Path:
- Path: c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\Extensions\Microsoft\LiveShare\Agent\vsls-agent.exe
Name: vsls-agent.exe
Resources:
- Link: https://twitter.com/bohops/status/1583916360404729857
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/vsls-agent.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_vslsagent_agentextensionpath_load.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_vslsagent_agentextensionpath_load.yml
```
