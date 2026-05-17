---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# From Misconfigured Certificate Template to Domain Admin

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-from-misconfigured-certificate-template-to-domain-admin` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/from-misconfigured-certificate-template-to-domain-admin.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [From Misconfigured Certificate Template to Domain Admin](../../topics/offensive-security-experiments/from-misconfigured-certificate-template-to-domain-admin.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-experiments-active-directory-kerberos-abuse-from-misconfigured-certificate-template-to-domain-admin |
| name | From Misconfigured Certificate Template to Domain Admin |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security-experiments/active-directory-kerberos-abuse/from-misconfigured-certificate-template-to-domain-admin.md |

## Preserved Source Material

````yaml
_asset_filenames:
- client-authentication.png
- enroll-anyone (1) (1) (1).png
- image (1082).png
- image (1083) (1).png
- image (1085) (1) (1) (1).png
- image (1086) (1) (1).png
- image (1088) (1) (1).png
- suppy-in-request.png
- testing-access.png
- tgt-retrieved.png
- vuln-template.png
_body: "# From Misconfigured Certificate Template to Domain Admin\n\nThis is a quick lab to familiarize with ECS1 privilege\
  \ escalation technique, that illustrates how it's possible to elevate from a regular user to domain administrator in a Windows\
  \ Domain by abusing over-permissioned Active Directory Certificate Services (ADCS) certificate templates.\n\nThis lab is\
  \ based on [Certified Pre-Owned: Abusing Active Directory Certificate Services](https://www.specterops.io/assets/resources/Certified\\\
  _Pre-Owned.pdf) whitepaper by [Will Schroeder](https://twitter.com/harmj0y) and [Lee Christensen](https://twitter.com/tifkin\\\
  _) from [SpecterOps](https://specterops.io/).\n\n## Finding Vulnerable Certificate Templates\n\nOnce in an AD environment,\
  \ we can find vulnerable certificate templates by using `Certify`, a tool released by SpecterOps as part of their research\
  \ mentioned above:\n\n{% code title=\"attacker@target\" %}\n```\ncertify.exe find /vulnerable\n```\n{% endcode %}\n\nBelow\
  \ shows a snippet of the redacted output from `Certify`, that provides information about a vulnerable certificate:\n\n![Vulnerable\
  \ certificate template identified by Certify](../../.gitbook/assets/vuln-template.png)\n\nIn the above screenshot, note\
  \ the following 3 key pieces of information, that tell us that the certificate template is vulnerable and can be abused\
  \ for privilege escalation from regular user to domain administrator:\n\n* `msPKI-Certificates-Name-Flag: ENROLLEE_SUPPLIES_SUBJECT`\
  \ field field, which indicates that the user, who is requesting a new certificate based on this certificate template, can\
  \ request the certificate for another user, meaning any user, including domain administrator user.\\\n  \\\n  Below shows\
  \ the same certificate template setting via GUI when inspecting certificate templates via `certsrv.msc`:\\\n  <img src=\"\
  ../../.gitbook/assets/suppy-in-request.png\" alt=\"\" data-size=\"original\">\\\n\n*   `PkiExtendedKeyUsage: Client Authentication`,\
  \ which indicates that the certificate that will be generated based on this certificate template can be used to authenticate\
  \ to computers in Active Directory.\\\n    \\\n    Below shows the same setting via GUI when inspecting certificate templates\
  \ via `certsrv.msc`:\n\n    <img src=\"../../.gitbook/assets/client-authentication.png\" alt=\"\" data-size=\"original\"\
  >\\\n\n* `Enrollment Rights: NT Authority\\Authenticated Users`, which indicates that any authenticated user in the Active\
  \ Directory is **allowed to request** new certificates to be generated based on this certificate template.\\\n  \\\n  Below\
  \ shows the same setting via GUI when inspecting certificate templates via `certsrv.msc`:\\\n  ![](<../../.gitbook/assets/enroll-anyone\
  \ (1) (1) (1).png>)\n\n## Requesting Certificate with Certify\n\nOnce the vulnerable certificate template has been identified,\
  \ we can request a new certificate on behalf of a domain administator using `Certify` by specifying the following parameters:\n\
  \n* `/ca` - speciffies the Certificate Authority server we're sending the request to;\n* `/template` - specifies the certificate\
  \ template that should be used for generating the new certificate;\n* `/altname` - specifies the AD user for which the new\
  \ certificate should be generated.\n\n{% code title=\"attacker@target\" %}\n```\ncertify.exe request /ca:<$certificateAuthorityHost>\
  \ /template:<$vulnerableCertificateTemplateName> /altname:<$adUserToImpersonate>\n```\n{% endcode %}\n\nBelow shows that\
  \ the certificate in `PEM` format has been issued successfully:\n\n![New certificate was issued off of the vulnerable certificate\
  \ template](<../../.gitbook/assets/image (1086) (1) (1).png>)\n\n## Converting PEM to PFX\n\nAs mentioned above, the certificate\
  \ we just retrieved is in a `PEM` format.&#x20;\n\nTo use it with a tool like `Rubeus` to request a Kerberos Ticket Granting\
  \ Ticket (TGT) for the user for which we minted the certificate, we need to convert the certificate to `PFX` format.\n\n\
  To do this, copy the certificate content printed out by `Rubeus` and paste it to a file called `cert.pem`.&#x20;\n\nThen,\
  \ convert it to `cert.pfx` with Open SSL (in Linux) like so:\n\n{% code title=\"attacker@target\" %}\n```\nopenssl pkcs12\
  \ -in cert.pem -keyex -CSP \"Microsoft Enhanced Cryptographic Provider v1.0\" -export -out cert.pfx\n```\n{% endcode %}\n\
  \n## Requesting TGT with Certificate\n\nOnce we have the certificate in `cert.pfx`, we can request a Kerberos TGT for the\
  \ user for which we minted the new certificate:\n\n{% code title=\"attacker@target\" %}\n```\nRubeus.exe asktgt /user:<$adUserToImpersonate>\
  \ /certificate:cert.pfx /ptt\n```\n{% endcode %}\n\nBelow shows that a new TGT for the target user (Domain Admin in our\
  \ case) using [Rubeus](https://github.com/GhostPack/Rubeus) was requested and injected in to the current logon session (because\
  \ of the `/ptt`):\n\n![Using rubeus to request a TGT for a user for which we minted the certificate](../../.gitbook/assets/tgt-retrieved.png)\n\
  \nAt this point, we can test if we elevated our privileges to domain administrator by listing the administrative `c$` share\
  \ on a server that we don't normally have local administrator privileges on:\n\n![Listing a C$ share to confirm administrator\
  \ access on a server](../../.gitbook/assets/testing-access.png)\n\n## Bonus: Requesting Certificate Manually\n\nThis is\
  \ a bonus section that shows how we can request a new certificate for a targeted user without Rubeus, but with a Certificate\
  \ Signing Request (CSR) file crafted manually and later submitted to Active Directory Certificate Services self-service\
  \ web portal.\n\n### Crafting Certificate Signing Request File\n\nCreate a new file `cert.cnf` with the following contents\
  \ (modify fields as deemed appropriate):\n\n{% code title=\"cert.cnf\" %}\n```\n[ req ]\ndefault_bits       = 2048\ndistinguished_name\
  \ = req_distinguished_name\nreq_extensions     = req_ext\n[ req_distinguished_name ]\ncountryName                 = GB\n\
  stateOrProvinceName         = State or Province Name (full name)\nlocalityName               = Locality Name (eg, city)\n\
  organizationName           = Organization Name (eg, company)\ncommonName                 = Common Name (e.g. server FQDN\
  \ or YOUR name)\n[ req_ext ]\nsubjectAltName = otherName:1.3.6.1.4.1.311.20.2.3;UTF8:$adUserToImpersonate\n```\n{% endcode\
  \ %}\n\nThe most important is line 12, which defines the `subjectAltName` field, which is a `samaccountname` of the user\
  \ in Active Directory, which we want to ultimately impersonate (i.e. domain administrator) for which we will be requesting\
  \ the certificate. \\\n\\\n`Samaccountname` value in this file is defined in the variable `$adUserToImpersonate` - you'd\
  \ need to change it to the administrator's `samaacountname` you want to impersonate.\n\nOnce the `cert.cnf` file is ready,\
  \ generate the actual Certificate Signing Request with `openssl` (in Linux):\n\n```\nopenssl req -out cert-request.csr -newkey\
  \ rsa:2048 -nodes -keyout key.key -config cert.cnf\n```\n\nBelow shows how a base64 encoded Certificate Signing Request\
  \ file `cert-request.csr` was created:\n\n![Certificate Signing Request being generated with open ssl](<../../.gitbook/assets/image\
  \ (1082).png>)\n\nNow, copy the contents of the `cert-request.csr` as we will need it in the last step of this process as\
  \ described below.\n\n### Requesting Certificate via CertSrv Web Portal\n\nNavigate to `https://$adcs/certsrv`, where `$adcs`\
  \ is the Active Directory Certificate Services host and click `Request a certificate`:\n\n![Requesting certificates via\
  \ ADCS web self service portal](<../../.gitbook/assets/image (1088) (1) (1).png>)\n\nClick `advanced certificate request`:\n\
  \n![](<../../.gitbook/assets/image (1083) (1).png>)\n\nFinally, select the vulnerable certificate template you want to base\
  \ your new rogue certificate on, paste the contents of the `cert-request.csr` into the request field and hit `Submit` to\
  \ retrieve the new certificate for your target user:\n\n![Portal for submitting advanced certificate request](<../../.gitbook/assets/image\
  \ (1085) (1) (1) (1).png>)\n\n## References\n\n{% embed url=\"https://posts.specterops.io/certified-pre-owned-d95910965cd2\"\
  \ %}\n\n[Certified Pre-Owned: Abusing Active Directory Certificate Services](https://www.specterops.io/assets/resources/Certified\\\
  _Pre-Owned.pdf)"
_relative_path: offensive-security-experiments/active-directory-kerberos-abuse/from-misconfigured-certificate-template-to-domain-admin.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/from-misconfigured-certificate-template-to-domain-admin.md
````
