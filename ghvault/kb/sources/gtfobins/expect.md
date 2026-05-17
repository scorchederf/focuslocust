---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# expect

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `expect` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/expect` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [expect](../../tools/linux/expect.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | expect |
| name | expect |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/expect/ |

## Preserved Source Material

```yaml
_body: ''
_name: expect
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/expect
functions:
  file-read:
  - code: expect /path/to/input-file
    comment: The file is read and parsed as an `expect` command file, the content of the first invalid line is returned in
      an error message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: expect -c 'spawn /bin/sh;interact'
    contexts:
      sudo: null
      suid:
        code: expect -c 'spawn /bin/sh -p;interact'
        shell: false
      unprivileged: null
```
