---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1677
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/saas
mitre-attack: kb/mitre/attack/techniques/T1677-poisoned-pipeline-execution
tactic:
    - Execution
platforms:
    - SaaS
permissions required:
    - none
---

## Description

Adversaries may manipulate continuous integration / continuous development (CI/CD) processes by injecting malicious code into the build process. There are several mechanisms for poisoning pipelines: <br><br>* In a <b>Direct Pipeline Execution</b> scenario, the threat actor directly modifies the CI configuration file (e.g., `gitlab-ci.yml` in GitLab). They may include a command to exfiltrate credentials leveraged in the build process to a remote server, or to export them as a workflow artifact.[^5] [^6] <br>* In an <b>Indirect Pipeline Execution</b> scenario, the threat actor injects malicious code into files referenced by the CI configuration file. These may include makefiles, scripts, unit tests, and linters.[^6] <br>* In a <b>Public Pipeline Execution</b> scenario, the threat actor does not have direct access to the repository but instead creates a malicious pull request from a fork that triggers a part of the CI/CD pipeline. For example, in GitHub Actions, the `pull_request_target` trigger allows workflows running from forked repositories to access secrets.  If this trigger is combined with an explicit pull request checkout and a location for a threat actor to insert malicious code (e.g., an `npm build` command), a threat actor may be able to leak pipeline credentials.[^5] [^2]  Similarly, threat actors may craft pull requests with malicious inputs (such as branch names) if the build pipeline treats those inputs as trusted.[^7] [^1] [^3]  Finally, if a pipeline leverages a self-hosted runner, a threat actor may be able to execute arbitrary code on a host inside the organization’s network.[^4] <br><br>By poisoning CI/CD pipelines, threat actors may be able to gain access to credentials, laterally move to additional hosts, or input malicious components to be shipped further down the pipeline (i.e., [[kb/mitre/attack/techniques/T1195-supply-chain-compromise|Supply Chain Compromise]]). 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S9008](https://attack.mitre.org/software/S9008) | Shai-Hulud | Shai-Hulud has also leveraged GitHub actions from stolen accounts in order to create a malicious Github workflow within `.github/workflows/discussion.yaml`.[^1] [^2] [^3] [^4]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Ensure that CI/CD pipelines only have permissions they require to complete their operations. Additionally, limit the number of users who have write access to internal repositories to only those necessary. |
| [[kb/mitre/attack/mitigations/M1054-software-configuration\|M1054]] | Software Configuration | Where possible, avoid allowing pipelines to run unreviewed code. Where this is necessary, ensure that these pipelines are executed on isolated nodes without access to secrets. In GitHub, avoid using the `pull_request_target` trigger if possible, do not treat user-controlled inputs (such as branch names) as trusted, and do not use self-hosted runners on public repositories.   |

 [^1]: [Synactiv Hijacking GitHub Runners](https://www.synacktiv.com/en/publications/hijacking-github-runners-to-compromise-the-organization)
 [^2]: [GitHub Security Lab GitHub Actions Security 2021](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/)
 [^3]: [GitHub Security Labs GitHub Actions Security Part 2 2021](https://securitylab.github.com/resources/github-actions-untrusted-input/)
 [^4]: [John Stawinski PyTorch Supply Chain Attack 2024](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/)
 [^5]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)
 [^6]: [OWASP CICD-SEC-4](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-04-Poisoned-Pipeline-Execution)
 [^7]: [Wiz Ultralytics AI Library Hijack 2024](https://www.wiz.io/blog/ultralytics-ai-library-hacked-via-github-for-cryptomining)
 [^8]: [Aikido Shai-Hulud September 2025](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
 [^9]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
 [^10]: [Palo Alto Unit 42 Shai-Hulud November 2025](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
 [^11]: [Socket Shai-Hulud November 2025](https://socket.dev/blog/shai-hulud-strikes-again-v2)
