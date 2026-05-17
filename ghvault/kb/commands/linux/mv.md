---
parsed_by: focuslocust
source: commands
type: generated
---
# mv Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## mv

Tool page: [mv](../../tools/linux/mv.md)

### file-write

```text
echo DATA >/path/to/temp-file
mv /path/to/temp-file /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mv` |
| Evidence | Function example preserved from source parser. |

### privilege-escalation

```text
mv /path/to/input-file /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mv` |
| Evidence | Function example preserved from source parser. |
