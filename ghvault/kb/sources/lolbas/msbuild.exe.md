---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Msbuild.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msbuild.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msbuild.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Msbuild.exe](../../tools/windows/msbuild.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msbuild.exe |
| name | Msbuild.exe |
| type | tool |
| source | lolbas |
| url | https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-response-files |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subtee'
  Person: Casey Smith
- Handle: '@Cneelis'
  Person: Cn33liz
- Handle: '@bohops'
  Person: Jimmy
Author: Oddvar Moe
Commands:
- Category: AWL Bypass
  Command: msbuild.exe {PATH:.xml}
  Description: Build and execute a C# project stored in the target XML file.
  MitreID: T1127.001
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CSharp
  Usecase: Compile and run code
- Category: Execute
  Command: msbuild.exe {PATH:.csproj}
  Description: Build and execute a C# project stored in the target csproj file.
  MitreID: T1127.001
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CSharp
  Usecase: Compile and run code
- Category: Execute
  Command: msbuild.exe /logger:TargetLogger,{PATH_ABSOLUTE:.dll};MyParameters,Foo
  Description: Executes generated Logger DLL file with TargetLogger export.
  MitreID: T1127.001
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Execute DLL
- Category: Execute
  Command: msbuild.exe {PATH:.proj}
  Description: Execute JScript/VBScript code through XML/XSL Transformation. Requires Visual Studio MSBuild v14.0+.
  MitreID: T1127.001
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: XSL
  Usecase: Execute project file that contains XslTransformation tag parameters
- Category: Execute
  Command: msbuild.exe @{PATH:.rsp}
  Description: By putting any valid msbuild.exe command-line options in an RSP file and calling it as above will interpret
    the options as if they were passed on the command line.
  MitreID: T1036
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Bypass command-line based detections
Created: 2018-05-25
Description: Used to compile and execute code
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_shell_write_susp_directory.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_msbuild_susp_parent_process.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_silenttrinity_stager_msbuild_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_msbuild_spawn.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_msbuild_rename.yml
- Splunk: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/msbuild_suspicious_spawned_by_script_process.yml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_msbuild_beacon_sequence.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_msbuild_making_network_connections.toml
- Elastic: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/defense_evasion_execution_msbuild_started_by_script.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_execution_msbuild_started_by_office_app.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_execution_msbuild_started_renamed.toml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Msbuild.exe should not normally be executed on workstations
Full_Path:
- Path: C:\Windows\Microsoft.NET\Framework\v2.0.50727\Msbuild.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v2.0.50727\Msbuild.exe
- Path: C:\Windows\Microsoft.NET\Framework\v3.5\Msbuild.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v3.5\Msbuild.exe
- Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\Msbuild.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Msbuild.exe
- Path: C:\Program Files (x86)\MSBuild\14.0\bin\MSBuild.exe
Name: Msbuild.exe
Resources:
- Link: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1127/T1127.md
- Link: https://github.com/Cn33liz/MSBuildShell
- Link: https://pentestlab.blog/2017/05/29/applocker-bypass-msbuild/
- Link: https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/
- Link: https://gist.github.com/bohops/4ffc43a281e87d108875f07614324191
- Link: https://github.com/LOLBAS-Project/LOLBAS/issues/165
- Link: https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-response-files
- Link: https://www.daveaglick.com/posts/msbuild-loggers-and-logging-events
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msbuild.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_execution_msbuild_started_by_office_app.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_execution_msbuild_started_renamed.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_msbuild_beacon_sequence.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_msbuild_making_network_connections.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/defense_evasion_execution_msbuild_started_by_script.toml
```

```text
IOC: Msbuild.exe should not normally be executed on workstations
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_shell_write_susp_directory.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_msbuild_susp_parent_process.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_silenttrinity_stager_msbuild_activity.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_msbuild_rename.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_msbuild_spawn.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/msbuild_suspicious_spawned_by_script_process.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_shell_write_susp_directory.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_msbuild_susp_parent_process.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_silenttrinity_stager_msbuild_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_msbuild_spawn.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_msbuild_rename.yml
- Splunk: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/msbuild_suspicious_spawned_by_script_process.yml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_msbuild_beacon_sequence.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_msbuild_making_network_connections.toml
- Elastic: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/defense_evasion_execution_msbuild_started_by_script.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_execution_msbuild_started_by_office_app.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_execution_msbuild_started_renamed.toml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Msbuild.exe should not normally be executed on workstations
```
