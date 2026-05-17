---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Powershell Profile Persistence

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-powershell-profile-persistence` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/powershell-profile-persistence.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

It's possible to use powershell profiles for persistence and/or privilege escalation.

## Preserved Body

````markdown
It's possible to use powershell profiles for persistence and/or privilege escalation.

## Execution

There are four places you can abuse the powershell profile, depending on the privileges you have:

```csharp
$PROFILE | select *
```

![](<../../_assets/image (219).png>)

Let's add the code to a `$profile` variable (that expands to the current user's profile file) that will get executed the next time the compromised user launches a powershell console:
```csharp
echo "whoami > c:\temp\whoami.txt" > $PROFILE
cat $PROFILE
```
![](<../../_assets/image (215).png>)

Once the compromised user launches powershell, our code gets executed:

![](<../../_assets/image (218).png>)
If the user is not using profiles, the technique will stick out immediately due to the "loading personal and system profiles..." message at the top.
## References
````

## Source Verification

[source record](../../sources/redteamingtactics/powershell-profile-persistence.md)

## Evidence Excerpt

```text
_asset_filenames:
- image (215).png
- image (218).png
- image (219).png
_body: '# Powershell Profile Persistence
It''s possible to use powershell profiles for persistence and/or privilege escalation.
## Execution
There are four places you can abuse the powershell profile, depending on the privileges you have:
```
