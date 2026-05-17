---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dosbox

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dosbox` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dosbox` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dosbox](../../tools/linux/dosbox.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dosbox |
| name | dosbox |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dosbox/ |

## Preserved Source Material

```yaml
_body: ''
_name: dosbox
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dosbox
comment: Basically `dosbox` allows to mount the local file system, so that it can be altered using DOS commands. Note that
  the DOS filename convention ([8.3](https://en.wikipedia.org/wiki/8.3_filename)) is used.
functions:
  file-read:
  - code: dosbox -c 'mount c /' -c 'type c:\path\to\input'
    comment: The file content will be displayed in the DOSBox graphical window.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - code: 'dosbox -c ''mount c /'' -c ''copy c:\path\to\input c:\path\to\output'' -c exit

      cat /path/to/OUTPUT'
    comment: The file is copied to a readable location.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: dosbox -c 'mount c /' -c "echo DATA >c:\path\to\output" -c exit
    comment: Note that `echo` terminates the string with a DOS-style line terminator (`\r\n`), if that's a problem and your
      scenario allows it, you can create the file outside `dosbox`, then use `copy` to do the actual write.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
