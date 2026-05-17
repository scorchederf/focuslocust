---
parsed_by: focuslocust
source: mitre
type: generated
---
# vSphere Installation Bundles

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1505.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [vSphere Installation Bundles](../../attack/techniques/T1505.006-vsphere-installation-bundles.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1505.006 |
| name | vSphere Installation Bundles |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1505/006 |

## Preserved Source Material

```yaml
created: '2025-03-27T18:41:08.494Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse vSphere Installation Bundles (VIBs) to establish persistent access to ESXi hypervisors.\
  \ VIBs are collections of files used for software distribution and virtual system management in VMware environments. Since\
  \ ESXi uses an in-memory filesystem where changes made to most files are stored in RAM rather than in persistent storage,\
  \ these modifications are lost after a reboot. However, VIBs can be used to create startup tasks, apply custom firewall\
  \ rules, or deploy binaries that persist across reboots. Typically, administrators use VIBs for updates and system maintenance.\n\
  \nVIBs can be broken down into three components:(Citation: VMware VIBs)\n\n* VIB payload: a `.vgz` archive containing the\
  \ directories and files to be created and executed on boot when the VIBs are loaded.  \n* Signature file: verifies the host\
  \ acceptance level of a VIB, indicating what testing and validation has been done by VMware or its partners before publication\
  \ of a VIB. By default, ESXi hosts require a minimum acceptance level of PartnerSupported for VIB installation, meaning\
  \ the VIB is published by a trusted VMware partner. However, privileged users can change the default acceptance level using\
  \ the `esxcli` command line interface. Additionally, VIBs are able to be installed regardless of acceptance level by using\
  \ the <code> esxcli software vib install --force</code> command. \n* XML descriptor file: a configuration file containing\
  \ associated VIB metadata, such as the name of the VIB and its dependencies.  \n\nAdversaries may leverage malicious VIB\
  \ packages to maintain persistent access to ESXi hypervisors, allowing system changes to be executed upon each bootup of\
  \ ESXi – such as using  `esxcli` to enable firewall rules for backdoor traffic, creating listeners on hard coded ports,\
  \ and executing backdoors.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) Adversaries may also masquerade their\
  \ malicious VIB files as PartnerSupported by modifying the XML descriptor file.(Citation: Google Cloud Threat Intelligence\
  \ ESXi VIBs 2022)"
external_references:
- external_id: T1505.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1505/006
- description: 'Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part
    One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.'
  source_name: Google Cloud Threat Intelligence ESXi VIBs 2022
  url: https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence
- description: Kyle Gleed. (2011, September 13). What's in a VIB?. Retrieved March 27, 2025.
  source_name: VMware VIBs
  url: https://blogs.vmware.com/vsphere/2011/09/whats-in-a-vib.html
id: attack-pattern--f8ba7d61-11c5-4130-bafd-7c3ff5fbf4b5
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-04-15T21:24:04.676Z'
name: vSphere Installation Bundles
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Janantha Marasinghe
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
x_mitre_version: '1.0'
```
