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

## Summary

The AWS Command Line Interface (CLI) is a unified tool to manage AWS services from the command line. Using the AWS CLI, you can control multiple AWS services, automate tasks, and manage configurations through profiles.

## Preserved Body

````markdown
The AWS Command Line Interface (CLI) is a unified tool to manage AWS services from the command line. Using the AWS CLI, you can control multiple AWS services, automate tasks, and manage configurations through profiles.

## Set up AWS CLI

Install AWS CLI and configure it for the first time:

```ps1
aws configure
```

This will prompt for:

* AWS Access Key ID
* AWS Secret Access Key
* Default region name
* Default output format

## Creating Profiles

You can configure multiple profiles in `~/.aws/credentials` and `~/.aws/config`.

* `~/.aws/credentials` (stores credentials)

    ```ini
    [default]
    aws_access_key_id = <default-access-key>
    aws_secret_access_key = <default-secret-key>

    [dev-profile]
    aws_access_key_id = <dev-access-key>
    aws_secret_access_key = <dev-secret-key>

    [prod-profile]
    aws_access_key_id = <prod-access-key>
    aws_secret_access_key = <prod-secret-key>
    ```

* `~/.aws/config` (stores region and output settings)

    ```ini
    [default]
    region = us-east-1
    output = json

    [profile dev-profile]
    region = us-west-2
    output = yaml

    [profile prod-profile]
    region = eu-west-1
    output = json
    ```

You can also create profiles via the command line:

```ps1
aws configure --profile dev-profile
```

## Using Profiles

When running AWS CLI commands, you can specify which profile to use by adding the `--profile` flag:

```ps1
aws s3 ls --profile dev-profile
```

If no profile is specified, the **default** profile is used.
````

## Source Verification

[source record](../../sources/internalallthethings/aws-cli.md)

## Evidence Excerpt

````text
_body: "# AWS - CLI\n\nThe AWS Command Line Interface (CLI) is a unified tool to manage AWS services from the command line.\
\ Using the AWS CLI, you can control multiple AWS services, automate tasks, and manage configurations through profiles.\n\
\n## Set up AWS CLI\n\nInstall AWS CLI and configure it for the first time:\n\n```ps1\naws configure\n```\n\nThis will prompt\
\ for:\n\n* AWS Access Key ID\n* AWS Secret Access Key\n* Default region name\n* Default output format\n\n## Creating Profiles\n\
\nYou can configure multiple profiles in `~/.aws/credentials` and `~/.aws/config`.\n\n* `~/.aws/credentials` (stores credentials)\n\
\n    ```ini\n    [default]\n    aws_access_key_id = <default-access-key>\n    aws_secret_access_key = <default-secret-key>\n\
\n    [dev-profile]\n    aws_access_key_id = <dev-access-key>\n    aws_secret_access_key = <dev-secret-key>\n\n    [prod-profile]\n\
\    aws_access_key_id = <prod-access-key>\n    aws_secret_access_key = <prod-secret-key>\n    ```\n\n* `~/.aws/config`\
````
