---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Create Account

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1136-create-account` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1136-create-account.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

bash

## Preserved Body

````markdown
## Execution
```bash
net user test test123 /add /domain
```
## Observations

![commandline arguments](<../../_assets/account-add.png>)

There is a whole range of interesting events that could be monitored related to new account creation:

![](<../../_assets/account-events.png>)

Details for the newly added account are logged as event `4720` :

![](<../../_assets/account-created.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/create-account.md)

## Evidence Excerpt

```text
_asset_filenames:
- account-add.png
- account-created.png
- account-events.png
_body: '---
description: Persistence
---
# Create Account
```
