---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# AWS - Service - Lambda & API Gateway

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-aws-aws-lambda` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-lambda.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AWS - Service - Lambda & API Gateway](../../topics/cloud/aws-service-lambda-and-api-gateway.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-aws-aws-lambda |
| name | AWS - Service - Lambda & API Gateway |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/aws/aws-lambda.md |

## Preserved Source Material

````yaml
_body: "# AWS - Service - Lambda & API Gateway\n\n## List Lambda Functions\n\n```ps1\naws lambda list-functions\n```\n\n###\
  \ Invoke a Lambda Function\n\n```ps1\naws lambda invoke --function-name name response.json --region region \n```\n\n## Extract\
  \ Function's Code\n\n```powershell\naws lambda list-functions --profile uploadcreds\naws lambda get-function --function-name\
  \ \"LAMBDA-NAME-HERE-FROM-PREVIOUS-QUERY\" --query 'Code.Location' --profile uploadcreds\nwget -O lambda-function.zip url-from-previous-query\
  \ --profile uploadcreds\n```\n\n## List API Gateway\n\n```ps1\naws apigateway get-rest-apis\naws apigateway get-rest-api\
  \ --rest-api-id ID\n```\n\n## Listing Information About Endpoints\n\n```ps1\naws apigateway get-resources --rest-api-id\
  \ ID\naws apigateway get-resource --rest-api-id ID --resource-id ID\naws apigateway get-method --rest-api-id ApiID --resource-id\
  \ ID --http-method method\n```\n\n## Listing API Keys\n\n```ps1\naws apigateway get-api-keys --include-values\n```\n\n##\
  \ Getting Information About A Specific Api Key\n\n```ps1\naws apigateway get-api-key --api-key KEY\n```\n\n## References\n\
  \n* [Getting shell and data access in AWS by chaining vulnerabilities - Appsecco - Riyaz Walikar - Aug 29, 2019](https://blog.appsecco.com/getting-shell-and-data-access-in-aws-by-chaining-vulnerabilities-7630fa57c7ed)"
_relative_path: cloud/aws/aws-lambda.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-lambda.md
````
