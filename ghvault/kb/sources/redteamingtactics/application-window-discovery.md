---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Application Window Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-enumeration-and-discovery-t1010-application-window-discovery` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/t1010-application-window-discovery.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Application Window Discovery](../../topics/offensive-security/application-window-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-enumeration-and-discovery-t1010-application-window-discovery |
| name | Application Window Discovery |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/enumeration-and-discovery/t1010-application-window-discovery.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Annotation 2019-06-18 224603.png
- window-titles.png
_body: '---

  description: Discovery

  ---


  # Application Window Discovery


  Retrieving running application window titles:


  {% code title="attacker@victim" %}

  ```csharp

  get-process | where-object {$_.mainwindowtitle -ne ""} | Select-Object mainwindowtitle

  ```

  {% endcode %}


  ![](../../.gitbook/assets/window-titles.png)


  A COM method that also includes the process path and window location coordinates:


  {% code title="attacker@victim" %}

  ```csharp

  [activator]::CreateInstance([type]::GetTypeFromCLSID("13709620-C279-11CE-A49E-444553540000")).windows()

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Annotation 2019-06-18 224603.png>)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1010" %}'
_relative_path: offensive-security/enumeration-and-discovery/t1010-application-window-discovery.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/t1010-application-window-discovery.md
````
