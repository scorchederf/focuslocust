---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0052
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0052-social-media
---

## Description

Established, compromised, or otherwise acquired by adversaries to conduct reconnaissance, influence operations, social engineering, or other cyber threats.<br><br>*Data Collection Measures:*<br><br>- API Monitoring	<br>    - Social media APIs (e.g., Twitter API, Facebook Graph API) can extract behavioral patterns of accounts.<br>- Web Scraping<br>    - Extracts public profile data, friend lists, or interactions to identify impersonation attempts.<br>- Threat Intelligence Feeds	<br>    - External feeds track malicious personas linked to disinformation campaigns or phishing.<br>- OSINT Tools<br>    - Maltego, SpiderFoot, and OpenCTI can map social media persona relationships.<br>- Endpoint Detection	<br>    - EDR logs user behavior and alerts on suspicious social media interactions.<br>- SIEM Logging<br>    - Detects access to known phishing pages or social media abuse via proxy logs.<br>- Dark Web Monitoring	<br>    - Identifies compromised social media credentials being sold.
