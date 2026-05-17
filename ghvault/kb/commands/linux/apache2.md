---
parsed_by: focuslocust
source: commands
type: generated
---
# apache2 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## apache2

Tool page: [apache2](../../tools/linux/apache2.md)

### file-read

```text
apache2 -f /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apache2` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
apache2 -C 'Define APACHE_RUN_DIR /' -C 'Include /path/to/input-file'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apache2` |
| Evidence | Function example preserved from source parser. |
