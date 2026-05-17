---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# CI/CD Attacks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-devops-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CI/CD Attacks](../../topics/devops/ci-cd-attacks.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-devops-readme |
| name | CI/CD Attacks |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/devops/README.md |

## Preserved Source Material

```yaml
_body: "# CI/CD Attacks\n\n> CI/CD pipelines are often triggered by untrusted actions such a forked pull requests and new\
  \ issue submissions for public git repositories. These systems often contain sensitive secrets or run in privileged environments.\
  \ Attackers may gain an RCE into such systems by submitting crafted payloads that trigger the pipelines. Such vulnerabilities\
  \ are also known as Poisoned Pipeline Execution (PPE).\n\n## Summary\n\n- [Tools](#tools)\n- [CI/CD Products](#summary)\n\
  \    - [GitHub Actions](./cicd-github-actions)\n    - [Gitlab CI](./cicd-gitlab-ci)\n    - [Azure Pipelines (Azure DevOps)](./cicd-azure-devops)\n\
  \    - [Circle CI](./cicd-circle-ci)\n    - [Drone CI](./cicd-drone-ci)\n    - [BuildKite](./cicd-buildkite)\n- [Hardcoded\
  \ Secrets Enumeration](./secrets-enumeration)\n- [Package Managers and Build Files](./package-managers)\n- [References](#references)\n\
  \n## Tools\n\n- [praetorian-inc/gato](https://github.com/praetorian-inc/gato) - GitHub Self-Hosted Runner Enumeration and\
  \ Attack Tool\n- [AdnaneKhan/Gato-X](https://github.com/AdnaneKhan/Gato-X) - Fork of Gato - Gato (Github Attack TOolkit)\
  \ - Extreme Edition\n- [messypoutine/gravy-overflow](https://github.com/messypoutine/gravy-overflow) - A GitHub Actions\
  \ Supply Chain CTF / Goat\n- [xforcered/SCMKit](https://github.com/xforcered/SCMKit) - Source Code Management Attack Toolkit\n\
  - [synacktiv/octoscan](https://github.com/synacktiv/octoscan) - Octoscan is a static vulnerability scanner for GitHub action\
  \ workflows.\n- [synacktiv/gh-hijack-runner](https://github.com/synacktiv/gh-hijack-runner) - A python script to create\
  \ a fake GitHub runner and hijack pipeline jobs to leak CI/CD secrets.\n- [synacktiv/nord-stream](https://github.com/synacktiv/nord-stream)\
  \ - List the secrets stored inside CI/CD environments and extract them by deploying malicious pipelines\n- [praetorian-inc/glato](https://github.com/praetorian-inc/glato)\
  \ - GitLab Attack TOolkit\n\n## References\n\n- [Poisoned Pipeline Execution](https://web.archive.org/web/20240226215436/https://www.cidersecurity.io/top-10-cicd-security-risks/poisoned-pipeline-execution-ppe/)\n\
  - [DEF CON 25 - Exploiting Continuous Integration (CI) and Automated Build systems - spaceB0x - 2 nov. 2017](https://youtu.be/mpUDqo7tIk8)\n\
  - [Controlling the Source: Abusing Source Code Management Systems - Brett Hawkins - August 9, 2022](https://securityintelligence.com/posts/abusing-source-code-management-systems/)\n\
  - [Fixing Typos and Breaching Microsoft’s Perimeter - John Stawinski IV - April 15, 2024](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/)"
_relative_path: devops/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/README.md
```
