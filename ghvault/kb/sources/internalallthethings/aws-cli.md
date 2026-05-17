---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# AWS - CLI

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-aws-aws-cli` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-cli.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AWS - CLI](../../topics/cloud/aws-cli.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-aws-aws-cli |
| name | AWS - CLI |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/aws/aws-cli.md |

## Preserved Source Material

````yaml
_body: "# AWS - CLI\n\nThe AWS Command Line Interface (CLI) is a unified tool to manage AWS services from the command line.\
  \ Using the AWS CLI, you can control multiple AWS services, automate tasks, and manage configurations through profiles.\n\
  \n## Set up AWS CLI\n\nInstall AWS CLI and configure it for the first time:\n\n```ps1\naws configure\n```\n\nThis will prompt\
  \ for:\n\n* AWS Access Key ID\n* AWS Secret Access Key\n* Default region name\n* Default output format\n\n## Creating Profiles\n\
  \nYou can configure multiple profiles in `~/.aws/credentials` and `~/.aws/config`.\n\n* `~/.aws/credentials` (stores credentials)\n\
  \n    ```ini\n    [default]\n    aws_access_key_id = <default-access-key>\n    aws_secret_access_key = <default-secret-key>\n\
  \n    [dev-profile]\n    aws_access_key_id = <dev-access-key>\n    aws_secret_access_key = <dev-secret-key>\n\n    [prod-profile]\n\
  \    aws_access_key_id = <prod-access-key>\n    aws_secret_access_key = <prod-secret-key>\n    ```\n\n* `~/.aws/config`\
  \ (stores region and output settings)\n\n    ```ini\n    [default]\n    region = us-east-1\n    output = json\n\n    [profile\
  \ dev-profile]\n    region = us-west-2\n    output = yaml\n\n    [profile prod-profile]\n    region = eu-west-1\n    output\
  \ = json\n    ```\n\nYou can also create profiles via the command line:\n\n```ps1\naws configure --profile dev-profile\n\
  ```\n\n## Using Profiles\n\nWhen running AWS CLI commands, you can specify which profile to use by adding the `--profile`\
  \ flag:\n\n```ps1\naws s3 ls --profile dev-profile\n```\n\nIf no profile is specified, the **default** profile is used."
_relative_path: cloud/aws/aws-cli.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-cli.md
````
