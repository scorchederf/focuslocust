---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1003 - OS Credential Dumping

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password. Credentials can be obtained from OS caches, memory, or structures. Credentials can then be used to perform Lateral Movement and access restricted information.

Several of the tools mentioned in associated sub-techniques may be used by both adversaries and professional security testers. Additional custom tools likely exist as well.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Createdump.exe](../../tools/windows/createdump.exe.md) | explicit | source | Command metadata lists T1003: createdump.exe -n -f {PATH:.dmp} {PID} |
| [Rpcping.exe](../../tools/windows/rpcping.exe.md) | explicit | source | Command metadata lists T1003: rpcping -s 127.0.0.1 -e 1234 -a privacy -u NTLM |
| [Sqldumper.exe](../../tools/windows/sqldumper.exe.md) | explicit | source | Command metadata lists T1003: sqldumper.exe 464 0 0x0110 |
| [Tttracer.exe](../../tools/windows/tttracer.exe.md) | explicit | source | Command metadata lists T1003: TTTracer.exe -dumpFull -attach {PID} |
| [rdrleakdiag.exe](../../tools/windows/rdrleakdiag.exe.md) | explicit | source | Command metadata lists T1003: rdrleakdiag.exe /p 940 /o {PATH_ABSOLUTE:folder} /fullmemdmp /wait 1 |

## Source Verification

[source record](../../sources/mitre/os-credential-dumping.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:19.735Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the
form of a hash or a clear text password. Credentials can be obtained from OS caches, memory, or structures.(Citation: Brining
MimiKatz to Unix) Credentials can then be used to perform [Lateral Movement](https://attack.mitre.org/tactics/TA0008) and
access restricted information.
Several of the tools mentioned in associated sub-techniques may be used by both adversaries and professional security testers.
Additional custom tools likely exist as well.
```
