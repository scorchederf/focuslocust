---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Credentials in Registry

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-t1214-credentials-in-registry` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/t1214-credentials-in-registry.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Scanning registry hives for the value password:

## Preserved Body

````markdown
## Execution

Scanning registry hives for the value `password`:
```csharp
reg query HKLM /f password /t REG_SZ /s
# or
reg query HKCU /f password /t REG_SZ /s
```
## Observations

As a defender, you may want to monitor commandline argument logs and look for any that include `req query` and `password`strings:

![](<../../_assets/passwords-registry.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/credentials-in-registry.md)

## Evidence Excerpt

```text
_asset_filenames:
- passwords-registry.png
_body: '---
description: ''Internal recon, hunting for passwords in Windows registry''
---
# Credentials in Registry
## Execution
Scanning registry hives for the value `password`:
```
