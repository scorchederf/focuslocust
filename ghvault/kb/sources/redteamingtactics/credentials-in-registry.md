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

## Generated Concept Page

- [Credentials in Registry](../../topics/offensive-security/credentials-in-registry.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-t1214-credentials-in-registry |
| name | Credentials in Registry |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/t1214-credentials-in-registry.md |

## Preserved Source Material

````yaml
_asset_filenames:
- passwords-registry.png
_body: '---

  description: ''Internal recon, hunting for passwords in Windows registry''

  ---


  # Credentials in Registry


  ## Execution


  Scanning registry hives for the value `password`:


  {% code title="attacker@victim" %}

  ```csharp

  reg query HKLM /f password /t REG_SZ /s

  # or

  reg query HKCU /f password /t REG_SZ /s

  ```

  {% endcode %}


  ## Observations


  As a defender, you may want to monitor commandline argument logs and look for any that include `req query` and `password`strings:


  ![](../../.gitbook/assets/passwords-registry.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1214" %}'
_relative_path: offensive-security/credential-access-and-credential-dumping/t1214-credentials-in-registry.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/t1214-credentials-in-registry.md
````
