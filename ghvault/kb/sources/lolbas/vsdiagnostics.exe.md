---
parsed_by: focuslocust
source: lolbas
type: generated
---
# VSDiagnostics.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vsdiagnostics.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VSDiagnostics.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [VSDiagnostics.exe](../../tools/windows/vsdiagnostics.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | vsdiagnostics.exe |
| name | VSDiagnostics.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/0xBoku/status/1679200664013135872 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@0xBoku'
  Person: Bobby Cooke
Author: Bobby Cooke
Commands:
- Category: Execute
  Command: VSDiagnostics.exe start 1 /launch:{PATH:.exe}
  Description: Starts a collection session with sessionID 1 and calls kernelbase.CreateProcessW to launch specified executable.
  MitreID: T1127
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Proxy execution of binary
- Category: Execute
  Command: VSDiagnostics.exe start 2 /launch:{PATH:.exe} /launchArgs:"{CMD:args}"
  Description: Starts a collection session with sessionID 2 and calls kernelbase.CreateProcessW to launch specified executable.
    Arguments specified in launchArgs are passed to CreateProcessW.
  MitreID: T1127
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Proxy execution of binary with arguments
Created: 2023-07-12
Description: Command-line tool used for performing diagnostics.
Detection:
- Sigma: https://github.com/tsale/Sigma_rules/blob/d5b4a09418edfeeb3a2d654f556d5bca82003cd7/LOL_BINs/VSDiagnostics_LoLBin.yml
Full_Path:
- Path: C:\Program Files\Microsoft Visual Studio\2022\Community\Team Tools\DiagnosticsHub\Collector\VSDiagnostics.exe
Name: VSDiagnostics.exe
Resources:
- Link: https://twitter.com/0xBoku/status/1679200664013135872
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VSDiagnostics.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/tsale/Sigma_rules/blob/d5b4a09418edfeeb3a2d654f556d5bca82003cd7/LOL_BINs/VSDiagnostics_LoLBin.yml
```

```text
- Sigma: https://github.com/tsale/Sigma_rules/blob/d5b4a09418edfeeb3a2d654f556d5bca82003cd7/LOL_BINs/VSDiagnostics_LoLBin.yml
```
