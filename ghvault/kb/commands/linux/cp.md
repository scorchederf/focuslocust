---
parsed_by: focuslocust
source: commands
type: generated
---
# cp Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## cp

Tool page: [cp](../../tools/linux/cp.md)

### file-read

```text
cp /path/to/input-file /dev/stdout
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cp` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA | cp /dev/stdin /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cp` |
| Evidence | Function example preserved from source parser. |

### privilege-escalation

```text
cp /path/to/input-file /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cp` |
| Evidence | Function example preserved from source parser. |

### privilege-escalation

```text
cp --attributes-only --preserve=all /path/to/input-file /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cp` |
| Evidence | Function example preserved from source parser. |
