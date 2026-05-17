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

## Summary

ps1

## Preserved Body

````markdown
## List Lambda Functions

```ps1
aws lambda list-functions
```

### Invoke a Lambda Function

```ps1
aws lambda invoke --function-name name response.json --region region 
```

## Extract Function's Code

```powershell
aws lambda list-functions --profile uploadcreds
aws lambda get-function --function-name "LAMBDA-NAME-HERE-FROM-PREVIOUS-QUERY" --query 'Code.Location' --profile uploadcreds
wget -O lambda-function.zip url-from-previous-query --profile uploadcreds
```

## List API Gateway

```ps1
aws apigateway get-rest-apis
aws apigateway get-rest-api --rest-api-id ID
```

## Listing Information About Endpoints

```ps1
aws apigateway get-resources --rest-api-id ID
aws apigateway get-resource --rest-api-id ID --resource-id ID
aws apigateway get-method --rest-api-id ApiID --resource-id ID --http-method method
```

## Listing API Keys

```ps1
aws apigateway get-api-keys --include-values
```

## Getting Information About A Specific Api Key

```ps1
aws apigateway get-api-key --api-key KEY
```

## References

* [Getting shell and data access in AWS by chaining vulnerabilities - Appsecco - Riyaz Walikar - Aug 29, 2019](https://blog.appsecco.com/getting-shell-and-data-access-in-aws-by-chaining-vulnerabilities-7630fa57c7ed)
````

## Source Verification

[source record](../../sources/internalallthethings/aws-service-lambda-and-api-gateway.md)

## Evidence Excerpt

````text
_body: "# AWS - Service - Lambda & API Gateway\n\n## List Lambda Functions\n\n```ps1\naws lambda list-functions\n```\n\n###\
\ Invoke a Lambda Function\n\n```ps1\naws lambda invoke --function-name name response.json --region region \n```\n\n## Extract\
\ Function's Code\n\n```powershell\naws lambda list-functions --profile uploadcreds\naws lambda get-function --function-name\
\ \"LAMBDA-NAME-HERE-FROM-PREVIOUS-QUERY\" --query 'Code.Location' --profile uploadcreds\nwget -O lambda-function.zip url-from-previous-query\
\ --profile uploadcreds\n```\n\n## List API Gateway\n\n```ps1\naws apigateway get-rest-apis\naws apigateway get-rest-api\
\ --rest-api-id ID\n```\n\n## Listing Information About Endpoints\n\n```ps1\naws apigateway get-resources --rest-api-id\
\ ID\naws apigateway get-resource --rest-api-id ID --resource-id ID\naws apigateway get-method --rest-api-id ApiID --resource-id\
\ ID --http-method method\n```\n\n## Listing API Keys\n\n```ps1\naws apigateway get-api-keys --include-values\n```\n\n##\
````
