---
parsed_by: focuslocust
source: commands
type: generated
---
# Pktmon Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Pktmon.exe

Tool page: [Pktmon.exe](../../tools/windows/pktmon.exe.md)

### use this a built in network sniffer on windows 10 to capture senstive traffic

```text
pktmon.exe start --etw
```

Description:

Will start a packet capture and store log file as PktMon.etl. Use pktmon.exe stop

Related ATT&CK:

- [T1040](../../attack/techniques/T1040-network-sniffing.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pktmon.yml` |
| Evidence | Command preserved from source parser. |

### Look for interesting traffic such as telent or FTP

```text
pktmon.exe filter add -p 445
```

Description:

Select Desired ports for packet capture

Related ATT&CK:

- [T1040](../../attack/techniques/T1040-network-sniffing.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pktmon.yml` |
| Evidence | Command preserved from source parser. |
