---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Compiling a Simple Kernel Driver, DbgPrint, DbgView

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-compiling-first-kernel-driver-kdprint-dbgprint-and-debugview` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/compiling-first-kernel-driver-kdprint-dbgprint-and-debugview.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Compiling a Simple Kernel Driver, DbgPrint, DbgView](../../topics/miscellaneous-reversing-forensics/compiling-a-simple-kernel-driver-dbgprint-dbgview.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-compiling-first-kernel-driver-kdprint-dbgprint-and-debugview |
| name | Compiling a Simple Kernel Driver, DbgPrint, DbgView |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel/compiling-first-kernel-driver-kdprint-dbgprint-and-debugview.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (137).png
- image (176).png
- image (414).png
- image (447).png
- image (504).png
- image (510).png
- image (58).png
- image (81).png
_body: "# Compiling a Simple Kernel Driver, DbgPrint, DbgView\n\n## Simple Windows Driver Framework \\(WDF\\) Kernel Driver\n\
  \nSelect Kernel Mode Driver, Emtpy \\(KMDF\\) from templates:\n\n![](../../.gitbook/assets/image%20%28510%29.png)\n\n##\
  \ Create a driver.c\n\nCreate a new `driver.c` file under `Source Files`:\n\n![](../../.gitbook/assets/image%20%2881%29.png)\n\
  \n## Add Driver Code\n\n{% code title=\"driver.c\" %}\n```c\n#include <ntddk.h>\n#include <wdf.h>\n\nDRIVER_INITIALIZE DriverEntry;\n\
  EVT_WDF_DRIVER_DEVICE_ADD EvtDriverDeviceAdd;\nEVT_WDF_DRIVER_UNLOAD UnloadDriver;\n\n_Use_decl_annotations_\nvoid UnloadDriver(IN\
  \ WDFDRIVER driver)\n{\n    UNREFERENCED_PARAMETER(driver);\n    DbgPrint(\"Driver unloaded\");\n}\n\nNTSTATUS DriverEntry(_In_\
  \ PDRIVER_OBJECT DriverObject, _In_ PUNICODE_STRING RegistryPath)\n{\n    WDF_DRIVER_CONFIG config;\n    WDF_DRIVER_CONFIG_INIT(&config,\
  \ EvtDriverDeviceAdd);\n    config.EvtDriverUnload = UnloadDriver;\n    NTSTATUS status = WdfDriverCreate(DriverObject,\
  \ RegistryPath, WDF_NO_OBJECT_ATTRIBUTES, &config, WDF_NO_HANDLE);\n    \n    DbgPrint(\"Driver loaded\");\n\n    return\
  \ status;\n}\n\nNTSTATUS EvtDriverDeviceAdd(_In_ WDFDRIVER Driver,_Inout_ PWDFDEVICE_INIT DeviceInit)\n{\n    UNREFERENCED_PARAMETER(Driver);\n\
  \    WDFDEVICE device;\n    NTSTATUS status = WdfDeviceCreate(&DeviceInit, WDF_NO_OBJECT_ATTRIBUTES, &device);\n    \n \
  \   return status;\n}\n```\n{% endcode %}\n\n## Enable DbgPrint Monitoring for WinDBG\n\nChange the debug output verbosity:\n\
  \n```text\ned kd_default_mask 0xf\n```\n\n![](../../.gitbook/assets/image%20%2858%29.png)\n\n[Starting the driver](loading-a-windows-kernel-driver-to-windows-10.md)\
  \ allows us to see the debug output in WinDBG:\n\n![](../../.gitbook/assets/image%20%28447%29.png)\n\n## Enable DbgPrint\
  \ Monitoring for DbgView\n\nCreate a sub-key `Debug Print Filter` if it does not exist:\n\n```text\nComputer\\HKEY_LOCAL_MACHINE\\\
  SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Debug Print Filter\n```\n\nAdd a new DWORD value `DEFAULT` and set\
  \ its Data field to `0xf`:\n\n![](../../.gitbook/assets/image%20%28414%29.png)\n\nIf we load the driver now and start it,\
  \ we can see the debug output in DbgView too:\n\n![](../../.gitbook/assets/image%20%28176%29.png)\n\n## Requested Control\
  \ is Not Valid for This Service\n\nThe below error message is seen if you attempt to stop the WDF driver via OSR Driver\
  \ Loader or the native sc.exe, even if you have defined the driver unloading routine:\n\n![](../../.gitbook/assets/image%20%28137%29.png)\n\
  \nI could not find a solution to this, but WDM driver has no such issue - see the code below.\n\n## Simple Windows Driver\
  \ Model \\(WDM\\) Kernel Driver Load and Unload\n\nBelow is a simple WDM driver that can be compiled and then loaded and\
  \ stopped with OSR Driver Loader:\n\n```c\n#include <ntddk.h>\n\nvoid DriverUnload(PDRIVER_OBJECT dob)\n{\n\tUNREFERENCED_PARAMETER(dob);\n\
  \tDbgPrint(\"Driver unloaded\");\n}\n\nNTSTATUS DriverEntry(PDRIVER_OBJECT DriverObject, PUNICODE_STRING RegistryPath) {\n\
  \n\tUNREFERENCED_PARAMETER(DriverObject);\n\tUNREFERENCED_PARAMETER(RegistryPath);\n\n\tDriverObject->DriverUnload = DriverUnload;\n\
  \tDbgPrint(\"Driver loaded\");\n\n\treturn STATUS_SUCCESS;\n}\n```\n\nBelow shows how our driver is loaded and unloaded\
  \ via OSR Loader while DbgView prints our DbgPrint output defined in the above `DriverEntry` and `DriverUnload` routines:\n\
  \n![](../../.gitbook/assets/image%20%28504%29.png)\n\n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/writing-a-very-small-kmdf--driver\"\
  \ %}\n\n{% embed url=\"http://www.osronline.com/article.cfm%5earticle=295.htm\" %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel/compiling-first-kernel-driver-kdprint-dbgprint-and-debugview.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/compiling-first-kernel-driver-kdprint-dbgprint-and-debugview.md
````
