---
parsed_by: focuslocust
source: commands
type: generated
---
# setfacl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## setfacl

Tool page: [setfacl](../../tools/linux/setfacl.md)

### privilege-escalation

```text
setfacl -m u:$(id -un):rwx /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setfacl` |
| Evidence | Function example preserved from source parser. |
