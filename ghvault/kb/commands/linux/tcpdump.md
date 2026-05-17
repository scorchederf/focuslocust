---
parsed_by: focuslocust
source: commands
type: generated
---
# tcpdump Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## tcpdump

Tool page: [tcpdump](../../tools/linux/tcpdump.md)

### command

```text
echo /path/to/command >/path/to/temp-file
chmod +x /path/to/temp-file
tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tcpdump` |
| Evidence | Function example preserved from source parser. |

### command

```text
tcpdump -ln -i lo -w 'command-argument' -W 1 -G 1 -z /path/to/command
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tcpdump` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
tcpdump -ln -i lo -w /path/to/output-file -c 1 -Z user
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tcpdump` |
| Evidence | Function example preserved from source parser. |
