---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# AWS - Access Token & Secrets

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-aws-aws-access-token` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-access-token.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AWS - Access Token & Secrets](../../topics/cloud/aws-access-token-and-secrets.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-aws-aws-access-token |
| name | AWS - Access Token & Secrets |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/aws/aws-access-token.md |

## Preserved Source Material

````yaml
_body: "# AWS - Access Token & Secrets\n\n## URL Services\n\n| Service      | URL                   |\n|--------------|-----------------------|\n\
  | s3           | `https://{user_provided}.s3.amazonaws.com` |\n| cloudfront   | `https://{random_id}.cloudfront.net` |\n\
  | ec2          | `https://ec2-{ip-seperated}.compute-1.amazonaws.com` |\n| es           | `https://{user_provided}-{random_id}.{region}.es.amazonaws.com`\
  \ |\n| elb          | `http://{user_provided}-{random_id}.{region}.elb.amazonaws.com:80/443` |\n| elbv2        | `https://{user_provided}-{random_id}.{region}.elb.amazonaws.com`\
  \ |\n| rds          | `mysql://{user_provided}.{random_id}.{region}.rds.amazonaws.com:3306` |\n| rds          | `postgres://{user_provided}.{random_id}.{region}.rds.amazonaws.com:5432`\
  \ |\n| route 53     | `{user_provided}` |\n| execute-api  | `https://{random_id}.execute-api.{region}.amazonaws.com/{user_provided}`\
  \ |\n| cloudsearch  | `https://doc-{user_provided}-{random_id}.{region}.cloudsearch.amazonaws.com` |\n| transfer     | `sftp://s-{random_id}.server.transfer.{region}.amazonaws.com`\
  \ |\n| iot          | `mqtt://{random_id}.iot.{region}.amazonaws.com:8883` |\n| iot          | `https://{random_id}.iot.{region}.amazonaws.com:8443`\
  \ |\n| iot          | `https://{random_id}.iot.{region}.amazonaws.com:443` |\n| mq           | `https://b-{random_id}-{1,2}.mq.{region}.amazonaws.com:8162`\
  \ |\n| mq           | `ssl://b-{random_id}-{1,2}.mq.{region}.amazonaws.com:61617` |\n| kafka        | `b-{1,2,3,4}.{user_provided}.{random_id}.c{1,2}.kafka.{region}.amazonaws.com`\
  \ |\n| kafka        | `{user_provided}.{random_id}.c{1,2}.kafka.useast-1.amazonaws.com` |\n| cloud9       | `https://{random_id}.vfs.cloud9.{region}.amazonaws.com`\
  \ |\n| mediastore   | `https://{random_id}.data.mediastore.{region}.amazonaws.com` |\n| kinesisvideo | `https://{random_id}.kinesisvideo.{region}.amazonaws.com`\
  \ |\n| mediaconvert | `https://{random_id}.mediaconvert.{region}.amazonaws.com` |\n| mediapackage | `https://{random_id}.mediapackage.{region}.amazonaws.com/in/v1/{random_id}/channel`\
  \ |\n\n## Access Key ID & Secret\n\nIAM uses the following prefixes to indicate what type of resource each unique ID applies\
  \ to. The first four characters are the prefix that depends on the type of the key.\n\n| Prefix       | Resource type  \
  \         |\n|--------------|-------------------------|\n| ABIA | AWS STS service bearer token |\n| ACCA | Context-specific\
  \ credential |\n| AGPA | User group |\n| AIDA | IAM user |\n| AIPA | Amazon EC2 instance profile |\n| AKIA | Access key\
  \ |\n| ANPA | Managed policy |\n| ANVA | Version in a managed policy |\n| APKA | Public key |\n| AROA | Role |\n| ASCA |\
  \ Certificate |\n| ASIA | Temporary (AWS STS) access key |\n\nThe rest of the string is Base32 encoded and can be used to\
  \ recover the account id.\n\n```py\nimport base64\nimport binascii\n\ndef AWSAccount_from_AWSKeyID(AWSKeyID):\n    \n  \
  \  trimmed_AWSKeyID = AWSKeyID[4:] #remove KeyID prefix\n    x = base64.b32decode(trimmed_AWSKeyID) #base32 decode\n   \
  \ y = x[0:6]\n    \n    z = int.from_bytes(y, byteorder='big', signed=False)\n    mask = int.from_bytes(binascii.unhexlify(b'7fffffffff80'),\
  \ byteorder='big', signed=False)\n    \n    e = (z & mask)>>7\n    return (e)\n\n\nprint (\"account id:\" + \"{:012d}\"\
  .format(AWSAccount_from_AWSKeyID(\"ASIAQNZGKIQY56JQ7WML\")))\n```\n\n## Regions\n\n* US Standard - [s3.amazonaws.com](http://s3.amazonaws.com)\n\
  * Ireland - [s3-eu-west-1.amazonaws.com](http://s3-eu-west-1.amazonaws.com)\n* Northern California - [s3-us-west-1.amazonaws.com](http://s3-us-west-1.amazonaws.com)\n\
  * Singapore - [s3-ap-southeast-1.amazonaws.com](http://s3-ap-southeast-1.amazonaws.com)\n* Tokyo - [s3-ap-northeast-1.amazonaws.com](http://s3-ap-northeast-1.amazonaws.com)\n\
  \n## Gaining AWS Console Access via API Keys\n\nA utility to convert your AWS CLI credentials into AWS console access.\n\
  \n* Using [NetSPI/aws_consoler](https://github.com/NetSPI/aws_consoler)\n\n    ```powershell\n    $> aws_consoler -v -a\
  \ AKIA[REDACTED] -s [REDACTED]\n    2020-03-13 19:44:57,800 [aws_consoler.cli] INFO: Validating arguments...\n    2020-03-13\
  \ 19:44:57,801 [aws_consoler.cli] INFO: Calling logic.\n    2020-03-13 19:44:57,820 [aws_consoler.logic] INFO: Boto3 session\
  \ established.\n    2020-03-13 19:44:58,193 [aws_consoler.logic] WARNING: Creds still permanent, creating federated session.\n\
  \    2020-03-13 19:44:58,698 [aws_consoler.logic] INFO: New federated session established.\n    2020-03-13 19:44:59,153\
  \ [aws_consoler.logic] INFO: Session valid, attempting to federate as arn:aws:sts::123456789012:federated-user/aws_consoler.\n\
  \    2020-03-13 19:44:59,668 [aws_consoler.logic] INFO: URL generated!\n    https://signin.aws.amazon.com/federation?Action=login&Issuer=consoler.local&Destination=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3Fregion%3Dus-east-1&SigninToken=[REDACTED]\n\
  \    ```\n\n## References\n\n* [A short note on AWS KEY ID - Tal Be'ery - Oct 27, 2023](https://medium.com/@TalBeerySec/a-short-note-on-aws-key-id-f88cc4317489)\n\
  * [Gaining AWS Console Access via API Keys - Ian Williams - March 18th, 2020](https://blog.netspi.com/gaining-aws-console-access-via-api-keys/)"
_relative_path: cloud/aws/aws-access-token.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-access-token.md
````
