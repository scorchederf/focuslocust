---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ssh-keyscan

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ssh-keyscan` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-keyscan` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ssh-keyscan](../../tools/linux/ssh-keyscan.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ssh-keyscan |
| name | ssh-keyscan |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ssh-keyscan/ |

## Preserved Source Material

```yaml
_body: ''
_name: ssh-keyscan
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-keyscan
functions:
  file-read:
  - code: ssh-keyscan -f /path/to/input-file
    comment: The file content is actually parsed so only a part of each line is returned as a part of an error message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
