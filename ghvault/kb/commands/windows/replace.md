---
parsed_by: focuslocust
source: commands
type: generated
---
# Replace Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Replace.exe

Tool page: [Replace.exe](../../tools/windows/replace.exe.md)

### Copy files

```text
replace.exe {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE:folder} /A
```

Description:

Copy .cab file to destination

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Replace.yml` |
| Evidence | Command preserved from source parser. |

### Download file

```text
replace.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:folder} /A
```

Description:

Download/Copy executable to specified folder

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Replace.yml` |
| Evidence | Command preserved from source parser. |
