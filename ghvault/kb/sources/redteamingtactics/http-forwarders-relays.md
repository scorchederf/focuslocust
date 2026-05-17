---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# HTTP Forwarders / Relays

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-red-team-infrastructure-redirectors-forwarders` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/red-team-infrastructure/redirectors-forwarders.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [HTTP Forwarders / Relays](../../topics/offensive-security/http-forwarders-relays.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-red-team-infrastructure-redirectors-forwarders |
| name | HTTP Forwarders / Relays |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/red-team-infrastructure/redirectors-forwarders.md |

## Preserved Source Material

````yaml
_asset_filenames:
- redirector-conversations.png
- redirector-socat.gif
- redirector.gif
- redirectors-iptables.png
_body: "---\ndescription: >-\n  Concealing attacking hosts through with redirectors/traffic forwarders using\n  iptables or\
  \ socat\n---\n\n# HTTP Forwarders / Relays\n\n## Purpose\n\nRe-directors or traffic forwarders are essentially proxies between\
  \ the red teaming server \\(say the one for sending phishing emails or a C2\\) and the victim - `victim <> re-director <>\
  \ team server`\n\nThe purpose of the re-director host is as usual:\n\n* Obscure the red teaming server by concealing its\
  \ IP address. In other words - the victim will see traffic coming from the re-director host rather than the team server.\n\
  * If incident responders detect suspicious activity originating from the redirector, it can be \"easily\" decommissioned\
  \ and replaced with another one, which is \"easier\" than rebuilding the team server.\n\n## HTTP Forwarding with iptables\n\
  \nI will explore simple HTTP forwarders which are just that - they simply listen on a given interface and port and forward\
  \ all the traffic they receive on that port, to a listener port on the team server.\n\nMy environment in this lab:\n\n*\
  \ Team server and a listening port: `10.0.0.2:80`\n* Re-director host and a listening port: `10.0.0.5:80`\n* Victim host:\
  \ `10.0.0.11`\n\nAn easy way to create an HTTP re-director is to use a Linux box and its iptables capability. \n\nBelow\
  \ shows how to turn a Linux box into an HTTP re-director. In this case, all the HTTP traffic to `10.0.0.5:80` \\(redirector\\\
  ) will be forwarded to `10.0.0.2:80` \\(team server\\) :\n\n```csharp\niptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT\n\
  iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.0.0.2:80\niptables -t nat -A POSTROUTING -j\
  \ MASQUERADE\niptables -I FORWARD -j ACCEPT\niptables -P FORWARD ACCEPT\nsysctl net.ipv4.ip_forward=1\n```\n\nChecking that\
  \ the iptables rules were created successfully:\n\n![](../../.gitbook/assets/redirectors-iptables.png)\n\n### Testing iptables\n\
  \nLet's simulate a simplified reverse shell from the victim system 10.0.0.11 to the attacking system 10.0.0.2 using our\
  \ redirector system 10.0.0.5 as a proxy and inspect the traffic crossing over the wire - if the redirector was setup correctly,\
  \ we should see that systems 10.0.0.11 and 10.0.0.2 will not be communicating directly - all the traffic will be flowing\
  \ through the box at 10.0.0.5 and 10.0.0.2 \\(attacking system\\) will not be visible to the victim 10.0.0.11:\n\n![](../../.gitbook/assets/redirector.gif)\n\
  \nHaving a closer look at the traffic/conversations between the endpoints, we can clearly see that at no point the victim\
  \ system 10.0.0.11 communicated directly with the attacking system 10.0.0.2 - all communications were flowing through the\
  \ redirector host 10.0.0.5 as described earlier:\n\n![](../../.gitbook/assets/redirector-conversations.png)\n\n{% file src=\"\
  ../../.gitbook/assets/redirector.pcapng\" caption=\"Redirector Network Trace\" %}\n\n## HTTP Forwarding with SOCAT\n\nSOCAT\
  \ is another tool that can be used to do the \"dumb pipe\" traffic forwarding. The environment in this  exercise remains\
  \ the same as in the previous scenario.\n\nSetting up an HTTP redirector with socat:\n\n```csharp\nsocat TCP4-LISTEN:80,fork\
  \ TCP4:10.0.0.2:80\n```\n\n![](../../.gitbook/assets/redirector-socat.gif)\n\n## References\n\n{% embed url=\"https://github.com/bluscreenofjeff/Red-Team-Infrastructure-Wiki\\\
  #https\" %}\n\n{% embed url=\"https://www.frozentux.net/iptables-tutorial/chunkyhtml/x4033.html\" %}\n\n{% embed url=\"\
  http://linux-training.be/networking/ch14.html\" %}\n\n{% embed url=\"http://technostuff.blogspot.com/2008/10/some-useful-socat-commands.html\"\
  \ %}\n\n{% embed url=\"https://www.thegeekstuff.com/2011/01/iptables-fundamentals/\" %}"
_relative_path: offensive-security/red-team-infrastructure/redirectors-forwarders.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/red-team-infrastructure/redirectors-forwarders.md
````
