---
parsed_by: focuslocust
source: commands
type: generated
---
# ip Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ip

Tool page: [ip](../../tools/linux/ip.md)

### file-read

```text
ip -force -batch /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ip` |
| Evidence | Function example preserved from source parser. |

### shell

```text
ip netns add foo
ip netns exec foo /bin/sh
ip netns delete foo
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ip` |
| Evidence | Function example preserved from source parser. |

### shell

```text
ip netns add foo
ip netns exec foo /bin/ln -s /proc/1/ns/net /var/run/netns/bar
ip netns exec bar /bin/sh
ip netns delete foo
ip netns delete bar
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ip` |
| Evidence | Function example preserved from source parser. |
