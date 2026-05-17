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

## Summary

Replace the originali sethc.exe with a cmd.exe and rename it. You may need to change sethc.exe owner to yourself first as TrustedIntaller may be giving you a hard time:

## Preserved Body

```markdown
## Execution

Replace the originali sethc.exe with a cmd.exe and rename it. You may need to change sethc.exe owner to yourself first as TrustedIntaller may be giving you a hard time:

![](<../../_assets/sethc-trustedinstaller.png>)

![](<../../_assets/sethc-backdoor.png>)

Hit shift 5 times while on the logon screen to invoke the backdoor:

![](<../../_assets/sethc-logon (1).png>)

## Observations

If you notice sethc.exe spawning well known windows processes, you may want to investigate the endpoint further:

![](<../../_assets/sethc-enumeration.png>)
```

## Source Verification

[source record](../../sources/redteamingtactics/sticky-keys.md)

## Evidence Excerpt

```text
_asset_filenames:
- sethc-backdoor.png
- sethc-enumeration.png
- sethc-logon (1).png
- sethc-trustedinstaller.png
_body: '---
description: Sticky keys backdoor.
---
```
