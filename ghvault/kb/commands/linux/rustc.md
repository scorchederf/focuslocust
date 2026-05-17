---
parsed_by: focuslocust
source: commands
type: generated
---
# rustc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## rustc

Tool page: [rustc](../../tools/linux/rustc.md)

### file-read

```text
rustc /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustc` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo 'fn main() { println!("DATA"); }' >/path/to/temp-file
rustc /path/to/temp-file -o /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustc` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
rustc --explain E0001
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustc` |
| Evidence | Function example preserved from source parser. |
