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

## Summary

GTFOBins entry for docker covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/docker.md)
- Source verification: [source record](../../sources/gtfobins/docker.md)

## Aliases

- `docker`

## Source Verification

[source record](../../sources/gtfobins/docker.md)

## Evidence Excerpt

```text
_body: ''
_name: docker
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/docker
comment: This requires the user to be privileged enough to run `docker`, e.g., being in the `docker` group or being `root`.
functions:
file-read:
- code: 'docker cp /path/to/input-file $CONTAINER_ID:input-file
docker cp $CONTAINER_ID:input-file /path/to/temp-file
```
