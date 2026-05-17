---
parsed_by: focuslocust
source: lolbas
type: generated
---
# vstest.console.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vstest.console.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/vstest.console.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [vstest.console.exe](../../tools/windows/vstest.console.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | vstest.console.exe |
| name | vstest.console.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/visualstudio/test/vstest-console-options?view=vs-2022 |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: Onat Uzunyayla
- Person: Ayberk Halac
Author: Onat Uzunyayla
Code_Sample:
- Code: https://github.com/onatuzunyayla/vstest-lolbin-example/
Commands:
- Category: AWL Bypass
  Command: vstest.console.exe {PATH:.dll}
  Description: VSTest functionality may allow an adversary to executes their malware by wrapping it as a test method then
    build it to a .exe or .dll file to be later run by vstest.console.exe. This may both allow AWL bypass or defense bypass
    in general
  MitreID: T1127
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Proxy Execution and AWL bypass, Adversaries may run malicious code embedded inside the test methods of crafted
    dll/exe
Created: 2023-09-08
Description: VSTest.Console.exe is the command-line tool to run tests
Detection:
- IOC: vstest.console.exe spawning unexpected processes
Full_Path:
- Path: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe
- Path: C:\Program Files (x86)\Microsoft Visual Studio\2022\TestAgent\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe
Name: vstest.console.exe
Resources:
- Link: https://learn.microsoft.com/en-us/visualstudio/test/vstest-console-options?view=vs-2022
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/vstest.console.yml
```

## Detection / Analysis Notes

```text
IOC: vstest.console.exe spawning unexpected processes
```

```text
- IOC: vstest.console.exe spawning unexpected processes
```
