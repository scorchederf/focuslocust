---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# DNSCat pcap analysis

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-basic-forensic-methodology-pcap-inspection-dnscat-exfiltration` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/basic-forensic-methodology/pcap-inspection/dnscat-exfiltration.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

If you have pcap with data being exfiltrated by DNSCat (without using encryption), you can find the exfiltrated content.

## Preserved Body

````markdown
If you have pcap with data being **exfiltrated by DNSCat** (without using encryption), you can find the exfiltrated content.

You only need to know that the **first 9 bytes** are not real data but are related to the **C\&C communication**:

```python
from scapy.all import rdpcap, DNSQR, DNSRR
import struct

f = ""
last = ""
for p in rdpcap('ch21.pcap'):
	if p.haslayer(DNSQR) and not p.haslayer(DNSRR):

		qry = p[DNSQR].qname.replace(".jz-n-bs.local.","").strip().split(".")
		qry = ''.join(_.decode('hex') for _ in qry)[9:]
		if last != qry:
			print(qry)
			f += qry
		last = qry

#print(f)
```

For more information: [https://github.com/jrmdev/ctf-writeups/tree/master/bsidessf-2017/dnscap](https://github.com/jrmdev/ctf-writeups/tree/master/bsidessf-2017/dnscap)\
[https://github.com/iagox86/dnscat2/blob/master/doc/protocol.md](https://github.com/iagox86/dnscat2/blob/master/doc/protocol.md)

There is a script that works with Python3: [https://github.com/josemlwdf/DNScat-Decoder](https://github.com/josemlwdf/DNScat-Decoder)

```
python3 dnscat_decoder.py sample.pcap bad_domain
```
````

## Source Verification

[source record](../../sources/hacktricks/dnscat-pcap-analysis.md)

## Evidence Excerpt

````text
_body: "# DNSCat pcap analysis\n\n{{#include ../../../banners/hacktricks-training.md}}\n\nIf you have pcap with data being\
\ **exfiltrated by DNSCat** (without using encryption), you can find the exfiltrated content.\n\nYou only need to know that\
\ the **first 9 bytes** are not real data but are related to the **C\\&C communication**:\n\n```python\nfrom scapy.all import\
\ rdpcap, DNSQR, DNSRR\nimport struct\n\nf = \"\"\nlast = \"\"\nfor p in rdpcap('ch21.pcap'):\n\tif p.haslayer(DNSQR) and\
\ not p.haslayer(DNSRR):\n\n\t\tqry = p[DNSQR].qname.replace(\".jz-n-bs.local.\",\"\").strip().split(\".\")\n\t\tqry = ''.join(_.decode('hex')\
\ for _ in qry)[9:]\n\t\tif last != qry:\n\t\t\tprint(qry)\n\t\t\tf += qry\n\t\tlast = qry\n\n#print(f)\n```\n\nFor more\
\ information: [https://github.com/jrmdev/ctf-writeups/tree/master/bsidessf-2017/dnscap](https://github.com/jrmdev/ctf-writeups/tree/master/bsidessf-2017/dnscap)\\\
\n[https://github.com/iagox86/dnscat2/blob/master/doc/protocol.md](https://github.com/iagox86/dnscat2/blob/master/doc/protocol.md)\n\
````
