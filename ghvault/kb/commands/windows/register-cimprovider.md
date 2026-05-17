---
parsed_by: focuslocust
source: commands
type: generated
---
# Register-cimprovider Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Register-cimprovider.exe

Tool page: [Register-cimprovider.exe](../../tools/windows/register-cimprovider.exe.md)

### Execute code within dll file

```text
Register-cimprovider -path {PATH_ABSOLUTE:.dll}
```

Description:

Load the target .DLL.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Register-cimprovider.yml` |
| Evidence | Command preserved from source parser. |
