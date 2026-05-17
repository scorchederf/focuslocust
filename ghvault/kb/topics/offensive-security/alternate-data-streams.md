---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Alternate Data Streams

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-t1096-alternate-data-streams` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1096-alternate-data-streams.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Creating a benign text file:

## Preserved Body

````markdown
## Execution

Creating a benign text file:
```csharp
echo "this is benign" > benign.txt
Get-ChildItem
```
![](<../../_assets/ads-benign.png>)

![](broken-reference)

Hiding an `evil.txt` file inside the `benign.txt`
```csharp
cmd '/c echo "this is evil" > benign.txt:evil.txt'
```
![](<../../_assets/ads-evil.png>)

![](broken-reference)

Note how the evil.txt file is not visible through the explorer - that is because it is in the alternate data stream now. Opening the benign.txt shows no signs of evil.txt. However, the data from evil.txt can still be accessed as shown below in the commandline - `type benign.txt:evil.txt`:

![](<../../_assets/ads-evil-2.png>)

Additionally, we can view the data in the notepad as well by issuing:
```csharp
notepad .\benign.txt:evil.txt
```
![](<../../_assets/ads-evil3.png>)

## Observations

![](<../../_assets/ads-commandline.png>)

Note that powershell can also help finding alternate data streams:

```csharp
Get-Item c:\experiment\evil.txt -Stream *
Get-Content .\benign.txt -Stream evil.txt
```

![](<../../_assets/ads-powershell.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/alternate-data-streams.md)

## Evidence Excerpt

```text
_asset_filenames:
- ads-benign.png
- ads-commandline.png
- ads-evil-2.png
- ads-evil.png
- ads-evil3.png
- ads-powershell.png
_body: '# Alternate Data Streams
```
