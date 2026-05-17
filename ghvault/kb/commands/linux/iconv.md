---
parsed_by: focuslocust
source: commands
type: generated
---
# iconv Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## iconv

Tool page: [iconv](../../tools/linux/iconv.md)

### file-read

```text
iconv -f 8859_1 -t 8859_1 /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iconv` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA | iconv -f 8859_1 -t 8859_1 -o /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iconv` |
| Evidence | Function example preserved from source parser. |
