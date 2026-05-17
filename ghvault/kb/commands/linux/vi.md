---
parsed_by: focuslocust
source: commands
type: generated
---
# vi Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## vi

Tool page: [vi](../../tools/linux/vi.md)

### file-read

```text
vi /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vi` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
vi /path/to/output-file
iDATA
^[
w
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vi` |
| Evidence | Function example preserved from source parser. |

### shell

```text
vi -c ':!/bin/sh' /dev/null
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vi` |
| Evidence | Function example preserved from source parser. |

### shell

```text
vi -c ':shell'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vi` |
| Evidence | Function example preserved from source parser. |

### shell

```text
vi -c ':set shell=/bin/sh | shell'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vi` |
| Evidence | Function example preserved from source parser. |

### shell

```text
vi -c :terminal /bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vi` |
| Evidence | Function example preserved from source parser. |
