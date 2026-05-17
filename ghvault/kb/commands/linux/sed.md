---
parsed_by: focuslocust
source: commands
type: generated
---
# sed Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## sed

Tool page: [sed](../../tools/linux/sed.md)

### file-read

```text
sed '' /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sed` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
sed -n '1s/.*/DATA/w /path/to/output-file' /etc/hosts
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sed` |
| Evidence | Function example preserved from source parser. |

### shell

```text
sed -n '1e exec /bin/sh 1>&0' /etc/hosts
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sed` |
| Evidence | Function example preserved from source parser. |

### shell

```text
sed e
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sed` |
| Evidence | Function example preserved from source parser. |
