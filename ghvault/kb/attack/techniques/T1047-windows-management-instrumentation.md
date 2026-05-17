---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1047 - Windows Management Instrumentation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1047` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may abuse Windows Management Instrumentation (WMI) to execute malicious commands and payloads. WMI is designed for programmers and is the infrastructure for management data and operations on Windows systems. WMI is an administration feature that provides a uniform environment to access Windows system components.

The WMI service enables both local and remote access, though the latter is facilitated by Remote Services such as Distributed Component Object Model and Windows Remote Management. Remote WMI over DCOM operates using port 135, whereas WMI over WinRM operates over port 5985 when using HTTP and 5986 for HTTPS. 

An adversary can use WMI to interact with local and remote systems and use it as a means to execute various behaviors, such as gathering information for Discovery as well as Execution of commands and payloads. For example, `wmic.exe` can be abused by an adversary to delete shadow copies with the command `wmic.exe Shadowcopy Delete` (i.e., Inhibit System Recovery).

**Note:** `wmic.exe` is deprecated as of January of 2024, with the WMIC feature being “disabled by default” on Windows 11+. WMIC will be removed from subsequent Windows releases and replaced by PowerShell as the primary WMI interface. In addition to PowerShell and tools like `wbemtool.exe`, COM APIs can also be used to programmatically interact with WMI via C++, .NET, VBScript, etc.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use WMI to move laterally.(Citation: Palo Alto Brute Ratel July 2022) |
| [Covenant](../../tools/unknown/covenant.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) can utilize WMI to install new Grunt listeners through XSL files or command one-liners.(Citation: Github Covenant) |
| [CrackMapExec](../../tools/unknown/crackmapexec.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can execute remote commands using Windows Management Instrumentation.(Citation: CME Github September 2018)	 |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use WMI to deliver a payload to a remote host.(Citation: Github PowerShell Empire)  |
| [Impacket](../../tools/unknown/impacket.md) | explicit | source | [Impacket](https://attack.mitre.org/software/S0357)'s `wmiexec` module can be used to execute commands through WMI.(Citation: Impacket Tools)(Citation: Sygnia VelvetAnt 2024A) |
| [Koadic](../../tools/unknown/koadic.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can use WMI to execute commands.(Citation: Github Koadic) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) has a number of modules that use WMI to execute tasks.(Citation: GitHub PoshC2) |
| [PowerSploit](../../tools/unknown/powersploit.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-WmiCommand</code> CodeExecution module uses WMI to execute and retrieve the output from a [PowerShell](https://attack.mitre.org/techniques/T1086) payload.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use WMI for lateral movement.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [wbemtest.exe](../../tools/windows/wbemtest.exe.md) | explicit | source | Command metadata lists T1047: wbemtest.exe |

## Source Verification

[source record](../../sources/mitre/windows-management-instrumentation.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:44.329Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Windows Management Instrumentation (WMI) to execute malicious commands and payloads. WMI
is designed for programmers and is the infrastructure for management data and operations on Windows systems.(Citation: WMI
1-3) WMI is an administration feature that provides a uniform environment to access Windows system components.
The WMI service enables both local and remote access, though the latter is facilitated by [Remote Services](https://attack.mitre.org/techniques/T1021)
such as [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) and [Windows Remote Management](https://attack.mitre.org/techniques/T1021/006).(Citation:
WMI 1-3) Remote WMI over DCOM operates using port 135, whereas WMI over WinRM operates over port 5985 when using HTTP and
```
