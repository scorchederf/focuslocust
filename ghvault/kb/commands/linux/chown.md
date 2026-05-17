---
parsed_by: focuslocust
source: commands
type: generated
---
# chown Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## chown

Tool page: [chown](../../tools/linux/chown.md)

### privilege-escalation

```text
chown $(id -un):$(id -gn) /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chown` |
| Evidence | Function example preserved from source parser. |
