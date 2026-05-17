---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Phishing: Embedded HTML Forms

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-initial-access-phishing-with-ms-office-phishing-embedded-html-forms` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-ms-office/phishing-embedded-html-forms.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Phishing: Embedded HTML Forms](../../topics/offensive-security/phishing-embedded-html-forms.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-initial-access-phishing-with-ms-office-phishing-embedded-html-forms |
| name | Phishing: Embedded HTML Forms |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/initial-access/phishing-with-ms-office/phishing-embedded-html-forms.md |

## Preserved Source Material

```yaml
_asset_filenames:
- phishing-forms-ancestry.png
- phishing-forms-clsid.png
- phishing-forms-shell.gif
- phishing-forms-xml.png
_body: '---

  description: Code execution with embedded HTML Form Objects

  ---


  # Phishing: Embedded HTML Forms


  In this phishing lab I am just playing around with the POCs researched, coded and described by Yorick Koster in his blog
  post [Click me if you can, Office social engineering with embedded objects](https://securify.nl/blog/SFY20180801/click-me-if-you-can\_-office-social-engineering-with-embedded-objects.html)


  ## Execution


  ![](../../../.gitbook/assets/phishing-forms-shell.gif)


  {% file src="../../../.gitbook/assets/Forms.HTML.ps1" %}

  Forms.ps1

  {% endfile %}


  {% file src="../../../.gitbook/assets/Forms.HTML.docx" %}

  Forms.docx

  {% endfile %}


  ## Observations


  These types of phishing documents can be identified by looking for the CLSID 5512D112-5CC6-11CF-8D67-00AA00BDCE1D in the
  embedded `.bin` files:


  ![](../../../.gitbook/assets/phishing-forms-clsid.png)


  ...as well as inside the activeX1.xml file:


  ![](../../../.gitbook/assets/phishing-forms-xml.png)


  As usual, MS Office applications spawning cmd.exe or powershell.exe should be investigated:


  ![](../../../.gitbook/assets/phishing-forms-ancestry.png)


  ## References


  {% embed url="https://securify.nl/blog/SFY20180801/click-me-if-you-can_-office-social-engineering-with-embedded-objects.html"
  %}'
_relative_path: offensive-security/initial-access/phishing-with-ms-office/phishing-embedded-html-forms.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-ms-office/phishing-embedded-html-forms.md
```
