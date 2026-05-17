---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Debugging Client Side JS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-xss-cross-site-scripting-debugging-client-side-js` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/xss-cross-site-scripting/debugging-client-side-js.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Debugging Client Side JS](../../topics/pentesting-web/debugging-client-side-js.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-xss-cross-site-scripting-debugging-client-side-js |
| name | Debugging Client Side JS |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/xss-cross-site-scripting/debugging-client-side-js.md |

## Preserved Source Material

```yaml
_body: '# Debugging Client Side JS


  {{#include ../../banners/hacktricks-training.md}}


  Debugging client side JS can be a pain because every-time you change the URL (including a change in the params used or param
  values) you need to **reset the breakpoint and reload the page**.


  ### `debugger;`


  If you place the line `debugger;` inside a JS file, when the **browser** executes the JS it will **stop** the **debugger**
  in that place. Therefore, one way to set constant breakpoints would be to **download all the files locally and change set
  breakpoints in the JS code**.


  ### Overrides


  Browser overrides allows to have a local copy of the code that is going to be executed and execute that one instead of the
  one from the remote server.\

  You can **access the overrides** in "Dev Tools" --> "Sources" --> "Overrides".


  You need to **create a local empty folder to be used to store the overrides**, so just create a new local folder and set
  is as override in that page.


  Then, in "Dev Tools" --> "Sources" **select the file** you want to override and with **right click select "Save for overrides"**.


  ![](<../../images/image (742).png>)


  This will **copy the JS file locally** and you will be able to **modify that copy in the browser**. So just add the **`debugger;`**
  command wherever you want, **save** the change and **reload** the page, and every-time you access that web page **your local
  JS copy is going to be loaded** and your debugger command maintained in its place:


  ![](<../../images/image (594).png>)


  ## References


  - [https://www.youtube.com/watch?v=BW\_-RCo9lo8\&t=1529s](https://www.youtube.com/watch?v=BW_-RCo9lo8&t=1529s)


  {{#include ../../banners/hacktricks-training.md}}'
_relative_path: pentesting-web/xss-cross-site-scripting/debugging-client-side-js.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/xss-cross-site-scripting/debugging-client-side-js.md
```
