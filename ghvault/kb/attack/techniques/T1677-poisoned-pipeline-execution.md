---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1677 - Poisoned Pipeline Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1677` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may manipulate continuous integration / continuous development (CI/CD) processes by injecting malicious code into the build process. There are several mechanisms for poisoning pipelines: 

* In a <b>Direct Pipeline Execution</b> scenario, the threat actor directly modifies the CI configuration file (e.g., `gitlab-ci.yml` in GitLab). They may include a command to exfiltrate credentials leveraged in the build process to a remote server, or to export them as a workflow artifact.
* In an <b>Indirect Pipeline Execution</b> scenario, the threat actor injects malicious code into files referenced by the CI configuration file. These may include makefiles, scripts, unit tests, and linters.
* In a <b>Public Pipeline Execution</b> scenario, the threat actor does not have direct access to the repository but instead creates a malicious pull request from a fork that triggers a part of the CI/CD pipeline. For example, in GitHub Actions, the `pull_request_target` trigger allows workflows running from forked repositories to access secrets.  If this trigger is combined with an explicit pull request checkout and a location for a threat actor to insert malicious code (e.g., an `npm build` command), a threat actor may be able to leak pipeline credentials. Similarly, threat actors may craft pull requests with malicious inputs (such as branch names) if the build pipeline treats those inputs as trusted. Finally, if a pipeline leverages a self-hosted runner, a threat actor may be able to execute arbitrary code on a host inside the organization’s network.

By poisoning CI/CD pipelines, threat actors may be able to gain access to credentials, laterally move to additional hosts, or input malicious components to be shipped further down the pipeline (i.e., Supply Chain Compromise).

## Source Verification

[source record](../../sources/mitre/poisoned-pipeline-execution.md)

## Evidence Excerpt

```text
created: '2025-05-22T20:01:16.611Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may manipulate continuous integration / continuous development (CI/CD) processes by injecting malicious\
\ code into the build process. There are several mechanisms for poisoning pipelines: \n\n* In a <b>Direct Pipeline Execution</b>\
\ scenario, the threat actor directly modifies the CI configuration file (e.g., `gitlab-ci.yml` in GitLab). They may include\
\ a command to exfiltrate credentials leveraged in the build process to a remote server, or to export them as a workflow\
\ artifact.(Citation: Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025)(Citation: OWASP CICD-SEC-4)\n* In an <b>Indirect\
\ Pipeline Execution</b> scenario, the threat actor injects malicious code into files referenced by the CI configuration\
```
