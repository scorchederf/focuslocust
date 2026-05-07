---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1668
tags:
    - attack/domain/enterprise_attack
    - attack/tactic/persistence
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1668-exclusive-control
tactic:
    - Persistence
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries who successfully compromise a system may attempt to maintain persistence by “closing the door” behind them  – in other words, by preventing other threat actors from initially accessing or maintaining a foothold on the same system. <br><br>For example, adversaries may patch a vulnerable, compromised system[^5] [^2]  to prevent other threat actors from leveraging that vulnerability in the future. They may “close the door” in other ways, such as disabling vulnerable services[^4] , stripping privileges from accounts[^1] , or removing other malware already on the compromised device.[^3] <br><br>Hindering other threat actors may allow an adversary to maintain sole access to a compromised system or network. This prevents the threat actor from needing to compete with or even being removed themselves by other threat actors. It also reduces the “noise” in the environment, lowering the possibility of being caught and evicted by defenders. Finally, in the case of [[kb/mitre/attack/techniques/T1496-resource-hijacking|Resource Hijacking]], leveraging a compromised device’s full power allows the threat actor to maximize profit.[^4] 

 [^1]: [aquasec-postgres-processes](https://www.aquasec.com/blog/pg_mem-a-malware-hidden-in-the-postgres-processes/)
 [^2]: [CERT AT Fortinent Ransomware 2025](https://www.cert.at/de/warnungen/2025/3/ransomware-gruppen-nutzen-weiterhin-kritische-fortinet-schwachstellen-warnung-vor-gepatchten-aber-bereits-kompromittierten-geraten)
 [^3]: [fsecure-netsky](https://www.f-secure.com/v-descs/netsky-h.shtml)
 [^4]: [sophos-multiple-attackers](https://news.sophos.com/en-us/2022/08/09/multiple-attackers-increase-pressure-on-victims-complicate-incident-response/#:~:text=While%20some%20threat%20actors%20are%20interdependent%20%28e.g.%2C%20IABs,vulnerabilities%20or%20disabling%20vulnerable%20services%20after%20gaining%20access)
 [^5]: [Mandiant-iab-control](https://cloud.google.com/blog/topics/threat-intelligence/initial-access-brokers-exploit-f5-screenconnect)
