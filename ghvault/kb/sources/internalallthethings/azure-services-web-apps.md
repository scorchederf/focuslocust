---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Web Apps

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-web-apps` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-web-apps.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure Services - Web Apps](../../topics/cloud/azure-services-web-apps.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-services-web-apps |
| name | Azure Services - Web Apps |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-services-web-apps.md |

## Preserved Source Material

````yaml
_body: "# Azure Services - Web Apps\n\n## List Web App\n\n```ps1\naz webapp list\n```\n\n## Execute Commands\n\n```ps1\n$ARMToken\
  \ = Get-ARMTokenWithRefreshToken `\n    -RefreshToken \"0.ARwA6WgJJ9X2qk...\" `\n    -TenantID \"contoso.onmicrosoft.com\"\
  \n\nInvoke-AzureRMWebAppShellCommand `\n    -KuduURI \"https://<webapp>.scm.azurewebsites.net/api/command\" `\n    -Token\
  \ $ARMToken `\n    -Command \"whoami\"\n```\n\n## SSH Connection\n\nFirst check if the SSH over HTTP connection is enabled:\
  \ `(curl https://${appName}?app.scm.azurewebsites.net/webssh/host).statuscode`\n\n```powershell\naz webapp create-remote-connection\
  \ --subscription <SUBSCRIPTION-ID> --resource-group <RG-NAME> -n <APP-SERVICE-NAME>\n```\n\n## Kudu\n\nIn Azure App Service,\
  \ Kudu is the advanced management and deployment tool used for various operations such as continuous integration, troubleshooting,\
  \ and diagnostic tasks for your web applications. It provides a set of utilities and features for managing your app’s environment,\
  \ including access to application settings, log streams, and deployment management.\n\nYou can access this Kudu app at the\
  \ following URLs:\n\n* App not in the Isolated tier: `https://<app-name>.scm.azurewebsites.net`\n* Internet-facing app in\
  \ the Isolated tier (App Service Environment): `https://<app-name>.scm.<ase-name>.p.azurewebsites.net`\n* Internal app in\
  \ the Isolated tier (App Service Environment for internal load balancing): `https://<app-name>.scm.<ase-name>.appserviceenvironment.net`\n\
  \nKey Features of Kudu in App Service:\n\n* **Web-Based Console**: Provides a command-line interface (CLI) to execute commands\
  \ directly on the App Service environment.\n* **File Explorer**: Lets you view and manage files in your app’s environment.\n\
  * **Environment Diagnostics**: Offers insights into the environment variables, app settings, and detailed diagnostic logs.\n\
  * **Process Explorer**: Allows you to monitor and manage running processes in your app’s environment.\n* **Access to Logs**:\
  \ Easily view, download, and stream logs for debugging and troubleshooting.\n\n## References\n\n* [Training - Attacking\
  \ and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-web-apps.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-web-apps.md
````
