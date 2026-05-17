---
parsed_by: focuslocust
source: commands
type: generated
---
# Regedit Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Regedit.exe

Tool page: [Regedit.exe](../../tools/windows/regedit.exe.md)

### Hide registry data in alternate data stream

```text
regedit /E {PATH_ABSOLUTE}:regfile.reg HKEY_CURRENT_USER\MyCustomRegKey
```

Description:

Export the target Registry key to the specified .REG file.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regedit.yml` |
| Evidence | Command preserved from source parser. |

### Import hidden registry data from alternate data stream

```text
regedit {PATH_ABSOLUTE}:regfile.reg
```

Description:

Import the target .REG file into the Registry.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regedit.yml` |
| Evidence | Command preserved from source parser. |
