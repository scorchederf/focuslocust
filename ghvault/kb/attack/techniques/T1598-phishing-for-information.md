---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1598 - Phishing for Information

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1598` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may send phishing messages to elicit sensitive information that can be used during targeting. Phishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Phishing for information is different from Phishing in that the objective is gathering data from the victim rather than executing malicious code.

All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass credential harvesting campaigns.

Adversaries may also try to obtain information directly through the exchange of emails, instant messages, or other electronic conversation means. Victims may also receive phishing messages that direct them to call a phone number where the adversary attempts to collect confidential information.

Phishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: Establish Accounts or Compromise Accounts) and/or sending multiple, seemingly urgent messages. Another way to accomplish this is by Email Spoofing the identity of the sender, which can be used to fool both the human recipient as well as automated security tools. 

Phishing for information may also involve evasive techniques, such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., Email Hiding Rules).

## Source Verification

[source record](../../sources/mitre/phishing-for-information.md)

## Evidence Excerpt

```text
created: '2020-10-02T17:07:01.502Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may send phishing messages to elicit sensitive information that can be used during targeting. Phishing\
\ for information is an attempt to trick targets into divulging information, frequently credentials or other actionable\
\ information. Phishing for information is different from [Phishing](https://attack.mitre.org/techniques/T1566) in that\
\ the objective is gathering data from the victim rather than executing malicious code.\n\nAll forms of phishing are electronically\
\ delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual,\
\ company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing,\
```
