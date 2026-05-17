---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Installing Root Certificate

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1130-install-root-certificate` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1130-install-root-certificate.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adding a certificate with a native windows binary:

## Preserved Body

````markdown
## Execution

Adding a certificate with a native windows binary:
```csharp
certutil.exe -addstore -f -user Root C:\Users\spot\Downloads\certnew.cer
```
![](<../../_assets/certs-certutil.png>)

Checking to see the certificate got installed:

![](<../../_assets/certs-installed.png>)

Adding the certificate with powershell:
```csharp
Import-Certificate -FilePath C:\Users\spot\Downloads\certnew.cer -CertStoreLocation Cert:\CurrentUser\Root\
```
![](<../../_assets/certs-add-with-ps.png>)

## Observations

Advanced poweshell logging to the rescue:

![](<../../_assets/certs-ps-logging.png>)

Commandline logging:

![](<../../_assets/certs-logs.png>)

The CAs get installed to:

```csharp
Computer\HKEY_CURRENT_USER\Software\Microsoft\SystemCertificates\Root\Certificates\C6B22A75B0633E76C9F21A81F2EE6E991F5C94AE
```

..so it is worth monitoring registry changes there:

![](<../../_assets/certs-registry.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/installing-root-certificate.md)

## Evidence Excerpt

```text
_asset_filenames:
- certs-add-with-ps.png
- certs-certutil.png
- certs-installed.png
- certs-logs.png
- certs-ps-logging.png
- certs-registry.png
_body: '---
```
