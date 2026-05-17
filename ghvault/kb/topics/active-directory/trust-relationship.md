---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Trust - Relationship

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-trust-relationship` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/trust-relationship.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

- One-way

## Preserved Body

````markdown
- One-way
    - Domain B trusts A
    - Users in Domain A can access resources in Domain B
    - Users in Domain B cannot access resources in Domain A
- Two-way
    - Domain A trusts Domain B
    - Domain B trusts Domain A
    - Authentication requests can be passed between the two domains in both directions

## Enumerate trusts between domains

- Native `nltest`

  ```powershell
  nltest /trusted_domains
  ```

- PowerShell `GetAllTrustRelationships`

  ```powershell
  ([System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()).GetAllTrustRelationships()

  SourceName          TargetName                    TrustType      TrustDirection
  ----------          ----------                    ---------      --------------
  domainA.local      domainB.local                  TreeRoot       Bidirectional
  ```

- netexec module `enum_trusts`

  ```powershell
  nxc ldap <ip> -u <user> -p <pass> -M enum_trusts 
  ```

## Exploit trusts between domains

:warning: Require a Domain-Admin level access to the current domain.

| Source     | Target  | Technique to use  | Trust relationship  |
|---|---|---|---|
| Root      | Child  | Golden Ticket + Enterprise Admin group (Mimikatz /groups) | Inter Realm (2-way)  |
| Child     | Child  | SID History exploitation (Mimikatz /sids)                 | Inter Realm Parent-Child (2-way)  |
| Child     | Root   | SID History exploitation (Mimikatz /sids)                 | Inter Realm Tree-Root (2-way)  |
| Forest A  | Forest B  | PrinterBug + Unconstrained delegation ?  | Inter Realm Forest or External (2-way)  |

## References

- [External Trusts Are Evil - 14 March 2023 - Charlie Clark (@exploitph)](https://exploit.ph/external-trusts-are-evil.html)
- [Carlos Garcia - Rooted2019 - Pentesting Active Directory Forests public.pdf](https://www.dropbox.com/s/ilzjtlo0vbyu1u0/Carlos%20Garcia%20-%20Rooted2019%20-%20Pentesting%20Active%20Directory%20Forests%20public.pdf?dl=0)
- [Training - Attacking and Defending Active Directory Lab - Altered Security](https://www.alteredsecurity.com/adlab)
````

## Source Verification

[source record](../../sources/internalallthethings/trust-relationship.md)

## Evidence Excerpt

````text
_body: "# Trust - Relationship\n\n- One-way\n    - Domain B trusts A\n    - Users in Domain A can access resources in Domain\
\ B\n    - Users in Domain B cannot access resources in Domain A\n- Two-way\n    - Domain A trusts Domain B\n    - Domain\
\ B trusts Domain A\n    - Authentication requests can be passed between the two domains in both directions\n\n## Enumerate\
\ trusts between domains\n\n- Native `nltest`\n\n  ```powershell\n  nltest /trusted_domains\n  ```\n\n- PowerShell `GetAllTrustRelationships`\n\
\n  ```powershell\n  ([System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()).GetAllTrustRelationships()\n\
\n  SourceName          TargetName                    TrustType      TrustDirection\n  ----------          ----------  \
\                  ---------      --------------\n  domainA.local      domainB.local                  TreeRoot       Bidirectional\n\
\  ```\n\n- netexec module `enum_trusts`\n\n  ```powershell\n  nxc ldap <ip> -u <user> -p <pass> -M enum_trusts \n  ```\n\
````
