---
parsed_by: focuslocust
source: commands
type: generated
---
# Pester.bat Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Pester.bat

Tool page: [Pester.bat](../../tools/windows/pester.bat.md)

### Proxy execution

```text
Pester.bat [/help|?|-?|/?] "$null; {CMD}"
```

Description:

Execute code using Pester. The third parameter can be anything. The fourth is the payload.

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/pester.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution

```text
Pester.bat ;{PATH:.exe}
```

Description:

Execute code using Pester. Example here executes specified executable.

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/pester.yml` |
| Evidence | Command preserved from source parser. |
