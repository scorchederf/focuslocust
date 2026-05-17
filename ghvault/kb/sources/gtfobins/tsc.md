---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tsc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tsc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tsc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tsc](../../tools/linux/tsc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tsc |
| name | tsc |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tsc/ |

## Preserved Source Material

```yaml
_body: ''
_name: tsc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tsc
functions:
  file-read:
  - binary: false
    code: tsc /path/to/input-file.ts
    comment: Content is leaked as error messages. The file extension must be one of the supported ones, e.g., `.ts`, `.tsx`,
      etc.
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - binary: false
    code: tsc /path/to/input-file.ts --outFile /path/to/output-file
    comment: Content is leaked as error messages and written to file. The file extension must be one of the supported ones,
      e.g., `.ts`, `.tsx`, etc.
    contexts:
      sudo: null
      unprivileged: null
```
