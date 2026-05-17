---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AccCheckConsole.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `acccheckconsole.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/AccCheckConsole.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AccCheckConsole.exe](../../tools/windows/acccheckconsole.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | acccheckconsole.exe |
| name | AccCheckConsole.exe |
| type | tool |
| source | lolbas |
| url | https://gist.github.com/bohops/2444129419c8acf837aedda5f0e7f340 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@bohops'
  Person: Jimmy
Author: bohops
Code_Sample:
- Code: https://docs.microsoft.com/en-us/windows/win32/winauto/custom-verification-routines
Commands:
- Category: Execute
  Command: AccCheckConsole.exe -window "Untitled - Notepad" {PATH_ABSOLUTE:.dll}
  Description: Load a managed DLL in the context of AccCheckConsole.exe. The -window switch value can be set to an arbitrary
    active window name.
  MitreID: T1218
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: DLL (.NET)
  Usecase: Local execution of managed code from assembly DLL.
- Category: AWL Bypass
  Command: AccCheckConsole.exe -window "Untitled - Notepad" {PATH_ABSOLUTE:.dll}
  Description: Load a managed DLL in the context of AccCheckConsole.exe. The -window switch value can be set to an arbitrary
    active window name.
  MitreID: T1218
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: DLL (.NET)
  Usecase: Local execution of managed code to bypass AppLocker.
Created: 2022-01-02
Description: Verifies UI accessibility requirements
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_susp_acccheckconsole.yml
- IOC: Sysmon Event ID 1 - Process Creation
- Analysis: https://gist.github.com/bohops/2444129419c8acf837aedda5f0e7f340
Full_Path:
- Path: C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x86\AccChecker\AccCheckConsole.exe
- Path: C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x64\AccChecker\AccCheckConsole.exe
- Path: C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\arm\AccChecker\AccCheckConsole.exe
- Path: C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\arm64\AccChecker\AccCheckConsole.exe
Name: AccCheckConsole.exe
Resources:
- Link: https://gist.github.com/bohops/2444129419c8acf837aedda5f0e7f340
- Link: https://twitter.com/bohops/status/1477717351017680899
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/AccCheckConsole.yml
```

## Detection / Analysis Notes

```text
Analysis: https://gist.github.com/bohops/2444129419c8acf837aedda5f0e7f340
```

```text
IOC: Sysmon Event ID 1 - Process Creation
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_susp_acccheckconsole.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_susp_acccheckconsole.yml
- IOC: Sysmon Event ID 1 - Process Creation
- Analysis: https://gist.github.com/bohops/2444129419c8acf837aedda5f0e7f340
```
