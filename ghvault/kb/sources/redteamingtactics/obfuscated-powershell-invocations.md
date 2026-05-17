---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Obfuscated Powershell Invocations

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-t1027-obfuscated-powershell-invocations` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1027-obfuscated-powershell-invocations.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Obfuscated Powershell Invocations](../../topics/offensive-security/obfuscated-powershell-invocations.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-t1027-obfuscated-powershell-invocations |
| name | Obfuscated Powershell Invocations |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/t1027-obfuscated-powershell-invocations.md |

## Preserved Source Material

````yaml
_asset_filenames:
- kibana-cmdlines.png
- powershell-outlier.png
- powershell-single.png
_body: '---

  description: Defense Evasion

  ---


  # Obfuscated Powershell Invocations


  This topic is huge, but in this lab, I wanted to see if I could do a simple hunt for encoded powershell command invocations.


  ## Defining the Hunt


  I want to find processes with base64 encoded commandlines that may indicate obfuscated powershell invocations.


  Data source: sysmon logs that provide insight into process creation events, that contains commandlines the process was started.


  ## Execution


  I had a sample of 27000 events that had a commandline logged, which I exported to a .csv file:


  ![](../../.gitbook/assets/kibana-cmdlines.png)


  Since malicious encoded commands are usually lengthy, contiguous sequence of printable ASCII characters \(including characters
  such as =,/,+\), I decided to loop through the commandlines and only pull those that matched a simple regex `([A-Za-z0-9]){64,}`


  Full powershell one liner below:


  ```csharp

  Import-Csv .\cmdline.csv | Where-Object {$_."event_data.CommandLine" -match ''([A-Za-z0-9]){64,}'' }  | ForEach-Object {
  Write-Output $_.''event_data.CommandLine''; Write-host }

  ```


  Below are the results - note how out of 27000+ events, only a handful were returned, among which was one base64 encoded
  powershell commandline:


  ![](../../.gitbook/assets/powershell-outlier.png)


  Since I am looking for malicious powershell invocations, I could adjust the query as follows to remove processes that do
  not contain `powershell.exe` mentioned in them:


  ```csharp

  Import-Csv .\cmdline.csv | Where-Object {$."event_data.CommandLine" -match ''([A-Za-z0- 9]){64,}'' -and $."eventdata.CommandLine"
  -match ''powershell.exe'' } | ForEach-Object { Write-Output $.''event_data.Comm andLine''; Write-host }

  ```


  Bingo - only one result returned:


  ![](../../.gitbook/assets/powershell-single.png)


  This type of hunting is interesting, so I will be coming back to explore this area further.


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1027" %}'
_relative_path: offensive-security/defense-evasion/t1027-obfuscated-powershell-invocations.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1027-obfuscated-powershell-invocations.md
````
