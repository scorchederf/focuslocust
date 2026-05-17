---
parsed_by: focuslocust
source: commands
type: generated
---
# msgfilter Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## msgfilter

Tool page: [msgfilter](../../tools/linux/msgfilter.md)

### file-read

```text
msgfilter -P -i /path/to/input-file /bin/cat
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgfilter` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo x | msgfilter -P /bin/sh -c '/bin/sh 0<&2 1>&2; kill $PPID'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgfilter` |
| Evidence | Function example preserved from source parser. |
