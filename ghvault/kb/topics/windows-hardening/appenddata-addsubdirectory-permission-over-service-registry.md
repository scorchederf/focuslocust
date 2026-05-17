---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# AppendData/AddSubdirectory Permission over Service Registry

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-windows-hardening-windows-local-privilege-escalation-appenddata-addsubdirectory-permission-over-service-registry` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/windows-local-privilege-escalation/appenddata-addsubdirectory-permission-over-service-registry.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The original post is https://itm4n.github.io/windows-registry-rpceptmapper-eop/

## Preserved Body

```markdown
**The original post is** [**https://itm4n.github.io/windows-registry-rpceptmapper-eop/**](https://itm4n.github.io/windows-registry-rpceptmapper-eop/)
```

## Source Verification

[source record](../../sources/hacktricks/appenddata-addsubdirectory-permission-over-service-registry.md)

## Evidence Excerpt

```text
_body: '# AppendData/AddSubdirectory Permission over Service Registry
{{#include ../../banners/hacktricks-training.md}}
**The original post is** [**https://itm4n.github.io/windows-registry-rpceptmapper-eop/**](https://itm4n.github.io/windows-registry-rpceptmapper-eop/)
## Summary
Two registry keys were found to be writable by the current user:
- **`HKLM\SYSTEM\CurrentControlSet\Services\Dnscache`**
- **`HKLM\SYSTEM\CurrentControlSet\Services\RpcEptMapper`**
It was suggested to check the permissions of the **RpcEptMapper** service using the **regedit GUI**, specifically the **Advanced
```
