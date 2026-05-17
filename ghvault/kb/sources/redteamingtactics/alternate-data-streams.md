---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Alternate Data Streams

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-t1096-alternate-data-streams` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1096-alternate-data-streams.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Alternate Data Streams](../../topics/offensive-security/alternate-data-streams.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-t1096-alternate-data-streams |
| name | Alternate Data Streams |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/t1096-alternate-data-streams.md |

## Preserved Source Material

````yaml
_asset_filenames:
- ads-benign.png
- ads-commandline.png
- ads-evil-2.png
- ads-evil.png
- ads-evil3.png
- ads-powershell.png
_body: '# Alternate Data Streams


  ## Execution


  Creating a benign text file:


  {% code title="attacker@victim" %}

  ```csharp

  echo "this is benign" > benign.txt

  Get-ChildItem

  ```

  {% endcode %}


  ![](../../.gitbook/assets/ads-benign.png)


  ![](broken-reference)


  Hiding an `evil.txt` file inside the `benign.txt`


  {% code title="attacker@victim" %}

  ```csharp

  cmd ''/c echo "this is evil" > benign.txt:evil.txt''

  ```

  {% endcode %}


  ![](../../.gitbook/assets/ads-evil.png)


  ![](broken-reference)


  Note how the evil.txt file is not visible through the explorer - that is because it is in the alternate data stream now.
  Opening the benign.txt shows no signs of evil.txt. However, the data from evil.txt can still be accessed as shown below
  in the commandline - `type benign.txt:evil.txt`:


  ![](../../.gitbook/assets/ads-evil-2.png)


  Additionally, we can view the data in the notepad as well by issuing:


  {% code title="attacker@victim" %}

  ```csharp

  notepad .\benign.txt:evil.txt

  ```

  {% endcode %}


  ![](../../.gitbook/assets/ads-evil3.png)


  ## Observations


  ![](../../.gitbook/assets/ads-commandline.png)


  Note that powershell can also help finding alternate data streams:


  ```csharp

  Get-Item c:\experiment\evil.txt -Stream *

  Get-Content .\benign.txt -Stream evil.txt

  ```


  ![](../../.gitbook/assets/ads-powershell.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1096" %}


  {% embed url="https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/providers/filesystem-provider/get-item-for-filesystem?view=powershell-6"
  %}


  {% embed url="https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/" %}'
_relative_path: offensive-security/defense-evasion/t1096-alternate-data-streams.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1096-alternate-data-streams.md
````
