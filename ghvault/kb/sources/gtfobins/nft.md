---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nft

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nft` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nft` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nft](../../tools/linux/nft.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nft |
| name | nft |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nft/ |

## Preserved Source Material

```yaml
_body: ''
_name: nft
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nft
functions:
  file-read:
  - code: nft -f /path/to/input-file
    comment: The content is actually parsed and corrupted by the command.
    contexts:
      sudo: null
      unprivileged: null
    version: '`nftables` >= 0.9.0'
```
