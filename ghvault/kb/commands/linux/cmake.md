---
parsed_by: focuslocust
source: commands
type: generated
---
# cmake Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## cmake

Tool page: [cmake](../../tools/linux/cmake.md)

### file-read

```text
cmake -E cat /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cmake` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo 'execute_process(COMMAND /bin/sh)' >/path/to/CMakeLists.txt
cmake /path/to/
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cmake` |
| Evidence | Function example preserved from source parser. |
