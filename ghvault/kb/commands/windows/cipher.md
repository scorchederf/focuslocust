---
parsed_by: focuslocust
source: commands
type: generated
---
# Cipher Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Cipher.exe

Tool page: [Cipher.exe](../../tools/windows/cipher.exe.md)

### Can be used to forensically erase a file.

```text
cipher /w:{PATH_ABSOLUTE:folder}
```

Description:

Zero out a file

Related ATT&CK:

- [T1485](../../attack/techniques/T1485-data-destruction.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cipher.yml` |
| Evidence | Command preserved from source parser. |

### Can be used to impair defences by e.g. encrypting a critical EDR solution file.

```text
cipher.exe /e {PATH_ABSOLUTE}
```

Description:

Encrypt a file

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cipher.yml` |
| Evidence | Command preserved from source parser. |
