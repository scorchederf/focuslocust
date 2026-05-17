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

## Generated Concept Page

- [Trust - Relationship](../../topics/active-directory/trust-relationship.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-trust-relationship |
| name | Trust - Relationship |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/trust-relationship.md |

## Preserved Source Material

````yaml
_body: "# Trust - Relationship\n\n- One-way\n    - Domain B trusts A\n    - Users in Domain A can access resources in Domain\
  \ B\n    - Users in Domain B cannot access resources in Domain A\n- Two-way\n    - Domain A trusts Domain B\n    - Domain\
  \ B trusts Domain A\n    - Authentication requests can be passed between the two domains in both directions\n\n## Enumerate\
  \ trusts between domains\n\n- Native `nltest`\n\n  ```powershell\n  nltest /trusted_domains\n  ```\n\n- PowerShell `GetAllTrustRelationships`\n\
  \n  ```powershell\n  ([System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()).GetAllTrustRelationships()\n\
  \n  SourceName          TargetName                    TrustType      TrustDirection\n  ----------          ----------  \
  \                  ---------      --------------\n  domainA.local      domainB.local                  TreeRoot       Bidirectional\n\
  \  ```\n\n- netexec module `enum_trusts`\n\n  ```powershell\n  nxc ldap <ip> -u <user> -p <pass> -M enum_trusts \n  ```\n\
  \n## Exploit trusts between domains\n\n:warning: Require a Domain-Admin level access to the current domain.\n\n| Source\
  \     | Target  | Technique to use  | Trust relationship  |\n|---|---|---|---|\n| Root      | Child  | Golden Ticket + Enterprise\
  \ Admin group (Mimikatz /groups) | Inter Realm (2-way)  |\n| Child     | Child  | SID History exploitation (Mimikatz /sids)\
  \                 | Inter Realm Parent-Child (2-way)  |\n| Child     | Root   | SID History exploitation (Mimikatz /sids)\
  \                 | Inter Realm Tree-Root (2-way)  |\n| Forest A  | Forest B  | PrinterBug + Unconstrained delegation ?\
  \  | Inter Realm Forest or External (2-way)  |\n\n## References\n\n- [External Trusts Are Evil - 14 March 2023 - Charlie\
  \ Clark (@exploitph)](https://exploit.ph/external-trusts-are-evil.html)\n- [Carlos Garcia - Rooted2019 - Pentesting Active\
  \ Directory Forests public.pdf](https://www.dropbox.com/s/ilzjtlo0vbyu1u0/Carlos%20Garcia%20-%20Rooted2019%20-%20Pentesting%20Active%20Directory%20Forests%20public.pdf?dl=0)\n\
  - [Training - Attacking and Defending Active Directory Lab - Altered Security](https://www.alteredsecurity.com/adlab)"
_relative_path: active-directory/trust-relationship.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/trust-relationship.md
````
