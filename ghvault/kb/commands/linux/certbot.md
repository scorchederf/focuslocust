---
parsed_by: focuslocust
source: commands
type: generated
---
# certbot Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## certbot

Tool page: [certbot](../../tools/linux/certbot.md)

### shell

```text
certbot certonly -n -d x --standalone --dry-run --agree-tos --email x --logs-dir . --work-dir . --config-dir . --pre-hook '/bin/sh 1>&0 2>&0'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/certbot` |
| Evidence | Function example preserved from source parser. |
