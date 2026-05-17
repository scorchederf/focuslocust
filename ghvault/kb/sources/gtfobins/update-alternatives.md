---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# update-alternatives

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `update-alternatives` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/update-alternatives` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [update-alternatives](../../tools/linux/update-alternatives.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | update-alternatives |
| name | update-alternatives |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/update-alternatives/ |

## Preserved Source Material

```yaml
_body: ''
_name: update-alternatives
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/update-alternatives
functions:
  file-write:
  - code: 'echo DATA >/path/to/temp-file

      update-alternatives --force --install /path/to/output-file x /path/to/temp-file 0'
    comment: Write in `/path/to/output-file` a symlink to `/path/to/temp-file`.
    contexts:
      sudo: null
      suid: null
```
