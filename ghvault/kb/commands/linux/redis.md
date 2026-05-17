---
parsed_by: focuslocust
source: commands
type: generated
---
# redis Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## redis

Tool page: [redis](../../tools/linux/redis.md)

### file-write

```text
redis-cli -h 127.0.0.1
config set dir /path/to/output-dir/
config set dbfilename output-file
set x "DATA"
save
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/redis` |
| Evidence | Function example preserved from source parser. |
