---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# AWS - Service - S3 Buckets

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-aws-aws-s3-bucket` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-s3-bucket.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AWS - Service - S3 Buckets](../../topics/cloud/aws-service-s3-buckets.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-aws-aws-s3-bucket |
| name | AWS - Service - S3 Buckets |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/aws/aws-s3-bucket.md |

## Preserved Source Material

````yaml
_body: "# AWS - Service - S3 Buckets\n\nAn AWS S3 bucket is a cloud-based storage container that holds files, known as objects,\
  \ which can be accessed over the internet. It is highly scalable and can store large amounts of data, such as documents,\
  \ images, and backups. S3 provides robust security through access control, encryption, and permissions management. It ensures\
  \ high durability and availability, making it ideal for storing and retrieving data from anywhere.\n\n## Tools\n\n* [aws/aws-cli](https://github.com/aws/aws-cli)\
  \ - Universal Command Line Interface for Amazon Web Services\n\n ```ps1\n sudo apt install awscli\n ```\n\n* [digi.ninja/bucket-finder](https://digi.ninja/projects/bucket_finder.php)\
  \ - Search for public buckets, list and download all files if directory indexing is enabled\n\n ```powershell\n wget https://digi.ninja/files/bucket_finder_1.1.tar.bz2\
  \ -O bucket_finder_1.1.tar.bz2\n ./bucket_finder.rb my_words\n ./bucket_finder.rb --region ie my_words\n ./bucket_finder.rb\
  \ --download --region ie my_words\n ./bucket_finder.rb --log-file bucket.out my_words\n ```\n\n* [aws-sdk/boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)\
  \ - Amazon Web Services (AWS) SDK for Python\n\n ```python\n import boto3\n s3 = boto3.client('s3',aws_access_key_id='AKIAJQDP3RKREDACTED',aws_secret_access_key='igH8yFmmpMbnkcUaCqXJIRIozKVaREDACTED',region_name='us-west-1')\n\
  \n try:\n  result = s3.list_buckets()\n  print(result)\n except Exception as e:\n  print(e)\n ```\n\n* [nccgroup/s3_objects_check](https://github.com/nccgroup/s3_objects_check)\
  \ - Whitebox evaluation of effective S3 object permissions, to identify publicly accessible files\n\n    ```powershell\n\
  \    python3 -m venv env && source env/bin/activate\n    pip install -r requirements.txt\n    python s3-objects-check.py\
  \ -h\n    python s3-objects-check.py -p whitebox-profile -e blackbox-profile\n    ```\n\n* [grayhatwarfare/buckets](https://buckets.grayhatwarfare.com/)\
  \ - Search Public Buckets\n\n## Credentials and Profiles\n\nCreate a profile with your `AWSAccessKeyId` and `AWSSecretKey`,\
  \ then you can use `--profile nameofprofile` in the `aws` command.\n\n```js\naws configure --profile nameofprofile\nAWS\
  \ Access Key ID [None]: <AWSAccessKeyId>\nAWS Secret Access Key [None]: <AWSSecretKey>\nDefault region name [None]: \nDefault\
  \ output format [None]: \n```\n\nAlternatively you can use environment variables instead of creating a profile.\n\n```bash\n\
  export AWS_ACCESS_KEY_ID=ASIAZ[...]PODP56\nexport AWS_SECRET_ACCESS_KEY=fPk/Gya[...]4/j5bSuhDQ\nexport AWS_SESSION_TOKEN=FQoGZXIvYXdzE[...]8aOK4QU=\n\
  ```\n\n## Public S3 Bucket\n\nAn open S3 bucket refers to an Amazon Simple Storage Service (Amazon S3) bucket that has been\
  \ configured to allow public access, either intentionally or by mistake. This means that anyone on the internet could potentially\
  \ access, read, or even modify the data stored in the bucket, depending on the permissions set.\n\n* `http://s3.amazonaws.com/<bucket-name>`\n\
  * `http://<bucket-name>.s3.amazonaws.com`\n* `https://<bucket-name>.region.amazonaws.com/<file>`\n\nAWS S3 buckets name\
  \ examples: [http://flaws.cloud.s3.amazonaws.com](http://flaws.cloud.s3.amazonaws.com).\n\nEither bruteforce the buckets\
  \ name with keyword related to your target or search through the leaked one using OSINT tool such as [buckets.grayhatwarfare.com](https://buckets.grayhatwarfare.com/).\n\
  \nWhen file listing is enabled, the name is also displayed inside the `<Name>` XML tag.\n\n```xml\n<ListBucketResult xmlns=\"\
  http://s3.amazonaws.com/doc/2006-03-01/\">\n<Name>adobe-REDACTED-REDACTED-REDACTED</Name>\n```\n\n## Bucket Interations\n\
  \n### Find the Region\n\nTo find the region of an Amazon Web Services (AWS) service (such as an S3 bucket) using dig or\
  \ nslookup, query the DNS records for the service's domain or endpoint.\n\n```bash\n$ dig flaws.cloud\n;; ANSWER SECTION:\n\
  flaws.cloud.    5    IN    A    52.218.192.11\n\n$ nslookup 52.218.192.11\nNon-authoritative answer:\n11.192.218.52.in-addr.arpa\
  \ name = s3-website-us-west-2.amazonaws.com.\n```\n\n### List Files\n\nTo list files in an AWS S3 bucket using the AWS CLI,\
  \ you can use the following command:\n\n```bash\naws s3 ls <target> [--options]\naws s3 ls s3://bucket-name --no-sign-request\
  \ --region <insert-region-here>\naws s3 ls s3://flaws.cloud/ --no-sign-request --region us-west-2\n```\n\n### Copy, Upload\
  \ and Download Files\n\n* **Copy**\n\n ```bash\n aws s3 cp <source> <target> [--options]\n aws s3 cp local.txt s3://bucket-name/remote.txt\
  \ --acl authenticated-read\n aws s3 cp login.html s3://bucket-name --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers\n\
  \ ```\n\n* **Upload**\n\n ```bash\n aws s3 mv <source> <target> [--options]\n aws s3 mv test.txt s3://hackerone.files\n\
  \ SUCCESS : \"move: ./test.txt to s3://hackerone.files/test.txt\"\n ```\n\n* **Download**\n\n ```bash\n aws s3 sync <source>\
  \ <target> [--options]\n aws s3 sync s3://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/ . --no-sign-request --region\
  \ us-west-2\n ```\n\n### List File Versions\n\nWhen versioning is enabled in an AWS S3 bucket, list file history using the\
  \ AWS CLI:\n\n```bash\naws s3api list-object-versions --bucket <bucket-name> [--options]\naws s3api list-object-versions\
  \ --bucket <bucket-name> --prefix <file-path>\n```\n\n### Download a Specific File Version\n\n```bash\naws s3api get-object\
  \ --bucket <bucket-name> --key <source> --version-id <id> <target>\n```\n\n## References\n\n* [There's a Hole in 1,951 Amazon\
  \ S3 Buckets - Mar 27, 2013 - Rapid7 willis](https://community.rapid7.com/community/infosec/blog/2013/03/27/1951-open-s3-buckets)\n\
  * [Bug Bounty Survey - AWS Basic test](https://web.archive.org/web/20180808181450/https://twitter.com/bugbsurveys/status/860102244171227136)\n\
  * [flaws.cloud Challenge based on AWS vulnerabilities - Scott Piper - Summit Route](http://flaws.cloud/)\n* [flaws2.cloud\
  \ Challenge based on AWS vulnerabilities - Scott Piper - Summit Route](http://flaws2.cloud)\n* [Guardzilla video camera\
  \ hardcoded AWS credential - INIT_6 - December 27, 2018](https://blackmarble.sh/guardzilla-video-camera-hard-coded-aws-credentials/)\n\
  * [AWS PENETRATION TESTING PART 1. S3 BUCKETS - VirtueSecurity](https://www.virtuesecurity.com/aws-penetration-testing-part-1-s3-buckets/)\n\
  * [AWS PENETRATION TESTING PART 2. S3, IAM, EC2 - VirtueSecurity](https://www.virtuesecurity.com/aws-penetration-testing-part-2-s3-iam-ec2/)\n\
  * [A Technical Analysis of the Capital One Hack - CloudSploit - Aug 2 2019](https://blog.cloudsploit.com/a-technical-analysis-of-the-capital-one-hack-a9b43d7c8aea?gi=8bb65b77c2cf)"
_relative_path: cloud/aws/aws-s3-bucket.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-s3-bucket.md
````
