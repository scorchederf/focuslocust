---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rustc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rustc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rustc](../../tools/linux/rustc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rustc |
| name | rustc |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rustc/ |

## Preserved Source Material

```yaml
_body: ''
_name: rustc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustc
functions:
  file-read:
  - binary: false
    code: rustc /path/to/input-file
    comment: The compiler leaks some file lines in the compiler error.
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - code: 'echo ''fn main() { println!("DATA"); }'' >/path/to/temp-file

      rustc /path/to/temp-file -o /path/to/output-file'
    comment: The comment appears in the compiled program.
    contexts:
      sudo: null
      unprivileged: null
  inherit:
  - code: rustc --explain E0001
    contexts:
      sudo: null
      unprivileged: null
    from: less
```
