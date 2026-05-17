---
parsed_by: focuslocust
source: mitre
type: generated
---
# TruffleHog

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S9009` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

TruffleHog is an open-source secrets-discovery tool that is used to search for credentials, API keys, and encryption keys across a variety of data sources and environments. TruffleHog has the ability to discover credentials and secrets stored in code repositories, git history, CI/CD pipelines, among other common storage locations to include filesystems and cloud storage buckets. TruffleHog was first released by its author in 2016.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/trufflehog.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has gathered data from home directories of the victim environment.(Citation: Netskope Shai-Hulud November 2025) |
| [T1059.009 - Cloud API](../../attack/techniques/T1059.009-cloud-api.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has leveraged Cloud CLI in order to enumerate and gather credentials.(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [T1078.004 - Cloud Accounts](../../attack/techniques/T1078.004-cloud-accounts.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has used stolen credentials to log into cloud services to access cloud hosted repositories and other cloud storage solutions to discover sensitive data to include API Keys, tokens and credentials.(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has can browse and scan individual files and directories.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Netskope Shai-Hulud November 2025)(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [T1213.001 - Confluence](../../attack/techniques/T1213.001-confluence.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has collected credentials and data associated with Confluence.(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [T1213.002 - Sharepoint](../../attack/techniques/T1213.002-sharepoint.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has searched SharePoint for data and credentials.(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [T1213.003 - Code Repositories](../../attack/techniques/T1213.003-code-repositories.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has gathered data and credentials from code repositories.(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [T1213.005 - Messaging Applications](../../attack/techniques/T1213.005-messaging-applications.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has obtained data and credentials associated with messaging applications to include Slack.(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [T1526 - Cloud Service Discovery](../../attack/techniques/T1526-cloud-service-discovery.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has the ability to scan code repositories and CI/CD platforms.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [T1528 - Steal Application Access Token](../../attack/techniques/T1528-steal-application-access-token.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has gathered access tokens and API tokens from CI/CD pipeline solutions and repositories.(Citation: Black Hills Information Security TruffleHog January 2024) |
| [T1530 - Data from Cloud Storage](../../attack/techniques/T1530-data-from-cloud-storage.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has the ability to scan cloud storage services for credentials to include Amazon (AWS) S3 and Google Cloud Storage.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [T1552.001 - Credentials In Files](../../attack/techniques/T1552.001-credentials-in-files.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has obtained credentials stored in config files and credential files in victim environments.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Netskope Shai-Hulud November 2025) |
| [T1552.005 - Cloud Instance Metadata API](../../attack/techniques/T1552.005-cloud-instance-metadata-api.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) can query the AWS and GCP metadata endpoints for instances and service credentials.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [T1555.006 - Cloud Secrets Management Stores](../../attack/techniques/T1555.006-cloud-secrets-management-stores.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) can obtain secrets from AWS Secrets and GCP Secret Manager.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025) [TruffleHog](https://attack.mitre.org/software/S9009) has also gathered passwords, secrets and API keys from source repositories, .env files, and git history.(Citation: Netskope Shai-Hulud November 2025) |
| [T1580 - Cloud Infrastructure Discovery](../../attack/techniques/T1580-cloud-infrastructure-discovery.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) can enumerate AWS Infrastructure to include EC2 instances.(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [T1619 - Cloud Storage Object Discovery](../../attack/techniques/T1619-cloud-storage-object-discovery.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) can enumerate cloud storage environments including Amazon Web Service (AWS) S3 buckets and Google Cloud Storage buckets.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025) |

## Source Verification

[source record](../../sources/mitre/trufflehog.md)

## Evidence Excerpt

```text
created: '2026-04-09T19:12:38.917Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[TruffleHog](https://attack.mitre.org/software/S9009) is an open-source secrets-discovery tool that is used
to search for credentials, API keys, and encryption keys across a variety of data sources and environments.(Citation: Black
Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025) [TruffleHog](https://attack.mitre.org/software/S9009)
has the ability to discover credentials and secrets stored in code repositories, git history, CI/CD pipelines, among other
common storage locations to include filesystems and cloud storage buckets.(Citation: Black Hills Information Security TruffleHog
January 2024)(Citation: Netskope Shai-Hulud November 2025)(Citation: Github TruffleSecurity Trufflehog April 2025) [TruffleHog](https://attack.mitre.org/software/S9009)
```
