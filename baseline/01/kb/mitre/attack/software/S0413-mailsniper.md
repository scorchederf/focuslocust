---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0413
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0413-mailsniper
---

## Description

MailSniper is a penetration testing tool for searching through email in a Microsoft Exchange environment for specific terms (passwords, insider intel, network architecture information, etc.). It can be used by a non-administrative user to search their own email, or by an Exchange administrator to search the mailboxes of every user in a domain.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1087.003-email-account\|T1087.003]] | Email Account | [[kb/mitre/attack/software/S0413-mailsniper\|MailSniper]] can be used to obtain account names from Exchange and Office 365 using the `Get-GlobalAddressList` cmdlet.[^1]  |
| [[kb/mitre/attack/techniques/T1110.003-password-spraying\|T1110.003]] | Password Spraying | [[kb/mitre/attack/software/S0413-mailsniper\|MailSniper]] can be used for password spraying against Exchange and Office 365.[^1]  |
| [[kb/mitre/attack/techniques/T1114.002-remote-email-collection\|T1114.002]] | Remote Email Collection | [[kb/mitre/attack/software/S0413-mailsniper\|MailSniper]] can be used for searching through email in Exchange and Office 365 environments.[^1]  |

 [^1]: [GitHub MailSniper](https://github.com/dafthack/MailSniper)
 [^2]: [Black Hills Attacking Exchange MailSniper, 2016](https://www.blackhillsinfosec.com/attacking-exchange-with-mailsniper/)
