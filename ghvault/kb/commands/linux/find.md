---
parsed_by: focuslocust
source: commands
type: generated
---
# find Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## find

Tool page: [find](../../tools/linux/find.md)

### file-read

```text
find /path/to/input-file -exec cat {} \;
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/find` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
find / -fprintf /path/to/output-file DATA -quit
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/find` |
| Evidence | Function example preserved from source parser. |

### shell

```text
find . -exec /bin/sh \; -quit
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/find` |
| Evidence | Function example preserved from source parser. |
