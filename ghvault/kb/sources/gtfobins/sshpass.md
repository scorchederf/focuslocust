---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sshpass

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sshpass` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshpass` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [sshpass](../../tools/linux/sshpass.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sshpass |
| name | sshpass |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/sshpass/ |

## Preserved Source Material

```yaml
_body: ''
_name: sshpass
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshpass
functions:
  shell:
  - code: sshpass /bin/sh
    contexts:
      sudo: null
      suid:
        code: sshpass /bin/sh -p
        shell: false
      unprivileged: null
```
