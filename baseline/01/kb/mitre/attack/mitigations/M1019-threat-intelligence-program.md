---
parsed_by: focuslocust
source: mitre
type: mitigation
aliases:
    - M1019
tags:
    - attack/domain/enterprise_attack
    - attack/type/mitigation
mitre-attack: kb/mitre/attack/mitigations/M1019-threat-intelligence-program
---

## Description

A Threat Intelligence Program enables organizations to proactively identify, analyze, and act on cyber threats by leveraging internal and external data sources. The program supports decision-making processes, prioritizes defenses, and improves incident response by delivering actionable intelligence tailored to the organization's risk profile and operational environment. This mitigation can be implemented through the following measures:<br><br>Establish a Threat Intelligence Team:<br><br>- Form a dedicated team or assign responsibility to existing security personnel to collect, analyze, and act on threat intelligence.<br><br>Define Intelligence Requirements:<br><br>- Identify the organization’s critical assets and focus intelligence gathering efforts on threats targeting these assets.<br><br>Leverage Internal and External Data Sources:<br><br>- Collect intelligence from internal sources such as logs, incidents, and alerts.<br>Subscribe to external threat intelligence feeds, participate in ISACs, and monitor open-source intelligence (OSINT).<br><br>Implement Tools for Automation:<br><br>- Use threat intelligence platforms (TIPs) to automate the collection, enrichment, and dissemination of threat data.<br>- Integrate threat intelligence with SIEMs to correlate IOCs with internal events.<br><br>Analyze and Act on Intelligence:<br><br>- Use frameworks like MITRE ATT&CK to map intelligence to adversary TTPs.<br>- Prioritize defensive measures, such as patching vulnerabilities or deploying IOCs, based on analyzed threats.<br><br>Share and Collaborate:<br><br>- Share intelligence with industry peers through ISACs or threat-sharing platforms to enhance collective defense.<br><br>Evaluate and Update the Program:<br><br>- Regularly assess the effectiveness of the threat intelligence program.<br>- Update intelligence priorities and capabilities as new threats emerge.<br><br>*Tools for Implementation*<br><br>Threat Intelligence Platforms (TIPs):<br><br>- OpenCTI: An open-source platform for structuring and sharing threat intelligence.<br>- MISP: A threat intelligence sharing platform for sharing structured threat data.<br><br>Threat Intelligence Feeds:<br><br>- Open Threat Exchange (OTX): Provides free access to a large repository of threat intelligence.<br>- CIRCL OSINT Feed: A free source for IOCs and threat information.<br><br>Automation and Enrichment Tools:<br><br>- TheHive: An open-source incident response platform with threat intelligence integration.<br>- Yeti: A platform for managing and structuring knowledge about threats.<br><br>Analysis Frameworks:<br><br>- MITRE ATT&CK Navigator: A tool for mapping threat intelligence to adversary behaviors.<br>- Cuckoo Sandbox: Analyzes malware to extract behavioral indicators.<br><br>Community and Collaboration Tools:<br><br>- ISAC Memberships: Join industry-specific ISACs for intelligence sharing.<br>- Slack/Discord Channels: Participate in threat intelligence communities for real-time collaboration.

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1068-exploitation-for-privilege-escalation\|T1068]] | Exploitation for Privilege Escalation | Develop a robust cyber threat intelligence capability to determine what types and levels of threat may use software exploits and 0-days against a particular organization. |
| [[kb/mitre/attack/techniques/T1210-exploitation-of-remote-services\|T1210]] | Exploitation of Remote Services | Develop a robust cyber threat intelligence capability to determine what types and levels of threat may use software exploits and 0-days against a particular organization. |
| [[kb/mitre/attack/techniques/T1211-exploitation-for-stealth\|T1211]] | Exploitation for Stealth | Develop a robust cyber threat intelligence capability to determine what types and levels of threat may use software exploits and 0-days against a particular organization. |
| [[kb/mitre/attack/techniques/T1212-exploitation-for-credential-access\|T1212]] | Exploitation for Credential Access | Develop a robust cyber threat intelligence capability to determine what types and levels of threat may use software exploits and 0-days against a particular organization. |
| [[kb/mitre/attack/techniques/T1684.001-impersonation\|T1684.001]] | Impersonation | Threat intelligence helps defenders and users be aware of and defend against common lures and active campaigns that have been used for impersonation. |
