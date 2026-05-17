---
parsed_by: focuslocust
source: commands
type: generated
---
# nano Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## nano

Tool page: [nano](../../tools/linux/nano.md)

### file-read

```text
nano /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nano` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
nano /path/to/output-file
DATA
^O
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nano` |
| Evidence | Function example preserved from source parser. |

### shell

```text
nano
^R^X
reset; sh 1>&0 2>&0
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nano` |
| Evidence | Function example preserved from source parser. |

### shell

```text
nano -s /bin/sh
/bin/sh
^T^T
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nano` |
| Evidence | Function example preserved from source parser. |
