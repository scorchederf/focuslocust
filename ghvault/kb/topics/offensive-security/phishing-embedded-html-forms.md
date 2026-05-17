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

## Summary

In this phishing lab I am just playing around with the POCs researched, coded and described by Yorick Koster in his blog post Click me if you can, Office social engineering with embedded objects

## Preserved Body

```markdown
In this phishing lab I am just playing around with the POCs researched, coded and described by Yorick Koster in his blog post [Click me if you can, Office social engineering with embedded objects](https://securify.nl/blog/SFY20180801/click-me-if-you-can\_-office-social-engineering-with-embedded-objects.html)

## Execution

![](<../../../_assets/phishing-forms-shell.gif>)
Forms.ps1
Forms.docx
## Observations

These types of phishing documents can be identified by looking for the CLSID 5512D112-5CC6-11CF-8D67-00AA00BDCE1D in the embedded `.bin` files:

![](<../../../_assets/phishing-forms-clsid.png>)

...as well as inside the activeX1.xml file:

![](<../../../_assets/phishing-forms-xml.png>)

As usual, MS Office applications spawning cmd.exe or powershell.exe should be investigated:

![](<../../../_assets/phishing-forms-ancestry.png>)

## References
```

## Source Verification

[source record](../../sources/redteamingtactics/phishing-embedded-html-forms.md)

## Evidence Excerpt

```text
_asset_filenames:
- phishing-forms-ancestry.png
- phishing-forms-clsid.png
- phishing-forms-shell.gif
- phishing-forms-xml.png
_body: '---
description: Code execution with embedded HTML Form Objects
---
```
