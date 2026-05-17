---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# macOS Default Sandbox Debug

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-security-protections-macos-sandbox-macos-default-sandbox-debug` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-security-protections/macos-sandbox/macos-default-sandbox-debug.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [macOS Default Sandbox Debug](../../topics/macos-hardening/macos-default-sandbox-debug.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-security-protections-macos-sandbox-macos-default-sandbox-debug |
| name | macOS Default Sandbox Debug |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/macos-hardening/macos-security-and-privilege-escalation/macos-security-protections/macos-sandbox/macos-default-sandbox-debug.md |

## Preserved Source Material

````yaml
_body: "# macOS Default Sandbox Debug\n\n{{#include ../../../../banners/hacktricks-training.md}}\n\nIn this page you can find\
  \ how to create an app to launch arbitrary commands from inside the default macOS sandbox:\n\n1. Compile the application:\n\
  \n```objectivec:main.m\n#include <Foundation/Foundation.h>\n\nint main(int argc, const char * argv[]) {\n    @autoreleasepool\
  \ {\n        while (true) {\n            char input[512];\n\n            printf(\"Enter command to run (or 'exit' to quit):\
  \ \");\n            if (fgets(input, sizeof(input), stdin) == NULL) {\n                break;\n            }\n\n       \
  \     // Remove newline character\n            size_t len = strlen(input);\n            if (len > 0 && input[len - 1] ==\
  \ '\\n') {\n                input[len - 1] = '\\0';\n            }\n\n            if (strcmp(input, \"exit\") == 0) {\n\
  \                break;\n            }\n\n            system(input);\n        }\n    }\n    return 0;\n}\n```\n\nCompile\
  \ it running: `clang -framework Foundation -o SandboxedShellApp main.m`\n\n2. Build the `.app` bundle\n\n```bash\nmkdir\
  \ -p SandboxedShellApp.app/Contents/MacOS\nmv SandboxedShellApp SandboxedShellApp.app/Contents/MacOS/\n\ncat << EOF > SandboxedShellApp.app/Contents/Info.plist\n\
  <?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"\
  >\n<plist version=\"1.0\">\n<dict>\n    <key>CFBundleIdentifier</key>\n    <string>com.example.SandboxedShellApp</string>\n\
  \    <key>CFBundleName</key>\n    <string>SandboxedShellApp</string>\n    <key>CFBundleVersion</key>\n    <string>1.0</string>\n\
  \    <key>CFBundleExecutable</key>\n    <string>SandboxedShellApp</string>\n</dict>\n</plist>\nEOF\n```\n\n3. Define the\
  \ entitlements\n\n{{#tabs}}\n{{#tab name=\"sandbox\"}}\n\n```bash\ncat << EOF > entitlements.plist\n<?xml version=\"1.0\"\
  \ encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"\
  >\n<plist version=\"1.0\">\n<dict>\n    <key>com.apple.security.app-sandbox</key>\n    <true/>\n</dict>\n</plist>\nEOF\n\
  ```\n\n{{#endtab}}\n\n{{#tab name=\"sandbox + downloads\"}}\n\n```bash\ncat << EOF > entitlements.plist\n<?xml version=\"\
  1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"\
  >\n<plist version=\"1.0\">\n<dict>\n    <key>com.apple.security.app-sandbox</key>\n    <true/>\n    <key>com.apple.security.files.downloads.read-write</key>\n\
  \    <true/>\n</dict>\n</plist>\nEOF\n```\n\n{{#endtab}}\n{{#endtabs}}\n\n4. Sign the app (you need to create a certificate\
  \ in the keychain)\n\n```bash\ncodesign --entitlements entitlements.plist -s \"YourIdentity\" SandboxedShellApp.app\n./SandboxedShellApp.app/Contents/MacOS/SandboxedShellApp\n\
  \n# An d in case you need this in the future\ncodesign --remove-signature SandboxedShellApp.app\n```\n\n{{#include ../../../../banners/hacktricks-training.md}}"
_relative_path: macos-hardening/macos-security-and-privilege-escalation/macos-security-protections/macos-sandbox/macos-default-sandbox-debug.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-security-protections/macos-sandbox/macos-default-sandbox-debug.md
````
