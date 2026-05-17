---
parsed_by: focuslocust
source: commands
type: generated
---
# jshell Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## jshell

Tool page: [jshell](../../tools/linux/jshell.md)

### file-read

```text
jshell
jshell> /open /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jshell` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
jshell
String x = "DATA";
/save /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jshell` |
| Evidence | Function example preserved from source parser. |

### shell

```text
jshell
Runtime.getRuntime().exec("/path/to/command");
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jshell` |
| Evidence | Function example preserved from source parser. |
