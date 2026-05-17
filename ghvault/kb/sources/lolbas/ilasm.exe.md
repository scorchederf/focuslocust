---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ilasm.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ilasm.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ilasm.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ilasm.exe](../../tools/windows/ilasm.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ilasm.exe |
| name | Ilasm.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/LuxNoBulIshit/BeforeCompileBy-ilasm/blob/master/hello_world.txt |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@VakninHai'
  Person: Hai Vaknin(Lux)
- Person: Lior Adar
Author: Hai vaknin (lux)
Commands:
- Category: Compile
  Command: ilasm.exe {PATH_ABSOLUTE:.txt} /exe
  Description: Binary file used by .NET to compile C#/intermediate (IL) code to .exe
  MitreID: T1127
  OperatingSystem: Windows 7, Windows 10, Windows 11
  Privileges: User
  Usecase: Compile attacker code on system. Bypass defensive counter measures.
- Category: Compile
  Command: ilasm.exe {PATH_ABSOLUTE:.txt} /dll
  Description: Binary file used by .NET to compile C#/intermediate (IL) code to dll
  MitreID: T1127
  OperatingSystem: Windows 7, Windows 10, Windows 11
  Privileges: User
  Usecase: A description of the usecase
Created: 2020-03-17
Description: used for compile c# code into dll or exe.
Detection:
- IOC: Ilasm may not be used often in production environments (such as on endpoints)
- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbin_ilasm.yml
Full_Path:
- Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\ilasm.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ilasm.exe
Name: Ilasm.exe
Resources:
- Link: https://github.com/LuxNoBulIshit/BeforeCompileBy-ilasm/blob/master/hello_world.txt
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ilasm.yml
```

## Detection / Analysis Notes

```text
IOC: Ilasm may not be used often in production environments (such as on endpoints)
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbin_ilasm.yml
```

```text
- IOC: Ilasm may not be used often in production environments (such as on endpoints)
- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbin_ilasm.yml
```
