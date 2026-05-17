---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1119 - Automated Collection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1119` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Once established within a system or network, an adversary may use automated techniques for collecting internal data. Methods for performing this technique could include use of a Command and Scripting Interpreter to search for and copy information fitting set criteria such as file type, location, or name at specific time intervals. 

In cloud-based environments, adversaries may also use cloud APIs, data pipelines, command line interfaces, or extract, transform, and load (ETL) services to automatically collect data. 

This functionality could also be built into remote access tools. 

This technique may incorporate use of other techniques such as File and Directory Discovery and Lateral Tool Transfer to identify and move files, as well as Cloud Service Dashboard and Cloud Storage Object Discovery to identify resources in cloud environments.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can automatically gather the username, domain name, machine name, and other information from a compromised system.(Citation: Talos Frankenstein June 2019) |
| [Mythic](../../tools/unknown/mythic.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) supports scripting of file downloads from agents.(Citation: Mythc Documentation)	 |
| [NPPSPY](../../tools/unknown/nppspy.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) collection is automatically recorded to a specified file on the victim machine.(Citation: Huntress NPPSPY 2022) |
| [Pacu](../../tools/unknown/pacu.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can automatically collect data, such as CloudFormation templates, EC2 user data, AWS Inspector reports, and IAM credential reports.(Citation: GitHub Pacu) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains a module for recursively parsing through files and directories to gather valid credit card numbers.(Citation: GitHub PoshC2) |
| [ROADTools](../../tools/unknown/roadtools.md) | explicit | source | [ROADTools](https://attack.mitre.org/software/S0684) automatically gathers data from Azure AD environments using the Azure Graph API.(Citation: Roadtools) |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered information automatically, without instruction from a C2, related to the user and host machine that is compiled into a report and sent to the operators.(Citation: FOX-IT May 2016 Mofang) |

## Source Verification

[source record](../../sources/mitre/automated-collection.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:27.985Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Once established within a system or network, an adversary may use automated techniques for collecting internal\
\ data. Methods for performing this technique could include use of a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059)\
\ to search for and copy information fitting set criteria such as file type, location, or name at specific time intervals.\
\ \n\nIn cloud-based environments, adversaries may also use cloud APIs, data pipelines, command line interfaces, or extract,\
\ transform, and load (ETL) services to automatically collect data.(Citation: Mandiant UNC3944 SMS Phishing 2023) \n\nThis\
\ functionality could also be built into remote access tools. \n\nThis technique may incorporate use of other techniques\
```
