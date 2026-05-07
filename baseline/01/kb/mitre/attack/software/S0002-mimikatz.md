---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0002
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0002-mimikatz
---

## Description

[[kb/mitre/attack/software/S0002-mimikatz|Mimikatz]] is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. [^1]  [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-lsass-memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the LSASS Memory.[^1] [^2] [^3] [^4]  |
| [[kb/mitre/attack/techniques/T1003.002-security-account-manager\|T1003.002]] | Security Account Manager | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the SAM table.[^1] [^2] [^3] [^4]  |
| [[kb/mitre/attack/techniques/T1003.004-lsa-secrets\|T1003.004]] | LSA Secrets | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the LSA.[^1] [^2] [^3] [^4]  |
| [[kb/mitre/attack/techniques/T1003.006-dcsync\|T1003.006]] | DCSync | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from DCSync/NetSync.[^1] [^2] [^3] [^4] [^5]  |
| [[kb/mitre/attack/techniques/T1098-account-manipulation\|T1098]] | Account Manipulation | The [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] credential dumper has been extended to include Skeleton Key domain controller authentication bypass functionality. The `LSADUMP::ChangeNTLM` and `LSADUMP::SetNTLM` modules can also manipulate the password hash of an account without knowing the clear text value.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1134.005-sid-history-injection\|T1134.005]] | SID-History Injection | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]]'s `MISC::AddSid` module can append any SID or user/group account to a user's SID-History. [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] also utilizes [[kb/mitre/attack/techniques/T1134.005-sid-history-injection\|SID-History Injection]] to expand the scope of other components such as generated Kerberos Golden Tickets and DCSync beyond a single domain.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1207-rogue-domain-controller\|T1207]] | Rogue Domain Controller | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]]’s `LSADUMP::DCShadow` module can be used to make AD updates by temporarily setting a computer to be a DC.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1547.005-security-support-provider\|T1547.005]] | Security Support Provider | The [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] credential dumper contains an implementation of an SSP.[^1]  |
| [[kb/mitre/attack/techniques/T1550.002-pass-the-hash\|T1550.002]] | Pass the Hash | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]]'s `SEKURLSA::Pth` module can impersonate a user, with only a password hash, to execute arbitrary commands.[^1] [^2] [^3]  |
| [[kb/mitre/attack/techniques/T1550.003-pass-the-ticket\|T1550.003]] | Pass the Ticket | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]]’s `LSADUMP::DCSync` and `KERBEROS::PTT` modules implement the three steps required to extract the krbtgt account hash and create/use Kerberos tickets.[^1] [^2] [^3] [^4]  |
| [[kb/mitre/attack/techniques/T1552.004-private-keys\|T1552.004]] | Private Keys | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]]'s `CRYPTO::Extract` module can extract keys by interacting with Windows cryptographic application programming interface (API) functions.[^1]  |
| [[kb/mitre/attack/techniques/T1555-credentials-from-password-stores\|T1555]] | Credentials from Password Stores | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the credential vault and DPAPI.[^1] [^2] [^3] [^4] [^5] 	 |
| [[kb/mitre/attack/techniques/T1555.003-credentials-from-web-browsers\|T1555.003]] | Credentials from Web Browsers | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from DPAPI.[^1] [^2] [^3] [^4] 	 |
| [[kb/mitre/attack/techniques/T1555.004-windows-credential-manager\|T1555.004]] | Windows Credential Manager | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] contains functionality to acquire credentials from the Windows Credential Manager.[^1]  |
| [[kb/mitre/attack/techniques/T1558.001-golden-ticket\|T1558.001]] | Golden Ticket | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]]'s kerberos module can create golden tickets.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1558.002-silver-ticket\|T1558.002]] | Silver Ticket | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]]'s kerberos module can create silver tickets.[^1]  |
| [[kb/mitre/attack/techniques/T1649-steal-or-forge-authentication-certificates\|T1649]] | Steal or Forge Authentication Certificates | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]]'s `CRYPTO` module can create and export various types of authentication certificates.[^1]  |

 [^1]: [Deply Mimikatz](https://github.com/gentilkiwi/mimikatz)
 [^2]: [Adsecurity Mimikatz Guide](https://adsecurity.org/?page_id=1821)
 [^3]: [GitHub Mimikatz lsadump Module](https://github.com/gentilkiwi/mimikatz/wiki/module-~-lsadump)
 [^4]: [Directory Services Internals DPAPI Backup Keys Oct 2015](https://www.dsinternals.com/en/retrieving-dpapi-backup-keys-from-active-directory/)
 [^5]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
 [^6]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^7]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)
 [^8]: [Metcalf 2015](http://adsecurity.org/?p=1275)
 [^9]: [Harmj0y DCSync Sept 2015](http://www.harmj0y.net/blog/redteaming/mimikatz-and-dcsync-and-extrasids-oh-my/)
 [^10]: [GitHub Mimikatz kerberos Module](https://github.com/gentilkiwi/mimikatz/wiki/module-~-kerberos)
 [^11]: [Delpy Mimikatz Crendential Manager](https://github.com/gentilkiwi/mimikatz/wiki/howto-~-credential-manager-saved-credentials)
