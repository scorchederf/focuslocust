---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Android Enterprise Work Profile Required-App Replacement

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-mobile-pentesting-android-app-pentesting-android-enterprise-work-profile-bypass` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/mobile-pentesting/android-app-pentesting/android-enterprise-work-profile-bypass.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Android Enterprise Work Profile Required-App Replacement](../../topics/mobile-pentesting/android-enterprise-work-profile-required-app-replacement.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-mobile-pentesting-android-app-pentesting-android-enterprise-work-profile-bypass |
| name | Android Enterprise Work Profile Required-App Replacement |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/mobile-pentesting/android-app-pentesting/android-enterprise-work-profile-bypass.md |

## Preserved Source Material

````yaml
_body: "# Android Enterprise Work Profile Required-App Replacement\n\n{{#include ../../banners/hacktricks-training.md}}\n\n\
  ## Attack surface\n\nAndroid Enterprise Work Profiles are implemented as **secondary Android users** (BYOD example: user\
  \ `0` = personal, user `1` = work). Each user has independent `/data/user/<id>` trees, system apps, Play Services instances\
  \ and policy objects maintained by the MDM. When an MDM such as **Microsoft Intune** marks an app as *required* for the\
  \ Work Profile, the **Work-Profile Play Store (Finsky)** periodically confirms the package is present and auto-installs\
  \ it if missing.\n\nEven after the **CVE-2023-21257** patch that blocks ADB sideloads when `DISALLOW_INSTALL_APPS` or `DISALLOW_DEBUGGING_FEATURES`\
  \ are set, the following chain lets an attacker **replace any Intune-required Work Profile app** with arbitrary code:\n\n\
  1. Abuse Android Studio's **\"Install for all users\"** path to stage a malicious APK that looks like an update of the managed\
  \ package.\n2. Let the MDM notice the required app is missing. Intune triggers the Work-Profile Finsky instance to reinstall\
  \ it.\n3. Finsky compares the staged APK version with the Play Store version and silently installs the **highest `versionCode`**,\
  \ bypassing the original restriction.\n\n## Recon and prerequisite checks\n\n* Confirm multi-user layout and user IDs:\n\
  \n```bash\nadb shell pm list users\n# Expect user 0 = Owner, user 1 = Work profile (or higher if multiple profiles exist)\n\
  ```\n\n* Direct installs into the work user fail under policy (expected error):\n\n```bash\nadb install --user 1 legit.apk\n\
  # java.lang.SecurityException: Shell does not have permission to access user 1\n```\n\n* You must have **temporary physical\
  \ access to an unlocked BYOD** to enable Developer Options + USB debugging.\n* Identify the **package name** of a Work-Profile\
  \ app marked as *required* (e.g. `com.workday.workdroidapp`).\n\n## Weaponising the Android Studio multi-user installer\n\
  \nAndroid Studio's Run/Debug configuration can still push builds with the **`INSTALL_ALL_USERS`** flag. Before running,\
  \ enable *Deploy as instant app* → *Install for all users*.\n\nBuild the malicious payload with the **same package name**\
  \ as the managed app and a **much larger `versionCode`** so PackageManager/Finsky treats it as a newer release:\n\n```gradle\n\
  android {\n    namespace = \"com.workday.workdroidapp\"\n    defaultConfig {\n        applicationId = \"com.workday.workdroidapp\"\
  \n        versionCode = 900000004\n        versionName = \"9000000004.0\"\n    }\n}\n```\n\nWhen Android Studio deploys:\n\
  \n1. **Personal user (0)** installs the malicious package normally.\n2. **Work Profile user (1)** receives the APK in a\
  \ temporary staging area and tries to treat it as an update.\n3. CVE-2023-21257's logic sees the user is restricted → **install\
  \ is denied**, but the legitimate managed app is marked uninstalled and the staged APK remains cached.\n\n## Intune/Finsky\
  \ auto-install bypass\n\nWithin ~1–10 minutes (policy refresh interval):\n\n1. Intune/Company Portal detects the *required*\
  \ package is missing from the Work Profile.\n2. The Work-Profile **Finsky** instance is asked to reinstall it.\n3. During\
  \ version resolution Finsky compares:\n   * Play Store metadata for `com.workday.workdroidapp`.\n   * The locally staged\
  \ APK from the previous install attempt.\n4. Because the local build has the **highest `versionCode`**, Finsky trusts it\
  \ as the most recent release and installs it into the restricted Work Profile **without re-applying `DISALLOW_INSTALL_APPS`\
  \ / `DISALLOW_DEBUGGING_FEATURES` checks**.\n\nThe malicious binary now resides inside the Work Profile under the genuine\
  \ package name and is considered compliant by the MDM.\n\n## Post-exploitation opportunities\n\n* **Work-profile data access**\
  \ – other enterprise apps keep trusting Intents/content providers bound to the replaced package, enabling internal data\
  \ theft and covert exfiltration from the Work Profile to attacker infrastructure.\n* **Per-app VPN hijack** – if the replaced\
  \ package is mapped to an Intune per-app VPN (MS Tunnels + Defender), the malicious build automatically inherits the VPN\
  \ profile, giving direct access to internal hosts from an attacker-controlled process.\n* **Persistence** – because the\
  \ MDM now believes the required app is installed, it will **reinstall the malicious build** whenever the user or defender\
  \ removes it, providing long-term foothold on BYOD Work Profiles.\n\n## References\n\n- [Bypassing CVE-2023-21257 via Intune\
  \ Required-App Auto-Install](https://jgnr.ch/sites/android_enterprise.html)\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: mobile-pentesting/android-app-pentesting/android-enterprise-work-profile-bypass.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/mobile-pentesting/android-app-pentesting/android-enterprise-work-profile-bypass.md
````
