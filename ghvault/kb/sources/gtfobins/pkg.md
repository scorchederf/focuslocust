---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pkg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pkg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pkg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pkg](../../tools/linux/pkg.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pkg |
| name | pkg |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pkg/ |

## Preserved Source Material

````yaml
_body: ''
_name: pkg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pkg
functions:
  command:
  - code: pkg install -y --no-repo-update ./x-1.0.txz
    comment: 'Generate the FreeBSD package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.


      ```

      echo /path/to/command >x.sh

      fpm -n x -s dir -t freebsd -a all --before-install x.sh .

      ```'
    contexts:
      sudo: null
````
