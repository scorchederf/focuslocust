---
parsed_by: focuslocust
source: commands
type: generated
---
# sysctl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## sysctl

Tool page: [sysctl](../../tools/linux/sysctl.md)

### command

```text
sysctl 'kernel.core_pattern=|/path/to/command'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sysctl` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
sysctl -n "/../../path/to/input-file"
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sysctl` |
| Evidence | Function example preserved from source parser. |
