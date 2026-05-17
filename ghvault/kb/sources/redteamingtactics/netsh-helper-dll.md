---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# NetSh Helper DLL

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1128-netsh-helper-dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1128-netsh-helper-dll.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [NetSh Helper DLL](../../topics/offensive-security/netsh-helper-dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1128-netsh-helper-dll |
| name | NetSh Helper DLL |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1128-netsh-helper-dll.md |

## Preserved Source Material

````yaml
_asset_filenames:
- netsh-ancestry.png
- netsh-calc.png
- netsh-code (1).png
- netsh-logs1.png
- netsh-logs2.png
- netsh-procmon.png
- netsh-registry.png
_body: '---

  description: Persistence, code execution using netsh helper arbitrary libraries.

  ---


  # NetSh Helper DLL


  ## Execution


  [NetshHelperBeacon helper DLL](https://github.com/outflanknl/NetshHelperBeacon) will be used to test out this technique.
  A compiled x64 DLL can be downloaded below:


  {% file src="../../.gitbook/assets/NetshHelperBeacon.dll" %}

  NetshHelperBeacon

  {% endfile %}


  The helper library, once loaded, will start `calc.exe`:


  ![](<../../.gitbook/assets/netsh-code (1).png>)


  {% code title="attacker@victim" %}

  ```bash

  .\netsh.exe add helper C:\tools\NetshHelperBeacon.dll

  ```

  {% endcode %}


  ![](../../.gitbook/assets/netsh-calc.png)


  ## Observations


  Adding a new helper via commandline modifies registry, so as a defender you may want to monitor for registry changes in
  `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NetSh`:


  ![](../../.gitbook/assets/netsh-registry.png)


  When netsh is started, Procmon captures how `InitHelperDLL` expored function of our malicious DLL is called:


  ![](../../.gitbook/assets/netsh-procmon.png)


  As usual, monitoring command line arguments is a good idea that may help uncover suspicious activity:


  ![](../../.gitbook/assets/netsh-logs1.png)


  ![](../../.gitbook/assets/netsh-logs2.png)


  ## Interesting


  Loading the malicious helper DLL crashed netsh. Inspecting the calc.exe process after the crash with Process Explorer reveals
  that the parent process is svchost, although the sysmon logs showed cmd.exe as its parent:


  ![](../../.gitbook/assets/netsh-ancestry.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1128" %}'
_relative_path: offensive-security/persistence/t1128-netsh-helper-dll.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1128-netsh-helper-dll.md
````
