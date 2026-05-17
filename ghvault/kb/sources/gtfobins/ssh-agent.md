---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ssh-agent

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ssh-agent` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-agent` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ssh-agent](../../tools/linux/ssh-agent.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ssh-agent |
| name | ssh-agent |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ssh-agent/ |

## Preserved Source Material

```yaml
_body: ''
_name: ssh-agent
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-agent
functions:
  shell:
  - code: ssh-agent /bin/sh
    contexts:
      sudo: null
      suid:
        code: ssh-agent /bin/sh -p
        shell: false
      unprivileged: null
```
