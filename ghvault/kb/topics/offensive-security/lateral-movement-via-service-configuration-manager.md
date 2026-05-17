---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Lateral Movement via Service Configuration Manager

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-lateral-movement-abusing-service-configuration-manager` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/lateral-movement-abusing-service-configuration-manager.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

It's possible to execute commands on a remote host by abusing service configuration manager by changing the service binpath to your malicious command and restarting the service so your payload gets executed - this is all automated by a nice

## Preserved Body

````markdown
It's possible to execute commands on a remote host by abusing service configuration manager by changing the service binpath to your malicious command and restarting the service so your payload gets executed - this is all automated by a nice tool [SCShell](https://github.com/Mr-Un1k0d3r/SCShell)

## Execution

Scshell expects the following arguments: target, service, payload, username, domain, password:
```
.\scshell.exe ws01 XblAuthManager "C:\windows\system32\cmd.exe /c echo 'lateral hello' > c:\temp\lat.txt" spotless offense 123456
```
![](<../../_assets/scshell.gif>)

## Considerations

From the defensive side, you may want to consider about monitoring services that change their binPaths "too often" as this may not be normal in your environment, especially if the binPath is "very" different ([Levenshtein](https://www.google.com/search?q=levenshtein+distance\&oq=levensht\&aqs=chrome.1.69i57j0l5.2647j0j7\&sourceid=chrome\&ie=UTF-8)) to the previously known good value and if the service configuration is being changed over the network:

![](<../../_assets/image (245).png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/lateral-movement-via-service-configuration-manager.md)

## Evidence Excerpt

```text
_asset_filenames:
- image (245).png
- scshell.gif
_body: '# Lateral Movement via Service Configuration Manager
It''s possible to execute commands on a remote host by abusing service configuration manager by changing the service binpath
to your malicious command and restarting the service so your payload gets executed - this is all automated by a nice tool
[SCShell](https://github.com/Mr-Un1k0d3r/SCShell)
## Execution
```
