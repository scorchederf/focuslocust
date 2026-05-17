---
parsed_by: focuslocust
source: commands
type: generated
---
# vsls-agent Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## vsls-agent.exe

Tool page: [vsls-agent.exe](../../tools/windows/vsls-agent.exe.md)

### Execute proxied payload with Microsoft signed binary

```text
vsls-agent.exe --agentExtensionPath {PATH_ABSOLUTE:.dll}
```

Description:

Load a library payload using the --agentExtensionPath parameter (32-bit)

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/vsls-agent.yml` |
| Evidence | Command preserved from source parser. |
