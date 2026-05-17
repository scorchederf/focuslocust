---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cmake

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cmake` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cmake` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [cmake](../../tools/linux/cmake.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cmake |
| name | cmake |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/cmake/ |

## Preserved Source Material

```yaml
_body: ''
_name: cmake
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cmake
functions:
  file-read:
  - code: cmake -E cat /path/to/input-file
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: 'echo ''execute_process(COMMAND /bin/sh)'' >/path/to/CMakeLists.txt

      cmake /path/to/'
    contexts:
      sudo: null
      unprivileged: null
```
