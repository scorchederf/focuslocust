---
parsed_by: focuslocust
source: commands
type: generated
---
# csplit Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## csplit

Tool page: [csplit](../../tools/linux/csplit.md)

### file-read

```text
csplit /path/to/input-file 1
cat xx01
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csplit` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA >/path/to/temp-file
csplit -z -b '%doutput-file' /path/to/temp-file 1
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csplit` |
| Evidence | Function example preserved from source parser. |
