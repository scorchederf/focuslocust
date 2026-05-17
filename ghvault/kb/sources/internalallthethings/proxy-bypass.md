---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Proxy Bypass

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-evasion-proxy-bypass` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/proxy-bypass.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Proxy Bypass](../../topics/redteam/proxy-bypass.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-evasion-proxy-bypass |
| name | Proxy Bypass |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/evasion/proxy-bypass.md |

## Preserved Source Material

````yaml
_body: "# Proxy Bypass\n\n> An HTTP proxy server acts as an intermediary between a client (like a web browser) and a web server.\
  \ It processes client requests for web resources, fetches them from the destination server, and returns them to the client.\n\
  \n## Summary\n\n* [Methodology](#methodology)\n    * [Discover Proxy Configuration](#discover-proxy-configuration)\n   \
  \ * [PAC Proxy](#pac-proxy)\n    * [Common Bypass](#common-bypass)\n* [References](#references)\n\n## Methodology\n\n###\
  \ Discover Proxy Configuration\n\n* Windows, in the registry key `DefaultConnectionSettings`\n\n    ```ps1\n    Software\\\
  Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Connections\\DefaultConnectionSettings\n    Software\\Microsoft\\\
  Windows\\CurrentVersion\\Internet Settings\\ProxyServer\n    ```\n\n* Windows:\n\n    ```ps1\n    netsh winhttp show proxy\n\
  \    ```\n\n* Linux, in the environment variables `http_proxy` and `https_proxy`\n\n    ```ps1\n    env\n    cat /etc/profile.d/proxy.conf\n\
  \    ```\n\n### PAC Proxy\n\nPAC (Proxy Auto-Configuration) is a method to automatically determine whether web traffic should\
  \ go through a proxy server. It uses a .pac file that contains a JavaScript function called `FindProxyForURL(url, host)`.\n\
  \n* proxy.pac\n* wpad.dat\n\n**Example**:\n\n```ps1\nfunction FindProxyForURL(url, host) {\n    if (dnsDomainIs(host, '.example.com'))\
  \ {\n        return 'DIRECT';\n    }\n    return 'PROXY proxy.example.com:8080';\n}\n```\n\n**Tools**:\n\n* [PortSwigger\
  \ - Proxy Auto Config](https://portswigger.net/bappstore/7b3eae07aa724196ab85a8b64cd095d1) - This extension automatically\
  \ configures Burp upstream proxies to match desktop proxy settings. This includes support for Proxy Auto-Config (PAC) scripts.\n\
  \n### Common Bypass\n\n* Try several way to reach the Internet\n    * IP address\n    * Domain categorized in Health/Finance\n\
  \n* Use another proxy reachable in the same environment\n\n* Weak regular expression for URL can be abused to bypass the\
  \ proxy configuration\n\n    ```ps1\n    user:pass@domain/endpoint?parameter#hash\n    e.g: microsoft.com:microsoft.com@microsoft.com.evil.com/microsoft.com?microsoft.com#microsoft.com\n\
  \    ```\n\n* Trusted Websites: [Living Off Trusted Sites (LOTS) Project](https://lots-project.com/)\n    * Amazon Cloud:\
  \ AWS endpoints\n    * Microsoft Cloud: Azure endpoints\n    * Google Cloud: GCP endpoints\n    * live.sysinternals.com\n\
  \n* User-Agents\n    * Tools related User-Agent: curl, python, powershell\n\n        ```ps1\n        User-Agent: curl/8.11.0\n\
  \        User-Agent: python-requests/2.32.3\n        User-Agent: Mozilla/5.0 (Windows NT; Windows NT 10.0; fr-FR) WindowsPowerShell/5.1.26100.2161\n\
  \        ```\n\n    * Platform related User-Agent: Android/iOS/Tablet\n\n        ```ps1\n        Mozilla/5.0 (Linux; Android\
  \ 14; Pixel 9 Build/AD1A.240905.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.78 Mobile\
  \ Safari/537.36 [FB_IAB/FB4A;FBAV/484.0.0.63.83;IABMV/1;] \n        Mozilla/5.0 (iPhone; CPU iPhone OS 18_0_1 like Mac OS\
  \ X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBAV/485.1.0.45.110;FBBV/665337277;FBDV/iPhone17,1;FBMD/iPhone;FBSN/iOS;FBSV/18.0.1;FBSS/3;FBCR/;FBID/phone;FBLC/it_IT;FBOP/80]\
  \ \n        ```\n\n* Domain Fronting\n* Protocols\n    * TCP\n    * Websocket (HTTP)\n    * DNS Exfiltration\n\n## References\n\
  \n* [Proxy managed by enterprise? No problem! Abusing PAC and the registry to get burpin’ - Thomas Grimée - August 17, 2021](https://blog.nviso.eu/2021/08/17/proxy-managed-by-enterprise-no-problem-abusing-pac-and-the-registry-to-get-burpin/)\n\
  * [Proxy: Internal Proxy - MITRE ATT&CK - March 14, 2020](https://attack.mitre.org/versions/v16/techniques/T1090/001/)"
_relative_path: redteam/evasion/proxy-bypass.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/proxy-bypass.md
````
