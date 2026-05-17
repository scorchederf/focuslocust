---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# AWS Accounts, Users, Groups, Roles, Policies

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-cloud-aws-accounts-users-groups-roles-policies` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/cloud/aws-accounts-users-groups-roles-policies.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AWS Accounts, Users, Groups, Roles, Policies](../../topics/miscellaneous-reversing-forensics/aws-accounts-users-groups-roles-policies.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-cloud-aws-accounts-users-groups-roles-policies |
| name | AWS Accounts, Users, Groups, Roles, Policies |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/cloud/aws-accounts-users-groups-roles-policies.md |

## Preserved Source Material

```yaml
_asset_filenames:
- image (730).png
_body: "# AWS Accounts, Users, Groups, Roles, Policies\n\nBelow is a graphical representation of the key components of Identity\
  \ Access Mangement in AWS:\n\n![](<../../.gitbook/assets/image (730).png>)\n\n* Organization / root / management account\
  \ can have multiple other accounts\n* An account can have Users, Groups, Roles and Policies\n* Users can be members of Groups\
  \ and Groups can contain Users\n* Role is a secure way to grant termporary permissions to trusted entities:\n  * Another\
  \ AWS account (yours or 3rd party's)\n  * AWS service\n  * Web Identity\n  * SAML Federation\n  * All of the above mentioned\
  \ trusted entities can assume a Role given they have the permission `sts:AssumeRole`\n* Policies signify what can/can't\
  \ be done with resources (i.e EC2 `instance`, `image`, `network interface`, `security group`, etc.). Policies are defined\
  \ as JSON objects\n* Level of access that a User, Group or a Role (identities) has on certain resources, is defined by Policies\
  \ that are attached to said identities"
_relative_path: miscellaneous-reversing-forensics/cloud/aws-accounts-users-groups-roles-policies.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/cloud/aws-accounts-users-groups-roles-policies.md
```
