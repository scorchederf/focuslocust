---
parsed_by: focuslocust
source: commands
type: generated
---
# xxd Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## xxd

Tool page: [xxd](../../tools/linux/xxd.md)

### file-read

```text
xxd /path/to/input-file | xxd -r
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xxd` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA | xxd | xxd -r - /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xxd` |
| Evidence | Function example preserved from source parser. |
