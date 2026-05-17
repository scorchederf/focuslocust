---
parsed_by: focuslocust
source: commands
type: generated
---
# csvtool Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## csvtool

Tool page: [csvtool](../../tools/linux/csvtool.md)

### file-read

```text
csvtool trim t /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csvtool` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA >/path/to/temp-file
csvtool trim t /path/to/temp-file -o /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csvtool` |
| Evidence | Function example preserved from source parser. |

### shell

```text
csvtool call '/bin/sh;false' /etc/hosts
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csvtool` |
| Evidence | Function example preserved from source parser. |
