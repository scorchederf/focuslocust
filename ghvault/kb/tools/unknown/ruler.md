---
parsed_by: focuslocust
source: mitre
type: generated
---
# Ruler

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0358` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Ruler is a tool to abuse Microsoft Exchange services. It is publicly available on GitHub and the tool is executed via the command line. The creators of Ruler have also released a defensive tool, NotRuler, to detect its usage.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/ruler.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1087.003 - Email Account](../../attack/techniques/T1087.003-email-account.md) | explicit | source | [Ruler](https://attack.mitre.org/software/S0358) can be used to enumerate Exchange users and dump the GAL.(Citation: SensePost Ruler GitHub) |
| [T1137.003 - Outlook Forms](../../attack/techniques/T1137.003-outlook-forms.md) | explicit | source | [Ruler](https://attack.mitre.org/software/S0358) can be used to automate the abuse of Outlook Forms to establish persistence.(Citation: SensePost Ruler GitHub) |
| [T1137.004 - Outlook Home Page](../../attack/techniques/T1137.004-outlook-home-page.md) | explicit | source | [Ruler](https://attack.mitre.org/software/S0358) can be used to automate the abuse of Outlook Home Pages to establish persistence.(Citation: SensePost Ruler GitHub)  |
| [T1137.005 - Outlook Rules](../../attack/techniques/T1137.005-outlook-rules.md) | explicit | source | [Ruler](https://attack.mitre.org/software/S0358) can be used to automate the abuse of Outlook Rules to establish persistence.(Citation: SensePost Ruler GitHub)  |

## Source Verification

[source record](../../sources/mitre/ruler.md)

## Evidence Excerpt

```text
created: '2019-02-04T18:27:00.501Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Ruler](https://attack.mitre.org/software/S0358) is a tool to abuse Microsoft Exchange services. It is publicly
available on GitHub and the tool is executed via the command line. The creators of [Ruler](https://attack.mitre.org/software/S0358)
have also released a defensive tool, NotRuler, to detect its usage.(Citation: SensePost Ruler GitHub)(Citation: SensePost
NotRuler)'
external_references:
- external_id: S0358
```
