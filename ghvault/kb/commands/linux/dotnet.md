---
parsed_by: focuslocust
source: commands
type: generated
---
# dotnet Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## dotnet

Tool page: [dotnet](../../tools/linux/dotnet.md)

### file-read

```text
dotnet fsi
System.IO.File.ReadAllText("/path/to/input-file");;
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dotnet` |
| Evidence | Function example preserved from source parser. |

### shell

```text
dotnet fsi
System.Diagnostics.Process.Start("/bin/sh").WaitForExit();;
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dotnet` |
| Evidence | Function example preserved from source parser. |
