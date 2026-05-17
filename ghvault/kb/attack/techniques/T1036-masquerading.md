---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1036 - Masquerading

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1036` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.

Renaming abusable system utilities to evade security monitoring is also a form of Masquerading.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Diantz.exe](../../tools/windows/diantz.exe.md) | explicit | source | Command metadata lists T1036: diantz /f {PATH:.ddf} |
| [Makecab.exe](../../tools/windows/makecab.exe.md) | explicit | source | Command metadata lists T1036: makecab /F {PATH:.ddf} |
| [Msbuild.exe](../../tools/windows/msbuild.exe.md) | explicit | source | Command metadata lists T1036: msbuild.exe @{PATH:.rsp} |

## Source Verification

[source record](../../sources/mitre/masquerading.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:38.511Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to
users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated
or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users
into misidentifying the file type, and giving legitimate task or service names.
Renaming abusable system utilities to evade security monitoring is also a form of [Masquerading](https://attack.mitre.org/techniques/T1036).(Citation:
LOLBAS Main Site)'
```
