---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Active Directory Lab with Hyper-V and PowerShell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-active-directory-lab-with-hyper-v-and-powershell` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/active-directory-lab-with-hyper-v-and-powershell.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory Lab with Hyper-V and PowerShell](../../topics/offensive-security-experiments/active-directory-lab-with-hyper-v-and-powershell.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-experiments-active-directory-kerberos-abuse-active-directory-lab-with-hyper-v-and-powershell |
| name | Active Directory Lab with Hyper-V and PowerShell |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security-experiments/active-directory-kerberos-abuse/active-directory-lab-with-hyper-v-and-powershell.md |

## Preserved Source Material

````yaml
_asset_filenames:
- domain-created-dc-installed.gif
- image (749).png
- image (753).png
_body: "# Active Directory Lab with Hyper-V and PowerShell\n\nBelow are some notes with a couple of simple Powershell scripts\
  \ that I use to:\n\n* Promote a computer to Domain Controller\n* Create an Active Directory (AD) domain `offense.local`\n\
  * Join computer to `offense.local` domain\n* Create users in `offense.local` domain\n\n{% hint style=\"danger\" %}\nThe\
  \ scripts are not intended to fully automate building of the Active Directory lab, rather they serve as cheatsheets that\
  \ suit most of my needs most of the time.\n{% endhint %}\n\nI use Hyper-V to run my virtual machines (VM) which I installed\
  \ manually:\n\n* WS01 - Windows 10\n* DC01 - Windows Server 2019\n\n![](<../../.gitbook/assets/image (749).png>)\n\n## Promote\
  \ Computer to Domain Controller\n\nBelow script establishes a Powershell Remoting session to the `DC01` VM using credentials\
  \ `administrator:123456` (I set that password on `DC01` manually before running this script) and does the following:\n\n\
  * Congifures the IP/DNS addresses - Domain Controller `DC01` will have a static IP `10.0.0.6`;\n* Installs AD services and\
  \ management tools;\n* Creates a domain `offense.local`.\n\n{% hint style=\"info\" %}\nYou may need to change the passwords\
  \ depending on your password policies.\n{% endhint %}\n\n{% code title=\"Promote-DC.ps1\" %}\n```csharp\n$plainPassword\
  \ = \"123456\"\n$password = $plainPassword | ConvertTo-SecureString -asPlainText -Force\n$credential = New-Object System.Management.Automation.PSCredential(\"\
  administrator\", $password)\n\n$session = New-PSSession -Vmname dc01 -Credential $credential -Verbose\n\n$code = {\n   \
  \ $plainPassword = \"123456\"\n    $password = $plainPassword | ConvertTo-SecureString -asPlainText -Force\n    $credential\
  \ = New-Object System.Management.Automation.PSCredential(\"administrator\", $password)\n\n    netsh int ip set address \"\
  ethernet\" static 10.0.0.6 255.255.255.0 10.0.0.6 1\n    netsh int ip set dns \"ethernet\" static 10.0.0.6 primary \n\n\
  \    $domainName = \"offense\"\n    $domain = \"$domainName.local\"\n\n    Write-Host \"Installing management tools\"\n\
  \    Import-Module ServerManager\n    Add-WindowsFeature RSAT-AD-PowerShell,RSAT-AD-AdminCenter\n\n    Write-Host \"Deploying\
  \ Active Directory Domain...\"\n    Install-WindowsFeature AD-domain-services, DNS -IncludeAllSubFeature -IncludeManagementTools\
  \ -Restart\n    Import-Module ADDSDeployment\n    Install-ADDSForest `\n    -SafeModeAdministratorPassword $password `\n\
  \    -CreateDnsDelegation:$false `\n    -DatabasePath \"C:\\Windows\\NTDS\" `\n    -DomainMode \"7\" `\n    -DomainName\
  \ $domain `\n    -DomainNetbiosName $domainName `\n    -ForestMode \"7\" `\n    -InstallDns:$true `\n    -LogPath \"C:\\\
  Windows\\NTDS\" `\n    -NoRebootOnCompletion:$true `\n    -SysvolPath \"C:\\Windows\\SYSVOL\" `\n    -Force:$true\n\n  \
  \  Restart-Computer -Force -Verbose\n}\n\nInvoke-Command -Session $session -ScriptBlock $code\n```\n{% endcode %}\n\n![Output\
  \ of Promote-DC.ps1 ](../../.gitbook/assets/domain-created-dc-installed.gif)\n\n## Join Computer to Domain\n\nBelow script\
  \ establishes a Powershell Remoting session to the `WS01` VM using credentials `mantvydas:123456` (I set that password on\
  \ `WS01` manually before running this script) and does the following:\n\n* Configures IP/DNS settings - the workstation\
  \ `WS01` will have a static IP `10.0.0.7` and a DNS pointing to `10.0.0.6`, which is our `DC01`;\n* Adds computer to the\
  \ domain.\n\n{% code title=\"Join-Member.ps1\" %}\n```csharp\n$plainPassword = \"123456\"\n$password = $plainPassword |\
  \ ConvertTo-SecureString -asPlainText -Force\n$credential = New-Object System.Management.Automation.PSCredential(\"mantvydas\"\
  , $password)\n\n$session = New-PSSession -Vmname ws01 -Credential $credential -Verbose\n\n$code = {\n    netsh int ip set\
  \ address \"ethernet\" static 10.0.0.7 255.255.255.0 10.0.0.6 1\n    netsh int ip set dns \"ethernet\" static 10.0.0.6 primary\n\
  \n    $plainPassword = \"123456\"\n    $password = $plainPassword | ConvertTo-SecureString -asPlainText -Force\n    $credential\
  \ = New-Object System.Management.Automation.PSCredential(\"administrator\", $password)    \n    Add-computer -computername\
  \ ws01 -domain offense.local -domaincredential $credential -Verbose -Restart\n}\n\nInvoke-Command -Session $session -ScriptBlock\
  \ $code\n```\n{% endcode %}\n\n## Create Domain Users\n\nBelow script establishes a Powershell Remoting session to the `DC01`\
  \ VM and does the following:\n\n* Creates some domain users\n* Sets their passwords to `123456`\n\n{% code title=\"Create-Users.ps1\"\
  \ %}\n```csharp\n$plainPassword = \"123456\"\n$password = $plainPassword | ConvertTo-SecureString -asPlainText -Force\n\
  $credential = New-Object System.Management.Automation.PSCredential(\"offense\\administrator\", $password)\n\n$session =\
  \ New-PSSession -Vmname dc01 -Credential $credential -Verbose\n\n$code = {\n    $plainPassword = \"123456\"\n    $password\
  \ = $plainPassword | ConvertTo-SecureString -asPlainText -Force\n    $credential = New-Object System.Management.Automation.PSCredential(\"\
  offense\\administrator\", $password)\n    \n    # Create users\n    \"spotless\", \"sandy\", \"bob\" | % { New-ADUser $_\
  \ }\n    \n    # Reset users' passwords\n    Get-ADUser -Filter *  -Properties samaccountname | select -exp samaccountname\
  \  | ? {$_ -notmatch \"krb|guest\"} | ForEach-Object { Write-host Changing password for $_ to $plainPassword; net user $_\
  \ $plainPassword | out-null }\n}\n\nInvoke-Command -Session $session -ScriptBlock $code\n```\n{% endcode %}\n\nBefore running\
  \ this script, the password policy needs to be manually updated on `DC01`:\n\n* Minimum password length: `0`\n* Password\
  \ must meet complexity requirements: `disabled`\n\n![](<../../.gitbook/assets/image (753).png>)\n\n{% hint style=\"info\"\
  \ %}\nDon't forget to run `gpupdate.exe` on the `DC01` for the new password policy to take affect. This step is mandatory\
  \ before running `Create-Users.ps1` script, otherwise the user passwords will not be changed.\n{% endhint %}\n\n## Setting\
  \ up Kali in Enhanced Session Mode\n\nExecute the below in kali:\n\n```bash\nsudo git clone https://github.com/mimura1133/linux-vm-tools\
  \ /opt/linux-vm-tools\nsudo chmod 0755 /opt/linux-vm-tools/kali/2020.x/install.sh\nsudo /opt/linux-vm-tools/kali/2020.x/install.sh\n\
  sudo reboot -f\n```\n\nExecute the below on the host OS with Hyper V, that is hosting your kali VM:\n\n```bash\nSet-VM \"\
  KALI02\" -EnhancedSessionTransportType HVSocket\n```"
_relative_path: offensive-security-experiments/active-directory-kerberos-abuse/active-directory-lab-with-hyper-v-and-powershell.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/active-directory-lab-with-hyper-v-and-powershell.md
````
