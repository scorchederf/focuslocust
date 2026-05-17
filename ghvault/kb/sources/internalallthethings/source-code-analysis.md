---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Source Code Analysis

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-methodology-source-code-analysis` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/methodology/source-code-analysis.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Source Code Analysis](../../topics/methodology/source-code-analysis.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-methodology-source-code-analysis |
| name | Source Code Analysis |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/methodology/source-code-analysis.md |

## Preserved Source Material

````yaml
_body: "# Source Code Analysis\n\n> Source code analysis is the process of examining and reviewing the code of a software\
  \ program to identify errors, vulnerabilities, and potential improvements. This can be performed manually by developers\
  \ or through automated tools that scan the code for issues like security risks, coding standard violations, and performance\
  \ inefficiencies.\n\n## AI Analysis\n\n* [trailofbits/skills](https://github.com/trailofbits/skills) - Trail of Bits Claude\
  \ Code skills for security research, vulnerability detection, and audit workflows.\n\n```ps1\nnpm install -g @github/copilot\n\
  copilot\n/login\n/model\n/plugin marketplace add trailofbits/skills\n/plugin marketplace browse trailofbits\n/plugin install\
  \ ask-questions-if-underspecified@trailofbits\n/plugin install static-analysis@trailofbits\n/plugin install entry-point-analyzer@trailofbits\n\
  /plugin install semgrep-rule-creator@trailofbits\n/plugin install semgrep-rule-variant-creator@trailofbits\n/plugin install\
  \ sharp-edges@trailofbits\n/plugin install insecure-defaults@trailofbits\n```\n\n## Semgrep\n\n> Lightweight static analysis\
  \ for many languages. Find bug variants with patterns that look like source code.\n\n**Install**:\n\n* Binaries: [opengrep/opengrep](https://github.com/opengrep/opengrep)\
  \ / [semgrep/semgrep](https://github.com/semgrep/semgrep)\n* Ubuntu/WSL/Linux/macOS: `python3 -m pip install semgrep`\n\
  * macOS: `brew install semgrep`\n* Docker\n\n    ```ps1\n    docker run -it -v \"${PWD}:/src\" semgrep/semgrep semgrep login\n\
  \    docker run -e SEMGREP_APP_TOKEN=<TOKEN> --rm -v \"${PWD}:/src\" semgrep/semgrep semgrep ci\n    ```\n\n**Semgrep rules**:\n\
  \n* [semgrep/semgrep-rules](https://github.com/semgrep/semgrep-rules) - Official Semgrep rules registry\n* [trailofbits/semgrep-rules](https://github.com/trailofbits/semgrep-rules)\
  \ - Semgrep queries developed by Trail of Bits\n* [Decurity/semgrep-smart-contracts)](https://github.com/Decurity/semgrep-smart-contracts)\
  \ - Semgrep rules for smart contracts based on DeFi exploits\n* [0xdea/semgrep-rules](https://github.com/0xdea/semgrep-rules)\
  \ - A collection of Semgrep rules to facilitate vulnerability research.\n* [elttam/semgrep-rules](https://github.com/elttam/semgrep-rules)\
  \ - Elttam's public semgrep rules repository.\n\n**Other Tools**:\n\n* [Orange-Cyberdefense/grepmarx](https://github.com/Orange-Cyberdefense/grepmarx)\
  \ - A source code static analysis platform for AppSec enthusiasts, based on semgrep engine.\n\n## SonarQube\n\n> Continuous\
  \ Inspection\n\n**Install**\n\n* Docker\n\n    ```ps1\n    docker run -d --name sonarqube -p 9000:9000 sonarqube:community\n\
  \    ```\n\n**Configuration**\n\n* Go to localhost:9000\n* Login with `admin:admin`\n* Create a local project\n* Generate\
  \ a token for the project\n* Use `sonar-scanner-cli` with the generated token\n\n    ```ps1\n    docker run --rm -e SONAR_HOST_URL=\"\
  http://10.10.10.10:9000\" -v \"/tmp/www:/usr/src\" sonarsource/sonar-scanner-cli -Dsonar.projectKey=sonar-project-name -Dsonar.sources=.\
  \ -Dsonar.host.url=http://10.10.10.10:9000 -Dsonar.token=sqp_redacted\n    ```\n\n* Check the Security Hotspots tab: `http://10.10.10.10:9000/security_hotspots?id=sonar-project-name`\n\
  \n:warning: remove dead symbolic links before scanning a folder.\n\n## Psalm\n\n> A static analysis tool for finding errors\
  \ in PHP applications\n\n**Install**\n\n```ps1\ncomposer require --dev vimeo/psalm\n```\n\n**Configuration**\n\n* Create\
  \ a project and initiate a scan of the codebase\n\n    ```ps1\n    ./vendor/bin/psalm --init\n    ./vendor/bin/psalm --taint-analysis\n\
  \    ./vendor/bin/psalm --report=results.sarif\n    ```\n\n* Use a Sarif viewer to see the results: [microsoft.github.io/sarif-web-component](https://microsoft.github.io/sarif-web-component/)\n\
  \n## CodeQL\n\n> CodeQL: the libraries and queries that power security researchers around the world, as well as code scanning\
  \ in GitHub Advanced Security\n\n**Install**:\n\n* [github/codeql](https://github.com/github/codeql)\n\n**Configuration**\n\
  \n```ps1\ncodeql resolve packs\ncodeql resolve languages\ncodeql database create <database> --language=<language-identifier>\n\
  codeql database create --language=python <output-folder>/python-database\ncodeql database create --language=cpp <output-folder>/cpp-database\n\
  codeql database analyze <database> --format=<format> --output=<output> <query-specifiers>...\ncodeql database analyze /codeql-dbs/example-repo\
  \ javascript-code-scanning.qls --sarif-category=javascript-typescript  --format=sarif-latest --output=/temp/example-repo-js.sarif\n\
  codeql database analyze <database> microsoft/coding-standards@1.0.0 github/security-queries --format=sarifv2.1.0 --output=query-results.sarif\
  \ --download\n```\n\n## Snyk\n\n> Snyk CLI scans and monitors your projects for security vulnerabilities.\n\n**Install**\n\
  \n* [Snyk Security - Visual Studio](https://marketplace.visualstudio.com/items?itemName=snyk-security.snyk-vulnerability-scanner-vs)\n\
  * [Snyk Code / Snyk Open Source](https://app.snyk.io)\n\n    ```ps1\n    curl https://static.snyk.io/cli/latest/snyk-linux\
  \ -o snyk\n    chmod +x ./snyk\n    mv ./snyk /usr/local/bin/ \n\n    docker run -it \\\n        -e \"SNYK_TOKEN=<TOKEN>\"\
  \ \\\n        -v \"<PROJECT_DIRECTORY>:/project\" \\\n        -v \"/home/user/.gradle:/home/node/.gradle\" \\\n    snyk/snyk:gradle:6.4\
  \ test --org=my-org-name\n    ```\n\n**Configuration**\n\n```ps1\nsnyk auth\nsnyk ignore --file-path=<directory_or_file>\n\
  snyk code test\n\n# npm install snyk-to-html -g\nsnyk code test --json | snyk-to-html -o results-opensource.html\n```\n\n\
  ## References\n\n* [Code auditing 101 - Rodolphe Ghio - August 2, 2025](https://blog.rodolpheg.xyz/posts/code-auditing--101/)\n\
  * [Detect PHP security vulnerabilities with Psalm - Matt Brown - June 23, 2020](https://psalm.dev/articles/detect-security-vulnerabilities-with-psalm)\n\
  * [Security Analysis in Psalm - Official Documentation](https://psalm.dev/docs/security_analysis/)"
_relative_path: methodology/source-code-analysis.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/methodology/source-code-analysis.md
````
