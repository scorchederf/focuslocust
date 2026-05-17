---
parsed_by: focuslocust
source: commands
type: generated
---
# neofetch Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## neofetch

Tool page: [neofetch](../../tools/linux/neofetch.md)

### file-read

```text
neofetch --ascii /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/neofetch` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo 'exec /bin/sh' >/path/to/temp-file
neofetch --config /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/neofetch` |
| Evidence | Function example preserved from source parser. |
