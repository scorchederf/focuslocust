---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adds-enumerate` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-enumerate.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Enumeration](../../topics/active-directory/active-directory-enumeration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adds-enumerate |
| name | Active Directory - Enumeration |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adds-enumerate.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Enumeration\n\n## Using BloodHound\n\nUse the appropriate data collector to gather information\
  \ for **BloodHound** or **BloodHound Community Edition (CE)** across various platforms.\n\n* [BloodHoundAD/AzureHound](https://github.com/BloodHoundAD/AzureHound)\
  \ for Azure Active Directory\n* [BloodHoundAD/SharpHound](https://github.com/BloodHoundAD/SharpHound) for local Active Directory\
  \ (C# collector)\n* [FalconForceTeam/SOAPHound](https://github.com/FalconForceTeam/SOAPHound) for local Active Directory\
  \ (C# collector using ADWS)\n* [g0h4n/RustHound-CE](https://github.com/g0h4n/RustHound-CE) for local Active Directory (Rust\
  \ collector)\n* [NH-RED-TEAM/RustHound](https://github.com/NH-RED-TEAM/RustHound) for local Active Directory (Rust collector)\n\
  * [fox-it/BloodHound.py](https://github.com/fox-it/BloodHound.py) for local Active Directory (Python collector)\n* [coffeegist/bofhound](https://github.com/coffeegist/bofhound)\
  \ for local Active Directory  (Generate BloodHound compatible JSON from logs written by ldapsearch BOF, pyldapsearch and\
  \ Brute Ratel's LDAP Sentinel)\n* [c3c/ADExplorerSnapshot.py](https://github.com/c3c/ADExplorerSnapshot.py) for local Active\
  \ Directory (Generate BloodHound compatible JSON from AD Explorer snapshot)\n* [CrowdStrike/sccmhound](https://github.com/CrowdStrike/sccmhound)\
  \ for local Active Directory (C# collector using Microsoft Configuration Manager)\n* [SpecterOps/MSSQLHound](https://github.com/SpecterOps/MSSQLHound)\
  \ for MSSQL attack paths (BloodHound OpenGraph PowerShell collector)\n* [SpecterOps/SnowHound](https://github.com/SpecterOps/SnowHound)\
  \ for Snowflake attack paths (BloodHound OpenGraph PowerShell collector)\n* [SpecterOps/GitHound](https://github.com/SpecterOps/GitHound)\
  \ for GitHub attack paths (BloodHound OpenGraph PowerShell collector)\n* [SpecterOps/1PassHound](https://github.com/SpecterOps/1PassHound)\
  \ for 1Password attack paths (BloodHound OpenGraph PowerShell collector)\n* [TheSleekBoyCompany/AnsibleHound](https://github.com/TheSleekBoyCompany/AnsibleHound)\
  \ for Ansible WorX and Ansible Tower attack paths (BloodHound OpenGraph Go collector)\n* [p0dalirius/sharehound](https://github.com/p0dalirius/sharehound)\
  \ - for Network Shares attack paths (BloodHound OpenGraph Python collector)\n* [C0KERNEL/SecretHound](https://github.com/C0KERNEL/SecretHound)\
  \ - for secrets (BloodHound OpenGraph Python collector)\n* [F41zK4r1m/GCP-Hound](https://github.com/F41zK4r1m/GCP-Hound)\
  \ - for GCP attack path (BloodHound OpenGraph Python collector)\n* [SpecterOps/ConfigManBearPig](https://github.com/SpecterOps/ConfigManBearPig)\
  \ - for SCCM attack path (BloodHound OpenGraph PowerShell collector)\n\n**Examples**:\n\n* Use [BloodHoundAD/AzureHound](https://github.com/BloodHoundAD/AzureHound)\
  \ (more info: [Cloud - Azure Pentest](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Cloud%20-%20Azure%20Pentest.md#azure-recon-tools))\n\
  \n* Use [BloodHoundAD/SharpHound.exe](https://github.com/BloodHoundAD/BloodHound) - run the collector on the machine using\
  \ SharpHound.exe\n\n  ```powershell\n  .\\SharpHound.exe -c all -d active.htb --searchforest\n  .\\SharpHound.exe -c all,GPOLocalGroup\
  \ # all collection doesn't include GPOLocalGroup by default\n  .\\SharpHound.exe --CollectionMethod DCOnly # only collect\
  \ from the DC, doesn't query the computers (more stealthy)\n\n  .\\SharpHound.exe -c all --LdapUsername <UserName> --LdapPassword\
  \ <Password> --JSONFolder <PathToFile>\n  .\\SharpHound.exe -c all --LdapUsername <UserName> --LdapPassword <Password> --domaincontroller\
  \ 10.10.10.100 -d active.htb\n\n  .\\SharpHound.exe -c All,GPOLocalGroup --outputdirectory C:\\Windows\\Temp --prettyprint\
  \ --randomfilenames --collectallproperties --throttle 10000 --jitter 23  --outputprefix internalallthething\n  ```\n\n*\
  \ Use [BloodHoundAD/SharpHound.ps1](https://github.com/BloodHoundAD/BloodHound/blob/master/Collectors/SharpHound.ps1) -\
  \ run the collector on the machine using Powershell\n\n  ```powershell\n  Invoke-BloodHound -SearchForest -CSVFolder C:\\\
  Users\\Public\n  Invoke-BloodHound -CollectionMethod All  -LDAPUser <UserName> -LDAPPass <Password> -OutputDirectory <PathToFile>\n\
  \  ```\n\n* Use [ly4k/Certipy](https://github.com/ly4k/Certipy) to collect certificates data\n\n  ```ps1\n  certipy find\
  \ 'corp.local/john:Passw0rd@dc.corp.local' -bloodhound\n  certipy find 'corp.local/john:Passw0rd@dc.corp.local' -old-bloodhound\n\
  \  certipy find 'corp.local/john:Passw0rd@dc.corp.local' -vulnerable -hide-admins -username user@domain -password Password123\n\
  \  ```\n\n* Use [NH-RED-TEAM/RustHound](https://github.com/OPENCYBER-FR/RustHound)\n\n  ```ps1\n  # Windows with GSSAPI\
  \ session\n  rusthound.exe -d domain.local --ldapfqdn domain\n  # Windows/Linux simple bind connection username:password\n\
  \  rusthound.exe -d domain.local -u user@domain.local -p Password123 -o output -z\n  # Linux with username:password and\
  \ ADCS module for @ly4k BloodHound version\n  rusthound -d domain.local -u 'user@domain.local' -p 'Password123' -o /tmp/adcs\
  \ --adcs -z\n  ```\n\n* Use [FalconForceTeam/SOAPHound](https://github.com/FalconForceTeam/SOAPHound)\n\n  ```ps1\n  --buildcache:\
  \ Only build cache and not perform further actions\n  --bhdump: Dump BloodHound data\n  --certdump: Dump AD Certificate\
  \ Services (ADCS) data\n  --dnsdump: Dump AD Integrated DNS data\n\n  SOAPHound.exe --buildcache -c c:\\temp\\cache.txt\n\
  \  SOAPHound.exe -c c:\\temp\\cache.txt --bhdump -o c:\\temp\\bloodhound-output\n  SOAPHound.exe -c c:\\temp\\cache.txt\
  \ --bhdump -o c:\\temp\\bloodhound-output --autosplit --threshold 1000\n  SOAPHound.exe -c c:\\temp\\cache.txt --certdump\
  \ -o c:\\temp\\bloodhound-output\n  SOAPHound.exe --dnsdump -o c:\\temp\\dns-output\n  ```\n\n* Use [fox-it/BloodHound.py](https://github.com/fox-it/BloodHound.py)\n\
  \n  ```ps1\n  pip install bloodhound\n  bloodhound-python -d domain.local -u username -p password -gc LAB2008DC01.domain.local\
  \ -c all\n  ```\n\n* Use [c3c/ADExplorerSnapshot.py](https://github.com/c3c/ADExplorerSnapshot.py) to query data from SysInternals/ADExplorer\
  \ snapshot  (ADExplorer remains a legitimate binary signed by Microsoft, avoiding detection with security solutions).\n\n\
  \  ```py\n  ADExplorerSnapshot.py <snapshot path> -o <*.json output folder path>\n  ```\n\nThen import the zip/json files\
  \ into the Neo4J database and query them.\n\n```powershell\nroot@payload$ apt install bloodhound \n\n# start BloodHound\
  \ and the database\nroot@payload$ neo4j console\n# or use docker\nroot@payload$ docker run -itd -p 7687:7687 -p 7474:7474\
  \ --env NEO4J_AUTH=neo4j/bloodhound -v $(pwd)/neo4j:/data neo4j:4.4-community\n\nroot@payload$ ./bloodhound --no-sandbox\n\
  Go to http://127.0.0.1:7474, use db:bolt://localhost:7687, user:neo4J, pass:neo4j\n```\n\nNOTE: Currently BloodHound Community\
  \ Edition is still a work in progress, it is highly recommended to stay on the original [BloodHoundAD/BloodHound](https://github.com/BloodHoundAD/BloodHound/)\
  \ version.\n\n```ps1\ngit clone https://github.com/SpecterOps/BloodHound\ncd examples/docker-compose/\ncat docker-compose.yml\
  \ | docker compose -f - up\n# UI: http://localhost:8080/ui/login\n# Username: admin\n# Password: see your Docker logs\n\
  ```\n\nYou can add some custom queries like :\n\n* [BloodHound Queries For All - SpecterOps](https://queries.specterops.io/)\n\
  * [Bloodhound-Custom-Queries from @hausec](https://github.com/hausec/Bloodhound-Custom-Queries/blob/master/customqueries.json)\n\
  * [BloodHoundQueries from CompassSecurity](https://github.com/CompassSecurity/BloodHoundQueries/blob/master/customqueries.json)\n\
  * [BloodHound Custom Queries from Exegol - @ShutdownRepo](https://raw.githubusercontent.com/ThePorgs/Exegol-images/main/sources/assets/bloodhound/customqueries.json)\n\
  * [Certipy BloodHound Custom Queries from ly4k](https://github.com/ly4k/Certipy/blob/main/customqueries.json)\n\nReplace\
  \ the customqueries.json file located at `/home/username/.config/bloodhound/customqueries.json` or `C:\\Users\\USERNAME\\\
  AppData\\Roaming\\BloodHound\\customqueries.json`.\n\n## Using PowerView\n  \n* **Get Current Domain:** `Get-NetDomain`\n\
  * **Enum Other Domains:** `Get-NetDomain -Domain <DomainName>`\n* **Get Domain SID:** `Get-DomainSID`\n* **Get Domain Policy:**\n\
  \n  ```powershell\n  Get-DomainPolicy\n\n  #Will show us the policy configurations of the Domain about system access or\
  \ kerberos\n  (Get-DomainPolicy).\"system access\"\n  (Get-DomainPolicy).\"kerberos policy\"\n  ```\n\n* **Get Domain Controlers:**\n\
  \n  ```powershell\n  Get-NetDomainController\n  Get-NetDomainController -Domain <DomainName>\n  ```\n\n* **Enumerate Domain\
  \ Users:**\n\n  ```powershell\n  Get-NetUser\n  Get-NetUser -SamAccountName <user> \n  Get-NetUser | select cn\n  Get-UserProperty\n\
  \n  #Check last password change\n  Get-UserProperty -Properties pwdlastset\n\n  #Get a specific \"string\" on a user's attribute\n\
  \  Find-UserField -SearchField Description -SearchTerm \"wtver\"\n  \n  #Enumerate user logged on a machine\n  Get-NetLoggedon\
  \ -ComputerName <ComputerName>\n  \n  #Enumerate Session Information for a machine\n  Get-NetSession -ComputerName <ComputerName>\n\
  \  \n  #Enumerate domain machines of the current/specified domain where specific users are logged into\n  Find-DomainUserLocation\
  \ -Domain <DomainName> | Select-Object UserName, SessionFromName\n  ```\n\n* **Enum Domain Computers:**\n\n  ```powershell\n\
  \  Get-NetComputer -FullData\n  Get-DomainGroup\n\n  #Enumerate Live machines \n  Get-NetComputer -Ping\n  ```\n\n* **Enum\
  \ Groups and Group Members:**\n\n  ```powershell\n  Get-NetGroupMember -GroupName \"<GroupName>\" -Domain <DomainName>\n\
  \  \n  #Enumerate the members of a specified group of the domain\n  Get-DomainGroup -Identity <GroupName> | Select-Object\
  \ -ExpandProperty Member\n  \n  #Returns all GPOs in a domain that modify local group memberships through Restricted Groups\
  \ or Group Policy Preferences\n  Get-DomainGPOLocalGroup | Select-Object GPODisplayName, GroupName\n  ```\n\n* **Enumerate\
  \ Shares**\n\n  ```powershell\n  #Enumerate Domain Shares\n  Find-DomainShare\n  \n  #Enumerate Domain Shares the current\
  \ user has access\n  Find-DomainShare -CheckShareAccess\n  ```\n\n* **Enum Group Policies:**\n\n  ```powershell\n  Get-NetGPO\n\
  \n  # Shows active Policy on specified machine\n  Get-NetGPO -ComputerName <Name of the PC>\n  Get-NetGPOGroup\n\n  #Get\
  \ users that are part of a Machine's local Admin group\n  Find-GPOComputerAdmin -ComputerName <ComputerName>\n  ```\n\n\
  * **Enum OUs:**\n\n  ```powershell\n  Get-NetOU -FullData \n  Get-NetGPO -GPOname <The GUID of the GPO>\n  ```\n\n* **Enum\
  \ ACLs:**\n\n  ```powershell\n  # Returns the ACLs associated with the specified account\n  Get-ObjectAcl -SamAccountName\
  \ <AccountName> -ResolveGUIDs\n  Get-ObjectAcl -ADSprefix 'CN=Administrator, CN=Users' -Verbose\n\n  #Search for interesting\
  \ ACEs\n  Invoke-ACLScanner -ResolveGUIDs\n\n  #Check the ACLs associated with a specified path (e.g smb share)\n  Get-PathAcl\
  \ -Path \"\\\\Path\\Of\\A\\Share\"\n  ```\n\n* **Enum Domain Trust:**\n\n  ```powershell\n  Get-NetDomainTrust\n  Get-NetDomainTrust\
  \ -Domain <DomainName>\n  ```\n\n* **Enum Forest Trust:**\n\n  ```powershell\n  Get-NetForestDomain\n  Get-NetForestDomain\
  \ Forest <ForestName>\n\n  #Domains of Forest Enumeration\n  Get-NetForestDomain\n  Get-NetForestDomain Forest <ForestName>\n\
  \n  #Map the Trust of the Forest\n  Get-NetForestTrust\n  Get-NetDomainTrust -Forest <ForestName>\n  ```\n\n* **User Hunting:**\n\
  \n  ```powershell\n  #Finds all machines on the current domain where the current user has local admin access\n  Find-LocalAdminAccess\
  \ -Verbose\n\n  #Find local admins on all machines of the domain:\n  Invoke-EnumerateLocalAdmin -Verbose\n\n  #Find computers\
  \ were a Domain Admin OR a specified user has a session\n  Invoke-UserHunter\n  Invoke-UserHunter -GroupName \"RDPUsers\"\
  \n  Invoke-UserHunter -Stealth\n\n  #Confirming admin access:\n  Invoke-UserHunter -CheckAccess\n  ```\n\n## Using AD Module\n\
  \n* **Get Current Domain:** `Get-ADDomain`\n* **Enum Other Domains:** `Get-ADDomain -Identity <Domain>`\n* **Get Domain\
  \ SID:** `Get-DomainSID`\n* **Get Domain Controlers:**\n\n  ```powershell\n  Get-ADDomainController\n  Get-ADDomainController\
  \ -Identity <DomainName>\n  ```\n  \n* **Enumerate Domain Users:**\n\n  ```powershell\n  Get-ADUser -Filter * -Identity\
  \ <user> -Properties *\n\n  #Get a specific \"string\" on a user's attribute\n  Get-ADUser -Filter 'Description -like \"\
  *wtver*\"' -Properties Description | select Name, Description\n  ```\n\n* **Enum Domain Computers:**\n\n  ```powershell\n\
  \  Get-ADComputer -Filter * -Properties *\n  Get-ADGroup -Filter * \n  ```\n\n* **Enum Domain Trust:**\n\n  ```powershell\n\
  \  Get-ADTrust -Filter *\n  Get-ADTrust -Identity <DomainName>\n  ```\n\n* **Enum Forest Trust:**\n\n  ```powershell\n \
  \ Get-ADForest\n  Get-ADForest -Identity <ForestName>\n\n  #Domains of Forest Enumeration\n  (Get-ADForest).Domains\n  ```\n\
  \n* **Enum Local AppLocker Effective Policy:**\n\n ```powershell\n Get-AppLockerPolicy -Effective | select -ExpandProperty\
  \ RuleCollections\n ```\n\n## User Hunting\n\nSometimes you need to find a machine where a specific user is logged in.\n\
  You can remotely query every machines on the network to get a list of the users's sessions.\n\n* netexec\n\n  ```ps1\n \
  \ nxc smb 10.10.10.0/24 -u Administrator -p 'P@ssw0rd' --sessions\n  SMB         10.10.10.10    445    WIN-8OJFTLMU1IG \
  \ [+] Enumerated sessions\n  SMB         10.10.10.10    445    WIN-8OJFTLMU1IG  \\\\10.10.10.10            User:Administrator\n\
  \  ```\n\n* Impacket Smbclient\n\n  ```ps1\n  $ impacket-smbclient Administrator@10.10.10.10\n  # who\n  host:  \\\\10.10.10.10,\
  \ user: Administrator, active:     1, idle:     0\n  ```\n\n* PowerView Invoke-UserHunter\n\n  ```ps1\n  # Find computers\
  \ were a Domain Admin OR a specified user has a session\n  Invoke-UserHunter\n  Invoke-UserHunter -GroupName \"RDPUsers\"\
  \n  Invoke-UserHunter -Stealth\n  ```\n\n## RID cycling\n\nIn Windows, every security principal (user, group, etc.) has\
  \ a Security Identifier (SID). The SID is a unique identifier used for access control.\n\n```ps1\nS-1-5-21-<domain>-<RID>\n\
  ```\n\n* `S-1-5-21-<domain>` = Base domain SID\n* `<RID>` = Unique ID assigned to a user/group\n\nRID cycling involves brute-forcing\
  \ a range of RIDs (like 500–1500) by appending them to the known domain SID, and attempting to resolve each SID into a username.\n\
  \n* Using [Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec)\n\n  ```ps1\n  netexec smb 10.10.11.231 -u guest -p\
  \ '' --rid-brute 10000 --log rid-brute.txt\n  SMB         10.10.11.231    445    DC01             [*] Windows 10 / Server\
  \ 2019 Build 17763 x64 (name:DC01) (domain:rebound.htb) (signing:True) (SMBv1:False)\n  SMB         10.10.11.231    445\
  \    DC01             [+] rebound.htb\\guest: \n  SMB         10.10.11.231    445    DC01             498: rebound\\Enterprise\
  \ Read-only Domain Controllers (SidTypeGroup)\n  SMB         10.10.11.231    445    DC01             500: rebound\\Administrator\
  \ (SidTypeUser)\n  SMB         10.10.11.231    445    DC01             501: rebound\\Guest (SidTypeUser)\n  SMB        \
  \ 10.10.11.231    445    DC01             502: rebound\\krbtgt (SidTypeUser)\n  ```\n\n* Using Impacket script [impacket/lookupsid.py](https://github.com/fortra/impacket/blob/master/examples/lookupsid.py)\n\
  \n  ```ps1\n  lookupsid.py -no-pass 'guest@rebound.htb' 20000\n  ```\n\n## Other Interesting Commands\n\n* **Find Domain\
  \ Controllers**\n\n  ```ps1\n  nslookup domain.com\n  nslookup -type=srv _ldap._tcp.dc._msdcs.<domain>.com\n  nltest /dclist:domain.com\n\
  \  Get-ADDomainController -filter * | Select-Object name\n  gpresult /r\n  $Env:LOGONSERVER \n  echo %LOGONSERVER%\n  ```\n\
  \n## References\n\n* [Explain like I’m 5: Kerberos - Apr 2, 2013 - @roguelynn](https://www.roguelynn.com/words/explain-like-im-5-kerberos/)\n\
  * [Pen Testing Active Directory Environments - Part I: Introduction to netexec (and PowerView)](https://blog.varonis.com/pen-testing-active-directory-environments-part-introduction-netexec-powerview/)\n\
  * [Pen Testing Active Directory Environments - Part II: Getting Stuff Done With PowerView](https://blog.varonis.com/pen-testing-active-directory-environments-part-ii-getting-stuff-done-with-powerview/)\n\
  * [Pen Testing Active Directory Environments - Part III:  Chasing Power Users](https://blog.varonis.com/pen-testing-active-directory-environments-part-iii-chasing-power-users/)\n\
  * [Pen Testing Active Directory Environments - Part IV: Graph Fun](https://blog.varonis.com/pen-testing-active-directory-environments-part-iv-graph-fun/)\n\
  * [Pen Testing Active Directory Environments - Part V: Admins and Graphs](https://blog.varonis.com/pen-testing-active-directory-v-admins-graphs/)\n\
  * [Pen Testing Active Directory Environments - Part VI: The Final Case](https://blog.varonis.com/pen-testing-active-directory-part-vi-final-case/)\n\
  * [Attacking Active Directory: 0 to 0.9 - Eloy Pérez González - 2021/05/29](https://zer1t0.gitlab.io/posts/attacking_ad/)\n\
  * [Fun with LDAP, Kerberos (and MSRPC) in AD Environments](https://speakerdeck.com/ropnop/fun-with-ldap-kerberos-and-msrpc-in-ad-environments)\n\
  * [Penetration Testing Active Directory, Part I - March 5, 2019 - Hausec](https://hausec.com/2019/03/05/penetration-testing-active-directory-part-i/)\n\
  * [Penetration Testing Active Directory, Part II - March 12, 2019 - Hausec](https://hausec.com/2019/03/12/penetration-testing-active-directory-part-ii/)\n\
  * [Using bloodhound to map the user network - Hausec](https://hausec.com/2017/10/26/using-bloodhound-to-map-the-user-network/)\n\
  * [PowerView 3.0 Tricks - HarmJ0y](https://gist.github.com/HarmJ0y/184f9822b195c52dd50c379ed3117993)\n* [SOAPHound - tool\
  \ to collect Active Directory data via ADWS - Nikos Karouzos - 01/26/204](https://medium.com/falconforce/soaphound-tool-to-collect-active-directory-data-via-adws-165aca78288c)\n\
  * [Training - Attacking and Defending Active Directory Lab - Altered Security](https://www.alteredsecurity.com/adlab)"
_relative_path: active-directory/ad-adds-enumerate.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-enumerate.md
````
