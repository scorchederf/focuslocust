---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Sending Commands from your Userland Program to your Kernel Driver via IOCTL

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-sending-command-from-userland-to-your-kernel-driver-via-ioctl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/sending-command-from-userland-to-your-kernel-driver-via-ioctl.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Sending Commands from your Userland Program to your Kernel Driver via IOCTL](../../topics/miscellaneous-reversing-forensics/sending-commands-from-your-userland-program-to-your-kernel-driver-via-ioctl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-sending-command-from-userland-to-your-kernel-driver-via-ioctl |
| name | Sending Commands from your Userland Program to your Kernel Driver via IOCTL |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel/sending-command-from-userland-to-your-kernel-driver-via-ioctl.md |

## Preserved Source Material

````yaml
_asset_filenames:
- device-handles.gif
- image (118).png
- image (158).png
- image (180).png
- image (313).png
- image (37).png
- image (41).png
- image (445).png
- image (458).png
- image (495).png
- image (503).png
- image.png
- ioctl-driver-communication.gif
_body: "---\ndescription: Using Windows Driver Model (WDM)\n---\n\n# Sending Commands from your Userland Program to your Kernel\
  \ Driver via IOCTL\n\nThis is a quick lab that demonstrates how to:\n\n* create a simple WDM kernel mode driver that can\
  \ receive and respond to a custom defined input/output control code \\(IOCTL\\) that sent in from the userland program\n\
  * create a simple userland program that can sent a custom defined IOCTL to the kernel driver\n* pass some data from the\
  \ userland program to the kernel driver via `DeviceIoConctrol`\n* pass some data from the kernelland to userland program\n\
  \nBelow are the key code snippets that will make our kernel driver and the userland program.\n\n## Kernel Driver\n\n###\
  \ DriverEntry\n\n#### Populating DriverObject with Pointers\n\nInside driver's entry function, we populate our driver object\
  \ with pointers to important routines that will be executed, for example, when the driver is unloaded or a handle to its\
  \ device's symbolic link is obtained \\(`IRP_MJ_CREATE`\\) or closed \\(`IRP_MJ_CLOSE`\\):\n\n![](../../.gitbook/assets/image%20%28118%29.png)\n\
  \nThis is required, because these driver functions \\(callbacks\\) will be called by the OS when those events \\(i.e someone\
  \ trying to obtain a handle to your device, unload the driver or close device's handle\\) will fire. We do not want the\
  \ OS to not know what to do with our driver when the user attempts to unload it, therefore we tell it.\n\n#### Creating\
  \ Device and its Symbolic Link\n\nThis is where we create a device \\(that we are writing the driver for\\) and its symbolic\
  \ link. The symbolic link is required if we want to access our driver from the userland and ask it to execute some code\
  \ in respose to our custom defined IOCTL:\n\n![](../../.gitbook/assets/image%20%2841%29.png)\n\n![](../../.gitbook/assets/image%20%28445%29.png)\n\
  \n{% hint style=\"info\" %}\nIOCTL control code is a code that is sent to the device driver from the userland via a  `IRP_MJ_DEVICE_CONTROL`\
  \ request sent via `DeviceIoControl` WinAPI. IOCTL control code tells the driver what action the driver needs to perform.\
  \ For example, IOCTL code 0x202 \\(`IOCTL_STORAGE_EJECT_MEDIA`\\) could be sent to a USB/CDROM device and its  driver would\
  \ carry out an appropriate action for the given device, i.e open the CD tray for a CD-ROM or eject the USB media storage.\n\
  {% endhint %}\n\nBelow shows the device name and its symbolic link we are using in this exercise:\n\n![](../../.gitbook/assets/image%20%28180%29.png)\n\
  \nBelow shows how after the device and its symbolic links are created by our driver once the `DriverEntry` routine was called.\
  \ Also, the device `SpotlessDevice` is now visible inside WinObj:\n\n![](../../.gitbook/assets/image%20%28158%29.png)\n\n\
  Additionally, we can see the symbolic link too - note how `SpotlessDeviceLink` symbolic link points to our device `\\Device\\\
  SpotlessDevice`:\n\n![](../../.gitbook/assets/image%20%28313%29.png)\n\n### MajorFunctions\n\nThis function will handle\
  \ IRPs that request \\(`CreateFile`\\)/close \\(`CloseHandle`\\) a handle to our device's symbolic link:\n\n![](../../.gitbook/assets/image.png)\n\
  \nBelow you can see how `IRP_MJ_CREATE` and `IRP_MJ_CLOSE` requests are issued \\(for obtaining and closing the device's\
  \ handle respectively\\) are hit when we double click the `SpotlessDevice` in WinObj:\n\n![](../../.gitbook/assets/device-handles.gif)\n\
  \n### HandleCustomIOCTL\n\nThis routine will handle the IOCTL request sent from our userland program - it will print a string\
  \ that that will come from the userland. Additionally, it will send back a string to the userland:\n\n![](../../.gitbook/assets/image%20%2837%29.png)\n\
  \nWorth noting that when `IoDeviceControl` is called in the userland with a custom IOCTL and the input data that we want\
  \ to be sent to the kernel, the OS actually will intercept that request and package it into an I/O Packet \\(IRP, a complex\
  \ structure\\) that will then be handed to our callback `HandleCustomIOCTL` that we registered in the DriverEntry routine\
  \ for the IRP `IRP_MJ_DEVICE_CONTROL`.  IRP contains the incoming IOCTL code, the input data that was sent from the userland\
  \ and also a buffer that the kernel driver code can use to send the response back to the userland.\n\n### Defining Custom\
  \ IOCTL\n\n* IOCTL code needs to be defined both in the kernel driver as well as in the userland program\n* IOCTL code is\
  \ usually defined with a macro [`CTL_CODE`](https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/defining-i-o-control-codes).\
  \ Microsoft suggests that you can choose any code starting from 0x800:\n\n![](../../.gitbook/assets/image%20%28458%29.png)\n\
  \n## Userland Program\n\nBelow is the code that obtains a handle to the device `\\Device\\SpotlessDevice` via its symbolic\
  \ link `\\\\.\\SpotlessDeviceLink`, that we created earlier inside the driver's `DriverEntry` routine:\n\n![](../../.gitbook/assets/image%20%28503%29.png)\n\
  \nIssuing a custom defined IOCTL to the driver and sending it a pointer to the string that comes as a commandline argument\
  \ to our userland program: \n\n![](../../.gitbook/assets/image%20%28495%29.png)\n\nAdditionally, the above code prints out\
  \ the string received from the kernel.\n\n## Demo\n\nBelow shows how we execute our userland program with a string `spotless\
  \ saying ola from userland` as an argument, that gets sent to the kernel driver via our custom defined `IOCTL_SPOTLESS`\
  \ and receive some text back from the kernel:\n\n![](../../.gitbook/assets/ioctl-driver-communication.gif)\n\n## Code\n\n\
  * `driver.c` is our driver code that will receive and respond to IOCTL requests sent from the userland and send some data\
  \ back to the userland program. \n* `userland.cpp` is the userland program sending IOCTL and receiving data from the kernel\
  \ space\n\n{% tabs %}\n{% tab title=\"driver.c\" %}\n{% code title=\"\" %}\n```cpp\n#include <wdm.h>\n\nDRIVER_DISPATCH\
  \ HandleCustomIOCTL;\n#define IOCTL_SPOTLESS CTL_CODE(FILE_DEVICE_UNKNOWN, 0x2049, METHOD_BUFFERED, FILE_ANY_ACCESS)\nUNICODE_STRING\
  \ DEVICE_NAME = RTL_CONSTANT_STRING(L\"\\\\Device\\\\SpotlessDevice\");\nUNICODE_STRING DEVICE_SYMBOLIC_NAME = RTL_CONSTANT_STRING(L\"\
  \\\\??\\\\SpotlessDeviceLink\");\n\nvoid DriverUnload(PDRIVER_OBJECT dob)\n{\n\tDbgPrint(\"Driver unloaded, deleting symbolic\
  \ links and devices\");\n\tIoDeleteDevice(dob->DeviceObject);\n\tIoDeleteSymbolicLink(&DEVICE_SYMBOLIC_NAME);\n}\n\nNTSTATUS\
  \ HandleCustomIOCTL(PDEVICE_OBJECT DeviceObject, PIRP Irp)\n{\n\tUNREFERENCED_PARAMETER(DeviceObject);\n\tPIO_STACK_LOCATION\
  \ stackLocation = NULL;\n\tCHAR *messageFromKernel = \"ohai from them kernelz\";\n\n\tstackLocation = IoGetCurrentIrpStackLocation(Irp);\n\
  \t\n\tif (stackLocation->Parameters.DeviceIoControl.IoControlCode == IOCTL_SPOTLESS)\n\t{\n\t\tDbgPrint(\"IOCTL_SPOTLESS\
  \ (0x%x) issued\", stackLocation->Parameters.DeviceIoControl.IoControlCode);\n\t\tDbgPrint(\"Input received from userland:\
  \ %s\", (char*)Irp->AssociatedIrp.SystemBuffer);\n\t}\n\n\tIrp->IoStatus.Information = strlen(messageFromKernel);\n\tIrp->IoStatus.Status\
  \ = STATUS_SUCCESS;\n\t\n\tDbgPrint(\"Sending to userland: %s\", messageFromKernel);\n\tRtlCopyMemory(Irp->AssociatedIrp.SystemBuffer,\
  \ messageFromKernel, strlen(Irp->AssociatedIrp.SystemBuffer));\n\t\n\tIoCompleteRequest(Irp, IO_NO_INCREMENT);\n\n\treturn\
  \ STATUS_SUCCESS;\n}\n\nNTSTATUS MajorFunctions(PDEVICE_OBJECT DeviceObject, PIRP Irp)\n{\n\tUNREFERENCED_PARAMETER(DeviceObject);\n\
  \n\tPIO_STACK_LOCATION stackLocation = NULL;\n\tstackLocation = IoGetCurrentIrpStackLocation(Irp);\n\n\tswitch (stackLocation->MajorFunction)\n\
  \t{\n\tcase IRP_MJ_CREATE:\n\t\tDbgPrint(\"Handle to symbolink link %wZ opened\", DEVICE_SYMBOLIC_NAME);\n\t\tbreak;\n\t\
  case IRP_MJ_CLOSE:\n\t\tDbgPrint(\"Handle to symbolink link %wZ closed\", DEVICE_SYMBOLIC_NAME);\n\t\tbreak;\n\tdefault:\n\
  \t\tbreak;\n\t}\n\t\n\tIrp->IoStatus.Information = 0;\n\tIrp->IoStatus.Status = STATUS_SUCCESS;\n\tIoCompleteRequest(Irp,\
  \ IO_NO_INCREMENT);\n\n\treturn STATUS_SUCCESS;\n}\n\nNTSTATUS DriverEntry(PDRIVER_OBJECT DriverObject, PUNICODE_STRING\
  \ RegistryPath) \n{\n\tUNREFERENCED_PARAMETER(DriverObject);\n\tUNREFERENCED_PARAMETER(RegistryPath);\n\t\n\tNTSTATUS status\t\
  = 0;\n\n\t// routine that will execute when our driver is unloaded/service is stopped\n\tDriverObject->DriverUnload = DriverUnload;\n\
  \t\n\t// routine for handling IO requests from userland\n\tDriverObject->MajorFunction[IRP_MJ_DEVICE_CONTROL] = HandleCustomIOCTL;\n\
  \t\n\t// routines that will execute once a handle to our device's symbolik link is opened/closed\n\tDriverObject->MajorFunction[IRP_MJ_CREATE]\
  \ = MajorFunctions;\n\tDriverObject->MajorFunction[IRP_MJ_CLOSE] = MajorFunctions;\n\t\n\tDbgPrint(\"Driver loaded\");\n\
  \n\tIoCreateDevice(DriverObject, 0, &DEVICE_NAME, FILE_DEVICE_UNKNOWN, FILE_DEVICE_SECURE_OPEN, FALSE, &DriverObject->DeviceObject);\n\
  \tif (!NT_SUCCESS(status))\n\t{\n\t\tDbgPrint(\"Could not create device %wZ\", DEVICE_NAME);\n\t}\n\telse \n\t{\n\t\tDbgPrint(\"\
  Device %wZ created\", DEVICE_NAME);\n\t}\n\n\tstatus = IoCreateSymbolicLink(&DEVICE_SYMBOLIC_NAME, &DEVICE_NAME);\n\tif\
  \ (NT_SUCCESS(status))\n\t{\n\t\tDbgPrint(\"Symbolic link %wZ created\", DEVICE_SYMBOLIC_NAME);\n\t}\n\telse\n\t{\n\t\t\
  DbgPrint(\"Error creating symbolic link %wZ\", DEVICE_SYMBOLIC_NAME);\n\t}\n\t\n\treturn STATUS_SUCCESS;\n}\n```\n{% endcode\
  \ %}\n{% endtab %}\n\n{% tab title=\"userland.cpp\" %}\n```cpp\n#include <iostream>\n#include <Windows.h>\n\n#define IOCTL_SPOTLESS\
  \ CTL_CODE(FILE_DEVICE_UNKNOWN, 0x2049, METHOD_BUFFERED, FILE_ANY_ACCESS)\n\nint main(char argc, char ** argv)\n{\n    HANDLE\
  \ device = INVALID_HANDLE_VALUE;\n    BOOL status = FALSE;                 \n    DWORD bytesReturned = 0;\n    CHAR inBuffer[128]\
  \ = {0};\n    CHAR outBuffer[128] = {0};\n\n    RtlCopyMemory(inBuffer, argv[1], strlen(argv[1]));\n    \n    device = CreateFileW(L\"\
  \\\\\\\\.\\\\SpotlessDeviceLink\", GENERIC_ALL, 0, 0, OPEN_EXISTING, FILE_ATTRIBUTE_SYSTEM, 0);\n    \n    if (device ==\
  \ INVALID_HANDLE_VALUE)\n    {\n        printf_s(\"> Could not open device: 0x%x\\n\", GetLastError());\n        return\
  \ FALSE;\n    }\n\n    printf_s(\"> Issuing IOCTL_SPOTLESS 0x%x\\n\", IOCTL_SPOTLESS);\n    status = DeviceIoControl(device,\
  \ IOCTL_SPOTLESS, inBuffer, sizeof(inBuffer), outBuffer, sizeof(outBuffer), &bytesReturned, (LPOVERLAPPED)NULL);\n    printf_s(\"\
  > IOCTL_SPOTLESS 0x%x issued\\n\", IOCTL_SPOTLESS);\n    printf_s(\"> Received from the kernel land: %s. Received buffer\
  \ size: %d\\n\", outBuffer, bytesReturned);\n\n    CloseHandle(device);\n}\n```\n{% endtab %}\n{% endtabs %}\n\n## References\n\
  \n{% embed url=\"https://www.osronline.com/article.cfm%5Eid=92.htm\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol\"\
  \ %}\n\n{% embed url=\"https://www.drdobbs.com/windows/sending-ioctls-to-windows-nt-drivers/184416453\" %}\n\n{% embed url=\"\
  https://cylus.org/windows-drivers-part-2-ioctls-c678526f90ae\" %}\n\n{% embed url=\"https://ericasselin.com/userlandkernel-communication-deviceiocontrol-method\"\
  \ %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel/sending-command-from-userland-to-your-kernel-driver-via-ioctl.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/sending-command-from-userland-to-your-kernel-driver-via-ioctl.md
````
