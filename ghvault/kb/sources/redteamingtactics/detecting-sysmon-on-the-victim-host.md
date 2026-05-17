---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Detecting Sysmon on the Victim Host

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-enumeration-and-discovery-detecting-sysmon-on-the-victim-host` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/detecting-sysmon-on-the-victim-host.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Detecting Sysmon on the Victim Host](../../topics/offensive-security/detecting-sysmon-on-the-victim-host.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-enumeration-and-discovery-detecting-sysmon-on-the-victim-host |
| name | Detecting Sysmon on the Victim Host |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/enumeration-and-discovery/detecting-sysmon-on-the-victim-host.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2018-10-09 17-39-28.png
- Screenshot from 2018-10-09 17-48-11.png
- Screenshot from 2018-10-09 17-50-47.png
- Screenshot from 2018-10-09 17-51-45.png
- Screenshot from 2018-10-09 17-56-33.png
- Screenshot from 2018-10-09 18-12-09.png
- Screenshot from 2018-10-09 18-13-37.png
- Screenshot from 2018-10-09 18-14-57.png
- Screenshot from 2018-10-09 18-43-39.png
- Screenshot from 2018-10-09 18-57-32.png
_body: '---

  description: Exploring ways to detect Sysmon presence on the victim system

  ---


  # Detecting Sysmon on the Victim Host


  ## Processes


  {% code title="attacker@victim" %}

  ```csharp

  PS C:\> Get-Process | Where-Object { $_.ProcessName -eq "Sysmon" }

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Screenshot from 2018-10-09 17-39-28.png>)


  {% hint style="warning" %}

  Note: process name can be changed during installation

  {% endhint %}


  ## Services


  {% code title="attacker@victim" %}

  ```csharp

  Get-CimInstance win32_service -Filter "Description = ''System Monitor service''"

  # or

  Get-Service | where-object {$_.DisplayName -like "*sysm*"}

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Screenshot from 2018-10-09 17-48-11.png>)


  {% hint style="warning" %}

  Note: display names and descriptions can be changed

  {% endhint %}


  ## Windows Events


  {% code title="attacker@victim" %}

  ```csharp

  reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Sysmon/Operational

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Screenshot from 2018-10-09 17-50-47.png>)


  ## Filters


  {% code title="attacker@victim" %}

  ```

  PS C:\> fltMC.exe

  ```

  {% endcode %}


  Note how even though you can change the sysmon service and driver names, the sysmon altitude is always the same - `385201`


  ![](<../../.gitbook/assets/Screenshot from 2018-10-09 17-51-45.png>)


  ## Sysmon Tools + Accepted Eula


  {% code title="attacker@victim" %}

  ```

  ls HKCU:\Software\Sysinternals

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Screenshot from 2018-10-09 17-56-33.png>)


  ## Sysmon -c


  Once symon executable is found, the config file can be checked like so:


  ```

  sysmon -c

  ```


  ![](<../../.gitbook/assets/Screenshot from 2018-10-09 18-43-39.png>)


  ## Config File on the Disk


  If you are lucky enough, you may be able to find the config file itself on the disk by using native windows utility findstr:


  {% code title="attcker@victim" %}

  ```csharp

  findstr /si ''<ProcessCreate onmatch="exclude">'' C:\tools\*

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Screenshot from 2018-10-09 18-57-32.png>)


  ## Get-SysmonConfiguration


  A powershell tool by @mattifestation that extracts sysmon rules from the registry:


  {% code title="attacker@victim" %}

  ```csharp

  PS C:\tools> (Get-SysmonConfiguration).Rules

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Screenshot from 2018-10-09 18-12-09.png>)


  As an example, looking a bit deeper into the `ProcessCreate` rules:


  {% code title="attacker@victim" %}

  ```csharp

  (Get-SysmonConfiguration).Rules[0].Rules

  ```

  {% endcode %}


  We can see the rules almost as they were presented in the sysmon configuration XML file:


  ![](<../../.gitbook/assets/Screenshot from 2018-10-09 18-13-37.png>)


  A snippet from the actual sysmonconfig-export.xml file:


  ![](<../../.gitbook/assets/Screenshot from 2018-10-09 18-14-57.png>)


  ## Bypassing Sysmon


  Since [Get-SysmonConfiguration](detecting-sysmon-on-the-victim-host.md#get-sysmonconfiguration) gives you the ability to
  see the rules sysmon is monitoring on, you can play around those.


  Another way to bypass the sysmon altogether is explored here:


  {% content-ref url="../defense-evasion/unloading-sysmon-driver.md" %}

  [unloading-sysmon-driver.md](../defense-evasion/unloading-sysmon-driver.md)

  {% endcontent-ref %}


  ## References


  {% embed url="https://www.darkoperator.com/blog/2018/10/5/operating-offensively-against-sysmon" %}


  {% embed url="https://github.com/mattifestation/PSSysmonTools/blob/master/PSSysmonTools/Code/SysmonRuleParser.ps1" %}


  {% embed url="https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs/allocated-altitudes" %}


  {% embed url="https://github.com/GhostPack/Seatbelt" %}'
_relative_path: offensive-security/enumeration-and-discovery/detecting-sysmon-on-the-victim-host.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/detecting-sysmon-on-the-victim-host.md
````
