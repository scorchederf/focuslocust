---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1137 - Office Application Startup

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1137` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may leverage Microsoft Office-based applications for persistence between startups. Microsoft Office is a fairly common application suite on Windows-based operating systems within an enterprise network. There are multiple mechanisms that can be used with Office for persistence when an Office-based application is started; this can include the use of Office Template Macros and add-ins.

A variety of features have been discovered in Outlook that can be abused to obtain persistence, such as Outlook rules, forms, and Home Page. These persistence mechanisms can work within Outlook or be used through Office 365.

## Source Verification

[source record](../../sources/mitre/office-application-startup.md)

## Evidence Excerpt

```text
created: '2017-12-14T16:46:06.044Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may leverage Microsoft Office-based applications for persistence between startups. Microsoft Office
is a fairly common application suite on Windows-based operating systems within an enterprise network. There are multiple
mechanisms that can be used with Office for persistence when an Office-based application is started; this can include the
use of Office Template Macros and add-ins.
A variety of features have been discovered in Outlook that can be abused to obtain persistence, such as Outlook rules, forms,
and Home Page.(Citation: SensePost Ruler GitHub) These persistence mechanisms can work within Outlook or be used through
```
