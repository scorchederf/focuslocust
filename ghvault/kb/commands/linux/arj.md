---
parsed_by: focuslocust
source: commands
type: generated
---
# arj Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## arj

Tool page: [arj](../../tools/linux/arj.md)

### file-read

```text
arj a /path/to/output-file /path/to/input-file
arj p /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arj` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA >output-file
arj a x output-file
arj e x /path/to/output-dir/
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arj` |
| Evidence | Function example preserved from source parser. |
