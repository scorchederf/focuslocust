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

## Summary

Select Kernel Mode Driver, Emtpy \(KMDF\) from templates:

## Preserved Body

````markdown
## Simple Windows Driver Framework \(WDF\) Kernel Driver

Select Kernel Mode Driver, Emtpy \(KMDF\) from templates:

![](<../../_assets/image (510).png>)

## Create a driver.c

Create a new `driver.c` file under `Source Files`:

![](<../../_assets/image (81).png>)

## Add Driver Code
```c
#include <ntddk.h>
#include <wdf.h>

DRIVER_INITIALIZE DriverEntry;
EVT_WDF_DRIVER_DEVICE_ADD EvtDriverDeviceAdd;
EVT_WDF_DRIVER_UNLOAD UnloadDriver;

_Use_decl_annotations_
void UnloadDriver(IN WDFDRIVER driver)
{
    UNREFERENCED_PARAMETER(driver);
    DbgPrint("Driver unloaded");
}

NTSTATUS DriverEntry(_In_ PDRIVER_OBJECT DriverObject, _In_ PUNICODE_STRING RegistryPath)
{
    WDF_DRIVER_CONFIG config;
    WDF_DRIVER_CONFIG_INIT(&config, EvtDriverDeviceAdd);
    config.EvtDriverUnload = UnloadDriver;
    NTSTATUS status = WdfDriverCreate(DriverObject, RegistryPath, WDF_NO_OBJECT_ATTRIBUTES, &config, WDF_NO_HANDLE);
    
    DbgPrint("Driver loaded");

    return status;
}

NTSTATUS EvtDriverDeviceAdd(_In_ WDFDRIVER Driver,_Inout_ PWDFDEVICE_INIT DeviceInit)
{
    UNREFERENCED_PARAMETER(Driver);
    WDFDEVICE device;
    NTSTATUS status = WdfDeviceCreate(&DeviceInit, WDF_NO_OBJECT_ATTRIBUTES, &device);
    
    return status;
}
```
## Enable DbgPrint Monitoring for WinDBG

Change the debug output verbosity:

```text
ed kd_default_mask 0xf
```

![](<../../_assets/image (58).png>)

[Starting the driver](loading-a-windows-kernel-driver-to-windows-10.md) allows us to see the debug output in WinDBG:

![](<../../_assets/image (447).png>)

## Enable DbgPrint Monitoring for DbgView

Create a sub-key `Debug Print Filter` if it does not exist:

```text
Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Debug Print Filter
```

Add a new DWORD value `DEFAULT` and set its Data field to `0xf`:

![](<../../_assets/image (414).png>)

If we load the driver now and start it, we can see the debug output in DbgView too:

![](<../../_assets/image (176).png>)

## Requested Control is Not Valid for This Service

The below error message is seen if you attempt to stop the WDF driver via OSR Driver Loader or the native sc.exe, even if you have defined the driver unloading routine:

![](<../../_assets/image (137).png>)

I could not find a solution to this, but WDM driver has no such issue - see the code below.

## Simple Windows Driver Model \(WDM\) Kernel Driver Load and Unload

Below is a simple WDM driver that can be compiled and then loaded and stopped with OSR Driver Loader:

```c
#include <ntddk.h>

void DriverUnload(PDRIVER_OBJECT dob)
{
	UNREFERENCED_PARAMETER(dob);
	DbgPrint("Driver unloaded");
}

NTSTATUS DriverEntry(PDRIVER_OBJECT DriverObject, PUNICODE_STRING RegistryPath) {

	UNREFERENCED_PARAMETER(DriverObject);
	UNREFERENCED_PARAMETER(RegistryPath);

	DriverObject->DriverUnload = DriverUnload;
	DbgPrint("Driver loaded");

	return STATUS_SUCCESS;
}
```

Below shows how our driver is loaded and unloaded via OSR Loader while DbgView prints our DbgPrint output defined in the above `DriverEntry` and `DriverUnload` routines:

![](<../../_assets/image (504).png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/compiling-a-simple-kernel-driver-dbgprint-dbgview.md)

## Evidence Excerpt

```text
_asset_filenames:
- image (137).png
- image (176).png
- image (414).png
- image (447).png
- image (504).png
- image (510).png
- image (58).png
```
