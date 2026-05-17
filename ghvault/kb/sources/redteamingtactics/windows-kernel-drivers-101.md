---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Windows Kernel Drivers 101

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-windows-kernel-drivers-101` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/windows-kernel-drivers-101.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows Kernel Drivers 101](../../topics/miscellaneous-reversing-forensics/windows-kernel-drivers-101.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-windows-kernel-drivers-101 |
| name | Windows Kernel Drivers 101 |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel/windows-kernel-drivers-101.md |

## Preserved Source Material

````yaml
_asset_filenames: []
_body: "# Windows Kernel Drivers 101\n\n{% hint style=\"info\" %}\nWork In Progress\n{% endhint %}\n\nThis living document\
  \ captures some of the Kernel Driver and OS related concepts that I encounter as I study Windows kernel driver development.\n\
  \n## Driver Types\n\nThere are many different types of drivers, but I am mostly interested in `Sofware Drivers`.\n\n###\
  \ Software Driver\n\n* Not associated with any device\n* Useful for running code in the kernel mode\n* Can also be a user\
  \ mode driver\n* Drivers can be developed with Kernel-Mode Driver Framework \\(KMDF\\) and Windows Driver Model \\(WDM\\\
  )\n\n## KMDF vs WDM\n\n* WDM is very closely tied to the OS and interacts with the it calling system service routines directly\n\
  * KMDF is a framework that abstracts a lot of driver development and allows the developer to focus on his/her driver rather\
  \ than focusing on OS programming intricacies\n* KMDF is recommended and a preferred driver development model over WDM in\
  \ most cases\n\n## I/O Manager\n\n* I/O manager manages the communication between applications and the interfaces provided\
  \ by device drivers\n* I/O Manager creates a driver object \\(`DRIVER_OBJECT`\\) for each installed and loaded driver\n\
  * I/O Manager calls driver's `DriverEntry` routine, which supplies the driver'd DRIVER\\_OBJECT address\n* Accepts I/O requests,\
  \ which usually originate from user-mode applications\n* Creates IRPs to represent the I/O requests\n* Routes the IRPs to\
  \ the appropriate drivers\n\n## Uncategorized Notes\n\n* All drivers contain `DriverEntry` routine - similary to `main`\
  \ routine of an executable and `DllMain` of a DLL. This routine gets called once the driver is loaded and started by the\
  \ OS.\n* Memory allocated in paged pool can be paged out to a disk, whereas memory allocated from a  nonpaged pool cannot\n\
  * Requests sent to drivers are encapsulated in I/O Request Packets \\(IRP\\)\n* `DRIVER_OBJECT` represents the image of\
  \ a loaded kernel-mode driver:\n  * ```text\n    typedef struct _DRIVER_OBJECT {\n      CSHORT             Type;\n     \
  \ CSHORT             Size;\n      PDEVICE_OBJECT     DeviceObject;\n      ULONG              Flags;\n      PVOID       \
  \       DriverStart;\n      ULONG              DriverSize;\n      PVOID              DriverSection;\n      PDRIVER_EXTENSION\
  \  DriverExtension;\n      UNICODE_STRING     DriverName;\n      PUNICODE_STRING    HardwareDatabase;\n      PFAST_IO_DISPATCH\
  \  FastIoDispatch;\n      PDRIVER_INITIALIZE DriverInit;\n      PDRIVER_STARTIO    DriverStartIo;\n      PDRIVER_UNLOAD\
  \     DriverUnload;\n      PDRIVER_DISPATCH   MajorFunction[IRP_MJ_MAXIMUM_FUNCTION + 1];\n    } DRIVER_OBJECT, *PDRIVER_OBJECT;\n\
  \    ```\n* `DRIVER_OBJECT` contains references to entry points of driver's standard routines \\(i.e Unload\\)\n* Driver\
  \ standard routines receive IRPs as input as well as a pointer to the target device object\n* Drivers must create at least\
  \ one device object \\(`DEVICE_OBJECT`\\) for each device\n* Device objects serve as a target of operations performed on\
  \ a the device\n* Software only drivers that only handle I/O requests and do not pass them to hardware, still must create\
  \ a device object to represent the target of its operations\n\n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/packet-driven-i-o-with-reusable-irps\"\
  \ %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel/windows-kernel-drivers-101.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/windows-kernel-drivers-101.md
````
