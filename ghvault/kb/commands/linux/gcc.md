---
parsed_by: focuslocust
source: commands
type: generated
---
# gcc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## gcc

Tool page: [gcc](../../tools/linux/gcc.md)

### file-read

```text
gcc -x c -E /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcc` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
gcc @/path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcc` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
gcc -x c /dev/null -o /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcc` |
| Evidence | Function example preserved from source parser. |

### shell

```text
gcc -wrapper /bin/sh,-s x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcc` |
| Evidence | Function example preserved from source parser. |
