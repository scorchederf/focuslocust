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

## Summary

Executing commands on a remote host is possible by using a headless (non-GUI) RDP lateral movement technique brought by a tool called SharpRDP

## Preserved Body

````markdown
Executing commands on a remote host is possible by using a headless (non-GUI) RDP lateral movement technique brought by a tool called [SharpRDP](https://posts.specterops.io/revisiting-remote-desktop-lateral-movement-8fb905cb46c3?gi=fe80458d82a5).

## Execution

Executing a binary on a remote machine dc01 from a compromised system with offense\administrator credentials:

```
SharpRDP.exe computername=dc01 command=calc username=offense\administrator password=123456
```

![](<../../_assets/image (476).png>)

## Observations

Defenders may want to look for mstscax.dll module being loaded by suspicious binaries on a compromised host from which SharpRDP is being executed:

![](<../../_assets/image (477).png>)

Also, weird binaries making connections to port 3389:

![](<../../_assets/image (478).png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/lateral-movement-over-headless-rdp-with-sharprdp.md)

## Evidence Excerpt

```text
_asset_filenames:
- image (476).png
- image (477).png
- image (478).png
_body: '# Lateral Movement over headless RDP with SharpRDP
Executing commands on a remote host is possible by using a headless (non-GUI) RDP lateral movement technique brought by
a tool called [SharpRDP](https://posts.specterops.io/revisiting-remote-desktop-lateral-movement-8fb905cb46c3?gi=fe80458d82a5).
## Execution
```
