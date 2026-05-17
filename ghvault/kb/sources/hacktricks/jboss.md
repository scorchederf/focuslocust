---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# JBOSS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-web-jboss` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/jboss.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [JBOSS](../../topics/network-services-pentesting/jboss.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-web-jboss |
| name | JBOSS |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-web/jboss.md |

## Preserved Source Material

```yaml
_body: '# JBOSS


  {{#include ../../banners/hacktricks-training.md}}




  ## Enumeration and Exploitation Techniques


  When assessing the security of web applications, certain paths like _/web-console/ServerInfo.jsp_ and _/status?full=true_
  are key for revealing **server details**. For JBoss servers, paths such as _/admin-console_, _/jmx-console_, _/management_,
  and _/web-console_ can be crucial. These paths might allow access to **management servlets** with default credentials often
  set to **admin/admin**. This access facilitates interaction with MBeans through specific servlets:


  - For JBoss versions 6 and 7, **/web-console/Invoker** is used.

  - In JBoss 5 and earlier versions, **/invoker/JMXInvokerServlet** and **/invoker/EJBInvokerServlet** are available.


  Tools like **clusterd**, available at [https://github.com/hatRiot/clusterd](https://github.com/hatRiot/clusterd), and the
  Metasploit module `auxiliary/scanner/http/jboss_vulnscan` can be used for enumeration and potential exploitation of vulnerabilities
  in JBOSS services.


  ### Exploitation Resources


  To exploit vulnerabilities, resources such as [JexBoss](https://github.com/joaomatosf/jexboss) provide valuable tools.


  ### Finding Vulnerable Targets


  Google Dorking can aid in identifying vulnerable servers with a query like: `inurl:status EJInvokerServlet`




  {{#include ../../banners/hacktricks-training.md}}'
_relative_path: network-services-pentesting/pentesting-web/jboss.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/jboss.md
```
