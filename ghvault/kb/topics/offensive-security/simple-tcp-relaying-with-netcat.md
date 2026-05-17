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

## Summary

This is a simple lab that looks at how to setup a traffic relay using netcat.

## Preserved Body

````markdown
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

![](<../../_assets/Peek 2019-01-11 11-06.gif>)
````

## Source Verification

[source record](../../sources/redteamingtactics/simple-tcp-relaying-with-netcat.md)

## Evidence Excerpt

````text
_asset_filenames:
- Peek 2019-01-11 11-06.gif
_body: '# Simple TCP Relaying with NetCat
This is a simple lab that looks at how to setup a traffic relay using netcat.
We are amining to create a relay between ports 4444 and 22 - any traffic coming to 4444 will be redirected to port 22.
```bash
# setup listener on port 22
nc -lvvp 22
````
