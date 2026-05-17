---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1115 - Clipboard Data

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1115` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may collect data stored in the clipboard from users copying information within or between applications. 

For example, on Windows adversaries can access clipboard data by using <code>clip.exe</code> or <code>Get-Clipboard</code>. Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., Transmitted Data Manipulation).

macOS and Linux also have commands, such as <code>pbpaste</code>, to grab clipboard contents.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can harvest clipboard data on both Windows and macOS systems.(Citation: Github PowerShell Empire) |
| [Koadic](../../tools/unknown/koadic.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can retrieve the current content of the user clipboard.(Citation: Github Koadic) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) steals and modifies data from the clipboard.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can monitor Clipboard text and can use `System.Windows.Forms.Clipboard.GetText()` to collect data from the clipboard.(Citation: Github_SILENTTRINITY)   |

## Source Verification

[source record](../../sources/mitre/clipboard-data.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:25.967Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may collect data stored in the clipboard from users copying information within or between applications.\
\ \n\nFor example, on Windows adversaries can access clipboard data by using <code>clip.exe</code> or <code>Get-Clipboard</code>.(Citation:\
\ MSDN Clipboard)(Citation: clip_win_server)(Citation: CISA_AA21_200B) Additionally, adversaries may monitor then replace\
\ users’ clipboard with their data (e.g., [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002)).(Citation:\
\ mining_ruby_reversinglabs)\n\nmacOS and Linux also have commands, such as <code>pbpaste</code>, to grab clipboard contents.(Citation:\
\ Operating with EmPyre)"
```
