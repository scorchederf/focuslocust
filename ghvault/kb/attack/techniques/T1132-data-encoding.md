---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1132 - Data Encoding

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1132` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may encode data to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system. Use of data encoding may adhere to existing protocol specifications and includes use of ASCII, Unicode, Base64, MIME, or other binary-to-text and character encoding systems.  Some data encoding systems may also result in data compression, such as gzip.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Mythic](../../tools/unknown/mythic.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) provides various transform functions to encode and/or randomize C2 data.(Citation: Mythc Documentation)	 |
| [evilginx2](../../tools/unknown/evilginx2.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can randomly generate and Base64 encode parameters in phishing links to defeat static detection.(Citation: Breakdev Evilginx 2.4 SEP 2020) |

## Source Verification

[source record](../../sources/mitre/data-encoding.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:43.540Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may encode data to make the content of command and control traffic more difficult to detect. Command
and control (C2) information can be encoded using a standard data encoding system. Use of data encoding may adhere to existing
protocol specifications and includes use of ASCII, Unicode, Base64, MIME, or other binary-to-text and character encoding
systems.(Citation: Wikipedia Binary-to-text Encoding) (Citation: Wikipedia Character Encoding) Some data encoding systems
may also result in data compression, such as gzip.'
external_references:
```
