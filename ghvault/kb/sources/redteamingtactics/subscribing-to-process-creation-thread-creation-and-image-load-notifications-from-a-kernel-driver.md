---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Subscribing to Process Creation, Thread Creation and Image Load Notifications from a Kernel Driver

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-internals-subscribing-to-process-creation-thread-creation-and-image-load-notifications-from-a-kernel-driver` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/subscribing-to-process-creation-thread-creation-and-image-load-notifications-from-a-kernel-driver.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Subscribing to Process Creation, Thread Creation and Image Load Notifications from a Kernel Driver](../../topics/miscellaneous-reversing-forensics/subscribing-to-process-creation-thread-creation-and-image-load-notifications-from-a-kernel-driver.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-internals-subscribing-to-process-creation-thread-creation-and-image-load-notifications-from-a-kernel-driver |
| name | Subscribing to Process Creation, Thread Creation and Image Load Notifications from a Kernel Driver |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel-internals/subscribing-to-process-creation-thread-creation-and-image-load-notifications-from-a-kernel-driver.md |

## Preserved Source Material

````yaml
_asset_filenames:
- PsSetCreateProcessNotifyRoutine.gif
- PsSetCreateProcessNotifyRoutineEx.gif
- PsSetLoadImageNotifyRoutine.gif
- image (529).png
- image (530).png
_body: "# Subscribing to Process Creation, Thread Creation and Image Load Notifications from a Kernel Driver\n\nThis is a\
  \ quick lab to play with some of the interesting notifications that kernel drivers can subscribe to:\n\n* [`PsSetCreateProcessNotifyRoutine`](subscribing-to-process-creation-thread-creation-and-image-load-notifications-from-a-kernel-driver.md#pssetcreateprocessnotifyroutine)\
  \ - notifies the driver about new/terminated processes\n* [`PsSetCreateProcessNotifyRoutineEx`](subscribing-to-process-creation-thread-creation-and-image-load-notifications-from-a-kernel-driver.md#pssetcreateprocessnotifyroutineex)\
  \ - notifies the driver about new processes being created, allows to kill them before they can run\n* [`PsSetCreateThreadNotifyRoutine`](subscribing-to-process-creation-thread-creation-and-image-load-notifications-from-a-kernel-driver.md#pssetcreatethreadnotifyroutine)\
  \ - notifies the driver about new/terminated threads\n* [`PsSetLoadImageNotifyRoutine`](subscribing-to-process-creation-thread-creation-and-image-load-notifications-from-a-kernel-driver.md#pssetloadimagenotifyroutine)\
  \ - notifies the driver about DLLs loaded by processes\n\n## PsSetCreateProcessNotifyRoutine\n\n`PsSetCreateProcessNotifyRoutine`\
  \ takes two parameters:\n\n```cpp\nNTSTATUS PsSetCreateProcessNotifyRoutine(\n  // pointer to a function to be called when\
  \ a process is spawned or terminated\n  PCREATE_PROCESS_NOTIFY_ROUTINE NotifyRoutine,\n  // specifies whether to subscribe\
  \ or unsubscribe from this event\n  BOOLEAN                        Remove\n);\n```\n\nBelow is a snippet that shows how\
  \ the routine `sCreateProcessNotifyRoutine` (line 2) gets registered for new/terminated process notifications on line 24:\n\
  \n```cpp\n// handle incoming notifications about new/terminated processes\nvoid sCreateProcessNotifyRoutine(HANDLE ppid,\
  \ HANDLE pid, BOOLEAN create)\n{\n\tif (create)\n\t{\n\t\tPEPROCESS process = NULL;\n\t\tPUNICODE_STRING parentProcessName\
  \ = NULL, processName = NULL;\n\t\t\n\t\tPsLookupProcessByProcessId(ppid, &process);\n\t\tSeLocateProcessImageName(process,\
  \ &parentProcessName);\n\n\t\tPsLookupProcessByProcessId(pid, &process);\n\t\tSeLocateProcessImageName(process, &processName);\n\
  \n\t\tDbgPrint(\"%d %wZ\\n\\t\\t%d %wZ\", ppid, parentProcessName, pid, processName);\n\t}\n\telse\n\t{\n\t\tDbgPrint(\"\
  Process %d lost child %d\", ppid, pid);\n\t}\n}\n\n// register sCreateProcessNotifyRoutine function to receive notifications\
  \ about new/terminated processes\nPsSetCreateProcessNotifyRoutine(sCreateProcessNotifyRoutine, FALSE);\n```\n\nBelow shows\
  \ how the routine `sCreateProcessNotifyRoutine` gets executed when a new process hostname.exe (PID 2892) is spawned by powershell\
  \ (PID 7176). Additionally, it shows that the process 7176 (hostname) terminated:\n\n![](../../.gitbook/assets/PsSetCreateProcessNotifyRoutine.gif)\n\
  \n## PsSetLoadImageNotifyRoutine\n\n`PsSetLoadImageNotifyRoutine` only takes one parameter - a pointer to a function that\
  \ will handle notifications about DLLs that processes running on the system loaded:\n\n```\nNTSTATUS PsSetLoadImageNotifyRoutine(\n\
  \  PLOAD_IMAGE_NOTIFY_ROUTINE NotifyRoutine\n);\n```\n\nBelow indicates that the routine `sLoadImageNotifyRoutine` is going\
  \ to handle our notifications as registered with `PsSetLoadImageNotifyRoutine` on line 14:\n\n```cpp\n// handle incoming\
  \ notifications about module loads\nvoid sLoadImageNotifyRoutine(PUNICODE_STRING imageName,\tHANDLE pid, PIMAGE_INFO imageInfo)\n\
  {\n\tUNREFERENCED_PARAMETER(imageInfo);\n\tPEPROCESS process = NULL;\n\tPUNICODE_STRING processName = NULL;\n\tPsLookupProcessByProcessId(pid,\
  \ &process);\n\tSeLocateProcessImageName(process, &processName);\n\n\tDbgPrint(\"%wZ (%d) loaded %wZ\", processName, pid,\
  \ imageName);\n}\n\n// register sLoadImageNotifyRoutinefunction to receive notifications new DLLs being loaded to processes\n\
  PsSetLoadImageNotifyRoutine(sLoadImageNotifyRoutine);\n```\n\nTesting the driver - once we open a notepad.exe, our driver\
  \ gets notified about all the modules that notepad.exe loaded:\n\n![](../../.gitbook/assets/PsSetLoadImageNotifyRoutine.gif)\n\
  \n## PsSetCreateThreadNotifyRoutine\n\n`PsSetCreateThreadNotifyRoutine` only takes one parameter - a pointer to a function\
  \ that will handle notifications about new or killed threads across all the system processes:\n\n```\nNTSTATUS PsSetCreateThreadNotifyRoutine(\n\
  \  PCREATE_THREAD_NOTIFY_ROUTINE NotifyRoutine\n);\n```\n\nBelow indicates that the routine `sCreateThreadNotifyRoutine`\
  \ is going to handle our notifications as registered with `PsSetCreateThreadNotifyRoutine` on line 15:\n\n```cpp\n// handle\
  \ incoming notifications about new/terminated processes\nvoid sCreateThreadNotifyRoutine(HANDLE pid, HANDLE tid, BOOLEAN\
  \ create)\n{\n\tif (create)\n\t{\n\t\tDbgPrint(\"%d created thread %d\", pid, tid);\n\t}\n\telse\n\t{\n\t\tDbgPrint(\"Thread\
  \ %d of process %d exited\", tid, pid);\n\t}\n}\n\n// register sCreateThreadNotifyRoutine to receive notifications about\
  \ thread creation / termination\nPsSetCreateThreadNotifyRoutine(sCreateThreadNotifyRoutine);\n```\n\nTesting the driver\
  \ now, we can see we are indeed geting notified about new and terminated threads across processes on our system:\n\n![](<../../.gitbook/assets/image\
  \ (529).png>)\n\n## PsSetCreateProcessNotifyRoutineEx\n\n`PsSetCreateProcessNotifyRoutineEx` takes two arguments:\n\n```cpp\n\
  NTSTATUS PsSetCreateProcessNotifyRoutineEx(\n  // pointer to a function to be called when a process is spawned \n  PCREATE_PROCESS_NOTIFY_ROUTINE_EX\
  \ NotifyRoutine,\n  // specifies whether to subscribe or unsubscribe from this event\n  BOOLEAN                        \
  \   Remove\n);\n```\n\nBelow is a snippet that shows how the routine `sCreateProcessNotifyRoutineEx` (line 3) gets registered\
  \ for new process notifications on line 19. Processes with commandline containing `notepad` in them will be killed by setting\
  \ the `createInfo.reationStatus` member to `STATUS_ACCESS_DENIED` (line 13):\n\n```cpp\n// handle incoming notifications\
  \ about new/terminated processes and kill\n// processes that have \"notepad\" in their commandline arguments\nvoid sCreateProcessNotifyRoutineEx(PEPROCESS\
  \ process, HANDLE pid, PPS_CREATE_NOTIFY_INFO createInfo)\n{\n\tUNREFERENCED_PARAMETER(process);\n\tUNREFERENCED_PARAMETER(pid);\n\
  \t\n\tif (createInfo != NULL)\n\t{\n\t\tif (wcsstr(createInfo->CommandLine->Buffer, L\"notepad\") != NULL)\n\t\t{\n\t\t\t\
  DbgPrint(\"[!] Access to launch notepad.exe was denied!\");\n\t\t\tcreateInfo->CreationStatus = STATUS_ACCESS_DENIED;\n\t\
  \t}\n\t}\n}\n\n// subscribe sCreateProcessNotifyRoutineEx to new / terminated process notifications\nPsSetCreateProcessNotifyRoutineEx(sCreateProcessNotifyRoutineEx,\
  \ FALSE);\n```\n\n{% hint style=\"info\" %}\nIf `PsSetCreateProcessNotifyRoutineEx` is not working in your driver, you will\
  \ need to add a `/integritycheck` switch in your linker configuration\n{% endhint %}\n\n![](<../../.gitbook/assets/image\
  \ (530).png>)\n\nBelow shows how an attempt to spawn notepad.exe is blocked by our driver:\n\n![](../../.gitbook/assets/PsSetCreateProcessNotifyRoutineEx.gif)\n\
  \n## Code\n\nBelos is the full working driver code that registers all the callback routines mentioned above:\n\n```cpp\n\
  #include <Ntifs.h>\n#include <ntddk.h>\n#include <wdm.h>\n\nDRIVER_DISPATCH HandleCustomIOCTL;\n#define IOCTL_SPOTLESS CTL_CODE(FILE_DEVICE_UNKNOWN,\
  \ 0x2049, METHOD_BUFFERED, FILE_ANY_ACCESS)\nUNICODE_STRING DEVICE_NAME = RTL_CONSTANT_STRING(L\"\\\\Device\\\\SpotlessDevice\"\
  );\nUNICODE_STRING DEVICE_SYMBOLIC_NAME = RTL_CONSTANT_STRING(L\"\\\\??\\\\SpotlessDeviceLink\");\n\nvoid sCreateProcessNotifyRoutine(HANDLE\
  \ ppid, HANDLE pid, BOOLEAN create)\n{\n\tif (create)\n\t{\n\t\tPEPROCESS process = NULL;\n\t\tPUNICODE_STRING parentProcessName\
  \ = NULL, processName = NULL;\n\t\t\n\t\tPsLookupProcessByProcessId(ppid, &process);\n\t\tSeLocateProcessImageName(process,\
  \ &parentProcessName);\n\n\t\tPsLookupProcessByProcessId(pid, &process);\n\t\tSeLocateProcessImageName(process, &processName);\n\
  \n\t\tDbgPrint(\"%d %wZ\\n\\t\\t%d %wZ\", ppid, parentProcessName, pid, processName);\n\t}\n\telse\n\t{\n\t\tDbgPrint(\"\
  Process %d lost child %d\", ppid, pid);\n\t}\n}\n\nvoid sCreateProcessNotifyRoutineEx(PEPROCESS process, HANDLE pid, PPS_CREATE_NOTIFY_INFO\
  \ createInfo)\n{\n\tUNREFERENCED_PARAMETER(process);\n\tUNREFERENCED_PARAMETER(pid);\n\t\n\tif (createInfo != NULL)\n\t\
  {\n\t\tif (wcsstr(createInfo->CommandLine->Buffer, L\"notepad\") != NULL)\n\t\t{\n\t\t\tDbgPrint(\"[!] Access to launch\
  \ notepad.exe was denied!\");\n\t\t\tcreateInfo->CreationStatus = STATUS_ACCESS_DENIED;\n\t\t}\n\t}\n}\n\nvoid sLoadImageNotifyRoutine(PUNICODE_STRING\
  \ imageName,\tHANDLE pid, PIMAGE_INFO imageInfo)\n{\n\tUNREFERENCED_PARAMETER(imageInfo);\n\tPEPROCESS process = NULL;\n\
  \tPUNICODE_STRING processName = NULL;\n\tPsLookupProcessByProcessId(pid, &process);\n\tSeLocateProcessImageName(process,\
  \ &processName);\n\n\tDbgPrint(\"%wZ (%d) loaded %wZ\", processName, pid, imageName);\n}\n\nvoid sCreateThreadNotifyRoutine(HANDLE\
  \ pid, HANDLE tid, BOOLEAN create)\n{\n\tif (create)\n\t{\n\t\tDbgPrint(\"%d created thread %d\", pid, tid);\n\t}\n\telse\n\
  \t{\n\t\tDbgPrint(\"Thread %d of process %d exited\", tid, pid);\n\t}\n}\n\nvoid DriverUnload(PDRIVER_OBJECT dob)\n{\n\t\
  DbgPrint(\"Driver unloaded, deleting symbolic links and devices\");\n\tIoDeleteDevice(dob->DeviceObject);\n\tIoDeleteSymbolicLink(&DEVICE_SYMBOLIC_NAME);\n\
  \tPsSetCreateProcessNotifyRoutine(sCreateProcessNotifyRoutine, TRUE);\n\tPsRemoveLoadImageNotifyRoutine(sLoadImageNotifyRoutine);\n\
  \tPsRemoveCreateThreadNotifyRoutine(sCreateThreadNotifyRoutine);\n\tPsSetCreateProcessNotifyRoutineEx(sCreateProcessNotifyRoutineEx,\
  \ TRUE);\n}\n\nNTSTATUS HandleCustomIOCTL(PDEVICE_OBJECT DeviceObject, PIRP Irp)\n{\n\tUNREFERENCED_PARAMETER(DeviceObject);\n\
  \tPIO_STACK_LOCATION stackLocation = NULL;\n\tCHAR *messageFromKernel = \"ohai from them kernelz\";\n\n\tstackLocation =\
  \ IoGetCurrentIrpStackLocation(Irp);\n\t\n\tif (stackLocation->Parameters.DeviceIoControl.IoControlCode == IOCTL_SPOTLESS)\n\
  \t{\n\t\tDbgPrint(\"IOCTL_SPOTLESS (0x%x) issued\", stackLocation->Parameters.DeviceIoControl.IoControlCode);\n\t\tDbgPrint(\"\
  Input received from userland: %s\", (char*)Irp->AssociatedIrp.SystemBuffer);\n\t}\n\n\tIrp->IoStatus.Information = strlen(messageFromKernel);\n\
  \tIrp->IoStatus.Status = STATUS_SUCCESS;\n\t\n\tDbgPrint(\"Sending to userland: %s\", messageFromKernel);\n\tRtlCopyMemory(Irp->AssociatedIrp.SystemBuffer,\
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
  \n\t// subscribe to notifications\n\tPsSetCreateProcessNotifyRoutine(sCreateProcessNotifyRoutine, FALSE);\n\tPsSetLoadImageNotifyRoutine(sLoadImageNotifyRoutine);\n\
  \tPsSetCreateThreadNotifyRoutine(sCreateThreadNotifyRoutine);\n\tPsSetCreateProcessNotifyRoutineEx(sCreateProcessNotifyRoutineEx,\
  \ FALSE);\n\tDbgPrint(\"Listeners isntalled..\");\n\n\tIoCreateDevice(DriverObject, 0, &DEVICE_NAME, FILE_DEVICE_UNKNOWN,\
  \ FILE_DEVICE_SECURE_OPEN, FALSE, &DriverObject->DeviceObject);\n\tif (!NT_SUCCESS(status))\n\t{\n\t\tDbgPrint(\"Could not\
  \ create device %wZ\", DEVICE_NAME);\n\t}\n\telse \n\t{\n\t\tDbgPrint(\"Device %wZ created\", DEVICE_NAME);\n\t}\n\n\tstatus\
  \ = IoCreateSymbolicLink(&DEVICE_SYMBOLIC_NAME, &DEVICE_NAME);\n\tif (NT_SUCCESS(status))\n\t{\n\t\tDbgPrint(\"Symbolic\
  \ link %wZ created\", DEVICE_SYMBOLIC_NAME);\n\t}\n\telse\n\t{\n\t\tDbgPrint(\"Error creating symbolic link %wZ\", DEVICE_SYMBOLIC_NAME);\n\
  \t}\n\t\n\treturn STATUS_SUCCESS;\n}\n```\n\n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetcreateprocessnotifyroutine\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetloadimagenotifyroutine\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetcreatethreadnotifyroutine\"\
  \ %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel-internals/subscribing-to-process-creation-thread-creation-and-image-load-notifications-from-a-kernel-driver.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/subscribing-to-process-creation-thread-creation-and-image-load-notifications-from-a-kernel-driver.md
````
