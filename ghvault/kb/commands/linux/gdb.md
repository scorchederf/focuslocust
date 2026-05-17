---
parsed_by: focuslocust
source: commands
type: generated
---
# gdb Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## gdb

Tool page: [gdb](../../tools/linux/gdb.md)

### file-write

```text
gdb -nx -ex 'dump value /path/to/output-file "DATA"' -ex quit
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gdb` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
gdb -nx -ex 'python ...' -ex quit
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gdb` |
| Evidence | Function example preserved from source parser. |

### shell

```text
gdb -nx -ex '!/bin/sh' -ex quit
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gdb` |
| Evidence | Function example preserved from source parser. |
