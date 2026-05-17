---
parsed_by: focuslocust
source: commands
type: generated
---
# nmap Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## nmap

Tool page: [nmap](../../tools/linux/nmap.md)

### file-read

```text
nmap -iL /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nmap` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
nmap -oG=/path/to/output-file DATA
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nmap` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
echo '...' >/path/to/temp-file
nmap --script=/path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nmap` |
| Evidence | Function example preserved from source parser. |

### shell

```text
nmap --interactive
!/bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nmap` |
| Evidence | Function example preserved from source parser. |
