---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# iconv

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `iconv` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iconv` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [iconv](../../tools/linux/iconv.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iconv |
| name | iconv |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/iconv/ |

## Preserved Source Material

```yaml
_body: ''
_name: iconv
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iconv
comment: The `8859_1` encoding is used as it accepts any single-byte sequence, thus it allows to read/write arbitrary files.
  Other encoding combinations may corrupt the result.
functions:
  file-read:
  - code: iconv -f 8859_1 -t 8859_1 /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: echo DATA | iconv -f 8859_1 -t 8859_1 -o /path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
