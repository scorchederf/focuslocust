---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Simple TCP Relaying with NetCat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-simple-tcp-relaying-with-netcat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/simple-tcp-relaying-with-netcat.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Simple TCP Relaying with NetCat](../../topics/offensive-security/simple-tcp-relaying-with-netcat.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-simple-tcp-relaying-with-netcat |
| name | Simple TCP Relaying with NetCat |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/simple-tcp-relaying-with-netcat.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2019-01-11 11-06.gif
_body: '# Simple TCP Relaying with NetCat


  This is a simple lab that looks at how to setup a traffic relay using netcat.


  We are amining to create a relay between ports 4444 and 22 - any traffic coming to 4444 will be redirected to port 22.


  ```bash

  # setup listener on port 22

  nc -lvvp 22


  # setup listener on port 4444 and direct stdout to port 22 using netcat

  nc -lvvp 4444 | nc localhost 22


  # send a string "test" to port 4444 using netcat

  echo test | nc localhost 4444

  ```


  Below is an animated demo of how this all works in action:


  ![](<../../.gitbook/assets/Peek 2019-01-11 11-06.gif>)'
_relative_path: offensive-security/lateral-movement/simple-tcp-relaying-with-netcat.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/simple-tcp-relaying-with-netcat.md
````
