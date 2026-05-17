---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# RID Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-rid-hijacking` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/rid-hijacking.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

RID (Relative ID, part of the SID (Security Identifier)) hijacking is a persistence technique, where an attacker with SYSTEM level privileges assigns an RID 500 (default Windows administrator account) to some low privileged user, effectivel

## Preserved Body

```markdown
RID (Relative ID, part of the SID (Security Identifier)) hijacking is a persistence technique, where an attacker with SYSTEM level privileges assigns an RID 500 (default Windows administrator account) to some low privileged user, effectively making the low privileged account assume administrator privileges on the next logon.

This techniques was originally researched by [Sebastian Castro](https://twitter.com/r4wd3r) -   [https://r4wsecurity.blogspot.com/2017/12/rid-hijacking-maintaining-access-on.html](https://r4wsecurity.blogspot.com/2017/12/rid-hijacking-maintaining-access-on.html)

## Execution

This lab assumes that we've compromised the WS01 machine and have `NT SYSTEM` access to it.

Below shows that the user `hijacked` is a low privileged user and has an RID of 1006 or 0x3ee:

![](<../../_assets/image (495).png>)

If we try to write something to c:\windows\ with the user `hijacked`, as expected, we get `Access is Denied`:

![](<../../_assets/image (496).png>)

HKEY\_LOCAL\_MACHINE\SAM\SAM\Domains\Account\Users\000003EE stores some information about the user`hijacked` that is used by LSASS during the user logon/authentication process. Specifically, at offset `0030` in the value `F` there are bytes that denote user's RID, which in our case are 03ee (1006) for the user `hijacked`:

![](<../../_assets/image (497).png>)

We can change those 2 bytes to 0x1f4 (500 - default administrator RID), which will effectively make the user `hijacked` assume administrator privileges:

![](<../../_assets/image (498).png>)

## Demo

After changing the `hijacked` RID from 3ee to 1f4 and creating a new logon session, we can see that the user `hijacked` is now allowed to write to c:\windows\\, suggesting it now has administrative privileges:

![](<../../_assets/rid-hijacking.gif>)

Note, that the user `hijacked` still does not belong to local administrators group, but its RID is now 500:

![](<../../_assets/image (499).png>)

## Detection

Monitor HKEY\_LOCAL\_MACHINE\SAM\SAM\Domains\Account\Users\\\*\F for modifications, especially if they originate from unusual binaries.

## References
```

## Source Verification

[source record](../../sources/redteamingtactics/rid-hijacking.md)

## Evidence Excerpt

```text
_asset_filenames:
- image (495).png
- image (496).png
- image (497).png
- image (498).png
- image (499).png
- rid-hijacking.gif
_body: '# RID Hijacking
```
