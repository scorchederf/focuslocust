---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Application Window Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-enumeration-and-discovery-t1010-application-window-discovery` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/t1010-application-window-discovery.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Retrieving running application window titles:

## Preserved Body

````markdown
Retrieving running application window titles:
```csharp
get-process | where-object {$_.mainwindowtitle -ne ""} | Select-Object mainwindowtitle
```
![](<../../_assets/window-titles.png>)

A COM method that also includes the process path and window location coordinates:
```csharp
[activator]::CreateInstance([type]::GetTypeFromCLSID("13709620-C279-11CE-A49E-444553540000")).windows()
```
![](<../../_assets/Annotation 2019-06-18 224603.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/application-window-discovery.md)

## Evidence Excerpt

```text
_asset_filenames:
- Annotation 2019-06-18 224603.png
- window-titles.png
_body: '---
description: Discovery
---
# Application Window Discovery
Retrieving running application window titles:
```
