---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# AWS - Service - Cognito

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-aws-aws-cognito` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-cognito.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AWS - Service - Cognito](../../topics/cloud/aws-service-cognito.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-aws-aws-cognito |
| name | AWS - Service - Cognito |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/aws/aws-cognito.md |

## Preserved Source Material

````yaml
_body: "# AWS - Service - Cognito\n\nAWS Cognito is an AWS-managed service for authentication, authorization, and user management.\n\
  \n1. A user signs in through Cognito User Pools (authentication) or via a federated IdP (Google, Facebook, SAML, etc.).\n\
  2. Cognito Identity Pools can then exchange this identity for temporary AWS credentials (from STS — Security Token Service).\n\
  3. These credentials (Access Key ID, Secret Access Key, and Session Token) let the app directly call AWS services (e.g.,\
  \ S3, DynamoDB, API Gateway) with limited IAM roles/policies.\n\n## Tools\n\n* [Cognito Scanner](https://github.com/padok-team/cognito-scanner)\
  \ - A CLI tool for executing attacks on cognito such as *Unwanted account creation*, *Account Oracle* and *Identity Pool\
  \ escalation*.\n\n    ```ps1\n    # Installation\n    $ pip install cognito-scanner\n    # Usage\n    $ cognito-scanner\
  \ --help\n    # Get information about how to use the unwanted account creation script\n    $ cognito-scanner account-creation\
  \ --help\n    # For more details go to https://github.com/padok-team/cognito-scanner\n    ```\n\n## Identity Pool ID\n\n\
  * **User Pools** : User pools allow sign-in and sign-up functionality\n* **Identity Pools** : Identity pools allow authenticated\
  \ and unauthenticated users to access AWS resources using temporary credentials\n\nOnce you have the Cognito Identity Pool\
  \ Id token, you can proceed further and fetch Temporary AWS Credentials for an unauthenticated role using the identified\
  \ tokens.\n\n```py\nimport boto3\n\nregion='us-east-1'\nidentity_pool='us-east-1:5280c436-2198-2b5a-b87c-9f54094x8at9'\n\
  \nclient = boto3.client('cognito-identity',region_name=region)\n_id = client.get_id(IdentityPoolId=identity_pool)\n_id =\
  \ _id['IdentityId']\n\ncredentials = client.get_credentials_for_identity(IdentityId=_id)\naccess_key = credentials['Credentials']['AccessKeyId']\n\
  secret_key = credentials['Credentials']['SecretKey']\nsession_token = credentials['Credentials']['SessionToken']\nidentity_id\
  \ = credentials['IdentityId']\nprint(\"Access Key: \" + access_key)\nprint(\"Secret Key: \" + secret_key)\nprint(\"Session\
  \ Token: \" + session_token)\nprint(\"Identity Id: \" + identity_id)\n```\n\n## AWS Cognito Commands\n\n### Get User Information\n\
  \n```ps1\naws cognito-idp get-user --access-token $(cat access_token.txt)\n```\n\n### Admin Authentication\n\n```ps1\naws\
  \ cognito-idp admin-initiate-auth --access-token $(cat access_token)\n```\n\n### List User Groups\n\n```ps1\naws cognito-idp\
  \ admin-list-groups-for-user --username user.name@email.com --user-pool-id \"Group-Name\"\n```\n\n### Sign up\n\n```ps1\n\
  aws cognito-idp sign-up --client-id <client-id> --username <username> --password <password>\n```\n\n### Modify Attributes\n\
  \n```ps1\naws cognito-idp update-user-attributes --access-token $(cat access_token) --user-attributes Name=<attribute>,Value=<value>\n\
  ```\n\n## References\n\n* [Exploiting weak configurations in Amazon Cognito - Pankaj Mouriya - April 6, 2021](https://blog.appsecco.com/exploiting-weak-configurations-in-amazon-cognito-in-aws-471ce761963)"
_relative_path: cloud/aws/aws-cognito.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-cognito.md
````
