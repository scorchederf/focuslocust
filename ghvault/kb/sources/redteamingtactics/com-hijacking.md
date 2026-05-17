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

## Generated Concept Page

- [COM Hijacking](../../topics/offensive-security/com-hijacking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1122-com-hijacking |
| name | COM Hijacking |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1122-com-hijacking.md |

## Preserved Source Material

```yaml
_asset_filenames:
- com-powershell.png
- com-registry.png
- com-sysmon.png
_body: "---\ndescription: 'UAC Bypass/Defense Evasion, Persistence'\n---\n\n# COM Hijacking\n\n> The Microsoft Component Object\
  \ Model \\(COM\\) is a platform-independent, distributed, object-oriented system for creating binary software components\
  \ that can interact. COM is the foundation technology for Microsoft's OLE \\(compound documents\\), ActiveX \\(Internet-enabled\
  \ components\\), as well as others.\n\nIn this lab we will execute a file-less UAC bypass technique.\n\n## Execution\n\n\
  On the compromised system, change the `HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\mscfile\\shell\\open\\command` default value\
  \ to point to your binary. In this case I chose powershell.exe:\n\n![](../../.gitbook/assets/com-registry.png)\n\nBy default,\
  \ launching Windows Event Viewer calls under the hood:`\"C:\\Windows\\system32\\mmc.exe\" \"C:\\Windows\\system32\\eventvwr.msc\"\
  \ /s` \n\nSince we hijacked the `HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\mscfile\\shell\\open\\command` to point to powershell,\
  \ when launching Even Viewer, the powershell is invoked instead:\n\n![](../../.gitbook/assets/com-powershell.png)\n\n##\
  \ Observation\n\nMonitoring registry for changes in `HKEY_CLASSES_ROOT\\mscfile\\shell\\open\\command` can reveal this hijaking\
  \ activity:\n\n![](../../.gitbook/assets/com-sysmon.png)\n\n## References\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1122\"\
  \ %}\n\n{% embed url=\"https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/\"\
  \ %}\n\n{% embed url=\"https://www.greyhathacker.net/?p=796\" %}\n\n{% embed url=\"http://www.fuzzysecurity.com/tutorials/27.html\"\
  \ %}"
_relative_path: offensive-security/persistence/t1122-com-hijacking.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1122-com-hijacking.md
```
