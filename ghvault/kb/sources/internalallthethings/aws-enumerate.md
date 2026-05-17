---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# AWS - Enumerate

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-aws-aws-enumeration` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-enumeration.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AWS - Enumerate](../../topics/cloud/aws-enumerate.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-aws-aws-enumeration |
| name | AWS - Enumerate |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/aws/aws-enumeration.md |

## Preserved Source Material

````yaml
_body: "# AWS - Enumerate\n\n## Collectors\n\n* [nccgroup/ScoutSuite](https://github.com/nccgroup/ScoutSuite/wiki) - Multi-Cloud\
  \ Security Auditing Tool\n\n    ```powershell\n    $ python scout.py PROVIDER --help\n    # The --session-token is optional\
  \ and only used for temporary credentials (i.e. role assumption).\n    $ python scout.py aws --access-keys --access-key-id\
  \ <AKIAIOSFODNN7EXAMPLE> --secret-access-key <wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY> --session-token <token>\n    $ python\
  \ scout.py azure --cli\n    ```\n\n* [RhinoSecurityLabs/pacu](https://github.com/RhinoSecurityLabs/pacu) - Exploit configuration\
  \ flaws within an AWS environment using an extensible collection of modules with a diverse feature-set\n\n    ```powershell\n\
  \    $ bash install.sh\n    $ python3 pacu.py\n    set_keys/swap_keys\n    run <module_name> [--keyword-arguments]\n   \
  \ run <module_name> --regions eu-west-1,us-west-1\n    ```\n\n* [salesforce/cloudsplaining](https://github.com/salesforce/cloudsplaining)\
  \ - An AWS IAM Security Assessment tool that identifies violations of least privilege and generates a risk-prioritized report\n\
  \n    ```powershell\n    pip3 install --user cloudsplaining\n    cloudsplaining download --profile myawsprofile\n    cloudsplaining\
  \ scan --input-file default.json\n    ```\n\n* [duo-labs/cloudmapper](https://github.com/duo-labs/cloudmapper) - CloudMapper\
  \ helps you analyze your Amazon Web Services (AWS) environments\n\n    ```powershell\n    sudo apt-get install autoconf\
  \ automake libtool python3.7-dev python3-tk jq awscli build-essential\n    pipenv install --skip-lock\n    pipenv shell\n\
  \    report: Generate HTML report. Includes summary of the accounts and audit findings.\n    iam_report: Generate HTML report\
  \ for the IAM information of an account.\n    audit: Check for potential misconfigurations.\n    collect: Collect metadata\
  \ about an account.\n    find_admins: Look at IAM policies to identify admin users and roles, or principals with specific\
  \ privileges\n    ```\n\n* [cyberark/SkyArk](https://github.com/cyberark/SkyArk) - Discover the most privileged users in\
  \ the scanned AWS environment, including the AWS Shadow Admins\n\n    ```powershell\n    $ powershell -ExecutionPolicy Bypass\
  \ -NoProfile\n    PS C> Import-Module .\\SkyArk.ps1 -force\n    PS C> Start-AWStealth\n    PS C> Scan-AWShadowAdmins  \n\
  \    ```\n\n* [BishopFox/CloudFox](https://github.com/BishopFox/CloudFox/) - Automating situational awareness for cloud\
  \ penetration tests. Designed for white box enumeration (SecurityAudit/ReadOnly type permission), but can be used for black\
  \ box (found credentials) as well.\n\n    ```ps1\n    cloudfox aws --profile [profile-name] all-checks\n    ```\n\n* [toniblyx/Prowler](https://github.com/toniblyx/prowler)\
  \ - AWS security best practices assessments, audits, incident response, continuous monitoring, hardening and forensics readiness.\
  \ It follows guidelines of the CIS Amazon Web Services Foundations Benchmark and DOZENS of additional checks including GDPR\
  \ and HIPAA (+100).\n\n    ```powershell\n    pip install awscli ansi2html detect-secrets\n    sudo apt install jq\n   \
  \ ./prowler -E check42,check43\n    ./prowler -p custom-profile -r us-east-1 -c check11\n    ./prowler -A 123456789012 -R\
  \ ProwlerRole\n    ```\n\n* [nccgroup/PMapper](https://github.com/nccgroup/PMapper) - A tool for quickly evaluating IAM\
  \ permissions in AWS\n\n    ```powershell\n    pip install principalmapper\n    pmapper graph --create\n    pmapper visualize\
  \ --filetype png\n    pmapper analysis --output-type text\n\n    # Determine if PowerUser can escalate privileges\n    pmapper\
  \ query \"preset privesc user/PowerUser\"\n    pmapper argquery --principal user/PowerUser --preset privesc\n\n    # Find\
  \ all principals that can escalate privileges\n    pmapper query \"preset privesc *\"\n    pmapper argquery --principal\
  \ '*' --preset privesc\n\n    # Find all principals that PowerUser can access\n    pmapper query \"preset connected user/PowerUser\
  \ *\"\n    pmapper argquery --principal user/PowerUser --resource '*' --preset connected\n\n    # Find all principals that\
  \ can access PowerUser\n    pmapper query \"preset connected * user/PowerUser\"\n    pmapper argquery --principal '*' --resource\
  \ user/PowerUser --preset connected\n    ```\n\n## AWS - Enumerate IAM permissions\n\nEnumerate the permissions associated\
  \ with AWS credential set with [andresriancho/enumerate-iam](https://github.com/andresriancho/enumerate-iam)\n\n```powershell\n\
  git clone git@github.com:andresriancho/enumerate-iam.git\npip install -r requirements.txt\n./enumerate-iam.py --access-key\
  \ AKIA... --secret-key StF0q...\n2019-05-10 15:57:58,447 - 21345 - [INFO] Starting permission enumeration for access-key-id\
  \ \"AKIA...\"\n2019-05-10 15:58:01,532 - 21345 - [INFO] Run for the hills, get_account_authorization_details worked!\n2019-05-10\
  \ 15:58:01,537 - 21345 - [INFO] -- {\n    \"RoleDetailList\": [\n        {\n            \"Tags\": [],\n            \"AssumeRolePolicyDocument\"\
  : {\n                \"Version\": \"2008-10-17\",\n                \"Statement\": [\n                    {\n...\n2019-05-10\
  \ 15:58:26,709 - 21345 - [INFO] -- gamelift.list_builds() worked!\n2019-05-10 15:58:26,850 - 21345 - [INFO] -- cloudformation.list_stack_sets()\
  \ worked!\n2019-05-10 15:58:26,982 - 21345 - [INFO] -- directconnect.describe_locations() worked!\n2019-05-10 15:58:27,021\
  \ - 21345 - [INFO] -- gamelift.describe_matchmaking_rule_sets() worked!\n2019-05-10 15:58:27,311 - 21345 - [INFO] -- sqs.list_queues()\
  \ worked!\n```\n\n## References\n\n* [An introduction to penetration testing AWS - Akimbocore - HollyGraceful - 06 August\
  \ 2021](https://akimbocore.com/article/introduction-to-penetration-testing-aws/)\n* [AWS CLI Cheatsheet - apolloclark](https://gist.github.com/apolloclark/b3f60c1f68aa972d324b)\n\
  * [AWS - Cheatsheet - @Magnussen](https://www.magnussen.funcmylife.fr/article_35)\n* [Pacu Open source AWS Exploitation\
  \ framework - RhinoSecurityLabs](https://rhinosecuritylabs.com/aws/pacu-open-source-aws-exploitation-framework/)\n* [PACU\
  \ Spencer Gietzen - 30 juil. 2018](https://youtu.be/XfetW1Vqybw?list=PLBID4NiuWSmfdWCmYGDQtlPABFHN7HyD5)"
_relative_path: cloud/aws/aws-enumeration.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-enumeration.md
````
