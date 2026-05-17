---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Loading a Windows Kernel Driver to Windows 10

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-loading-a-windows-kernel-driver-to-windows-10` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/loading-a-windows-kernel-driver-to-windows-10.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Loading a Windows Kernel Driver to Windows 10](../../topics/miscellaneous-reversing-forensics/loading-a-windows-kernel-driver-to-windows-10.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-loading-a-windows-kernel-driver-to-windows-10 |
| name | Loading a Windows Kernel Driver to Windows 10 |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel/loading-a-windows-kernel-driver-to-windows-10.md |

## Preserved Source Material

````yaml
_asset_filenames:
- confirmdriverloaded.gif
- image (210).png
- image (36).png
- image (82).png
- loadkerneldriver.gif
_body: '# Loading a Windows Kernel Driver to Windows 10


  ## Loading a Driver


  On the system where you want to load your driver \(debugee\), from an elevated command prompt, disable the driver integrity
  checks so that we can load our unsigned drivers onto Windows 10:


  ```text

  bcdedit /set nointegritychecks on; bcdedit /set testsigning on

  ```


  ![](../../.gitbook/assets/image%20%28210%29.png)


  Once you have rebooted the system, open up the [OSR Loader](https://www.osronline.com/article.cfm%5Earticle=157.htm) and
  load the driver as shown below:


  ![](../../.gitbook/assets/loadkerneldriver.gif)


  Note that my driver name was `kmdfHelloDriver`. We can now confirm the driver loaded successfully by debugging the kernel:


  ```text

  0: kd> db kmdfHelloDriver

  ```


  ![](../../.gitbook/assets/confirmdriverloaded.gif)


  Additionally, we can check it this way by showing some basic details about the loaded module:


  ```text

  0: kd> ln kmdfHelloDriver

  ```


  ![](../../.gitbook/assets/image%20%2882%29.png)


  If we check it via the service configuration manager, we also see that our driver is now loaded and running:


  ```text

  sc.exe query kmdfHelloDriver

  ```


  ![](../../.gitbook/assets/image%20%2836%29.png)'
_relative_path: miscellaneous-reversing-forensics/windows-kernel/loading-a-windows-kernel-driver-to-windows-10.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/loading-a-windows-kernel-driver-to-windows-10.md
````
