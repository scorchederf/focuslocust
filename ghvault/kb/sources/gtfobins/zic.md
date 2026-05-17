---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# zic

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `zic` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zic` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [zic](../../tools/linux/zic.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | zic |
| name | zic |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/zic/ |

## Preserved Source Material

```yaml
_body: ''
_name: zic
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zic
functions:
  command:
  - code: 'echo ''Rule Jordan 0 1 xxx Jan lastSun 2 1:00d -'' >/path/to/temp-file

      echo ''Zone Test 2:00 Jordan CE%sT'' >>/path/to/temp-file

      zic -d . -y /path/to/command /path/to/temp-file'
    comment: 'This executes the command twice:


      - `/path/to/command 0 xxx`

      - `/path/to/command 1 xxx`


      Additionally the `Test` file is created.'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
