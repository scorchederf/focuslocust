---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0101
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0101-domain-registration
---

## Description

"Domain Name: Domain Registration" data component captures information about the assignment, ownership, and metadata of domain names. This information is often sourced from registries like WHOIS and includes details such as registrant names, contact information, registration dates, expiration dates, and registrar details. This data is invaluable for tracking domain ownership, detecting malicious domain registrations, and identifying trends in adversary behavior. Examples: <br><br>- Registrant Information: WHOIS lookup of example.com <br>- Registration and Expiration Dates: A domain registered a week before being used in phishing attacks.<br>- Domain Status: Status codes like clientTransferProhibited or serverHold indicate domain restrictions or potential hijacking activity.<br>- Name Server Information: Name servers point to a public DNS provider often associated with malicious campaigns.<br>- Privacy Protection: A domain uses WHOIS privacy protection to hide registrant details.<br><br>This data component can be collected through the following measures:<br><br>- WHOIS Services: Use tools or services to perform WHOIS lookups:<br>- WHOIS APIs: Automate domain registration lookups with APIs:<br>- Registrar Platforms: Directly query domain registrars (e.g., GoDaddy, Namecheap) for detailed registration data.<br>- Threat Intelligence Platforms: Integrate domain registration data from services like Recorded Future, RiskIQ, or PassiveTotal for enriched analysis.
