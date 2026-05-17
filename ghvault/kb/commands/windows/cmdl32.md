---
parsed_by: focuslocust
source: commands
type: generated
---
# cmdl32 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## cmdl32.exe

Tool page: [cmdl32.exe](../../tools/windows/cmdl32.exe.md)

### Download file from Internet

```text
cmdl32 /vpn /lan %cd%\config
```

Description:

Download a file from the web address specified in the configuration file. The downloaded file will be in %TMP% under the name VPNXXXX.tmp where "X" denotes a random number or letter.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmdl32.yml` |
| Evidence | Command preserved from source parser. |
