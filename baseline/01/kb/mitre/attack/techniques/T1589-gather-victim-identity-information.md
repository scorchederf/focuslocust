---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1589
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1589-gather-victim-identity-information
tactic:
    - Reconnaissance
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may gather information about the victim's identity that can be used during targeting. Information about identities may include a variety of details, including personal data (ex: employee names, email addresses, security question responses, etc.) as well as sensitive details such as credentials or multi-factor authentication (MFA) configurations.<br><br>Adversaries may gather this information in various ways, such as direct elicitation via [[kb/mitre/attack/techniques/T1598-phishing-for-information|Phishing for Information]]. Information about users could also be enumerated via other active means (i.e. [[kb/mitre/attack/techniques/T1595-active-scanning|Active Scanning]]) such as probing and analyzing responses from authentication services that may reveal valid usernames in a system or permitted MFA /methods associated with those usernames.[^4] [^8]  Information about victims may also be exposed to adversaries via online or other accessible data sets (ex: [[kb/mitre/attack/techniques/T1593.001-social-media|Social Media]] or [[kb/mitre/attack/techniques/T1594-search-victim-owned-websites|Search Victim-Owned Websites]]).[^1] [^10] [^5] [^2] [^9] [^3] [^6] [^7] <br><br>Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1593-search-open-websites-domains|Search Open Websites/Domains]] or [[kb/mitre/attack/techniques/T1598-phishing-for-information|Phishing for Information]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1586-compromise-accounts|Compromise Accounts]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1566-phishing|Phishing]] or [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]]).

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1589.002-email-addresses\|T1589.002]] | Email Addresses |
| [[kb/mitre/attack/techniques/T1589.003-employee-names\|T1589.003]] | Employee Names |
| [[kb/mitre/attack/techniques/T1589.001-credentials\|T1589.001]] | Credentials |

 [^1]: [OPM Leak](https://web.archive.org/web/20230602111604/https://www.opm.gov/cybersecurity/cybersecurity-incidents/)
 [^2]: [Detectify Slack Tokens](https://labs.detectify.com/writeups/slack-bot-token-leakage-exposing-business-critical-information/)
 [^3]: [GitHub truffleHog](https://github.com/dxa4481/truffleHog)
 [^4]: [GrimBlog UsernameEnum](https://grimhacker.com/2017/07/24/office365-activesync-username-enumeration/)
 [^5]: [Register Uber](https://www.theregister.com/2015/02/28/uber_subpoenas_github_for_hacker_details/)
 [^6]: [GitHub Gitrob](https://github.com/michenriksen/gitrob)
 [^7]: [CNET Leaks](https://www.cnet.com/news/massive-breach-leaks-773-million-emails-21-million-passwords/)
 [^8]: [Obsidian SSPR Abuse 2023](https://www.obsidiansecurity.com/blog/behind-the-breach-self-service-password-reset-azure-ad/)
 [^9]: [Forbes GitHub Creds](https://www.forbes.com/sites/runasandvik/2014/01/14/attackers-scrape-github-for-cloud-service-credentials-hijack-account-to-mine-virtual-currency/#242c479d3196)
 [^10]: [Register Deloitte](https://www.theregister.com/2017/09/26/deloitte_leak_github_and_google/)
