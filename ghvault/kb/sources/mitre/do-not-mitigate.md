---
parsed_by: focuslocust
source: mitre
type: generated
---
# Do Not Mitigate

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1055` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Do Not Mitigate](../../attack/mitigations/M1055-do-not-mitigate.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1055 |
| name | Do Not Mitigate |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1055 |

## Preserved Source Material

```yaml
created: '2019-07-19T14:58:42.715Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'The Do Not Mitigate category highlights scenarios where attempting to mitigate a specific technique may inadvertently
  increase the organization''s security risk or operational instability. This could happen due to the complexity of the system,
  the integration of critical processes, or the potential for introducing new vulnerabilities. Instead of direct mitigation,
  these situations may call for alternative strategies such as detection, monitoring, or response. The Do Not Mitigate category
  underscores the importance of assessing the trade-offs between mitigation efforts and overall system integrity. This mitigation
  can be implemented through the following measures:


  Complex Systems Where Mitigation is Risky:


  - Interpretation: In certain systems, direct mitigation could introduce new risks, especially if the system is highly interconnected
  or complex, such as in legacy industrial control systems (ICS). Patching or modifying these systems could result in unplanned
  downtime, disruptions, or even safety risks.

  - Use Case: In a power grid control system, attempting to patch or disable certain services related to device communications
  might disrupt critical operations, leading to unintended service outages.


  Risk of Reducing Security Coverage:


  - Interpretation: In some cases, mitigating a technique might reduce the visibility or effectiveness of other security controls,
  limiting an organization’s ability to detect broader attacks.

  - Use Case: Disabling script execution on a web server to mitigate potential PowerShell-based attacks could interfere with
  legitimate administrative operations that rely on scripting, while attackers may still find alternate ways to execute code.


  Introduction of New Vulnerabilities:


  - Interpretation: In highly sensitive or tightly controlled environments, implementing certain mitigations might create
  vulnerabilities in other parts of the system. For instance, disabling default security mechanisms in an attempt to resolve
  compatibility issues may open the system to exploitation.

  - Use Case: Disabling certificate validation to resolve internal communication issues in a secure environment could lead
  to man-in-the-middle attacks, creating a greater vulnerability than the original problem.


  Negative Impact on Performance and Availability:


  - Interpretation: Mitigations that involve removing or restricting system functionalities can have unintended consequences
  for system performance and availability. Some mitigations, while effective at blocking certain attacks, may introduce performance
  bottlenecks or compromise essential operations.

  - Use Case: Implementing high levels of encryption to mitigate data theft might result in significant performance degradation
  in systems handling large volumes of real-time transactions.'
external_references:
- external_id: M1055
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1055
id: course-of-action--787fb64d-c87b-4ee5-a341-0ef17ec4c15c
modified: '2024-12-10T19:25:57.870Z'
name: Do Not Mitigate
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
