---
parsed_by: focuslocust
source: commands
type: generated
---
# split Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## split

Tool page: [split](../../tools/linux/split.md)

### file-read

```text
split -b 999 --additional-suffix suffix /path/to/input-file prefix
cat prefixaasuffix
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/split` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
split -b 999 --additional-suffix suffix /path/to/input-file prefix
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/split` |
| Evidence | Function example preserved from source parser. |

### shell

```text
split --filter='/bin/sh -i 0<&2 1>&2' /etc/hosts
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/split` |
| Evidence | Function example preserved from source parser. |
