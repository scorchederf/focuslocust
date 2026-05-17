---
parsed_by: focuslocust
source: commands
type: generated
---
# dosbox Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## dosbox

Tool page: [dosbox](../../tools/linux/dosbox.md)

### file-read

```text
dosbox -c 'mount c /' -c 'type c:\path\to\input'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dosbox` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
dosbox -c 'mount c /' -c 'copy c:\path\to\input c:\path\to\output' -c exit
cat /path/to/OUTPUT
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dosbox` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
dosbox -c 'mount c /' -c "echo DATA >c:\path\to\output" -c exit
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dosbox` |
| Evidence | Function example preserved from source parser. |
