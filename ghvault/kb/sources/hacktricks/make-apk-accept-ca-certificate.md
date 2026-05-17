---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Make APK accept CA certificate

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-mobile-pentesting-android-app-pentesting-make-apk-accept-ca-certificate` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/mobile-pentesting/android-app-pentesting/make-apk-accept-ca-certificate.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Make APK accept CA certificate](../../topics/mobile-pentesting/make-apk-accept-ca-certificate.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-mobile-pentesting-android-app-pentesting-make-apk-accept-ca-certificate |
| name | Make APK accept CA certificate |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/mobile-pentesting/android-app-pentesting/make-apk-accept-ca-certificate.md |

## Preserved Source Material

````yaml
_body: "# Make APK accept CA certificate\n\n{{#include ../../banners/hacktricks-training.md}}\n\nSome applications don't like\
  \ user downloaded certificates, so in order to inspect web traffic for some apps we actually have to decompile the application\
  \ & add a few things & recompile it.\n\n## Automatic\n\nThe tool [**https://github.com/shroudedcode/apk-mitm**](https://github.com/shroudedcode/apk-mitm)\
  \ will **automatically** make the necessary changes to the application to start capturing the requests and will also disable\
  \ certificate pinning (if any).\n\n## Manual\n\nFirst we decompile the app: `apktool d *file-name*.apk`\n\n![](../../images/img9.png)\n\
  \nThen we go into the **Manifest.xml** file & scroll down to the `<\\application android>` tag & we are going to add the\
  \ following line if it isn't already there:\n\n`android:networkSecurityConfig=\"@xml/network_security_config\"`\n\nBefore\
  \ adding:\n\n![](../../images/img10.png)\n\nAfter adding:\n\n![](../../images/img11.png)\n\nNow go into the **res/xml**\
  \ folder & create/modify a file named network_security_config.xml with the following contents:\n\n```html\n<network-security-config>\n\
  \      <base-config>\n            <trust-anchors>\n                <!-- Trust preinstalled CAs -->\n                <certificates\
  \ src=\"system\" />\n                <!-- Additionally trust user added CAs -->\n                <certificates src=\"user\"\
  \ />\n           </trust-anchors>\n      </base-config>\n </network-security-config>\n```\n\nThen save the file & back out\
  \ of all the directories & rebuild the apk with the following command: `apktool b *folder-name/* -o *output-file.apk*`\n\
  \n![](../../images/img12.png)\n\nFinally, you need just to **sign the new application**. [Read this section of the page\
  \ Smali - Decompiling/\\[Modifying\\]/Compiling to learn how to sign it](smali-changes.md#sing-the-new-apk).\n\n{{#include\
  \ ../../banners/hacktricks-training.md}}"
_relative_path: mobile-pentesting/android-app-pentesting/make-apk-accept-ca-certificate.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/mobile-pentesting/android-app-pentesting/make-apk-accept-ca-certificate.md
````
