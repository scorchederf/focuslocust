---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1683
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/resource_development
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1683-generate-content
tactic:
    - Resource Development
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may create or generate content to support targeting and operations. This content may be used to establish personas, impersonate known individuals or organizations, and support [[kb/mitre/attack/techniques/T1684-social-engineering|Social Engineering]], fraud, or influence activities. Written materials, audio, images, video, or other media may be developed and tailored to the target and objective.[^1] <br><br>Content development may occur prior to or during an operation. Adversaries may develop or generate content in-house, source it through third parties, or produce it using AI-assisted tools. Adversaries may use AI to research targets, develop pretexts, and better understand the organizations and individuals they intend to target or deceive prior to generating content (i.e., [[kb/mitre/attack/techniques/T1682-query-public-ai-services|Query Public AI Services]]); for obtaining access to AI tools used in content generation, see [[kb/mitre/attack/techniques/T1588.007-artificial-intelligence|Artificial Intelligence]]. <br><br>Content may be leveraged in support of techniques such as [[kb/mitre/attack/techniques/T1566-phishing|Phishing]], [[kb/mitre/attack/techniques/T1598-phishing-for-information|Phishing for Information]], [[kb/mitre/attack/techniques/T1684-social-engineering|Social Engineering]], [[kb/mitre/attack/techniques/T1657-financial-theft|Financial Theft]], or [[kb/mitre/attack/techniques/T1585-establish-accounts|Establish Accounts]]. Generated or developed content does not include malicious code or scripts (i.e., [[kb/mitre/attack/techniques/T1587-develop-capabilities|Develop Capabilities]] and [[kb/mitre/attack/techniques/T1588.007-artificial-intelligence|Artificial Intelligence]]).

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on designing defenses that are not reliant on atomic indicators.  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1683.001-written-content\|T1683.001]] | Written Content |
| [[kb/mitre/attack/techniques/T1683.002-audio-visual-content\|T1683.002]] | Audio-Visual Content |

 [^1]: [IBM AI-Generated Content](https://www.ibm.com/think/insights/ai-generated-content)
