---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# clamscan

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `clamscan` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/clamscan` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [clamscan](../../tools/linux/clamscan.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | clamscan |
| name | clamscan |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/clamscan/ |

## Preserved Source Material

```yaml
_body: ''
_name: clamscan
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/clamscan
functions:
  file-read:
  - binary: false
    code: 'touch x.yara

      clamscan --no-summary -d x.yara -f /path/to/input-file 2>&1 | sed -nE ''s/^(.*): No such file or directory$/\1/p'''
    comment: Each line of the file is interpreted as a path and the content is leaked via error messages. The output can optionally
      be cleaned using `sed`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
