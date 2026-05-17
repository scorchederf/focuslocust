---
parsed_by: focuslocust
source: commands
type: generated
---
# wireshark Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## wireshark

Tool page: [wireshark](../../tools/linux/wireshark.md)

### file-write

```text
wireshark -c 1 -i lo -k -f 'udp port 12345' &
echo DATA | nc -u 127.127.127.127 12345
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wireshark` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
wireshark
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wireshark` |
| Evidence | Function example preserved from source parser. |
