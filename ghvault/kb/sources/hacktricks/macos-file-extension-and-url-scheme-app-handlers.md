---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# macOS File Extension & URL scheme app handlers

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-file-extension-apps` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-file-extension-apps.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [macOS File Extension & URL scheme app handlers](../../topics/macos-hardening/macos-file-extension-and-url-scheme-app-handlers.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-file-extension-apps |
| name | macOS File Extension & URL scheme app handlers |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/macos-hardening/macos-security-and-privilege-escalation/macos-file-extension-apps.md |

## Preserved Source Material

````yaml
_body: "# macOS File Extension & URL scheme app handlers\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## LaunchServices\
  \ Database\n\nThis is a database of all the installed applications in the macOS that can be queried to get information about\
  \ each installed application such as URL schemes it support and MIME types.\n\nIt's possible to dump this datase with:\n\
  \n```\n/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister\
  \ -dump\n```\n\nOr using the tool [**lsdtrip**](https://newosxbook.com/tools/lsdtrip.html).\n\n**`/usr/libexec/lsd`** is\
  \ the brain of the database. It provides **several XPC services** like `.lsd.installation`, `.lsd.open`, `.lsd.openurl`,\
  \ and more. But it also **requires some entitlements** to applications to be able to use the exposed XPC functionalities,\
  \ like `.launchservices.changedefaulthandler` or `.launchservices.changeurlschemehandler` to change default apps for mime\
  \ types or url schemes and others.\n\n**`/System/Library/CoreServices/launchservicesd`** claims the service `com.apple.coreservices.launchservicesd`\
  \ and can be queried to get information about running applications. It can be queried with the system tool /**`usr/bin/lsappinfo`**\
  \ or with [**lsdtrip**](https://newosxbook.com/tools/lsdtrip.html).\n\n## File Extension & URL scheme app handlers\n\nThe\
  \ following line can be useful to find the applications that can open files depending on the extension:\n\n```bash\n/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister\
  \ -dump | grep -E \"path:|bindings:|name:\"\n```\n\nOr use something like [**SwiftDefaultApps**](https://github.com/Lord-Kamina/SwiftDefaultApps):\n\
  \n```bash\n./swda getSchemes #Get all the available schemes\n./swda getApps #Get all the apps declared\n./swda getUTIs #Get\
  \ all the UTIs\n./swda getHandler --URL ftp #Get ftp handler\n```\n\nYou can also check the extensions supported by an application\
  \ doing:\n\n```\ncd /Applications/Safari.app/Contents\ngrep -A3 CFBundleTypeExtensions Info.plist  | grep string\n\t\t\t\
  \t<string>css</string>\n\t\t\t\t<string>pdf</string>\n\t\t\t\t<string>webarchive</string>\n\t\t\t\t<string>webbookmark</string>\n\
  \t\t\t\t<string>webhistory</string>\n\t\t\t\t<string>webloc</string>\n\t\t\t\t<string>download</string>\n\t\t\t\t<string>safariextz</string>\n\
  \t\t\t\t<string>gif</string>\n\t\t\t\t<string>html</string>\n\t\t\t\t<string>htm</string>\n\t\t\t\t<string>js</string>\n\
  \t\t\t\t<string>jpg</string>\n\t\t\t\t<string>jpeg</string>\n\t\t\t\t<string>jp2</string>\n\t\t\t\t<string>txt</string>\n\
  \t\t\t\t<string>text</string>\n\t\t\t\t<string>png</string>\n\t\t\t\t<string>tiff</string>\n\t\t\t\t<string>tif</string>\n\
  \t\t\t\t<string>url</string>\n\t\t\t\t<string>ico</string>\n\t\t\t\t<string>xhtml</string>\n\t\t\t\t<string>xht</string>\n\
  \t\t\t\t<string>xml</string>\n\t\t\t\t<string>xbl</string>\n\t\t\t\t<string>svg</string>\n```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: macos-hardening/macos-security-and-privilege-escalation/macos-file-extension-apps.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-file-extension-apps.md
````
