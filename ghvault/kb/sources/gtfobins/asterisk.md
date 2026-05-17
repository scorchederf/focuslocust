---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# asterisk

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `asterisk` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/asterisk` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [asterisk](../../tools/linux/asterisk.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | asterisk |
| name | asterisk |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/asterisk/ |

## Preserved Source Material

```yaml
_body: ''
_name: asterisk
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/asterisk
functions:
  shell:
  - code: 'asterisk -r

      !/bin/sh'
    comment: A server instance must be already running, otherwise it can be started with `sudo asterisk -F`. Moreover, the
      invoking user must be able to access the socket.
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
