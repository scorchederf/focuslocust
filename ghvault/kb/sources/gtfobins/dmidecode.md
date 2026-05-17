---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dmidecode

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dmidecode` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dmidecode` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dmidecode](../../tools/linux/dmidecode.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dmidecode |
| name | dmidecode |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dmidecode/ |

## Preserved Source Material

````yaml
_body: ''
_name: dmidecode
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dmidecode
functions:
  file-write:
  - binary: false
    code: dmidecode --no-sysfs -d x.dmi --dump-bin /path/to/output-file
    comment: 'It can be used to write files using a specially crafted SMBIOS file that can be read as a memory device by dmidecode.

      Generate the file with [dmiwrite](https://github.com/adamreiser/dmiwrite) and upload it to the target.


      - `--dump-bin`, will cause dmidecode to write the payload to the destination specified, prepended with 32 null bytes.


      - `--no-sysfs`, if the target system is using an older version of dmidecode, you may need to omit the option.


      ```

      make dmiwrite

      echo DATA >/path/to/temp-file

      ./dmiwrite /path/to/temp-file x.dmi

      ```'
    contexts:
      unprivileged: null
````
