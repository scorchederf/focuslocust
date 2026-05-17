---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# WinRS for Lateral Movement

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-winrs-for-lateral-movement` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/winrs-for-lateral-movement.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

It's possible to use a native Windows binary winrs to connect to a remote endpoint via WinRM like so:

## Preserved Body

````markdown
It's possible to use a native Windows binary `winrs` to connect to a remote endpoint via `WinRM` like so:

```
winrs -r:ws01 "cmd /c hostname & notepad"
```

Below shows how we connect from `DC01` to `WS01` and execute two processes `hostname`,`notepad` and the process partent/child relationship for processes spawned by the `winrshost.exe`:

![](<../../_assets/image (669).png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/winrs-for-lateral-movement.md)

## Evidence Excerpt

````text
_asset_filenames:
- image (669).png
_body: '# WinRS for Lateral Movement
It''s possible to use a native Windows binary `winrs` to connect to a remote endpoint via `WinRM` like so:
```
winrs -r:ws01 "cmd /c hostname & notepad"
```
Below shows how we connect from `DC01` to `WS01` and execute two processes `hostname`,`notepad` and the process partent/child
````
