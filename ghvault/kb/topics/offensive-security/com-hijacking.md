---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# COM Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1122-com-hijacking` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1122-com-hijacking.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The Microsoft Component Object Model \(COM\) is a platform-independent, distributed, object-oriented system for creating binary software components that can interact. COM is the foundation technology for Microsoft's OLE \(compound documents

## Preserved Body

```markdown
> The Microsoft Component Object Model \(COM\) is a platform-independent, distributed, object-oriented system for creating binary software components that can interact. COM is the foundation technology for Microsoft's OLE \(compound documents\), ActiveX \(Internet-enabled components\), as well as others.

In this lab we will execute a file-less UAC bypass technique.

## Execution

On the compromised system, change the `HKEY_LOCAL_MACHINE\SOFTWARE\Classes\mscfile\shell\open\command` default value to point to your binary. In this case I chose powershell.exe:

![](<../../_assets/com-registry.png>)

By default, launching Windows Event Viewer calls under the hood:`"C:\Windows\system32\mmc.exe" "C:\Windows\system32\eventvwr.msc" /s` 

Since we hijacked the `HKEY_LOCAL_MACHINE\SOFTWARE\Classes\mscfile\shell\open\command` to point to powershell, when launching Even Viewer, the powershell is invoked instead:

![](<../../_assets/com-powershell.png>)

## Observation

Monitoring registry for changes in `HKEY_CLASSES_ROOT\mscfile\shell\open\command` can reveal this hijaking activity:

![](<../../_assets/com-sysmon.png>)

## References
```

## Source Verification

[source record](../../sources/redteamingtactics/com-hijacking.md)

## Evidence Excerpt

```text
_asset_filenames:
- com-powershell.png
- com-registry.png
- com-sysmon.png
_body: "---\ndescription: 'UAC Bypass/Defense Evasion, Persistence'\n---\n\n# COM Hijacking\n\n> The Microsoft Component Object\
\ Model \\(COM\\) is a platform-independent, distributed, object-oriented system for creating binary software components\
\ that can interact. COM is the foundation technology for Microsoft's OLE \\(compound documents\\), ActiveX \\(Internet-enabled\
\ components\\), as well as others.\n\nIn this lab we will execute a file-less UAC bypass technique.\n\n## Execution\n\n\
```
