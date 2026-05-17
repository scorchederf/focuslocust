---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Using COM to Enumerate Hostname, Username, Domain, Network Drives

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-enumeration-and-discovery-using-com-to-enumerate-hostname-username-domain-network-drives` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/using-com-to-enumerate-hostname-username-domain-network-drives.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

At Computer\HKEYCLASSESROOT\CLSID\{093FF999-1EA0-4079-9525-9614C3504B74} we have a Windows Script Host Network Object COM object which allows us to get details such as computer name, logged on user, etc:

## Preserved Body

````markdown
At `Computer\HKEY_CLASSES_ROOT\CLSID\{093FF999-1EA0-4079-9525-9614C3504B74}` we have a **Windows Script Host Network Object** COM object which allows us to get details such as computer name, logged on user, etc:

![](<../../_assets/Annotation 2019-06-18 222057.png>)

```csharp
$o = [activator]::CreateInstance([type]::GetTypeFromCLSID("093FF999-1EA0-4079-9525-9614C3504B74"))
```

Below are all the properties and methods exposed by the object:

```csharp
$o | gm
```

![](<../../_assets/Annotation 2019-06-18 221846.png>)

Viewing username, domain, machine name, etc:

```
$o
```

![](<../../_assets/Annotation 2019-06-18 221927.png>)

We can also see any network connected drives:

```
$o.EnumNetworkDrives()
```

![](<../../_assets/Annotation 2019-06-18 221949.png>)

## Observations

Below shows what additional modules Powershell loads once the COM object is instantiated:

![](<../../_assets/loaded-dlls.gif>)
````

## Source Verification

[source record](../../sources/redteamingtactics/using-com-to-enumerate-hostname-username-domain-network-drives.md)

## Evidence Excerpt

```text
_asset_filenames:
- Annotation 2019-06-18 221846.png
- Annotation 2019-06-18 221927.png
- Annotation 2019-06-18 221949.png
- Annotation 2019-06-18 222057.png
- loaded-dlls.gif
_body: '# Using COM to Enumerate Hostname, Username, Domain, Network Drives
At `Computer\HKEY_CLASSES_ROOT\CLSID\{093FF999-1EA0-4079-9525-9614C3504B74}` we have a **Windows Script Host Network Object**
```
