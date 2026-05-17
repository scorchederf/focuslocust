---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Attack one-way trusted domain/forest (Trust account attack)

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-attack-one-way-trust` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/attack-one-way-trust.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

If an attacker has administrative access to FORESTB which trusts FORESTA, the attacker can obtain the credentials for a trust account located in FORESTA. This account is a member of Domain Users in FORESTA through its Primary Group. As we s

## Preserved Body

```markdown
If an attacker has administrative access to FORESTB which trusts FORESTA, the attacker can obtain the credentials for a _trust account_ located in FORESTA. This account is a member of Domain Users in FORESTA through its Primary Group. As we see too often, Domain Users membership is all that is necessary to identify and use other techniques and attack paths to become Domain Admin.

![](<https://images.squarespace-cdn.com/content/v1/5bbb4a7301232c6e6c8757fa/61a0233f-edd8-40b6-b6ae-8592a29875bd/Picture3.png>)

This technique is not limited to forest trust but works over any domain/forest one-way trust in the direction trusting -> trusted. 

The trust protections (SID filtering, disabled SID history, and disabled TGT delegation) do not mitigate the technique.

[Read more](https://improsec.com/tech-blog/sid-filter-as-security-boundary-between-domains-part-7-trust-account-attack-from-trusting-to-trusted)
```

## Source Verification

[source record](../../sources/redteamingtactics/attack-one-way-trusted-domain-forest-trust-account-attack.md)

## Evidence Excerpt

```text
_asset_filenames: []
_body: "# Attack one-way trusted domain/forest (Trust account attack)\nIf an attacker has administrative access to FORESTB\
\ which trusts FORESTA, the attacker can obtain the credentials for a _trust account_ located in FORESTA. This account is\
\ a member of Domain Users in FORESTA through its Primary Group. As we see too often, Domain Users membership is all that\
\ is necessary to identify and use other techniques and attack paths to become Domain Admin.\n\n![](<https://images.squarespace-cdn.com/content/v1/5bbb4a7301232c6e6c8757fa/61a0233f-edd8-40b6-b6ae-8592a29875bd/Picture3.png>)\n\
\nThis technique is not limited to forest trust but works over any domain/forest one-way trust in the direction trusting\
\ -> trusted. \n\nThe trust protections (SID filtering, disabled SID history, and disabled TGT delegation) do not mitigate\
\ the technique.\n\n[Read more](https://improsec.com/tech-blog/sid-filter-as-security-boundary-between-domains-part-7-trust-account-attack-from-trusting-to-trusted)"
```
