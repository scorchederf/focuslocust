---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Lateral Movement over headless RDP with SharpRDP

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-lateral-movement-over-headless-rdp-with-sharprdp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/lateral-movement-over-headless-rdp-with-sharprdp.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Lateral Movement over headless RDP with SharpRDP](../../topics/offensive-security/lateral-movement-over-headless-rdp-with-sharprdp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-lateral-movement-over-headless-rdp-with-sharprdp |
| name | Lateral Movement over headless RDP with SharpRDP |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/lateral-movement-over-headless-rdp-with-sharprdp.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (476).png
- image (477).png
- image (478).png
_body: '# Lateral Movement over headless RDP with SharpRDP


  Executing commands on a remote host is possible by using a headless (non-GUI) RDP lateral movement technique brought by
  a tool called [SharpRDP](https://posts.specterops.io/revisiting-remote-desktop-lateral-movement-8fb905cb46c3?gi=fe80458d82a5).


  ## Execution


  Executing a binary on a remote machine dc01 from a compromised system with offense\administrator credentials:


  ```

  SharpRDP.exe computername=dc01 command=calc username=offense\administrator password=123456

  ```


  ![](<../../.gitbook/assets/image (476).png>)


  ## Observations


  Defenders may want to look for mstscax.dll module being loaded by suspicious binaries on a compromised host from which SharpRDP
  is being executed:


  ![](<../../.gitbook/assets/image (477).png>)


  Also, weird binaries making connections to port 3389:


  ![](<../../.gitbook/assets/image (478).png>)


  ## References


  {% embed url="https://posts.specterops.io/revisiting-remote-desktop-lateral-movement-8fb905cb46c3?gi=fe80458d82a5" %}'
_relative_path: offensive-security/lateral-movement/lateral-movement-over-headless-rdp-with-sharprdp.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/lateral-movement-over-headless-rdp-with-sharprdp.md
````
