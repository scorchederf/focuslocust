---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1530 - Data from Cloud Storage

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1530` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may access data from cloud storage.

Many IaaS providers offer solutions for online data object storage such as Amazon S3, Azure Storage, and Google Cloud Storage. Similarly, SaaS enterprise platforms such as Office 365 and Google Workspace provide cloud-based document storage to users through services such as OneDrive and Google Drive, while SaaS application providers such as Slack, Confluence, Salesforce, and Dropbox may provide cloud storage solutions as a peripheral or primary use case of their platform. 

In some cases, as with IaaS-based cloud storage, there exists no overarching application (such as SQL or Elasticsearch) with which to interact with the stored objects: instead, data from these solutions is retrieved directly though the Cloud API. In SaaS applications, adversaries may be able to collect this data directly from APIs or backend cloud storage objects, rather than through their front-end application or interface (i.e., Data from Information Repositories). 

Adversaries may collect sensitive data from these cloud storage solutions. Providers typically offer security guides to help end users configure systems, though misconfigurations are a common problem. There have been numerous incidents where cloud storage has been improperly secured, typically by unintentionally allowing public access to unauthenticated users, overly-broad access by all users, or even access for any anonymous person outside the control of the Identity Access Management system without even needing basic user permissions.

This open access may expose various types of sensitive data, such as credit cards, personally identifiable information, or medical records.

Adversaries may also obtain then abuse leaked credentials from source repositories, logs, or other means as a way to gain access to cloud storage objects.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AADInternals](../../tools/unknown/aadinternals.md) | explicit | source | AADInternals can collect files from a user’s OneDrive.(Citation: AADInternals) |
| [Pacu](../../tools/unknown/pacu.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can enumerate and download files stored in AWS storage services, such as S3 buckets.(Citation: GitHub Pacu) |
| [Peirates](../../tools/unknown/peirates.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can dump the contents of AWS S3 buckets. It can also retrieve service account tokens from kOps buckets in Google Cloud Storage or S3.(Citation: Peirates GitHub) |
| [TruffleHog](../../tools/unknown/trufflehog.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has the ability to scan cloud storage services for credentials to include Amazon (AWS) S3 and Google Cloud Storage.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025) |

## Source Verification

[source record](../../sources/mitre/data-from-cloud-storage.md)

## Evidence Excerpt

```text
created: '2019-08-30T18:07:27.741Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may access data from cloud storage.\n\nMany IaaS providers offer solutions for online data object\
\ storage such as Amazon S3, Azure Storage, and Google Cloud Storage. Similarly, SaaS enterprise platforms such as Office\
\ 365 and Google Workspace provide cloud-based document storage to users through services such as OneDrive and Google Drive,\
\ while SaaS application providers such as Slack, Confluence, Salesforce, and Dropbox may provide cloud storage solutions\
\ as a peripheral or primary use case of their platform. \n\nIn some cases, as with IaaS-based cloud storage, there exists\
\ no overarching application (such as SQL or Elasticsearch) with which to interact with the stored objects: instead, data\
```
