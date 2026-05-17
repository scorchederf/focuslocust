---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1547 - Boot or Logon Autostart Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1547` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically running a program on system boot or account logon. These mechanisms may include automatically executing programs that are placed in specially designated directories or are referenced by repositories that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying or extending features of the kernel.

Since some boot or logon autostart programs run with higher privileges, an adversary may leverage these to elevate privileges.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Pnputil.exe](../../tools/windows/pnputil.exe.md) | explicit | source | Command metadata lists T1547: pnputil.exe -i -a {PATH_ABSOLUTE:.inf} |
| [Update.exe](../../tools/windows/update.exe.md) | explicit | source | Command metadata lists T1547: Update.exe --createShortcut={PATH:.exe} -l=Startup |

## Source Verification

[source record](../../sources/mitre/boot-or-logon-autostart-execution.md)

## Evidence Excerpt

```text
created: '2020-01-23T17:46:59.535Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may configure system settings to automatically execute a program during system boot or logon to
maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically
running a program on system boot or account logon.(Citation: Microsoft Run Key)(Citation: MSDN Authentication Packages)(Citation:
Microsoft TimeProvider)(Citation: Cylance Reg Persistence Sept 2013)(Citation: Linux Kernel Programming) These mechanisms
may include automatically executing programs that are placed in specially designated directories or are referenced by repositories
that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying
```
