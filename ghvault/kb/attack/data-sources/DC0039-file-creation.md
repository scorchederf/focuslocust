---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0039 - File Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0039` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

A new file is created on a system or network storage. This action often signifies an operation such as saving a document, writing data, or deploying a file. Logging these events helps identify legitimate or potentially malicious file creation activities. Examples include logging file creation events (e.g., Sysmon Event ID 11 or Linux auditd logs).

## Source Verification

[source record](../../sources/mitre/file-creation.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'A new file is created on a system or network storage. This action often signifies an operation such as saving
a document, writing data, or deploying a file. Logging these events helps identify legitimate or potentially malicious file
creation activities. Examples include logging file creation events (e.g., Sysmon Event ID 11 or Linux auditd logs). '
external_references:
- external_id: DC0039
source_name: mitre-attack
```
