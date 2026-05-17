---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Office Templates

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-office-templates` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/office-templates.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Office Templates](../../topics/offensive-security/office-templates.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-office-templates |
| name | Office Templates |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/office-templates.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Annotation 2019-06-23 120121.png
- Annotation 2019-06-23 120805.png
- word-template.gif
_body: '# Office Templates


  It''s possible to persist in the userland by abusing Microsof templates - documents that are used as base templates for
  all new documents created by Office. In this lab, I am abusing Ms Word templates.


  ## Weaponization


  Let''s open and edit the base template called `Normal` that can be found at:


  ```

  C:\Users\mantvydas\AppData\Roaming\Microsoft\Templates

  ```


  ![](<../../.gitbook/assets/Annotation 2019-06-23 120121.png>)


  Create a new AutoOpen macro and add your VBA code there:


  ```javascript

  Sub AutoOpen()

  MsgBox "Ohai from the template :)"

  End Sub

  ```


  ![](<../../.gitbook/assets/Annotation 2019-06-23 120805.png>)


  Save the template and exit. We''re now ready to create a new document, save it and launch it - at this point, we should
  get our VBA code executed. Below GIF shows exactly that:


  ![](../../.gitbook/assets/word-template.gif)


  ## References


  {% embed url="https://www.mdsec.co.uk/2019/05/persistence-the-continued-or-prolonged-existence-of-something-part-1-microsoft-office/"
  %}'
_relative_path: offensive-security/persistence/office-templates.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/office-templates.md
````
