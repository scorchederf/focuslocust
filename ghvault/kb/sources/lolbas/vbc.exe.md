---
parsed_by: focuslocust
source: lolbas
type: generated
---
# vbc.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vbc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Vbc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [vbc.exe](../../tools/windows/vbc.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | vbc.exe |
| name | vbc.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: Lior Adar
- Person: Hai Vaknin(Lux)
Author: Lior Adar
Commands:
- Category: Compile
  Command: vbc.exe /target:exe {PATH_ABSOLUTE:.vb}
  Description: Binary file used by .NET to compile Visual Basic code to an executable.
  MitreID: T1127
  OperatingSystem: Windows 7, Windows 10, Windows 11
  Privileges: User
  Usecase: Compile attacker code on system. Bypass defensive counter measures.
- Category: Compile
  Command: vbc -reference:Microsoft.VisualBasic.dll {PATH_ABSOLUTE:.vb}
  Description: Binary file used by .NET to compile Visual Basic code to an executable.
  MitreID: T1127
  OperatingSystem: Windows 7, Windows 10, Windows 11
  Privileges: User
  Usecase: Compile attacker code on system. Bypass defensive counter measures.
Created: 2020-02-27
Description: Binary file used for compile vbs code
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_visual_basic_compiler.yml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_dotnet_compiler_parent_process.toml
Full_Path:
- Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\vbc.exe
- Path: C:\Windows\Microsoft.NET\Framework\v3.5\vbc.exe
- Path: C:\Windows\Microsoft.NET\Framework\v2.0.50727\vbc.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\vbc.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v3.5\vbc.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v2.0.50727\vbc.exe
Name: vbc.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Vbc.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_dotnet_compiler_parent_process.toml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_visual_basic_compiler.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_visual_basic_compiler.yml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_dotnet_compiler_parent_process.toml
```
