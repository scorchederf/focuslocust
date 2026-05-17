---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nmap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nmap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nmap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nmap](../../tools/linux/nmap.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nmap |
| name | nmap |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nmap/ |

## Preserved Source Material

```yaml
_body: ''
_name: nmap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nmap
functions:
  file-read:
  - binary: false
    code: nmap -iL /path/to/input-file
    comment: The file is actually parsed as a list of hosts/networks, lines are leaked through error messages.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: nmap -oG=/path/to/output-file DATA
    comment: The payload appears inside the regular nmap output.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  inherit:
  - code: 'echo ''...'' >/path/to/temp-file

      nmap --script=/path/to/temp-file'
    comment: This allows to run Lua code (`...`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: lua
  shell:
  - code: 'nmap --interactive

      !/bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
    version: 2.02 to 5.21
```
