---
parsed_by: focuslocust
source: commands
type: generated
---
# nohup Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## nohup

Tool page: [nohup](../../tools/linux/nohup.md)

### command

```text
nohup /path/to/command
cat nohup.out
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nohup` |
| Evidence | Function example preserved from source parser. |

### shell

```text
nohup /bin/sh -c '/bin/sh </dev/tty >/dev/tty 2>/dev/tty'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nohup` |
| Evidence | Function example preserved from source parser. |
