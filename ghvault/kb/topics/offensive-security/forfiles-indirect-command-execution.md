---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Forfiles Indirect Command Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-t1202-forfiles-indirect-command-execution` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1202-forfiles-indirect-command-execution.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This technique launches an executable without a cmd.exe.

## Preserved Body

````markdown
This technique launches an executable without a cmd.exe.

## Execution

```csharp
forfiles /p c:\windows\system32 /m notepad.exe /c calc.exe
```

![](<../../_assets/forfiles-executed.png>)

## Observations

Defenders can monitor for process creation/commandline logs to detect this activity:

![](<../../_assets/forfiles-ancestry.png>)

![](<../../_assets/forfiles-cmdline.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/forfiles-indirect-command-execution.md)

## Evidence Excerpt

```text
_asset_filenames:
- forfiles-ancestry.png
- forfiles-cmdline.png
- forfiles-executed.png
_body: '---
description: Defense Evasion
---
# Forfiles Indirect Command Execution
```
