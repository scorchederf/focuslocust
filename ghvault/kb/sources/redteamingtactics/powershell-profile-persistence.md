---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Powershell Profile Persistence

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-powershell-profile-persistence` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/powershell-profile-persistence.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Powershell Profile Persistence](../../topics/offensive-security/powershell-profile-persistence.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-powershell-profile-persistence |
| name | Powershell Profile Persistence |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/powershell-profile-persistence.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (215).png
- image (218).png
- image (219).png
_body: '# Powershell Profile Persistence


  It''s possible to use powershell profiles for persistence and/or privilege escalation.


  ## Execution


  There are four places you can abuse the powershell profile, depending on the privileges you have:


  ```csharp

  $PROFILE | select *

  ```


  ![](<../../.gitbook/assets/image (219).png>)


  Let''s add the code to a `$profile` variable (that expands to the current user''s profile file) that will get executed the
  next time the compromised user launches a powershell console:


  {% code title="attacker@target" %}

  ```csharp

  echo "whoami > c:\temp\whoami.txt" > $PROFILE

  cat $PROFILE

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/image (215).png>)


  Once the compromised user launches powershell, our code gets executed:


  ![](<../../.gitbook/assets/image (218).png>)


  {% hint style="warning" %}

  If the user is not using profiles, the technique will stick out immediately due to the "loading personal and system profiles..."
  message at the top.

  {% endhint %}


  ## References


  {% embed url="https://attack.mitre.org/techniques/T1504/" %}'
_relative_path: offensive-security/persistence/powershell-profile-persistence.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/powershell-profile-persistence.md
````
