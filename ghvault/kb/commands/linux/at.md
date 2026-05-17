---
parsed_by: focuslocust
source: commands
type: generated
---
# at Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## at

Tool page: [at](../../tools/linux/at.md)

### command

```text
echo /path/to/command | at now
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/at` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo "/bin/sh <$(tty) >$(tty) 2>$(tty)" | at now; tail -f /dev/null
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/at` |
| Evidence | Function example preserved from source parser. |
