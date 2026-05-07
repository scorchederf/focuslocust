---
parsed_by: focuslocust
source: mitre
type: mitigation
aliases:
    - M1057
tags:
    - attack/domain/enterprise_attack
    - attack/type/mitigation
mitre-attack: kb/mitre/attack/mitigations/M1057-data-loss-prevention
---

## Description

Data Loss Prevention (DLP) involves implementing strategies and technologies to identify, categorize, monitor, and control the movement of sensitive data within an organization. This includes protecting data formats indicative of Personally Identifiable Information (PII), intellectual property, or financial data from unauthorized access, transmission, or exfiltration. DLP solutions integrate with network, endpoint, and cloud platforms to enforce security policies and prevent accidental or malicious data leaks. [^1]  This mitigation can be implemented through the following measures:<br><br>Sensitive Data Categorization:<br><br>- Use Case: Identify and classify data based on sensitivity (e.g., PII, financial data, trade secrets).<br>- Implementation: Use DLP solutions to scan and tag files containing sensitive information using predefined patterns, such as Social Security Numbers or credit card details.<br><br>Exfiltration Restrictions:<br><br>- Use Case: Prevent unauthorized transmission of sensitive data.<br>- Implementation: Enforce policies to block unapproved email attachments, unauthorized USB usage, or unencrypted data uploads to cloud storage.<br><br>Data-in-Transit Monitoring:<br><br>- Use Case: Detect and prevent the transmission of sensitive data over unapproved channels.<br>- Implementation: Deploy network-based DLP tools to inspect outbound traffic for sensitive content (e.g., financial records or PII) and block unapproved transmissions.<br><br>Endpoint Data Protection:<br><br>- Use Case: Monitor and control sensitive data usage on endpoints.<br>- Implementation: Use endpoint-based DLP agents to block copy-paste actions of sensitive data and unauthorized printing or file sharing.<br><br>Cloud Data Security:<br><br>- Use Case: Protect data stored in cloud platforms.<br>- Implementation: Integrate DLP with cloud storage platforms like Google Drive, OneDrive, or AWS to monitor and restrict sensitive data sharing or downloads.

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1005-data-from-local-system\|T1005]] | Data from Local System | Data loss prevention can restrict access to sensitive data and detect sensitive data that is unencrypted. |
| [[kb/mitre/attack/techniques/T1020.001-traffic-duplication\|T1020.001]] | Traffic Duplication | Implement Data Loss Prevention (DLP) solutions to monitor, detect, and control the flow of sensitive information. DLP tools can be configured to block unauthorized attempts to exfiltrate data, such as preventing emails from being forwarded to external recipients or monitoring for suspicious data transfers. By creating email flow rules and applying policies to detect anomalies, DLP solutions help mitigate the risk of data exfiltration over alternative protocols. |
| [[kb/mitre/attack/techniques/T1025-data-from-removable-media\|T1025]] | Data from Removable Media | Data loss prevention can restrict access to sensitive data and detect sensitive data that is unencrypted. |
| [[kb/mitre/attack/techniques/T1041-exfiltration-over-c2-channel\|T1041]] | Exfiltration Over C2 Channel | Data loss prevention can detect and block sensitive data being sent over unencrypted protocols. |
| [[kb/mitre/attack/techniques/T1048-exfiltration-over-alternative-protocol\|T1048]] | Exfiltration Over Alternative Protocol | Data loss prevention can detect and block sensitive data being uploaded via web browsers. |
| [[kb/mitre/attack/techniques/T1048.002-exfiltration-over-asymmetric-encrypted-non-c2-protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | Data loss prevention can detect and block sensitive data being uploaded via web browsers. |
| [[kb/mitre/attack/techniques/T1048.003-exfiltration-over-unencrypted-non-c2-protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | Data loss prevention can detect and block sensitive data being sent over unencrypted protocols. |
| [[kb/mitre/attack/techniques/T1052-exfiltration-over-physical-medium\|T1052]] | Exfiltration Over Physical Medium | Data loss prevention can detect and block sensitive data being copied to physical mediums. |
| [[kb/mitre/attack/techniques/T1052.001-exfiltration-over-usb\|T1052.001]] | Exfiltration over USB | Data loss prevention can detect and block sensitive data being copied to USB devices. |
| [[kb/mitre/attack/techniques/T1537-transfer-data-to-cloud-account\|T1537]] | Transfer Data to Cloud Account | Data loss prevention can prevent and block sensitive data from being shared with individuals outside an organization.[^2]  [^1]  |
| [[kb/mitre/attack/techniques/T1567-exfiltration-over-web-service\|T1567]] | Exfiltration Over Web Service | Data loss prevention can be detect and block sensitive data being uploaded to web services via web browsers. |
| [[kb/mitre/attack/techniques/T1567.004-exfiltration-over-webhook\|T1567.004]] | Exfiltration Over Webhook | Data loss prevention can be detect and block sensitive data being uploaded to web services via web browsers. |

 [^1]: [PurpleSec Data Loss Prevention](https://purplesec.us/data-loss-prevention/)
 [^2]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)
 [^3]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)
