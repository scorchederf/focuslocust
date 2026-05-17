---
parsed_by: focuslocust
source: commands
type: generated
---
# emacs Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## emacs

Tool page: [emacs](../../tools/linux/emacs.md)

### file-read

```text
emacs /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/emacs` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
emacs /path/to/output-file
DATA
C-x C-s
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/emacs` |
| Evidence | Function example preserved from source parser. |

### shell

```text
emacs -Q -nw --eval '(term "/bin/sh")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/emacs` |
| Evidence | Function example preserved from source parser. |
