---
parsed_by: focuslocust
source: commands
type: generated
---
# ed Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ed

Tool page: [ed](../../tools/linux/ed.md)

### file-read

```text
ed /path/to/input-file
,p
q
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ed` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
ed /path/to/output-file
a
DATA
.
w
q
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ed` |
| Evidence | Function example preserved from source parser. |

### shell

```text
ed
!/bin/sh
q
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ed` |
| Evidence | Function example preserved from source parser. |
