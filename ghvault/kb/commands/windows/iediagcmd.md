---
parsed_by: focuslocust
source: commands
type: generated
---
# iediagcmd Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## iediagcmd.exe

Tool page: [iediagcmd.exe](../../tools/windows/iediagcmd.exe.md)

### Spawn a pre-planted executable from iediagcmd.exe.

```text
set windir=c:\test& cd "C:\Program Files\Internet Explorer\" & iediagcmd.exe /out:{PATH_ABSOLUTE:.cab}
```

Description:

Executes binary that is pre-planted at C:\test\system32\netsh.exe.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Iediagcmd.yml` |
| Evidence | Command preserved from source parser. |
