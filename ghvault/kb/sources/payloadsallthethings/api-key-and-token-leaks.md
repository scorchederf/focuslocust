---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# API Key and Token Leaks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-api-key-leaks-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/API Key Leaks/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [API Key and Token Leaks](../../topics/api-key-leaks/api-key-and-token-leaks.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-api-key-leaks-readme |
| name | API Key and Token Leaks |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/API%20Key%20Leaks/README.md |

## Preserved Source Material

````yaml
_body: "# API Key and Token Leaks\n\n> API keys and tokens are forms of authentication commonly used to manage permissions\
  \ and access to both public and private services. Leaking these sensitive pieces of data can lead to unauthorized access,\
  \ compromised security, and potential data breaches.\n\n## Summary\n\n- [Tools](#tools)\n- [Methodology](#methodology)\n\
  \    - [Common Causes of Leaks](#common-causes-of-leaks)\n    - [Validate The API Key](#validate-the-api-key)\n- [Reducing\
  \ The Attack Surface](#reducing-the-attack-surface)\n- [References](#references)\n\n## Tools\n\n- [aquasecurity/trivy](https://github.com/aquasecurity/trivy)\
  \ - General purpose vulnerability and misconfiguration scanner which also searches for API keys/secrets.\n- [blacklanternsecurity/badsecrets](https://github.com/blacklanternsecurity/badsecrets)\
  \ - A library for detecting known or weak secrets on across many platforms.\n- [irsdl/crapsecrets](https://github.com/irsdl/crapsecrets)\
  \ - A library for detecting known secrets across many web frameworks.\n- [d0ge/sign-saboteur](https://github.com/d0ge/sign-saboteur)\
  \ - SignSaboteur is a Burp Suite extension for editing, signing, verifying various signed web tokens.\n- [mazen160/secrets-patterns-db](https://github.com/mazen160/secrets-patterns-db)\
  \ - Secrets Patterns DB: The largest open-source Database for detecting secrets, API keys, passwords, tokens, and more.\n\
  - [momenbasel/KeyFinder](https://github.com/momenbasel/KeyFinder) - is a tool that let you find keys while surfing the web.\n\
  - [streaak/keyhacks](https://github.com/streaak/keyhacks) - is a repository which shows quick ways in which API keys leaked\
  \ by a bug bounty program can be checked to see if they're valid.\n- [trufflesecurity/truffleHog](https://github.com/trufflesecurity/truffleHog)\
  \ - Find credentials all over the place.\n- [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)\
  \ - Use these templates to test an API token against many API service endpoints.\n\n    ```powershell\n    nuclei -t token-spray/\
  \ -var token=token_list.txt\n    ```\n\n## Methodology\n\n- **API Keys**: Unique identifiers used to authenticate requests\
  \ associated with your project or application.\n- **Tokens**: Security tokens (like OAuth tokens) that grant access to protected\
  \ resources.\n\n### Common Causes of Leaks\n\n- **Hardcoding in Source Code**: Developers may unintentionally leave API\
  \ keys or tokens directly in the source code.\n\n    ```py\n    # Example of hardcoded API key\n    api_key = \"1234567890abcdef\"\
  \n    ```\n\n- **Public Repositories**: Accidentally committing sensitive keys and tokens to publicly accessible version\
  \ control systems like GitHub.\n\n    ```ps1\n    ## Scan a Github Organization\n    docker run --rm -it -v \"$PWD:/pwd\"\
  \ trufflesecurity/trufflehog:latest github --org=trufflesecurity\n    \n    ## Scan a GitHub Repository, its Issues and\
  \ Pull Requests\n    docker run --rm -it -v \"$PWD:/pwd\" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys\
  \ --issue-comments --pr-comments\n    ```\n\n- **Hardcoding in Docker Images**: API keys and credentials might be hardcoded\
  \ in Docker images hosted on DockerHub or private registries.\n\n    ```ps1\n    # Scan a Docker image for verified secrets\n\
  \    docker run --rm -it -v \"$PWD:/pwd\" trufflesecurity/trufflehog:latest docker --image trufflesecurity/secrets\n   \
  \ ```\n\n- **Logs and Debug Information**: Keys and tokens might be inadvertently logged or printed during debugging processes.\n\
  \n- **Configuration Files**: Including keys and tokens in publicly accessible configuration files (e.g., .env files, config.json,\
  \ settings.py, or .aws/credentials.).\n\n### Validate The API Key\n\nIf assistance is needed in identifying the service\
  \ that generated the token, [mazen160/secrets-patterns-db](https://github.com/mazen160/secrets-patterns-db) can be consulted.\
  \ It is the largest open-source database for detecting secrets, API keys, passwords, tokens, and more. This database contains\
  \ regex patterns for various secrets.\n\n```yaml\npatterns:\n  - pattern:\n      name: AWS API Gateway\n      regex: '[0-9a-z]+.execute-api.[0-9a-z._-]+.amazonaws.com'\n\
  \      confidence: low\n  - pattern:\n      name: AWS API Key\n      regex: AKIA[0-9A-Z]{16}\n      confidence: high\n```\n\
  \nUse [streaak/keyhacks](https://github.com/streaak/keyhacks) or read the documentation of the service to find a quick way\
  \ to verify the validity of an API key.\n\n- **Example**: Telegram Bot API Token\n\n    ```ps1\n    curl https://api.telegram.org/bot<TOKEN>/getMe\n\
  \    ```\n\n## Reducing The Attack Surface\n\nCheck the existence of a private key or AWS credentials before committing\
  \ your changes in a GitHub repository.\n\nAdd these lines to your `.pre-commit-config.yaml` file.\n\n```yml\n-   repo: https://github.com/pre-commit/pre-commit-hooks\n\
  \    rev: v3.2.0\n    hooks:\n    -   id: detect-aws-credentials\n    -   id: detect-private-key\n```\n\n## References\n\
  \n- [Finding Hidden API Keys & How to Use Them - Sumit Jain - August 24, 2019](https://web.archive.org/web/20191012175520/https://medium.com/@sumitcfe/finding-hidden-api-keys-how-to-use-them-11b1e5d0f01d)\n\
  - [Introducing SignSaboteur: Forge Signed Web Tokens with Ease - Zakhar Fedotkin - May 22, 2024](https://web.archive.org/web/20240522172244/https://portswigger.net/research/introducing-signsaboteur-forge-signed-web-tokens-with-ease)\n\
  - [Private API Key Leakage Due to Lack of Access Control - yox - August 8, 2018](https://web.archive.org/web/20211208043535/https://hackerone.com/reports/376060)\n\
  - [Saying Goodbye to My Favorite 5 Minute P1 - Allyson O'Malley - January 6, 2020](https://web.archive.org/web/20250714230057/https://www.allysonomalley.com/2020/01/06/saying-goodbye-to-my-favorite-5-minute-p1/)"
_relative_path: API Key Leaks/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/API Key Leaks/README.md
````
