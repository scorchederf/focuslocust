---
parsed_by: focuslocust
source: commands
type: generated
---
# Cscript Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Cscript.exe

Tool page: [Cscript.exe](../../tools/windows/cscript.exe.md)

### Can be used to evade defensive countermeasures or to hide as a persistence mechanism

```text
cscript //e:vbscript {PATH_ABSOLUTE}:script.vbs
```

Description:

Use cscript.exe to exectute a Visual Basic script stored in an Alternate Data Stream (ADS).

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cscript.yml` |
| Evidence | Command preserved from source parser. |
