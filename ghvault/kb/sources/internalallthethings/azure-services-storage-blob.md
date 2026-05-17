---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Storage Blob

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-storage-blob` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-storage-blob.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure Services - Storage Blob](../../topics/cloud/azure-services-storage-blob.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-services-storage-blob |
| name | Azure Services - Storage Blob |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-services-storage-blob.md |

## Preserved Source Material

````yaml
_body: "# Azure Services - Storage Blob\n\n* Blobs - `*.blob.core.windows.net`\n* File Services - `*.file.core.windows.net`\n\
  * Data Tables - `*.table.core.windows.net`\n* Queues - `*.queue.core.windows.net`\n\n## Enumerate blobs\n\n```powershell\n\
  PS > . C:\\Tools\\MicroBurst\\Misc\\InvokeEnumerateAzureBlobs.ps1\nPS > Invoke-EnumerateAzureBlobs -Base <SHORT DOMAIN>\
  \ -OutputFile azureblobs.txt\nFound Storage Account -  redacted.blob.core.windows.net\n```\n\n## List and download blobs\n\
  \nVisiting `https://<storage-name>.blob.core.windows.net/<storage-container>?restype=container&comp=list` provides a JSON\
  \ file containing a complete list of the Azure Blobs.\n\n```xml\n<EnumerationResults ContainerName=\"https://<storage-name>.blob.core.windows.net/<storage-container>\"\
  >\n    <Blobs>\n        <Blob>\n            <Name>index.html</Name>\n            <Url>https://<storage-name>.blob.core.windows.net/<storage-container>/index.html</Url>\n\
  \            <Properties>\n            <Last-Modified>Fri, 20 Oct 2023 20:08:20 GMT</Last-Modified>\n            <Etag>0x8DBD1A84E6455C0</Etag>\n\
  \            <Content-Length>782359</Content-Length>\n            <Content-Type>text/html</Content-Type>\n            <Content-Encoding/>\n\
  \            <Content-Language/>\n            <Content-MD5>JSe+sM+pXGAEFInxDgv4CA==</Content-MD5>\n            <Cache-Control/>\n\
  \            <BlobType>BlockBlob</BlobType>\n            <LeaseStatus>unlocked</LeaseStatus>\n            </Properties>\n\
  \        </Blob>\n```\n\nBrowse deleted files.\n\n```ps1\n$ curl -s -H \"x-ms-version: 2019-12-12\" 'https://<storage-name>.blob.core.windows.net/<storage-container>?restype=container&comp=list&include=versions'\
  \ | xmllint --format - | grep Name\n\n<EnumerationResults ServiceEndpoint=\"https://<storage-name>.blob.core.windows.net/\"\
  \ ContainerName=\"<storage-container>\">\n      <Name>index.html</Name>\n      <Name>scripts-transfer.zip</Name>\n```\n\n\
  ```powershell\nPS Az> Get-AzResource\nPS Az> Get-AzStorageAccount -name <NAME> -ResourceGroupName <NAME>\nPS Az> Get-AzStorageContainer\
  \ -Context (Get-AzStorageAccount -name <NAME> -ResourceGroupName <NAME>).context\nPS Az> Get-AzStorageBlobContent -Container\
  \ <NAME> -Context (Get-AzStorageAccount -name <NAME> -ResourceGroupName <NAME>).context -Blob\n```\n\nRetrieve exposed containers\
  \ with public access\n\n```ps1\nPS Az> (Get-AzStorageAccount | Get-AzStorageContainer).cloudBlobContainer | select Uri,@{n='PublicAccess';e={$_.Properties.PublicAccess}}\n\
  ```\n\n## SAS URL\n\n* Use [Storage Explorer](https://azure.microsoft.com/en-us/features/storage-explorer/)\n* Click on\
  \ **Open Connect Dialog** in the left menu.\n* Select **Blob container**.\n* On the **Select Authentication Method** page\n\
  \    * Select **Shared access signature (SAS)** and click on Next\n    * Copy the URL in **Blob container SAS URL** field.\n\
  \n:warning: You can also use `subscription`(username/password) to access storage resources such as blobs and files.\n\n\
  ## References\n\n* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-storage-blob.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-storage-blob.md
````
