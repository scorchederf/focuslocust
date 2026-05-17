---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Word Macros

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-reversing-word-macros` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/reversing/word-macros.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

It's very common to find junk code that is never used to make the reversing of the macro more difficult.\

## Preserved Body

```markdown
### Junk Code

It's very common to find **junk code that is never used** to make the reversing of the macro more difficult.\
For example, in the following image you can see that and If that is never going to be true is used to execute some junk and useless code.

![](<../images/image (369).png>)

### Macro Forms

Using the **GetObject** function it's possible to obtain data from forms of the macro. This can be used to difficult the analysis. The following is a photo of a macro form used to **hide data inside text boxes** (a text box can be hiding other text boxes):

![](<../images/image (344).png>)
```

## Source Verification

[source record](../../sources/hacktricks/word-macros.md)

## Evidence Excerpt

```text
_body: '# Word Macros
{{#include ../banners/hacktricks-training.md}}
### Junk Code
It''s very common to find **junk code that is never used** to make the reversing of the macro more difficult.\
For example, in the following image you can see that and If that is never going to be true is used to execute some junk
and useless code.
![](<../images/image (369).png>)
### Macro Forms
```
