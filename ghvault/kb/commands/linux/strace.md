---
parsed_by: focuslocust
source: commands
type: generated
---
# strace Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## strace

Tool page: [strace](../../tools/linux/strace.md)

### file-write

```text
strace -s 999 -o /path/to/output-file strace - DATA
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/strace` |
| Evidence | Function example preserved from source parser. |

### shell

```text
strace -o /dev/null /bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/strace` |
| Evidence | Function example preserved from source parser. |
