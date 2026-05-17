---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Account Discovery & Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-enumeration-and-discovery-t1087-account-discovery` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/t1087-account-discovery.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Account Discovery & Enumeration](../../topics/offensive-security/account-discovery-and-enumeration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-enumeration-and-discovery-t1087-account-discovery |
| name | Account Discovery & Enumeration |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/enumeration-and-discovery/t1087-account-discovery.md |

## Preserved Source Material

````yaml
_asset_filenames:
- enumeration-hunt-1.png
- enumeration-hunt-2.png
- enumeration-hunt-3.png
- enumeration-hunt-4.png
- enumeration-hunt-5.png
_body: "---\ndescription: Discovery\n---\n\n# Account Discovery & Enumeration\n\n## Execution\n\nLet's run some of the popular\
  \ enumeration commands on the victim system:\n\n{% code title=\"attacker@victim\" %}\n```csharp\nnet user\nnet user administrator\n\
  whoami /user\nwhoami /all\n...\n```\n{% endcode %}\n\n## Hunting and Observations\n\nHaving command line logging can help\
  \ in identifying a cluster of enumeration commands executed in a relatively short span of time on a compromised host .\n\
  \nFor this lab, I exported 8600+ command lines from various processes and wrote a dirty powershell script that ingests those\
  \ command lines and inspects them for a couple of classic windows enumeration commands that are executed in the span of\
  \ 2 minutes and spits them out:\n\n{% code title=\"hunt.ps1\" %}\n```csharp\nfunction hunt() {\n    [CmdletBinding()]Param()\n\
  \    $commandlines = Import-Csv C:\\Users\\mantvydas\\Downloads\\cmd-test.csv\n    $watch = 'whoami|net1 user|hostname|netstat|net\
  \ localgroup|cmd /c'\n    $matchedCommandlines = $commandlines| where-object {  $_.\"event_data.CommandLine\" -match $watch}\n\
  \n    $matchedCommandlines| foreach-Object {\n        [datetime]$eventTime = $_.\"@timestamp\"\n        [datetime]$low =\
  \ $eventTime.AddSeconds(-60)\n        [datetime]$high = $eventTime.AddSeconds(60)\n        $clusteredCommandlines = $commandlines\
  \ | Where-Object { [datetime]$_.\"@timestamp\" -ge $low -and [datetime]$_.\"@timestamp\" -le $high -and  $_.\"event_data.CommandLine\"\
  \ -match $watch}\n        \n        if ($clusteredCommandlines.length -ge 4) {\n            Write-Verbose \"Possible enumeration\
  \ around time: $low - $high ($eventTime)\"\n            $clusteredCommandlines\n        }\n    }\n}\n```\n{% endcode %}\n\
  \nInvoking the script to start the hunt:\n\n```csharp\n. \\hunt.ps1; hunt -verbose\n```\n\nBelow are some of the findings\
  \ which may warrant further investigation of the suspect host:\n\n![](../../.gitbook/assets/enumeration-hunt-5.png)\n\n\
  ![](../../.gitbook/assets/enumeration-hunt-4.png)\n\n![](../../.gitbook/assets/enumeration-hunt-3.png)\n\n![](../../.gitbook/assets/enumeration-hunt-2.png)\n\
  \n![](../../.gitbook/assets/enumeration-hunt-1.png)\n\n## References\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1087\"\
  \ %}"
_relative_path: offensive-security/enumeration-and-discovery/t1087-account-discovery.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/t1087-account-discovery.md
````
