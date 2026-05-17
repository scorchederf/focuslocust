---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Enumerating COM Objects and their Methods

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-enumeration-and-discovery-enumerating-com-objects-and-their-methods` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/enumerating-com-objects-and-their-methods.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Enumerating COM Objects and their Methods](../../topics/offensive-security/enumerating-com-objects-and-their-methods.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-enumeration-and-discovery-enumerating-com-objects-and-their-methods |
| name | Enumerating COM Objects and their Methods |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/enumeration-and-discovery/enumerating-com-objects-and-their-methods.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (575).png
- image (578).png
- image (579).png
- image (580).png
_body: "# Enumerating COM Objects and their Methods\n\nThis is a quick note to capture some of the commands for finding interesting\
  \ COM objects and the methods they expose, based on the great [article](https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html)\
  \ from Fireeye.\n\n> The Microsoft Component Object Model (COM) is a platform-independent, distributed, object-oriented\
  \ system for creating binary software components that can interact\n>\n> [https://docs.microsoft.com/en-us/windows/win32/com/the-component-object-model](https://docs.microsoft.com/en-us/windows/win32/com/the-component-object-model)\n\
  \nThis is less of a post-exploitation technique, rather a method that allows one to look for interesting COM objects, that\
  \ could be leveraged by one's malware.\n\n## Enumerating COM Objects\n\nWe can find all the COM objects registered on the\
  \ Windows system with:\n\n```csharp\ngwmi Win32_COMSetting | ? {$_.progid } | sort | ft ProgId,Caption,InprocServer32\n\
  ```\n\n![](<../../.gitbook/assets/image (575).png>)\n\n## Enumerating COM Object Methods\n\nOnce we have the list of COM\
  \ objects and have identified an interesting COM object, we can now check the methods it exposes. In our case, let's pick\
  \ a COM object `WScript.Shell.1` and check its methods like so:\n\n```csharp\n$o = [activator]::CreateInstance([type]::GetTypeFromProgID((\"\
  WScript.Shell.1\"))) | gm\n```\n\nBelow are the methods exposed by `WScript.Shell.1` COM object, one of which is `RegRead`:\n\
  \n![](<../../.gitbook/assets/image (578).png>)\n\nLet's see if we can read a registry value with `RedRead` method exposed\
  \ by the `WScript.Shell.1`. `RedRead` accepts one string as an argument - a path to the registry value:\n\n```csharp\n$o.RegRead(\"\
  HKEY_CURRENT_USER\\Volatile Environment\\LOGONSERVER\")\n```\n\nBelow shows how a registry value was read successfully:\n\
  \n![](<../../.gitbook/assets/image (579).png>)\n\n## Exposing All COM Object Methods\n\nWe can iterate through all the COM\
  \ objects and list their methods and save it all to a text file that we can later on inspect for any other interesting methods:\n\
  \n```csharp\n$com = gwmi Win32_COMSetting | ? {$_.progid } | select ProgId,Caption,InprocServer32\n\n$com | % {\n    $_.progid\
  \ | out-file -append methods.txt\n    [activator]::CreateInstance([type]::GetTypeFromProgID(($_.progid))) | gm | out-file\
  \ -append methods.txt\n    \"`n`n\" | out-file -append methods.txt\n}\n```\n\nBelow shows the output file with all the methods\
  \ of all COM objects exposed, in focus are the methods for `Shell.Application.1` COM object:\n\n![](<../../.gitbook/assets/image\
  \ (580).png>)\n\n## References\n\n{% embed url=\"https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html\"\
  \ %}"
_relative_path: offensive-security/enumeration-and-discovery/enumerating-com-objects-and-their-methods.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/enumerating-com-objects-and-their-methods.md
````
