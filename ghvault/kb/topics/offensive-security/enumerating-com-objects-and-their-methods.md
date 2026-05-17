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

## Summary

This is a quick note to capture some of the commands for finding interesting COM objects and the methods they expose, based on the great article from Fireeye.

## Preserved Body

````markdown
This is a quick note to capture some of the commands for finding interesting COM objects and the methods they expose, based on the great [article](https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html) from Fireeye.

> The Microsoft Component Object Model (COM) is a platform-independent, distributed, object-oriented system for creating binary software components that can interact
>
> [https://docs.microsoft.com/en-us/windows/win32/com/the-component-object-model](https://docs.microsoft.com/en-us/windows/win32/com/the-component-object-model)

This is less of a post-exploitation technique, rather a method that allows one to look for interesting COM objects, that could be leveraged by one's malware.

## Enumerating COM Objects

We can find all the COM objects registered on the Windows system with:

```csharp
gwmi Win32_COMSetting | ? {$_.progid } | sort | ft ProgId,Caption,InprocServer32
```

![](<../../_assets/image (575).png>)

## Enumerating COM Object Methods

Once we have the list of COM objects and have identified an interesting COM object, we can now check the methods it exposes. In our case, let's pick a COM object `WScript.Shell.1` and check its methods like so:

```csharp
$o = [activator]::CreateInstance([type]::GetTypeFromProgID(("WScript.Shell.1"))) | gm
```

Below are the methods exposed by `WScript.Shell.1` COM object, one of which is `RegRead`:

![](<../../_assets/image (578).png>)

Let's see if we can read a registry value with `RedRead` method exposed by the `WScript.Shell.1`. `RedRead` accepts one string as an argument - a path to the registry value:

```csharp
$o.RegRead("HKEY_CURRENT_USER\Volatile Environment\LOGONSERVER")
```

Below shows how a registry value was read successfully:

![](<../../_assets/image (579).png>)

## Exposing All COM Object Methods

We can iterate through all the COM objects and list their methods and save it all to a text file that we can later on inspect for any other interesting methods:

```csharp
$com = gwmi Win32_COMSetting | ? {$_.progid } | select ProgId,Caption,InprocServer32

$com | % {
    $_.progid | out-file -append methods.txt
    [activator]::CreateInstance([type]::GetTypeFromProgID(($_.progid))) | gm | out-file -append methods.txt
    "`n`n" | out-file -append methods.txt
}
```

Below shows the output file with all the methods of all COM objects exposed, in focus are the methods for `Shell.Application.1` COM object:

![](<../../_assets/image (580).png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/enumerating-com-objects-and-their-methods.md)

## Evidence Excerpt

```text
_asset_filenames:
- image (575).png
- image (578).png
- image (579).png
- image (580).png
_body: "# Enumerating COM Objects and their Methods\n\nThis is a quick note to capture some of the commands for finding interesting\
\ COM objects and the methods they expose, based on the great [article](https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html)\
\ from Fireeye.\n\n> The Microsoft Component Object Model (COM) is a platform-independent, distributed, object-oriented\
```
