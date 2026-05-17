---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Memory dump analysis

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-basic-forensic-methodology-memory-dump-analysis-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Memory dump analysis](../../topics/generic-methodologies-and-resources/memory-dump-analysis.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-methodologies-and-resources-basic-forensic-methodology-memory-dump-analysis-readme |
| name | Memory dump analysis |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/README.md |

## Preserved Source Material

```yaml
_body: '# Memory dump analysis


  {{#include ../../../banners/hacktricks-training.md}}


  ## Start


  Start **searching** for **malware** inside the pcap. Use the **tools** mentioned in [**Malware Analysis**](../malware-analysis.md).


  ## [Volatility](volatility-cheatsheet.md)


  **Volatility is the main open-source framework for memory dump analysis**. This Python tool analyzes dumps from external
  sources or VMware VMs, identifying data like processes and passwords based on the dump''s OS profile. It''s extensible with
  plugins, making it highly versatile for forensic investigations.


  [**Find here a cheatsheet**](volatility-cheatsheet.md)


  ## Mini dump crash report


  When the dump is small (just some KB, maybe a few MB) then it''s probably a mini dump crash report and not a memory dump.


  ![](<../../../images/image (532).png>)


  If you have Visual Studio installed, you can open this file and bind some basic information like process name, architecture,
  exception info and modules being executed:


  ![](<../../../images/image (263).png>)


  You can also load the exception and see the decompiled instructions


  ![](<../../../images/image (142).png>)


  ![](<../../../images/image (610).png>)


  Anyway, Visual Studio isn''t the best tool to perform an analysis of the depth of the dump.


  You should **open** it using **IDA** or **Radare** to inspection it in **depth**.


  ​


  {{#include ../../../banners/hacktricks-training.md}}'
_relative_path: generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/README.md
```
