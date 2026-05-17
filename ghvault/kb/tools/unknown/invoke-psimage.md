---
parsed_by: focuslocust
source: mitre
type: generated
---
# Invoke-PSImage

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0231` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Invoke-PSImage takes a PowerShell script and embeds the bytes of the script into the pixels of a PNG image. It generates a one liner for executing either from a file of from the web. Example of usage is embedding the PowerShell code from the Invoke-Mimikatz module and embed it into an image file. By calling the image file from a macro for example, the macro will download the picture and execute the PowerShell code, which in this case will dump the passwords.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/invoke-psimage.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1027.003 - Steganography](../../attack/techniques/T1027.003-steganography.md) | explicit | source | [Invoke-PSImage](https://attack.mitre.org/software/S0231) can be used to embed a PowerShell script within the pixels of a PNG file.(Citation: GitHub Invoke-PSImage) |
| [T1027.009 - Embedded Payloads](../../attack/techniques/T1027.009-embedded-payloads.md) | explicit | source | [Invoke-PSImage](https://attack.mitre.org/software/S0231) can be used to embed payload data within a new image file.(Citation: GitHub PSImage) |

## Source Verification

[source record](../../sources/mitre/invoke-psimage.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Invoke-PSImage](https://attack.mitre.org/software/S0231) takes a PowerShell script and embeds the bytes of
the script into the pixels of a PNG image. It generates a one liner for executing either from a file of from the web. Example
of usage is embedding the PowerShell code from the Invoke-Mimikatz module and embed it into an image file. By calling the
image file from a macro for example, the macro will download the picture and execute the PowerShell code, which in this
case will dump the passwords. (Citation: GitHub Invoke-PSImage)'
external_references:
```
