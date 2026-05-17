---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Timestomping

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-t1099-timestomping` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1099-timestomping.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Checking original timestamps of the nc.exe:

## Preserved Body

````markdown
## Execution

Checking original timestamps of the `nc.exe`:

```csharp
.\timestomp.exe .\nc.exe -v
```

![](<../../_assets/timestomp-original.png>)

Forging the file creation date:

```csharp
.\timestomp.exe .\nc.exe -c "Monday 7/25/2005 5:15:55 AM"
```

![](<../../_assets/timestomp-forged.png>)

Checking the `$MFT` for changes - first of, dumping the `$MFT`:

```csharp
.\RawCopy64.exe /FileNamePath:C:\$MFT /OutputName:c:\experiments\mft.dat
```

![](<../../_assets/timestomp-dump-parse-mft.png>)

Let's find the `nc.exe` record and check its timestamps:

```csharp
Import-Csv .\mft.csv -Delimiter "`t" | Where-Object {$_.Filename -eq "nc.exe"}
```

Note how `fnCreateTime` did not get updated:

![](<../../_assets/timestomp-mft-timestamps.png>)

For this reason, it is always a good idea to check both `$STANDARD_INFO` and `$FILE_NAME` times during the investigation to have a better chance at detecting timestomping.

Note that if we moved the nc.exe file to any other folder on the system and re-parsed the $MFT again, the `fnCreateTime` timestamp would inherit the timestamp from `siCreateTime`:

![](<../../_assets/timestomp-moved.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/timestomping.md)

## Evidence Excerpt

```text
_asset_filenames:
- timestomp-dump-parse-mft.png
- timestomp-forged.png
- timestomp-mft-timestamps.png
- timestomp-moved.png
- timestomp-original.png
_body: '---
description: Defense Evasion
```
