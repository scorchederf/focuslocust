---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Hidden Files

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-t1158-hidden-files` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1158-hidden-files.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hidden Files](../../topics/offensive-security/hidden-files.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-t1158-hidden-files |
| name | Hidden Files |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/t1158-hidden-files.md |

## Preserved Source Material

````yaml
_asset_filenames:
- attrib-nofile.png
- attrib-reveal.png
- attrib-set.png
_body: '---

  description: ''Defense Evasion, Persistence''

  ---


  # Hidden Files


  ## Execution


  Hiding the file mantvydas.sdb using a native windows binary:


  {% code title="attacker@victim" %}

  ```csharp

  PS C:\experiments> attrib.exe +h .\mantvydas.sdb

  ```

  {% endcode %}


  Note how powershell \(or cmd\) says the file does not exist, however you can type out its contents if you know the file
  exists:


  ![](../../.gitbook/assets/attrib-nofile.png)


  Note, that `dir /a:h` \(attribute: hidden\) reveals files with a "hidden" attribute set:


  ![](../../.gitbook/assets/attrib-reveal.png)


  ## Observations


  As usual, monitoring commandline arguments may be a good idea if you want to identify these events:


  ![](../../.gitbook/assets/attrib-set.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1158" %}'
_relative_path: offensive-security/defense-evasion/t1158-hidden-files.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1158-hidden-files.md
````
