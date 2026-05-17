---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# varnishncsa

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `varnishncsa` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/varnishncsa` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [varnishncsa](../../tools/linux/varnishncsa.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | varnishncsa |
| name | varnishncsa |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/varnishncsa/ |

## Preserved Source Material

````yaml
_body: ''
_name: varnishncsa
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/varnishncsa
comment: A running `varnishd` instance must be available.
functions:
  file-write:
  - binary: false
    code: varnishncsa -g request -q 'ReqURL ~ "/xxxxxxxxxx"' -F '%{yyy}i' -w /path/to/output-file
    comment: 'The command hangs, so the trigger command must be performed asynchronously or in another terminal:


      ```

      curl -H ''xxx: DATA'' http://localhost:6081/xxxxxxxxxx

      ```'
    contexts:
      sudo: null
      suid: null
````
