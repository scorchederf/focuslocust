---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# procmail

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `procmail` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/procmail` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [procmail](../../tools/linux/procmail.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | procmail |
| name | procmail |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/procmail/ |

## Preserved Source Material

```yaml
_body: ''
_name: procmail
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/procmail
functions:
  command:
  - blind: false
    code: 'echo -e '':0\n| /path/to/command >/path/to/temp-file

      procmail -m /path/to/temp-file'
    comment: The program is picky about the file ownership, and waits for some input.
    contexts:
      sudo: null
      unprivileged: null
```
