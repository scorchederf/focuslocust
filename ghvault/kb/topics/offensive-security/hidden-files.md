---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Hidden Files

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-t1158-hidden-files` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1158-hidden-files.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Hiding the file mantvydas.sdb using a native windows binary:

## Preserved Body

````markdown
## Execution

Hiding the file mantvydas.sdb using a native windows binary:
```csharp
PS C:\experiments> attrib.exe +h .\mantvydas.sdb
```
Note how powershell \(or cmd\) says the file does not exist, however you can type out its contents if you know the file exists:

![](<../../_assets/attrib-nofile.png>)

Note, that `dir /a:h` \(attribute: hidden\) reveals files with a "hidden" attribute set:

![](<../../_assets/attrib-reveal.png>)

## Observations

As usual, monitoring commandline arguments may be a good idea if you want to identify these events:

![](<../../_assets/attrib-set.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/hidden-files.md)

## Evidence Excerpt

```text
_asset_filenames:
- attrib-nofile.png
- attrib-reveal.png
- attrib-set.png
_body: '---
description: ''Defense Evasion, Persistence''
---
# Hidden Files
```
