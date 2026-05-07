---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0093
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0093-certificate-registration
---

## Description

Certificate Registration refers to the collection and analysis of information about digital certificates, including current, revoked, and expired certificates. Sources such as Certificate Transparency logs and other public resources provide visibility into certificates issued for specific domains or organizations. Monitoring certificate registrations can help identify potential misuse, such as unauthorized certificates or signs of adversary reconnaissance. Examples: <br><br>- Certificate Transparency Logs: These logs record the issuance of SSL/TLS certificates by trusted Certificate Authorities (CAs).<br>- Revoked Certificates: Information about certificates that have been invalidated before their expiration date.<br>- Expired Certificates: Reports of expired certificates for a domain, which may indicate lax security practices or opportunities for adversaries to exploit expired credentials.<br>- Domain Monitoring for Certificates: Maps SSL/TLS certificates to domains and subdomains, helping to identify any rogue certificates.<br>- Public Certificate Directories: Services providing APIs to query issued certificates for analysis.<br><br>This data component can be collected through the following measures:<br><br>Use Certificate Transparency Monitors<br><br>- Tools like crt.sh, CertStream, or APIs provided by certificate authorities (CAs) allow you to monitor issued certificates in real-time.<br>- Example: Use CertStream to stream certificate issuance logs and filter for domains of interest.<br><br>Analyze Certificate Revocation Sources<br><br>- Monitor CRLs or query OCSP responders to detect revoked certificates.<br>- Configure tools like OpenSSL or browsers to validate certificate revocation status automatically.<br><br>Leverage Public Scanning Tools<br><br>- Use tools such as SSL Labs, Censys, or Shodan to scan for certificate details related to your domain or network.<br><br>Automate Certificate Monitoring<br><br>- Set up automated scripts or services to parse Certificate Transparency logs for anomalies.<br>- Example: Automate searches on crt.sh to identify certificates issued for typo-squatted domains.<br><br>Integrate with Threat Intelligence<br><br>- Enrich certificate data with threat intelligence feeds to detect connections to known adversary-controlled infrastructure.<br>- Tools like VirusTotal can identify malicious certificates based on associated indicators.
