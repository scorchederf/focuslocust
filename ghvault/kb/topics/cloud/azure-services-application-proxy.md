---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Application Proxy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-application-proxy` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-application-proxy.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Enumerate applications that have Proxy

## Preserved Body

````markdown
## Enumerate

* Enumerate applications that have Proxy

    ```powershell
    PS C:\Tools> Get-AzureADApplication -All $true | %{try{GetAzureADApplicationProxyApplication -ObjectId $_.ObjectID;$_.DisplayName;$_.ObjectID}catch{}}
    PS C:\Tools> Get-AzureADServicePrincipal -All $true | ?{$_.DisplayName -eq "Finance Management System"}

    PS C:\Tools> . C:\Tools\GetApplicationProxyAssignedUsersAndGroups.ps1
    PS C:\Tools> Get-ApplicationProxyAssignedUsersAndGroups -ObjectId <OBJECT-ID>
    ```

## References

* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)
````

## Source Verification

[source record](../../sources/internalallthethings/azure-services-application-proxy.md)

## Evidence Excerpt

````text
_body: "# Azure Services - Application Proxy\n\n## Enumerate\n\n* Enumerate applications that have Proxy\n\n    ```powershell\n\
\    PS C:\\Tools> Get-AzureADApplication -All $true | %{try{GetAzureADApplicationProxyApplication -ObjectId $_.ObjectID;$_.DisplayName;$_.ObjectID}catch{}}\n\
\    PS C:\\Tools> Get-AzureADServicePrincipal -All $true | ?{$_.DisplayName -eq \"Finance Management System\"}\n\n    PS\
\ C:\\Tools> . C:\\Tools\\GetApplicationProxyAssignedUsersAndGroups.ps1\n    PS C:\\Tools> Get-ApplicationProxyAssignedUsersAndGroups\
\ -ObjectId <OBJECT-ID>\n    ```\n\n## References\n\n* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-application-proxy.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-application-proxy.md
````
