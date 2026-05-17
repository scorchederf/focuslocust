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

## Generated Concept Page

- [Installing Root Certificate](../../topics/offensive-security/installing-root-certificate.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1130-install-root-certificate |
| name | Installing Root Certificate |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1130-install-root-certificate.md |

## Preserved Source Material

````yaml
_asset_filenames:
- certs-add-with-ps.png
- certs-certutil.png
- certs-installed.png
- certs-logs.png
- certs-ps-logging.png
- certs-registry.png
_body: '---

  description: Defense Evasion

  ---


  # Installing Root Certificate


  ## Execution


  Adding a certificate with a native windows binary:


  {% code title="attacker@victim" %}

  ```csharp

  certutil.exe -addstore -f -user Root C:\Users\spot\Downloads\certnew.cer

  ```

  {% endcode %}


  ![](../../.gitbook/assets/certs-certutil.png)


  Checking to see the certificate got installed:


  ![](../../.gitbook/assets/certs-installed.png)


  Adding the certificate with powershell:


  {% code title="attacker@victim" %}

  ```csharp

  Import-Certificate -FilePath C:\Users\spot\Downloads\certnew.cer -CertStoreLocation Cert:\CurrentUser\Root\

  ```

  {% endcode %}


  ![](../../.gitbook/assets/certs-add-with-ps.png)


  ## Observations


  Advanced poweshell logging to the rescue:


  ![](../../.gitbook/assets/certs-ps-logging.png)


  Commandline logging:


  ![](../../.gitbook/assets/certs-logs.png)


  The CAs get installed to:


  ```csharp

  Computer\HKEY_CURRENT_USER\Software\Microsoft\SystemCertificates\Root\Certificates\C6B22A75B0633E76C9F21A81F2EE6E991F5C94AE

  ```


  ..so it is worth monitoring registry changes there:


  ![](../../.gitbook/assets/certs-registry.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1130" %}'
_relative_path: offensive-security/persistence/t1130-install-root-certificate.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1130-install-root-certificate.md
````
