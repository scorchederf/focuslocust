---
parsed_by: focuslocust
source: commands
type: generated
---
# ltrace Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ltrace

Tool page: [ltrace](../../tools/linux/ltrace.md)

### file-read

```text
ltrace -F /path/to/input-file /dev/null
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ltrace` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
ltrace -s 999 -o /path/to/input-file ltrace -F DATA
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ltrace` |
| Evidence | Function example preserved from source parser. |

### shell

```text
ltrace -b -L /bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ltrace` |
| Evidence | Function example preserved from source parser. |
