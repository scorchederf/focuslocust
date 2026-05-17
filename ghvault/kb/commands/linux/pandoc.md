---
parsed_by: focuslocust
source: commands
type: generated
---
# pandoc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## pandoc

Tool page: [pandoc](../../tools/linux/pandoc.md)

### file-read

```text
pandoc -t plain /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pandoc` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA | pandoc -t plain -o /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pandoc` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
echo '...' >/path/to/temp-file
pandoc -L /path/to/temp-file /dev/null
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pandoc` |
| Evidence | Function example preserved from source parser. |
