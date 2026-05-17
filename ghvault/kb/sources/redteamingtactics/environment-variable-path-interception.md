---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Environment Variable $Path Interception

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-privilege-escalation-environment-variable-path-interception` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/environment-variable-path-interception.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Environment Variable $Path Interception](../../topics/offensive-security/environment-variable-path-interception.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-privilege-escalation-environment-variable-path-interception |
| name | Environment Variable $Path Interception |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/privilege-escalation/environment-variable-path-interception.md |

## Preserved Source Material

```yaml
_asset_filenames:
- image (485).png
- image (486).png
- image (487).png
- image (488).png
_body: '# Environment Variable $Path Interception


  It''s possible to abuse `$PATH` environment variable to elevate privileges if the variable:


  * contains a folder that a malicious user can write to

  * that folder precedes c:\windows\system32\\


  Below is an example, showing how c:\temp precedes c:\windows\system32:


  ![](<../../.gitbook/assets/image (485).png>)


  Let''s make sure c:\temp is (M)odifiable by low privileged users:


  ![](<../../.gitbook/assets/image (488).png>)


  Let''s now drop our malicious file (calc.exe in this case) into c:\temp and call it cmd.exe:


  ![](<../../.gitbook/assets/image (486).png>)


  Now, the next time a high privileged user invokes cmd.exe, our malicious cmd.exe will be invoked from the c:\temp:


  ![](<../../.gitbook/assets/image (487).png>)


  This can be very easily abused in environments where software deployment packages call powershell, cmd, cscript and other
  similar system binaries with `NT SYSTEM` privileges to carry out their tasks.'
_relative_path: offensive-security/privilege-escalation/environment-variable-path-interception.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/environment-variable-path-interception.md
```
