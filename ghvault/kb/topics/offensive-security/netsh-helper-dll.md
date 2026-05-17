---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# NetSh Helper DLL

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1128-netsh-helper-dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1128-netsh-helper-dll.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

NetshHelperBeacon helper DLL will be used to test out this technique. A compiled x64 DLL can be downloaded below:

## Preserved Body

````markdown
## Execution

[NetshHelperBeacon helper DLL](https://github.com/outflanknl/NetshHelperBeacon) will be used to test out this technique. A compiled x64 DLL can be downloaded below:
NetshHelperBeacon
The helper library, once loaded, will start `calc.exe`:

![](<../../_assets/netsh-code (1).png>)
```bash
.\netsh.exe add helper C:\tools\NetshHelperBeacon.dll
```
![](<../../_assets/netsh-calc.png>)

## Observations

Adding a new helper via commandline modifies registry, so as a defender you may want to monitor for registry changes in `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NetSh`:

![](<../../_assets/netsh-registry.png>)

When netsh is started, Procmon captures how `InitHelperDLL` expored function of our malicious DLL is called:

![](<../../_assets/netsh-procmon.png>)

As usual, monitoring command line arguments is a good idea that may help uncover suspicious activity:

![](<../../_assets/netsh-logs1.png>)

![](<../../_assets/netsh-logs2.png>)

## Interesting

Loading the malicious helper DLL crashed netsh. Inspecting the calc.exe process after the crash with Process Explorer reveals that the parent process is svchost, although the sysmon logs showed cmd.exe as its parent:

![](<../../_assets/netsh-ancestry.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/netsh-helper-dll.md)

## Evidence Excerpt

```text
_asset_filenames:
- netsh-ancestry.png
- netsh-calc.png
- netsh-code (1).png
- netsh-logs1.png
- netsh-logs2.png
- netsh-procmon.png
- netsh-registry.png
```
