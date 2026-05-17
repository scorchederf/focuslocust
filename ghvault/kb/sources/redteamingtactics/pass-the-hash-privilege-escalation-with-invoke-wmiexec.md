---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Pass The Hash: Privilege Escalation with Invoke-WMIExec

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-privilege-escalation-pass-the-hash-privilege-escalation-with-invoke-wmiexec` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/pass-the-hash-privilege-escalation-with-invoke-wmiexec.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pass The Hash: Privilege Escalation with Invoke-WMIExec](../../topics/offensive-security/pass-the-hash-privilege-escalation-with-invoke-wmiexec.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-privilege-escalation-pass-the-hash-privilege-escalation-with-invoke-wmiexec |
| name | Pass The Hash: Privilege Escalation with Invoke-WMIExec |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/privilege-escalation/pass-the-hash-privilege-escalation-with-invoke-wmiexec.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (166).png
- image (167).png
- image (168).png
- image (171).png
- image (172).png
- image (174).png
- image (175).png
_body: '# Pass The Hash: Privilege Escalation with Invoke-WMIExec


  ## Execution


  If you have an NTLMv2 hash of a local administrator on a box ws01, it''s possible to pass that hash and execute code with
  privileges of that local administrator account:


  ```csharp

  Invoke-WmiExec -target ws01 -hash 32ed87bd5fdc5e9cba88547376818d4 -username administrator -command hostname

  ```


  Below shows how the user `low` is not a local admin, passes the hash of the local `administrator` account on ws01 and executes
  a command successfully:


  ![](<../../.gitbook/assets/image (167).png>)


  ## RID != 500 - No Pass The Hash for You


  Say you have a hash of the user spotless who you know is a local admin on ws01:


  ![](<../../.gitbook/assets/image (175).png>)


  ...but when you attempt passing the hash, you get access denied - why is that?


  ![](<../../.gitbook/assets/image (174).png>)


  It may be because hashes for accounts that are not RID=500 (not default administrator accounts) are stripped of some privileges
  during the token creation.


  ![](<../../.gitbook/assets/image (172).png>)


  ![](<../../.gitbook/assets/image (171).png>)


  If the target system you are passing the hash to, has the following registry key/value/data set to 0x1, pass the hash will
  work even for accounts that are not RID 500:


  ```

  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy

  ```


  ![](<../../.gitbook/assets/image (166).png>)


  ```csharp

  Invoke-WmiExec -target ws01 -hash 32ed87bd5fdc5e9cba88547376818d4 -username spotless -command hostname

  ```


  ![](<../../.gitbook/assets/image (168).png>)


  ## References


  {% embed url="https://www.harmj0y.net/blog/redteaming/pass-the-hash-is-dead-long-live-localaccounttokenfilterpolicy/" %}'
_relative_path: offensive-security/privilege-escalation/pass-the-hash-privilege-escalation-with-invoke-wmiexec.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/pass-the-hash-privilege-escalation-with-invoke-wmiexec.md
````
