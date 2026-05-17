---
parsed_by: focuslocust
source: lolbas
type: generated
---
# cmdl32.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cmdl32.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmdl32.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [cmdl32.exe](../../tools/windows/cmdl32.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cmdl32.exe |
| name | cmdl32.exe |
| type | tool |
| source | lolbas |
| url | https://elliotonsecurity.com/living-off-the-land-reverse-engineering-methodology-plus-tips-and-tricks-cmdl32-case-study/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@elliotkillick'
  Person: Elliot Killick
Author: Elliot Killick
Commands:
- Category: Download
  Command: cmdl32 /vpn /lan %cd%\config
  Description: Download a file from the web address specified in the configuration file. The downloaded file will be in %TMP%
    under the name VPNXXXX.tmp where "X" denotes a random number or letter.
  MitreID: T1105
  OperatingSystem: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Download file from Internet
Created: 2021-08-26
Description: Microsoft Connection Manager Auto-Download
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_cmdl32.yml
- IOC: Reports of downloading from suspicious URLs in %TMP%\config.log
- IOC: Useragent Microsoft(R) Connection Manager Vpn File Update
Full_Path:
- Path: C:\Windows\System32\cmdl32.exe
- Path: C:\Windows\SysWOW64\cmdl32.exe
Name: cmdl32.exe
Resources:
- Link: https://github.com/LOLBAS-Project/LOLBAS/pull/151
- Link: https://twitter.com/ElliotKillick/status/1455897435063074824
- Link: https://elliotonsecurity.com/living-off-the-land-reverse-engineering-methodology-plus-tips-and-tricks-cmdl32-case-study/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmdl32.yml
```

## Detection / Analysis Notes

```text
IOC: Reports of downloading from suspicious URLs in %TMP%\config.log
```

```text
IOC: Useragent Microsoft(R) Connection Manager Vpn File Update
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_cmdl32.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_cmdl32.yml
- IOC: Reports of downloading from suspicious URLs in %TMP%\config.log
- IOC: Useragent Microsoft(R) Connection Manager Vpn File Update
```
