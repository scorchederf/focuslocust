---
parsed_by: focuslocust
source: mitre
type: generated
---
# SSL／TLS Inspection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1020` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SSL／TLS Inspection](../../attack/mitigations/M1020-ssl-tls-inspection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1020 |
| name | SSL／TLS Inspection |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1020 |

## Preserved Source Material

```yaml
created: '2019-06-06T20:15:34.146Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'SSL/TLS inspection involves decrypting encrypted network traffic to examine its content for signs of malicious
  activity. This capability is crucial for detecting threats that use encryption to evade detection, such as phishing, malware,
  or data exfiltration. After inspection, the traffic is re-encrypted and forwarded to its destination. This mitigation can
  be implemented through the following measures:


  Deploy SSL/TLS Inspection Appliances:


  - Implement SSL/TLS inspection solutions to decrypt and inspect encrypted traffic.

  - Ensure appliances are placed at critical network choke points for maximum coverage.


  Configure Decryption Policies:


  - Define rules to decrypt traffic for specific applications, ports, or domains.

  - Avoid decrypting sensitive or privacy-related traffic, such as financial or healthcare websites, to comply with regulations.


  Integrate Threat Intelligence:


  - Use threat intelligence feeds to correlate inspected traffic with known indicators of compromise (IOCs).


  Integrate with Security Tools:


  - Combine SSL/TLS inspection with SIEM and NDR tools to analyze decrypted traffic and generate alerts for suspicious activity.

  - Example Tools: Splunk, Darktrace


  Implement Certificate Management:


  - Use trusted internal or third-party certificates for traffic re-encryption after inspection.

  - Regularly update certificate authorities (CAs) to ensure secure re-encryption.


  Monitor and Tune:


  - Continuously monitor SSL/TLS inspection logs for anomalies and fine-tune policies to reduce false positives.'
external_references:
- external_id: M1020
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1020
id: course-of-action--7bb5fae9-53ad-4424-866b-f0ea2a8b731d
modified: '2024-12-24T13:46:05.302Z'
name: SSL/TLS Inspection
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: course-of-action
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '1.1'
```
