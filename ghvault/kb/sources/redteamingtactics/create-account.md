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

## Generated Concept Page

- [Create Account](../../topics/offensive-security/create-account.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1136-create-account |
| name | Create Account |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1136-create-account.md |

## Preserved Source Material

````yaml
_asset_filenames:
- account-add.png
- account-created.png
- account-events.png
_body: '---

  description: Persistence

  ---


  # Create Account


  ## Execution


  {% code title="attacker@victim" %}

  ```bash

  net user test test123 /add /domain

  ```

  {% endcode %}


  ## Observations


  ![commandline arguments](../../.gitbook/assets/account-add.png)


  There is a whole range of interesting events that could be monitored related to new account creation:


  ![](../../.gitbook/assets/account-events.png)


  Details for the newly added account are logged as event `4720` :


  ![](../../.gitbook/assets/account-created.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1136" %}'
_relative_path: offensive-security/persistence/t1136-create-account.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1136-create-account.md
````
