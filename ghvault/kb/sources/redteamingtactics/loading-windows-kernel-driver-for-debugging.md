---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Loading Windows Kernel Driver for Debugging

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-internals-loading-a-windows-kernel-driver-osr-driver-loader-debugging-with-source-code` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/loading-a-windows-kernel-driver-osr-driver-loader-debugging-with-source-code.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Loading Windows Kernel Driver for Debugging](../../topics/miscellaneous-reversing-forensics/loading-windows-kernel-driver-for-debugging.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-internals-loading-a-windows-kernel-driver-osr-driver-loader-debugging-with-source-code |
| name | Loading Windows Kernel Driver for Debugging |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel-internals/loading-a-windows-kernel-driver-osr-driver-loader-debugging-with-source-code.md |

## Preserved Source Material

````yaml
_asset_filenames:
- confirmdriverloaded.gif
- debugging-kernel-source-code.gif
- image (253).png
- image (254).png
- image (255).png
- image (596).png
- image (599).png
- load-driver.gif
- loadkerneldriver.gif
_body: "# Loading Windows Kernel Driver for Debugging\n\n## Loading a Driver with OSR Driver Loader\n\nOn the system where\
  \ you want to load your driver (debugee), from an elevated command prompt, disable the driver integrity checks so that we\
  \ can load our unsigned drivers onto Windows 10:\n\n```\nbcdedit /set nointegritychecks on; bcdedit /set testsigning on\n\
  ```\n\n![](<../../.gitbook/assets/image (253).png>)\n\nOnce you have rebooted the system, open up the [OSR Loader](https://www.osronline.com/article.cfm^article=157.htm)\
  \ and load the driver as shown below:\n\n![](../../.gitbook/assets/loadkerneldriver.gif)\n\nNote that my driver name was\
  \ `kmdfHelloDriver`. We can now confirm the driver loaded successfully by debugging the kernel:\n\n```\n0: kd> db kmdfHelloDriver\n\
  ```\n\n![](../../.gitbook/assets/confirmdriverloaded.gif)\n\nAdditionally, we can check it this way by showing some basic\
  \ details about the loaded module:\n\n```\n0: kd> ln kmdfHelloDriver\n```\n\n![](<../../.gitbook/assets/image (254).png>)\n\
  \nIf we check it via the service configuration manager, we also see that our driver is now loaded and running:\n\n```\n\
  sc.exe query kmdfHelloDriver\n```\n\n![](<../../.gitbook/assets/image (255).png>)\n\n## Loading a Driver via Command Prompt\
  \ + WinDBG\n\nThe benefit of loading a kernel driver this way is that it does not rely on OSR Driver Loader or any other\
  \ 3rd party tools and also is much more efficient.\n\n{% hint style=\"info\" %}\n**Important**\\\nIn order for this technique\
  \ to work, the WinDBG debugger needs to be attached to the debugee.\n{% endhint %}\n\n### Preparing Powershell Profile\n\
  \nOn the debuggee, launch an elevated powershell console and do the following:\n\n```\nnotepad $PROFILE.AllUsersAllHosts\n\
  ```\n\nin the powershell profile, add the following powershell function:\n\n```csharp\nfunction Install-Driver($name)\n\
  {\n\t$cleanName = $name -replace \".sys|.\\\\\", \"\"\n\n\tsc.exe stop $cleanName\n\tsc.exe delete $cleanName\n\n\tcp $name\
  \ c:\\windows\\system32\\drivers\\ -verbose -force\n\tsc.exe create $cleanName type= kernel start= demand error= normal\
  \ binPath= c:\\windows\\System32\\Drivers\\$cleanName.sys DisplayName= $cleanName\n\n\tsc.exe start $cleanName\n}\n```\n\
  \nThe above function `Install-Driver` takes one parameter `$name`, which signifies a driver name that we want to install.&#x20;\n\
  \nThe function `Install-Driver` will:\n\n* Attempt to stop the service (unload the driver) if it's already running (no error\
  \ checking)\n* Attempt to delete the service (no error checking)\n* Copy the driver from the current directory to c:\\windows\\\
  system32\\drivers\n* Create a service for the driver\n* Start the service (load the driver)\n\nBelow screenshot shows the\
  \ two steps explained above:\n\n![](<../../.gitbook/assets/image (596).png>)\n\n{% hint style=\"info\" %}\nOnce the powershell\
  \ profile is saved, close the powershell console and open it again for the function `Install-Driver` to become usable.\n\
  {% endhint %}\n\n### Loading the Driver\n\nNavigate to the folder that contains the .sys file of the driver you want to\
  \ install, which in my case is `wdm-helloworld.sys` in Z:\\wdm-helloworld\\x64\\Debug:\n\n![](<../../.gitbook/assets/image\
  \ (599).png>)\n\nNow, we can install the driver by simply invoking:\n\n```csharp\nInstall-Driver wdm-helloworld.sys\n```\n\
  \n![](../../.gitbook/assets/load-driver.gif)\n\n### Stepping through Source Code\n\nIf we have source code for the driver\
  \ we want to debug, we can load its source code and step through it in WinDBG.  Load the source code via the `Source > Open\
  \ Source File` and re-load the driver again using `Install-Driver` function:\n\n![Stepping through driver's C code](../../.gitbook/assets/debugging-kernel-source-code.gif)"
_relative_path: miscellaneous-reversing-forensics/windows-kernel-internals/loading-a-windows-kernel-driver-osr-driver-loader-debugging-with-source-code.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/loading-a-windows-kernel-driver-osr-driver-loader-debugging-with-source-code.md
````
