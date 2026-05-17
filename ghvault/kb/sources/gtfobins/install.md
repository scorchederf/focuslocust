---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# install

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `install` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/install` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [install](../../tools/linux/install.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | install |
| name | install |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/install/ |

## Preserved Source Material

```yaml
_body: ''
_name: install
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/install
functions:
  privilege-escalation:
  - code: install -m 6777 /path/to/input-file /path/to/output-dir/
    comment: This can be run with elevated privileges to change permissions (`6` denotes the SUID bits) and then read, write,
      or execute a file.
    contexts:
      sudo: null
      suid: null
```
