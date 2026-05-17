---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fail2ban-client

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fail2ban-client` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fail2ban-client` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [fail2ban-client](../../tools/linux/fail2ban-client.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | fail2ban-client |
| name | fail2ban-client |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/fail2ban-client/ |

## Preserved Source Material

```yaml
_body: ''
_name: fail2ban-client
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fail2ban-client
functions:
  command:
  - blind: true
    code: 'fail2ban-client add x

      fail2ban-client set x addaction x

      fail2ban-client set x action x actionban /path/to/command

      fail2ban-client start x

      fail2ban-client set x banip 999.999.999.999

      fail2ban-client set x unbanip 999.999.999.999

      fail2ban-client stop x'
    comment: The subprocess is immediately sent to the background, but `fail2ban-client` waits on a return code from the subprocess.
      The `banip` command will hang until the subprocess returns.
    contexts:
      sudo: null
  - blind: true
    code: 'cat >/path/to/temp-dir/fail2ban.conf <<EOF

      [Definition]

      EOF


      cat >/path/to/temp-dir/jail.local <<EOF

      [x]

      enabled = true

      action = x

      EOF


      mkdir -p /path/to/temp-dir/action.d/

      cat >/path/to/temp-dir/action.d/x.conf <<EOF

      [Definition]

      actionstart = /path/to/command

      EOF


      mkdir -p /path/to/temp-dir/filter.d/

      cat >/path/to/temp-dir/filter.d/x.conf <<EOF

      [Definition]

      EOF


      fail2ban-client -c /path/to/temp-dir/ -v restart'
    contexts:
      sudo: null
```
