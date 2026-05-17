---
parsed_by: focuslocust
source: commands
type: generated
---
# rustdoc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## rustdoc

Tool page: [rustdoc](../../tools/linux/rustdoc.md)

### file-read

```text
rustdoc /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustdoc` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo '//! DATA' >/path/to/temp-file
rustdoc /path/to/temp-file -o /path/to/output-dir/
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustdoc` |
| Evidence | Function example preserved from source parser. |
