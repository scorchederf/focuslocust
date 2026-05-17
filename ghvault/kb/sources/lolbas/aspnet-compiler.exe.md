---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Aspnet_Compiler.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `aspnet-compiler.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Aspnet_Compiler.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Aspnet_Compiler.exe](../../tools/windows/aspnet-compiler.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | aspnet-compiler.exe |
| name | Aspnet_Compiler.exe |
| type | tool |
| source | lolbas |
| url | https://docs.microsoft.com/en-us/dotnet/api/system.web.compilation.buildprovider.generatecode?view=netframework-4.8 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@cpl3h'
  Person: cpl
Author: Jimmy (@bohops)
Code_Sample:
- Code: https://github.com/ThunderGunExpress/BringYourOwnBuilder
Commands:
- Category: AWL Bypass
  Command: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_compiler.exe -v none -p C:\users\cpl.internal\desktop\asptest\
    -f C:\users\cpl.internal\desktop\asptest\none -u
  Description: Execute C# code with the Build Provider and proper folder structure in place.
  MitreID: T1127
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Execute proxied payload with Microsoft signed binary to bypass application control solutions
Created: 2021-09-26
Description: ASP.NET Compilation Tool
Detection:
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_aspnet_compiler.yml
Full_Path:
- Path: c:\Windows\Microsoft.NET\Framework\v4.0.30319\aspnet_compiler.exe
- Path: c:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_compiler.exe
Name: Aspnet_Compiler.exe
Resources:
- Link: https://ijustwannared.team/2020/08/01/the-curious-case-of-aspnet_compiler-exe/
- Link: https://docs.microsoft.com/en-us/dotnet/api/system.web.compilation.buildprovider.generatecode?view=netframework-4.8
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Aspnet_Compiler.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_aspnet_compiler.yml
```

```text
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_aspnet_compiler.yml
```
