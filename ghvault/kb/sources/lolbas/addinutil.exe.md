---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AddinUtil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `addinutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Addinutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AddinUtil.exe](../../tools/windows/addinutil.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | addinutil.exe |
| name | AddinUtil.exe |
| type | tool |
| source | lolbas |
| url | https://www.blue-prints.blog/content/blog/posts/lolbin/addinutil-lolbas.html |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@MckinleyMike'
  Person: Michael McKinley
- Handle: '@TheLatteri'
  Person: Tony Latteri
Author: Michael McKinley @MckinleyMike
Code_Sample:
- Code: https://gist.github.com/SILJAEUROPA/a850d476179d73df230a876944e9f3b1#file-addins-store
Commands:
- Category: Execute
  Command: C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe -AddinRoot:.
  Description: AddinUtil is executed from the directory where the 'Addins.Store' payload exists, AddinUtil will execute the
    'Addins.Store' payload.
  MitreID: T1218
  OperatingSystem: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: .NetObjects
  Usecase: Proxy execution of malicious serialized payload
Created: 2023-10-05
Description: .NET Tool used for updating cache files for Microsoft Office Add-Ins.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_suspicious_cmdline.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_child_process.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_cmdline.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_dir_exec.yml
Full_Path:
- Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\AddinUtil.exe
- Path: C:\Windows\Microsoft.NET\Framework\v3.5\AddInUtil.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v3.5\AddInUtil.exe
Name: AddinUtil.exe
Resources:
- Link: https://www.blue-prints.blog/content/blog/posts/lolbin/addinutil-lolbas.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Addinutil.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_suspicious_cmdline.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_child_process.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_cmdline.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_dir_exec.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_suspicious_cmdline.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_child_process.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_cmdline.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_dir_exec.yml
```
