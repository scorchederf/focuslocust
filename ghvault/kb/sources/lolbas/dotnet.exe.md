---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Dotnet.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dotnet.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dotnet.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Dotnet.exe](../../tools/windows/dotnet.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dotnet.exe |
| name | Dotnet.exe |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2019/08/19/dotnet-core-a-vector-for-awl-bypass-defense-evasion/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@_felamos'
  Person: felamos
- Handle: '@bohops'
  Person: Jimmy
- Handle: '@mavinject'
  Person: yamalon
Author: felamos
Commands:
- Category: AWL Bypass
  Command: dotnet.exe {PATH:.dll}
  Description: dotnet.exe will execute any DLL even if applocker is enabled.
  MitreID: T1218
  OperatingSystem: Windows 7 and up with .NET installed
  Privileges: User
  Tags:
  - Execute: DLL (.NET)
  Usecase: Execute code bypassing AWL
- Category: Execute
  Command: dotnet.exe {PATH:.dll}
  Description: dotnet.exe will execute any DLL.
  MitreID: T1218
  OperatingSystem: Windows 7 and up with .NET installed
  Privileges: User
  Tags:
  - Execute: DLL (.NET)
  Usecase: Execute DLL
- Category: Execute
  Command: dotnet.exe fsi
  Description: dotnet.exe will open a console which allows for the execution of arbitrary F# commands
  MitreID: T1059
  OperatingSystem: Windows 10 and up with .NET SDK installed
  Privileges: User
  Tags:
  - Execute: FSharp
  Usecase: Execute arbitrary F# code
- Category: AWL Bypass
  Command: dotnet.exe msbuild {PATH:.csproj}
  Description: dotnet.exe with msbuild (SDK Version) will execute unsigned code
  MitreID: T1218
  OperatingSystem: Windows 10 and up with .NET Core installed
  Privileges: User
  Tags:
  - Execute: CSharp
  Usecase: Execute code bypassing AWL
Created: 2019-11-12
Description: dotnet.exe comes with .NET Framework
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dotnet.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: dotnet.exe spawned an unknown process
Full_Path:
- Path: C:\Program Files\dotnet\dotnet.exe
Name: Dotnet.exe
Resources:
- Link: https://twitter.com/_felamos/status/1204705548668555264
- Link: https://gist.github.com/bohops/3f645a7238d8022830ecf5511b3ecfbc
- Link: https://bohops.com/2019/08/19/dotnet-core-a-vector-for-awl-bypass-defense-evasion/
- Link: https://learn.microsoft.com/en-us/dotnet/fsharp/tools/fsharp-interactive/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dotnet.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
IOC: dotnet.exe spawned an unknown process
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dotnet.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dotnet.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: dotnet.exe spawned an unknown process
```
