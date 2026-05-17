---
parsed_by: focuslocust
source: commands
type: generated
---
# mawk Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## mawk

Tool page: [mawk](../../tools/linux/mawk.md)

### file-read

```text
mawk '//' /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mawk` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
mawk 'BEGIN { print "DATA" > "/path/to/output-file" }'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mawk` |
| Evidence | Function example preserved from source parser. |

### shell

```text
mawk 'BEGIN {system("/bin/sh")}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mawk` |
| Evidence | Function example preserved from source parser. |
