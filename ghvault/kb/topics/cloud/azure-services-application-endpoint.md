---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Application Endpoint

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-application-endpoint` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-application-endpoint.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Enumerate possible endpoints for applications starting/ending with PREFIX

## Preserved Body

````markdown
## Enumerate

* Enumerate possible endpoints for applications starting/ending with PREFIX

    ```powershell
    PS C:\Tools> Get-AzureADServicePrincipal -All $true -Filter "startswith(displayName,'PREFIX')" | % {$_.ReplyUrls}
    PS C:\Tools> Get-AzureADApplication -All $true -Filter "endswith(displayName,'PREFIX')" | Select-Object ReplyUrls,WwwHomePage,HomePage
    ```

## Access

```ps1
https://myapps.microsoft.com/signin/<App ID>?tenantId=<TenantID>
```

## References

* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)
````

## Source Verification

[source record](../../sources/internalallthethings/azure-services-application-endpoint.md)

## Evidence Excerpt

````text
_body: "# Azure Services - Application Endpoint\n\n## Enumerate\n\n* Enumerate possible endpoints for applications starting/ending\
\ with PREFIX\n\n    ```powershell\n    PS C:\\Tools> Get-AzureADServicePrincipal -All $true -Filter \"startswith(displayName,'PREFIX')\"\
\ | % {$_.ReplyUrls}\n    PS C:\\Tools> Get-AzureADApplication -All $true -Filter \"endswith(displayName,'PREFIX')\" | Select-Object\
\ ReplyUrls,WwwHomePage,HomePage\n    ```\n\n## Access\n\n```ps1\nhttps://myapps.microsoft.com/signin/<App ID>?tenantId=<TenantID>\n\
```\n\n## References\n\n* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-application-endpoint.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-application-endpoint.md
````
