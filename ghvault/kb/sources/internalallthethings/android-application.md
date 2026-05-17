---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Android Application

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-methodology-android-applications` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/methodology/android-applications.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Android Application](../../topics/methodology/android-application.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-methodology-android-applications |
| name | Android Application |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/methodology/android-applications.md |

## Preserved Source Material

````yaml
_body: "# Android Application\n\n## Lab\n\n* [payatu/diva-android](https://github.com/payatu/diva-android) - Damn Insecure\
  \ and vulnerable App for Android\n* [HTB VIP - Pinned](https://app.hackthebox.com/challenges/282) - Hack The Box challenge\n\
  * [HTB VIP - Manager](https://app.hackthebox.com/challenges/283) - Hack The Box challenge\n\n## Extract APK\n\n### ADB Method\n\
  \nConnect to ADB shell and list/download packages.\nYou might need to enable `Developer mode` and `Debugging` in order to\
  \ connect with `adb`\n\n```powershell\nadb shell pm list packages\nadb shell pm path com.example.someapp\nadb pull /data/app/com.example.someapp-2.apk\n\
  ```\n\n### Stores\n\nWarning: Downloading APK files from unofficial stores can compromise your device's security. These\
  \ sources often host malware and malicious software. Always use trusted and official app stores for downloads.\n\n* [Google\
  \ Play](https://play.google.com/store/apps) - Official Store\n* [Apkpure.fr](https://apkpure.fr/fr/) - Alternative to Google\
  \ Play\n* [Apkpure.co](https://apkpure.co) - Alternative to Google Play\n* [Aptoide](https://fr.aptoide.com/) - Alternative\
  \ to Google Play\n* [Aurora Store](https://f-droid.org/fr/packages/com.aurora.store/) - Alternative to Google Play\n\nDownload\
  \ APK from Google Play using a 3rd Party:\n\n* [apkcombo.com](https://apkcombo.com/downloader/)\n* [apps.evozi.com](https://apps.evozi.com/apk-downloader/)\n\
  \n## Static Analysis\n\n### Extract Contents From APK\n\nSearch for strings `flag`,`secret`, the default string file is\
  \ `Resources/resources.arsc/res/values/strings.xml`.\n\n```powershell\napktool d application.apk\n```\n\n### Decompile Data\
  \ as Java Code\n\n* Rename `application.apk` to `application.zip`: `mv application.apk application.zip`\n* Extract `classes.dex`:\
  \ `unzip application.zip`\n* Use `dex2jar` to obtain a jar file: `/usr/bin/d2j-dex2jar classes.dex`\n* Use `jadx` using\
  \ full CPU: `jadx classes.dex -j $(grep -c ^processor /proc/cpuinfo) -d Downloads/app/ > /dev/null`\n\n    ```powershell\n\
  \    jadx-gui\n    --deobf # remove obfuscation by AndroGuard\n    -e      # generate a gradle project for Android Studio\
  \ (easy to find function)\n    ```\n\nTo reverse `.odex` you need to provide the `/system/framework/arm`, fortunately since\
  \ we have the firmware we have it.\n\n```powershell\njava -jar baksmali-2.3.4.jar x application.odex -d k107-mb-8.1/system/framework/arm\
  \ -o application\napktool d application.apk \napktool b rebuild_folder -o rebuilt.apk\n```\n\n### Decompile Native Code\n\
  \nNative library are represented as `.so` files.\nThese libraries by default are included in the APK at the file path `/lib/<cpu>/lib<name>.so`\
  \ or `/assets/<custom_name>`.\n\nUse `IDA`, `Radare2/Cutter` or `Ghidra` to reverse them.\n\n| CPU Native         | Library\
  \ Path                |\n|----------------------|-----------------------------|\n| \"generic\" 32-bit ARM | lib/armeabi/libcalc.so\
  \      |\n| x86                  | lib/x86/libcalc.so          |\n| x64                  | lib/x86_64/libcalc.so       |\n\
  | ARMv7                | lib/armeabi-v7a/libcalc.so  |\n| ARM64                | lib/arm64-v8a/libcalc.so    |\n\n:warning:\
  \ The shared object file (`.so`) doesn't need to be embedded in the app.\n\n### Sign and Package APK\n\n* `apktool` + `jarsigner`\n\
  \n    ```powershell\n    apktool b ./application.apk\n    keytool -genkey -v -keystore application.keystore -alias application\
  \ -keyalg RSA -keysize 2048 -validity 10000\n    jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore application.keystore\
  \ application.apk application\n    zipalign -v 4 application.apk application-signed.apk\n    ```\n\n* `apktool` + `signapk`\n\
  \n    ```powershell\n    apktool b app-release\n    ./signapk app-release/dist/app-release.apk\n    ```\n\n* [patrickfav/uber-apk-signer](https://github.com/patrickfav/uber-apk-signer)\
  \ (Linux only)\n\n    ```powershell\n    java -jar uber-apk-signer.jar --apks /path/to/apks\n    ```\n\n* [APK Toolkit v1.3](https://xdaforums.com/t/tool-apk-toolkit-v1-3-windows.4572881/)\
  \ (Windows only)\n\n### Mobile Security Framework Static\n\n> Mobile Security Framework (MobSF) is an automated, all-in-one\
  \ mobile application (Android/iOS/Windows) pen-testing, malware analysis and security assessment framework capable of performing\
  \ static and dynamic analysis.\n\n* [MobSF - Documentation](https://mobsf.github.io/docs/#/)\n* [MobSF - Github](https://github.com/MobSF/Mobile-Security-Framework-MobSF)\n\
  * [MobSF - Live Demo](https://mobsf.live/)\n\nRun [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)\n\
  \n* Latest version from DockerHub\n\n    ```powershell\n    docker run -it --name mobsf -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest\n\
  \    ```\n\n* Enable persistence on the Docker container\n\n    ```powershell\n    docker run -it --rm --name mobsf -p 8000:8000\
  \ -v <your_local_dir>:/root/.MobSF opensecurity/mobile-security-framework-mobsf:latest\n    ```\n\n### Online Assets\n\n\
  :warning: Uploading APKs to uncontrolled websites risks data leaks, malware, intellectual property theft, and privacy violations.\
  \ Use trusted platforms only to ensure the security and integrity of your app.\n\n* [appetize.io](https://appetize.io/)\
  \ - Instantly run mobile apps in your browser\n* [mobsf.live](https://mobsf.live/) - Demo version of MobSF\n* [hybrid-analysis.com](https://www.hybrid-analysis.com/sample/573df0b1cb5ffc0a25306be5ec83483ed1b2acdba37dd93223b9f14f42b2fdea?environmentId=200)\
  \ - Sandbox analysis of APK files\n\n### React Native and Hermes\n\nIdentify React Native app with `index.android.bundle`\
  \ inside the `assets` folder\n\n```ps1\nHermes: pip install hbctool\n╰─$ hbctool disasm index.android.bundle indexasm\n\
  [*] Disassemble 'index.android.bundle' to 'indexasm' path\n[*] Hermes Bytecode [ Source Hash: 4013cb75f7e16d4474f5cf258edc45ee16585560,\
  \ HBC Version: 74 ]\n[*] Done\n```\n\n### Flutter\n\nIndentify Flutter use in the `MANIFEST.MF` and search for `libflutter.so`.\n\
  \n* [worawit/blutter](https://github.com/worawit/blutter) - Flutter Mobile Application Reverse Engineering Tool\n\n    ```ps1\n\
  \    blutter jadx/resources/lib/arm64-v8a/ ./blutter_output\n    ```\n\n## Dynamic Analysis\n\nDynamic analysis for Android\
  \ malware involves executing and monitoring an app in a controlled environment to observe its behavior. This technique detects\
  \ malicious activities like data exfiltration, unauthorized access, and system modifications. Additionally, it aids in reverse\
  \ engineering app features, revealing hidden functionalities and potential vulnerabilities for better threat mitigation.\n\
  \n### Burp Suite\n\n* Proxy > Listen to all interfaces\n* Import/Export CA certificate\n* `adb push burp.der /sdcard/burp.crt`\n\
  * Open the Settings on the device and search \"Install Cert\"\n* Click Install certificates from SD card\n* Configure the\
  \ AVD to use the proxy\n\n```ps1\n# Convert Burp certificate for Android\nopenssl x509 -inform DER -in burp.der -out burp.pem\n\
  openssl x509 -inform PEM -subject_hash_old -in burp.pem |head -1\nmv burp.pem <hash output>.0\n\n# Push the certificate\
  \ in the AVD\nemulator -list-avds\nemulator -avd Pentesting_Device -writable-system\nadb root\nadb remount\nadb push <hash>.0\
  \ /sdcard/\n\n# Change the permissions\nadb shell\nmv /sdcard/<hash>.0 /system/etc/security/cacerts/\nchmod 644 /system/etc/security/cacerts/<hash>.0\n\
  chown root:root /system/etc/security/cacerts/<hash>.0\n```\n\n### Frida\n\n* [Frida - Documentation](https://frida.re/docs/android)\n\
  * [Frida - Github](https://github.com/frida/frida/)\n\nDownload [`frida`](https://github.com/frida/frida/releases) from\
  \ releases.\n\n```ps1\npip install frida-tools\nunxz frida-server.xz\nadb root # might be required\nadb push frida-server\
  \ /data/local/tmp/\nadb shell \"chmod 755 /data/local/tmp/frida-server\"\nadb shell \"/data/local/tmp/frida-server &\"\n\
  ```\n\nInteresting Frida scripts:\n\n* [Universal Android SSL Pinning Bypass with Frida](https://codeshare.frida.re/@pcipolloni/universal-android-ssl-pinning-bypass-with-frida/)\
  \ -  `frida --codeshare pcipolloni/universal-android-ssl-pinning-bypass-with-frida -f YOUR_BINARY`\n* [frida-multiple-unpinning](https://codeshare.frida.re/@akabe1/frida-multiple-unpinning/)\
  \ - `frida --codeshare akabe1/frida-multiple-unpinning -f YOUR_BINARY`\n* [aesinfo](https://codeshare.frida.re/@dzonerzy/aesinfo/)\
  \ - `frida --codeshare dzonerzy/aesinfo -f YOUR_BINARY`\n* [fridantiroot](https://codeshare.frida.re/@dzonerzy/fridantiroot/)\
  \ - `frida --codeshare dzonerzy/fridantiroot -f YOUR_BINARY`\n* [anti-frida-bypass](https://codeshare.frida.re/@enovella/anti-frida-bypass/)\
  \ - `frida --codeshare enovella/anti-frida-bypass -f YOUR_BINARY`\n* [xamarin-antiroot](https://codeshare.frida.re/@Gand3lf/xamarin-antiroot/)\
  \ - `frida --codeshare Gand3lf/xamarin-antiroot -f YOUR_BINARY`\n* [Intercept Android APK Crypto Operations](https://codeshare.frida.re/@fadeevab/intercept-android-apk-crypto-operations/)\
  \ - `frida --codeshare fadeevab/intercept-android-apk-crypto-operations -f YOUR_BINARY`\n* [Android Location Spoofing](https://codeshare.frida.re/@dzervas/android-location-spoofing/)\
  \ - `frida --codeshare dzervas/android-location-spoofing -f YOUR_BINARY`\n* [java-crypto-viewer](https://codeshare.frida.re/@Serhatcck/java-crypto-viewer/)\
  \ - `frida --codeshare Serhatcck/java-crypto-viewer -f YOUR_BINARY`\n\n### Runtime Mobile Security\n\n> Runtime Mobile Security\
  \ (RMS) \U0001F4F1\U0001F525 - is a powerful web interface that helps you to manipulate Android and iOS Apps at Runtime\n\
  \n* [RMS - Github](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security)\n\n**Requirements**:\n\n* `adb`\n* `frida`:\
  \ server up and running on the target device\n\nIn case of issue with your favorite Browser, please use Google Chrome (fully\
  \ supported).\n\n* Install RMS\n\n    ```powershell\n    npm install -g rms-runtime-mobile-security\n    ```\n\n* Make sure\
  \ `frida-server` is up and running on the target device.\n* Launch RMS: `rms`\n* Open your browser at `http://127.0.0.1:5491/`\n\
  * Attach to the app, find name with `adb shell pm list package | grep NAME`\n\n### Genymotion\n\nGenymotion is a robust\
  \ Android emulator designed for developers, offering fast and reliable virtual devices for app testing. It features GPS,\
  \ battery, and network simulation, enabling comprehensive testing and development\n\n* [Genymotion](https://www.genymotion.com/)\n\
  * [Genymotion Desktop](https://www.genymotion.com/product-desktop/)\n* [Genymotion Device Image](https://www.genymotion.com/product-device-image/)\n\
  * [Genymotion SaaS](https://www.genymotion.com/product-cloud/)\n\n### Android SDK emulator\n\nAndroid Virtual Device (AVD)\
  \ without Google Play Store.\n\n* Download the files for an API 25 build\n\n    ```powershell\n    sdkmanager \"system-images;android-25;google_apis;x86_64\"\
  \n    ```\n\n* Create a device based on what we downloaded previously\n\n    ```powershell\n    avdmanager create avd x86_64_api_25\
  \ -k \"system-images;android-25;google_apis;x86_64\"\n    ```\n\n* Run the emulator\n\n    ```powershell\n    emulator @x86_64_api_25\n\
  \n    emulator -list-avds\n    emulator -avd <non_production_avd_name> -writable-system -no-snapshot\n    emulator -avd\
  \ Pixel_XL_API_31 -writable-system -http-proxy 127.0.0.1:8080\n    ```\n\n* Install the APK\n\n    ```powershell\n    adb\
  \ install ./challenge.apk\n    ```\n\n* Start the App\n\n    ```powershell\n    adb shell monkey -p com.scottyab.rootbeer.sample\
  \ 1\n    ```\n\n### Mobile Security Framework Dynamic\n\n:warning: Dynamic Analysis will not work if you use MobSF docker\
  \ container or setup MobSF inside a Virtual Machine.\n\n**Requirements**:\n\n* Genymotion (Supports x86_64 architecture\
  \ Android 4.1 - 11.0, upto API 30)\n    * Android 5.0 - 11.0 - uses Frida and works out of the box with zero configuration\
  \ or setup.\n    * Android 4.1 - 4.4 - uses Xposed Framework and requires MobSFy\n* Genymotion Cloud\n    * [Amazon Marketplace\
  \ - TCP 5555](https://aws.amazon.com/marketplace/seller-profile?id=933724b4-d35f-4266-905e-e52e4792bc45)\n    * [Azure Marketplace\
  \ - TCP 5555](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/genymobile.genymotion-cloud)\n* Android Studio\
  \ Emulator (only Android images upto API 28 are supported)\n    * AVD without Google Play Store\n\nDynamic Analysis from\
  \ MobSF grants you the following features:\n\n* Web API Viewer\n* Frida API Monitor\n\n### Appium\n\nAppium is an open-source\
  \ project and ecosystem of related software, designed to facilitate UI automation of many app platforms, including mobile\
  \ (iOS, Android, Tizen), browser (Chrome, Firefox, Safari), desktop (macOS, Windows), TV (Roku, tvOS, Android TV, Samsung),\
  \ and more!\n\n* Install appium: `npm install -g appium`\n* Install and validate the `uiautomator2` driver\n\n    ```ps1\n\
  \    export JAVA_HOME=/usr/lib/jvm/default-java\n    export ANDROID_HOME=/home/user/Android/Sdk/\n    wget https://github.com/google/bundletool/releases/download/1.17.1/bundletool-all-1.17.1.jar\n\
  \    sudo mv bundletool-all-1.17.1.jar /usr/local/bin\n    appium driver install uiautomator2\n    appium driver doctor\
  \ uiautomator2\n    ```\n\n* Start the server on the default host (0.0.0.0) and port (4723): `appium server`\n* Install\
  \ the Appium Python client: `pip install Appium-Python-Client`\n* Use the [appium/appium-inspector](https://github.com/appium/appium-inspector)\
  \ with the following capability\n\n    ```json\n    {\n    \"platformName\": \"Android\",\n    \"appium:automationName\"\
  : \"UiAutomator2\"\n    }\n    ```\n\nExamples:\n\n* [quickstarts/py/test.py](https://github.com/appium/appium/blob/master/packages/appium/sample-code/quickstarts/py/test.py)\n\
  * [quickstarts/js/test.js](https://github.com/appium/appium/blob/master/packages/appium/sample-code/quickstarts/js/test.js)\n\
  * [quickstarts/js/test.rb](https://github.com/appium/appium/blob/master/packages/appium/sample-code/quickstarts/rb/test.rb)\n\
  \n### Flutter\n\nRepackage a Flutter Android application to allow Burp Suite proxy interception.\n\n* [ptswarm/reFlutter](https://github.com/ptswarm/reFlutter)\
  \ - Flutter Reverse Engineering Framework\n\n    ```ps1\n    pip3 install reflutter\n    reflutter application.apk\n   \
  \ ```\n\n* Sign the apk with [patrickfav/uber-apk-signer](https://github.com/patrickfav/uber-apk-signer/releases/tag/v1.2.1)\n\
  \n    ```ps1\n    java -jar ./uber-apk-signer-1.3.0.jar --apks release.apk\n    java -jar ./uber-apk-signer.jar --allowResign\
  \ -a release.RE.apk\n    ```\n\nAn alternative way to do it is using a rooted Android device with `zygisk-reflutter`.\n\n\
  * [yohanes/zygisk-reflutter](https://github.com/yohanes/zygisk-reflutter) - Zygisk-based reFlutter (Rooted Android with\
  \ Magisk installed and Zygisk Enabled)\n\n    ```ps1\n    adb push  zygiskreflutter_1.0.zip /sdcard/\n    adb shell su -c\
  \ magisk --install-module /sdcard/zygiskreflutter_1.0.zip\n    adb reboot\n    ```\n\n## SSL Pinning Bypass\n\nSSL certificate\
  \ pinning in an APK involves embedding a server's public key or certificate directly into the app. This ensures the app\
  \ only trusts specific certificates, preventing man-in-the-middle attacks by rejecting any certificates not matching the\
  \ pinned ones, even if they are otherwise valid.\n\n:warning: Android 9.0 is changing the defaults for Network Security\
  \ Configuration to block all cleartext traffic.\n\n* [shroudedcode/apk-mitm](https://github.com/shroudedcode/apk-mitm) -\
  \ A CLI application that automatically prepares Android APK files for HTTPS inspection\n\n    ```powershell\n    $ npx apk-mitm\
  \ application.apk\n    npx: 139 installé(s) en 12.206s\n    ╭ apk-mitm v0.6.1\n    ├ apktool v2.4.1\n    ╰ uber-apk-signer\
  \ v1.1.0\n    Using temporary directory:\n    /tmp/87d3a4921ddf86cde634205480f89e90\n    ✔ Decoding APK file\n    ✔ Modifying\
  \ app manifest\n    ✔ Modifying network security config\n    ✔ Disabling certificate pinning\n    ✔ Encoding patched APK\
  \ file\n    ✔ Signing patched APK file\n    Done!  Patched file: ./application.apk\n    ```\n\n* [51j0/Android-CertKiller](https://github.com/51j0/Android-CertKiller)\
  \ - An automation script to bypass SSL/Certificate pinning in Android\n\n    ```powershell\n    python main.py -w #(Wizard\
  \ mode)\n    python main.py -p 'root/Desktop/base.apk' #(Manual mode)\n    ```\n\n* [frida/frida](https://github.com/frida/frida)\
  \ - Universal SSL Pinning Bypass\n\n    ```javascript\n    $ adb devices\n    $ adb root\n    $ adb shell\n    $ phone:/#\
  \ ./frida-server\n\n    // https://codeshare.frida.re/@pcipolloni/universal-android-ssl-pinning-bypass-with-frida/\n   \
  \ $ frida -U --codeshare pcipolloni/universal-android-ssl-pinning-bypass-with-frida -f com.example.pinned\n\n    $ frida\
  \ -U -f org.package.name -l universal-ssl-check-bypass.js --no-pause\n    Java.perform(function() {                \n  \
  \      var array_list = Java.use(\"java.util.ArrayList\");\n        var ApiClient = Java.use('com.android.org.conscrypt.TrustManagerImpl');\n\
  \        ApiClient.checkTrustedRecursive.implementation = function(a1,a2,a3,a4,a5,a6) {\n            var k = array_list.$new();\
  \ \n            return k;\n        }\n    },0);\n    ```\n\n* [m0bilesecurity/RMS-Runtime-Mobile-Security](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security)\
  \ - Certificate Pinning bypass script (all + okhttpv3)\n* [federicodotta/Brida](https://github.com/federicodotta/Brida)\
  \ - The new bridge between Burp Suite and Frida\n\n## Root Detection Bypass\n\nCommon root detection techniques:\n\n* Su\
  \ binaries: `su`/`busybox`\n* Known Root Files/Paths : `Superuser.apk`\n* Root Management Apps: `Magisk`, `SuperSU`\n* RW\
  \ paths:  `/system`, `/data` directories\n* System Properties\n\nCommon bypass:\n\n* [fridantiroot](https://codeshare.frida.re/@dzonerzy/fridantiroot/)\
  \ - `frida --codeshare dzonerzy/fridantiroot -f YOUR_BINARY`\n* [xamarin-antiroot](https://codeshare.frida.re/@Gand3lf/xamarin-antiroot/)\
  \ - `frida --codeshare Gand3lf/xamarin-antiroot -f YOUR_BINARY`\n* [multiple-root-detection-bypass/](https://codeshare.frida.re/@KishorBal/multiple-root-detection-bypass/)\
  \ - `frida --codeshare KishorBal/multiple-root-detection-bypass -f YOUR_BINARY`\n\n## Android Debug Bridge\n\nAndroid Debug\
  \ Bridge (ADB) is a versatile command-line tool that enables communication between a computer and an Android device. It\
  \ facilitates tasks like installing apps, debugging, accessing the device's shell, and transferring files, making it essential\
  \ for developers and power users in Android development and troubleshooting.\n\n### USB Debugging\n\n* Open the **Settings**\
  \ app.\n* Select **System**.\n* Scroll to the bottom and select **About phone**.\n* Scroll to the bottom and tap **Build\
  \ number** 7 times.\n* Return to the previous screen to find **Developer options** near the bottom.\n* Scroll down and enable\
  \ **USB debugging**.\n\n```ps1\n./platform-tools/adb connect IP:PORT\n./platform-tools/adb shell\n```\n\n### Wireless Debugging\n\
  \n* Open the **Settings** app.\n* Select **System**.\n* Scroll to the bottom and select **About phone**.\n* Scroll to the\
  \ bottom and tap **Build number** 7 times.\n* Return to the previous screen to find **Developer options** near the bottom.\n\
  * Scroll down and enable **Wifi debugging**.\n* Click on **Wifi debugging** to access the settings\n\nOne more step, you\
  \ need to pair the devices using a code.\n\n```ps1\n./platform-tools/adb pair IP:PORT CODE\n./platform-tools/adb connect\
  \ IP:PORT\n./platform-tools/adb shell\n```\n\n| Command                      | Description                             \
  \       |\n|------------------------------|------------------------------------------------|\n| `adb devices`          \
  \      | List devices                                   |\n| `adb connect <IP>:<PORT>`    | Connect to a remote device \
  \                    |\n| `adb install app.apk`        | Install application                            |\n| `adb uninstall\
  \ app.apk`      | Uninstall application                          |\n| `adb root`                   | Restarting adbd as\
  \ root                        |\n| `adb shell pm list packages` | List packages                                  |\n| `adb\
  \ shell pm list packages -3` | Show third party packages                   |\n| `adb shell pm list packages -f` | Show packages\
  \ and associated files          |\n| `adb shell pm clear com.test.abc` | Delete all data associated with a package |\n|\
  \ `adb pull <remote> <local>`  | Download file                                  |\n| `adb push <local> <remote>`  | Upload\
  \ file                                    |\n| `adb shell screenrecord /sdcard/demo.mp4`| Record video of the screen   \
  \      |\n| `adb shell am start -n com.test.abc` | Start an activity                      |\n| `adb shell am startservice`\
  \ | Start a service                                |\n| `adb shell am broadcast`    | Send a broadcast                 \
  \              |\n| `adb logcat *:D`             | Show log with Debug level                      |\n| `adb logcat -c` \
  \             | Clears the entire log                          |\n\n## Android Virtual Device\n\nAn Android Virtual Device\
  \ (AVD) is an emulator configuration that mimics a physical Android device. It allows developers to test and run Android\
  \ apps in a simulated environment with specific hardware profiles, screen sizes, and Android versions, facilitating app\
  \ testing without needing actual devices.\n\n```ps1\nemulator -avd Pixel_8_API_34 -writable-system\n```\n\n| Command   \
  \                   | Description                                    |\n|------------------------------|------------------------------------------------|\n\
  | `-tcpdump /path/dumpfile.cap`| Capture all the traffic in a file |\n| `-dns-server X.X.X.X`        | Set DNS servers |\n\
  | `-http-proxy X.X.X.X:8080`   | Set HTTP proxy |\n| `-port 5556`                 | Set the ADB TCP port number |\n\n##\
  \ Unlock Bootloader\n\n**Requirements**:\n\n* Enable `Settings` > `Developer Options` > `OEM unlocking`\n* Enable `Settings`\
  \ > `Developer Options` > `USB Debugging`\n\nUnlock the bootloader will wipe the userdata partition. On some device these\
  \ methods will require a key to successfully unlock the bootloader.\n\n* Method 1\n\n    ```ps1\n    adb reboot bootloader\n\
  \    fastboot oem unlock\n    ```\n\n* Method 2\n\n    ```ps1\n    adb reboot bootloader\n    fastboot flashing unlock\n\
  \    ```\n\n* Methods based on the chip\n    * For Qualcomm devices, you can use EDL (Emergency Download Mode)\n    * For\
  \ MediaTek devices, BROM (Boot ROM) mode\n    * For Unisoc devices, Research Download Mode.\n\n## References\n\n* [A beginners\
  \ guide to using Frida to bypass root detection. - DianaOpanga - November 27, 2023](https://medium.com/@dianaopanga/a-beginners-guide-to-using-frida-to-bypass-root-detection-16af76b989ac)\n\
  * [Android App Reverse Engineering 101 - @maddiestone](https://www.ragingrock.com/AndroidAppRE/)\n* [Android app vulnerability\
  \ classes - Google Play Protect](https://static.googleusercontent.com/media/www.google.com/fr//about/appsecurity/play-rewards/Android_app_vulnerability_classes.pdf)\n\
  * [Appium documentation](https://appium.io/docs/en/latest/)\n* [Configuring Android Emulator with Burp Suite - Jarrod @Jrod_R87\
  \ - January 8, 2025](https://owlhacku.com/configuring-android-emulator-with-burp-suite/)\n* [Configuring Burp Suite with\
  \ Android Emulators - Aashish Tamang - June 6, 2022](https://blog.yarsalabs.com/setting-up-burp-for-android-application-testing/)\n\
  * [Configuring Burp Suite With Android Nougat - ropnop - January 18, 2018](https://blog.ropnop.com/configuring-burp-suite-with-android-nougat)\n\
  * [Configuring Frida with BurpSuite and Genymotion to bypass Android SSL Pinning - arben - September 4, 2020](https://spenkk.github.io/bugbounty/Configuring-Frida-with-Burp-and-GenyMotion-to-bypass-SSL-Pinning/)\n\
  * [How to root an Android device for analysis and vulnerability assessment - Joe Lovett - August 23, 2024](https://www.pentestpartners.com/security-blog/how-to-root-an-android-device-for-analysis-and-vulnerability-assessment/)\n\
  * [Intercepting OkHttp at Runtime With Frida - A Practical Guide - Szymon Drosdzol - January 22, 2026](https://blog.doyensec.com/2026/01/22/frida-instrumentation.html)\n\
  * [Introduction to Android Pentesting - Jarrod - July 8, 2024](https://owlhacku.com/introduction-to-android-pentesting/)\n\
  * [Mobile Systems and Smartphone Security - @reyammer](https://mobisec.reyammer.io)\n* [Rooting an Android Emulator for\
  \ Mobile Security Testing - 8ksecresearch - April 17, 2025](https://8ksec.io/rooting-an-android-emulator-for-mobile-security-testing/)"
_relative_path: methodology/android-applications.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/methodology/android-applications.md
````
