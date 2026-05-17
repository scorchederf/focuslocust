---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Sticky Keys

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1015-sethc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1015-sethc.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Sticky Keys](../../topics/offensive-security/sticky-keys.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1015-sethc |
| name | Sticky Keys |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1015-sethc.md |

## Preserved Source Material

```yaml
_asset_filenames:
- sethc-backdoor.png
- sethc-enumeration.png
- sethc-logon (1).png
- sethc-trustedinstaller.png
_body: '---

  description: Sticky keys backdoor.

  ---


  # Sticky Keys


  ## Execution


  Replace the originali sethc.exe with a cmd.exe and rename it. You may need to change sethc.exe owner to yourself first as
  TrustedIntaller may be giving you a hard time:


  ![](../../.gitbook/assets/sethc-trustedinstaller.png)


  ![](../../.gitbook/assets/sethc-backdoor.png)


  Hit shift 5 times while on the logon screen to invoke the backdoor:


  ![](<../../.gitbook/assets/sethc-logon (1).png>)


  ## Observations


  If you notice sethc.exe spawning well known windows processes, you may want to investigate the endpoint further:


  ![](../../.gitbook/assets/sethc-enumeration.png)'
_relative_path: offensive-security/persistence/t1015-sethc.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1015-sethc.md
```
