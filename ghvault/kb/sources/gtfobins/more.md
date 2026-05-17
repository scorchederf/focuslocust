---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# more

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `more` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/more` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [more](../../tools/linux/more.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | more |
| name | more |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/more/ |

## Preserved Source Material

```yaml
_body: ''
_name: more
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/more
functions:
  file-read:
  - code: more /path/to/input-file
    comment: The file is displayed in the terminal interface.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'more /etc/hosts

      !/bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
