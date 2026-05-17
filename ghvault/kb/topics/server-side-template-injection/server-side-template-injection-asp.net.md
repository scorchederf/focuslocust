---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Server Side Template Injection - ASP.NET

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-server-side-template-injection-asp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/ASP.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Server-Side Template Injection (SSTI)  is a class of vulnerabilities where an attacker can inject malicious input into a server-side template, causing the template engine to execute arbitrary code on the server. In the context of ASP.NET, S

## Preserved Body

````markdown
> Server-Side Template Injection (SSTI)  is a class of vulnerabilities where an attacker can inject malicious input into a server-side template, causing the template engine to execute arbitrary code on the server. In the context of ASP.NET, SSTI can occur if user input is directly embedded into a template (such as Razor, ASPX, or other templating engines) without proper sanitization.

## ASP.NET Razor

[Official website](https://docs.microsoft.com/en-us/aspnet/web-pages/overview/getting-started/introducing-razor-syntax-c)

> Razor is a markup syntax that lets you embed server-based code (Visual Basic and C#) into web pages.

### ASP.NET Razor - Basic Injection

```powershell
@(1+2)
```

### ASP.NET Razor - Command Execution

```csharp
@{
  // C# code
}
```

## References

- [Server-Side Template Injection (SSTI) in ASP.NET Razor - Clément Notin - April 15, 2020](https://web.archive.org/web/20240905143644/http://clement.notin.org/blog/2020/04/15/Server-Side-Template-Injection-(SSTI)-in-ASP.NET-Razor/)
````

## Source Verification

[source record](../../sources/payloadsallthethings/server-side-template-injection-asp.net.md)

## Evidence Excerpt

````text
_body: "# Server Side Template Injection - ASP.NET\n\n> Server-Side Template Injection (SSTI)  is a class of vulnerabilities\
\ where an attacker can inject malicious input into a server-side template, causing the template engine to execute arbitrary\
\ code on the server. In the context of ASP.NET, SSTI can occur if user input is directly embedded into a template (such\
\ as Razor, ASPX, or other templating engines) without proper sanitization.\n\n## Summary\n\n- [ASP.NET Razor](#aspnet-razor)\n\
\    - [ASP.NET Razor - Basic Injection](#aspnet-razor---basic-injection)\n    - [ASP.NET Razor - Command Execution](#aspnet-razor---command-execution)\n\
- [References](#references)\n\n## ASP.NET Razor\n\n[Official website](https://docs.microsoft.com/en-us/aspnet/web-pages/overview/getting-started/introducing-razor-syntax-c)\n\
\n> Razor is a markup syntax that lets you embed server-based code (Visual Basic and C#) into web pages.\n\n### ASP.NET\
\ Razor - Basic Injection\n\n```powershell\n@(1+2)\n```\n\n### ASP.NET Razor - Command Execution\n\n```csharp\n@{\n  //\
````
