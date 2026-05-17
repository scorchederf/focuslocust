---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Cipher.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cipher.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cipher.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cipher.exe](../../tools/windows/cipher.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cipher.exe |
| name | Cipher.exe |
| type | tool |
| source | lolbas |
| url | https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@i_am_tutu'
  Person: Ade Ogunsowo
- Handle: '@conitrade'
  Person: Alexander Sennhauser
Author: Adetutu Ogunsowo
Commands:
- Category: Tamper
  Command: cipher /w:{PATH_ABSOLUTE:folder}
  Description: Zero out a file
  MitreID: T1485
  OperatingSystem: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Can be used to forensically erase a file.
- Category: Tamper
  Command: cipher.exe /e {PATH_ABSOLUTE}
  Description: Encrypt a file
  MitreID: T1562
  OperatingSystem: Windows 10
  Privileges: Admin
  Usecase: Can be used to impair defences by e.g. encrypting a critical EDR solution file.
Created: 2024-11-22
Description: File Encryption Utility
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_cipher_overwrite_deleted_data.yml
- IOC: cipher.exe process with /w on the command line
Full_Path:
- Path: c:\windows\system32\cipher.exe
- Path: c:\windows\syswow64\cipher.exe
Name: Cipher.exe
Resources:
- Link: https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cipher.yml
```

## Detection / Analysis Notes

```text
IOC: cipher.exe process with /w on the command line
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_cipher_overwrite_deleted_data.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_cipher_overwrite_deleted_data.yml
- IOC: cipher.exe process with /w on the command line
```
