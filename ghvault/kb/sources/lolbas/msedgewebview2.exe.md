---
parsed_by: focuslocust
source: lolbas
type: generated
---
# msedgewebview2.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msedgewebview2.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedgewebview2.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [msedgewebview2.exe](../../tools/windows/msedgewebview2.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msedgewebview2.exe |
| name | msedgewebview2.exe |
| type | tool |
| source | lolbas |
| url | https://medium.com/@MalFuzzer/one-electron-to-rule-them-all-dc2e9b263daf |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@MalFuzzer'
  Person: Uriel Kosayev
- Handle: '@VakninHai'
  Person: Hai Vaknin
- Handle: '@Tamirye94'
  Person: Tamir Yehuda
- Handle: '@Bl4ckShad3'
  Person: Matan Bahar
Author: Matan Bahar
Commands:
- Category: Execute
  Command: msedgewebview2.exe --no-sandbox --browser-subprocess-path="{PATH_ABSOLUTE:.exe}"
  Description: This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified
    executable as its subprocess.
  MitreID: T1218.015
  OperatingSystem: Windows 10, Windows 11
  Privileges: Low privileges
  Tags:
  - Execute: EXE
  Usecase: Proxy execution of binary
- Category: Execute
  Command: msedgewebview2.exe --utility-cmd-prefix="{CMD}"
  Description: This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified
    command as its subprocess.
  MitreID: T1218.015
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Proxy execution of binary
- Category: Execute
  Command: msedgewebview2.exe --disable-gpu-sandbox --gpu-launcher="{CMD}"
  Description: This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified
    command as its subprocess.
  MitreID: T1218.015
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Proxy execution of binary
- Category: Execute
  Command: msedgewebview2.exe --no-sandbox --renderer-cmd-prefix="{CMD}"
  Description: This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified
    command as its subprocess.
  MitreID: T1218.015
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Proxy execution of binary
Created: 2023-06-15
Description: msedgewebview2.exe is the executable file for Microsoft Edge WebView2, which is a web browser control used by
  applications to display web content.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml
- IOC: 'msedgewebview2.exe spawned with any of the following: --gpu-launcher, --utility-cmd-prefix, --renderer-cmd-prefix,
    --browser-subprocess-path'
Full_Path:
- Path: C:\Program Files (x86)\Microsoft\Edge\Application\114.0.1823.43\msedgewebview2.exe
- Path: C:\Program Files (x86)\Microsoft\EdgeWebView\Application\131.0.2903.70\msedgewebview2.exe
Name: msedgewebview2.exe
Resources:
- Link: https://medium.com/@MalFuzzer/one-electron-to-rule-them-all-dc2e9b263daf
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedgewebview2.yml
```

## Detection / Analysis Notes

```text
IOC: msedgewebview2.exe spawned with any of the following: --gpu-launcher, --utility-cmd-prefix, --renderer-cmd-prefix, --browser-subprocess-path
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml
- IOC: 'msedgewebview2.exe spawned with any of the following: --gpu-launcher, --utility-cmd-prefix, --renderer-cmd-prefix,
    --browser-subprocess-path'
```
