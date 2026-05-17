---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1594 - Search Victim-Owned Websites

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1594` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may search websites owned by the victim for information that can be used during targeting. Victim-owned websites may contain a variety of details, including names of departments/divisions, physical locations, and data about key employees such as names, roles, and contact info (ex: Email Addresses). These sites may also have details highlighting business operations and relationships.

Adversaries may search victim-owned websites to gather actionable information. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: Phishing for Information or Search Open Technical Databases), establishing operational resources (ex: Establish Accounts or Compromise Accounts), and/or initial access (ex: Trusted Relationship or Phishing).

In addition to manually browsing the website, adversaries may attempt to identify hidden directories or files that could contain additional sensitive information or vulnerable functionality. They may do this through automated activities such as Wordlist Scanning, as well as by leveraging files such as sitemap.xml and robots.txt.

## Source Verification

[source record](../../sources/mitre/search-victim-owned-websites.md)

## Evidence Excerpt

```text
created: '2020-10-02T16:51:50.306Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search websites owned by the victim for information that can be used during targeting. Victim-owned
websites may contain a variety of details, including names of departments/divisions, physical locations, and data about
key employees such as names, roles, and contact info (ex: [Email Addresses](https://attack.mitre.org/techniques/T1589/002)).
These sites may also have details highlighting business operations and relationships.(Citation: Comparitech Leak)
Adversaries may search victim-owned websites to gather actionable information. Information from these sources may reveal
opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598)
```
