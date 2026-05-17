---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# MSI Wrapper

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-windows-hardening-windows-local-privilege-escalation-msi-wrapper` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/windows-local-privilege-escalation/msi-wrapper.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Download the free version app from https://www.exemsi.com/documentation/getting-started/, execute it and wrap the "malicious" binary on it.\

## Preserved Body

```markdown
Download the free version app from [https://www.exemsi.com/documentation/getting-started/](https://www.exemsi.com/download/), execute it and wrap the "malicious" binary on it.\
Note that you can wrap a "**.bat**" if you **just** want to **execute** **command lines (instead of cmd.exe select the .bat file)**

![](<../../images/image (417).png>)

And this is the most important part of the configuration:

![](<../../images/image (312).png>)

![](<../../images/image (346).png>)

![](<../../images/image (1072).png>)

(Please, note that if you try to pack your own binary you will be able to modify these values)

From here just click on **next buttons** and the last **build button and your installer/wrapper will be generated.**
```

## Source Verification

[source record](../../sources/hacktricks/msi-wrapper.md)

## Evidence Excerpt

```text
_body: '# MSI Wrapper
{{#include ../../banners/hacktricks-training.md}}
Download the free version app from [https://www.exemsi.com/documentation/getting-started/](https://www.exemsi.com/download/),
execute it and wrap the "malicious" binary on it.\
Note that you can wrap a "**.bat**" if you **just** want to **execute** **command lines (instead of cmd.exe select the .bat
file)**
![](<../../images/image (417).png>)
And this is the most important part of the configuration:
```
