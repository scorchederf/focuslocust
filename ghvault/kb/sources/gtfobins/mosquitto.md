---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mosquitto

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mosquitto` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mosquitto` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [mosquitto](../../tools/linux/mosquitto.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mosquitto |
| name | mosquitto |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/mosquitto/ |

## Preserved Source Material

```yaml
_body: ''
_name: mosquitto
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mosquitto
functions:
  file-read:
  - code: mosquitto -c /path/to/input-file
    comment: The file is actually parsed and the first wrong line (ending with a newline or a null character) is returned
      in an error message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
