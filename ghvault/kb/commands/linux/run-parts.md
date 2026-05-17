---
parsed_by: focuslocust
source: commands
type: generated
---
# run-parts Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## run-parts

Tool page: [run-parts](../../tools/linux/run-parts.md)

### shell

```text
run-parts --new-session --regex '^sh$' /bin
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/run-parts` |
| Evidence | Function example preserved from source parser. |

### shell

```text
cp /bin/sh /path/to/temp-dir/
run-parts /path/to/temp-dir/
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/run-parts` |
| Evidence | Function example preserved from source parser. |
