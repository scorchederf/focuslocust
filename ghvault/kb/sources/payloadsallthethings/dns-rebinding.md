---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# DNS Rebinding

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-dns-rebinding-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/DNS Rebinding/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DNS Rebinding](../../topics/dns-rebinding/dns-rebinding.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-dns-rebinding-readme |
| name | DNS Rebinding |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/DNS%20Rebinding/README.md |

## Preserved Source Material

````yaml
_body: "# DNS Rebinding\n\n> DNS rebinding changes the IP address of an attacker controlled machine name to the IP address\
  \ of a target application, bypassing the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)\
  \ and thus allowing the browser to make arbitrary requests to the target application and read their responses.\n\n## Summary\n\
  \n* [Tools](#tools)\n* [Methodology](#methodology)\n* [Protection Bypasses](#protection-bypasses)\n    * [0.0.0.0](#0000)\n\
  \    * [CNAME](#cname)\n    * [localhost](#localhost)\n* [References](#references)\n\n## Tools\n\n* [nccgroup/singularity](https://github.com/nccgroup/singularity)\
  \ - A DNS rebinding attack framework.\n* [rebind.it](http://rebind.it/) - Singularity of Origin Web Client.\n* [taviso/rbndr](https://github.com/taviso/rbndr)\
  \ - Simple DNS Rebinding Service\n* [taviso/rebinder](https://lock.cmpxchg8b.com/rebinder.html) - rbndr Tool Helper\n\n\
  ## Methodology\n\n**Setup Phase**:\n\n* Register a malicious domain (e.g., `malicious.com`).\n* Configure a custom DNS server\
  \ capable of resolving `malicious.com` to different IP addresses.\n\n**Initial Victim Interaction**:\n\n* Create a webpage\
  \ on `malicious.com` containing malicious JavaScript or another exploit mechanism.\n* Entice the victim to visit the malicious\
  \ webpage (e.g., via phishing, social engineering, or advertisements).\n\n**Initial DNS Resolution**:\n\n* When the victim's\
  \ browser accesses `malicious.com`, it queries the attacker's DNS server for the IP address.\n* The DNS server resolves\
  \ `malicious.com` to an initial, legitimate-looking IP address (e.g., 203.0.113.1).\n\n**Rebinding to Internal IP**:\n\n\
  * After the browser's initial request, the attacker's DNS server updates the resolution for `malicious.com` to a private\
  \ or internal IP address (e.g., 192.168.1.1, corresponding to the victim’s router or other internal devices).\n\nThis is\
  \ often achieved by setting a very short TTL (time-to-live) for the initial DNS response, forcing the browser to re-resolve\
  \ the domain.\n\n**Same-Origin Exploitation:**\n\nThe browser treats subsequent responses as coming from the same origin\
  \ (`malicious.com`).\n\nMalicious JavaScript running in the victim's browser can now make requests to internal IP addresses\
  \ or local services (e.g., 192.168.1.1 or 127.0.0.1), bypassing same-origin policy restrictions.\n\n**Example:**\n\n1. Register\
  \ a domain.\n2. [Setup Singularity of Origin](https://github.com/nccgroup/singularity/wiki/Setup-and-Installation).\n3.\
  \ Edit the [autoattack HTML page](https://github.com/nccgroup/singularity/blob/master/html/autoattack.html) for your needs.\n\
  4. Browse to `http://rebinder.your.domain:8080/autoattack.html`.\n5. Wait for the attack to finish (it can take few seconds/minutes).\n\
  \n## Protection Bypasses\n\n> Most DNS protections are implemented in the form of blocking DNS responses containing unwanted\
  \ IP addresses at the perimeter, when DNS responses enter the internal network. The most common form of protection is to\
  \ block private IP addresses as defined in RFC 1918 (i.e. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). Some tools allow to\
  \ additionally block localhost (127.0.0.0/8), local (internal) networks, or 0.0.0.0/0 network ranges.\n\nIn the case where\
  \ DNS protection are enabled (generally disabled by default), NCC Group has documented multiple [DNS protection bypasses](https://github.com/nccgroup/singularity/wiki/Protection-Bypasses)\
  \ that can be used.\n\n### 0.0.0.0\n\nWe can use the IP address 0.0.0.0 to access the localhost (127.0.0.1) to bypass filters\
  \ blocking DNS responses containing 127.0.0.1 or 127.0.0.0/8.\n\n### CNAME\n\nWe can use DNS CNAME records to bypass a DNS\
  \ protection solution that blocks all internal IP addresses.\nSince our response will only return a CNAME of an internal\
  \ server,\nthe rule filtering internal IP addresses will not be applied.\nThen, the local, internal DNS server will resolve\
  \ the CNAME.\n\n```bash\n$ dig cname.example.com +noall +answer\n; <<>> DiG 9.11.3-1ubuntu1.15-Ubuntu <<>> example.com +noall\
  \ +answer\n;; global options: +cmd\ncname.example.com.            381     IN      CNAME   target.local.\n```\n\n### localhost\n\
  \nWe can use \"localhost\" as a DNS CNAME record to bypass filters blocking DNS responses containing 127.0.0.1.\n\n```bash\n\
  $ dig www.example.com +noall +answer\n; <<>> DiG 9.11.3-1ubuntu1.15-Ubuntu <<>> example.com +noall +answer\n;; global options:\
  \ +cmd\nlocalhost.example.com.            381     IN      CNAME   localhost.\n```\n\n## References\n\n* [How Do DNS Rebinding\
  \ Attacks Work? - NCC Group - April 9, 2019](https://github.com/nccgroup/singularity/wiki/How-Do-DNS-Rebinding-Attacks-Work%3F)"
_relative_path: DNS Rebinding/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/DNS Rebinding/README.md
````
