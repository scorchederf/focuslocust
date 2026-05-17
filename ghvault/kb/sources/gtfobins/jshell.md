---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# jshell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `jshell` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jshell` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [jshell](../../tools/linux/jshell.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | jshell |
| name | jshell |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/jshell/ |

## Preserved Source Material

```yaml
_body: ''
_name: jshell
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jshell
functions:
  file-read:
  - binary: false
    code: 'jshell

      jshell> /open /path/to/input-file'
    comment: The content is leaked as error messages.
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - binary: false
    code: 'jshell

      String x = "DATA";

      /save /path/to/output-file'
    comment: Writes only the valid Java code to file.
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - blind: true
    code: 'jshell

      Runtime.getRuntime().exec("/path/to/command");'
    contexts:
      sudo: null
      unprivileged: null
```
