---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Business Logic Errors

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-business-logic-errors-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Business Logic Errors/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Business Logic Errors](../../topics/business-logic-errors/business-logic-errors.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-business-logic-errors-readme |
| name | Business Logic Errors |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Business%20Logic%20Errors/README.md |

## Preserved Source Material

```yaml
_body: "# Business Logic Errors\n\n> Business logic errors, also known as business logic flaws, are a type of application\
  \ vulnerability that stems from the application's business logic, which is the part of the program that deals with real-world\
  \ business rules and processes. These rules could include things like pricing models, transaction limits, or the sequences\
  \ of operations that need to be followed in a multi-step process.\n\n## Summary\n\n* [Methodology](#methodology)\n    *\
  \ [Review Feature Testing](#review-feature-testing)\n    * [Discount Code Feature Testing](#discount-code-feature-testing)\n\
  \    * [Delivery Fee Manipulation](#delivery-fee-manipulation)\n    * [Currency Arbitrage](#currency-arbitrage)\n    * [Premium\
  \ Feature Exploitation](#premium-feature-exploitation)\n    * [Refund Feature Exploitation](#refund-feature-exploitation)\n\
  \    * [Cart/Wishlist Exploitation](#cartwishlist-exploitation)\n    * [Thread Comment Testing](#thread-comment-testing)\n\
  \    * [Rounding Error](#rounding-error)\n* [References](#references)\n\n## Methodology\n\nUnlike other types of security\
  \ vulnerabilities like SQL injection or cross-site scripting (XSS), business logic errors do not rely on problems in the\
  \ code itself (like unfiltered user input). Instead, they take advantage of the normal, intended functionality of the application,\
  \ but use it in ways that the developer did not anticipate and that have undesired consequences.\n\nCommon examples of Business\
  \ Logic Errors.\n\n### Review Feature Testing\n\n* Assess if you can post a product review as a verified reviewer without\
  \ having purchased the item.\n* Attempt to provide a rating outside of the standard scale, for instance, a 0, 6 or negative\
  \ number in a 1 to 5 scale system.\n* Test if the same user can post multiple ratings for a single product. This is useful\
  \ in detecting potential race conditions.\n* Determine if the file upload field permits all extensions; developers often\
  \ overlook protections on these endpoints.\n* Investigate the possibility of posting reviews impersonating other users.\n\
  * Attempt Cross-Site Request Forgery (CSRF) on this feature, as it's frequently unprotected by tokens.\n\n### Discount Code\
  \ Feature Testing\n\n* Try to apply the same discount code multiple times to assess if it's reusable.\n* If the discount\
  \ code is unique, evaluate for race conditions by applying the same code for two accounts simultaneously.\n* Test for Mass\
  \ Assignment or HTTP Parameter Pollution to see if you can apply multiple discount codes when the application is designed\
  \ to accept only one.\n* Test for vulnerabilities from missing input sanitization such as XSS, SQL Injection on this feature.\n\
  * Attempt to apply discount codes to non-discounted items by manipulating the server-side request.\n\n### Delivery Fee Manipulation\n\
  \n* Experiment with negative values for delivery charges to see if it reduces the final amount.\n* Evaluate if free delivery\
  \ can be activated by modifying parameters.\n\n### Currency Arbitrage\n\n* Attempt to pay in one currency, for example,\
  \ USD, and request a refund in another, like EUR. The difference in conversion rates could result in a profit.\n\n### Premium\
  \ Feature Exploitation\n\n* Explore the possibility of accessing premium account-only sections or endpoints without a valid\
  \ subscription.\n* Purchase a premium feature, cancel it, and see if you can still use it after a refund.\n* Look for true/false\
  \ values in requests/responses that validate premium access. Use tools like Burp's Match & Replace to alter these values\
  \ for unauthorized premium access.\n* Review cookies or local storage for variables validating premium access.\n\n### Refund\
  \ Feature Exploitation\n\n* Purchase a product, ask for a refund, and see if the product remains accessible.\n* Look for\
  \ opportunities for currency arbitrage.\n* Submit multiple cancellation requests for a subscription to check the possibility\
  \ of multiple refunds.\n\n### Cart/Wishlist Exploitation\n\n* Test the system by adding products in negative quantities,\
  \ along with other products, to balance the total.\n* Try to add more of a product than is available.\n* Check if a product\
  \ in your wishlist or cart can be moved to another user's cart or removed from it.\n\n### Thread Comment Testing\n\n* Check\
  \ if there's a limit to the number of comments on a thread.\n* If a user can only comment once, use race conditions to see\
  \ if multiple comments can be posted.\n* If the system allows comments by verified or privileged users, try to mimic these\
  \ parameters and see if you can comment as well.\n* Attempt to post comments impersonating other users.\n\n### Rounding\
  \ Error\n\nThe report [hackerone #176461](https://web.archive.org/web/20170303191338/https://hackerone.com/reports/176461)\
  \ describes a business logic flaw in a cryptocurrency platform (using XBT/Bitcoin), where an attacker exploits a rounding\
  \ error in the internal transfer system to generate money out of nothing.\n\nThe attacker initiate a transfer of 0.000000005\
  \ XBT (0.5 satoshi), this is below the system's minimum precision which is 1 satoshi minimum.\n\n* Sender's balance doesn't\
  \ change. The algorithm might be rounded down to 0 satoshi.\n* Receiver's balance increases by 1 satoshi (0.00000001). The\
  \ algorithm might be rounding up to 1 satoshi.\n\nThe attacker generated 0.00000001 XBT from nothing, since there's no rate\
  \ limit, OTP, or fraud detection, the attacker can automate this process and repeat it infinitely, effectively printing\
  \ money.\n\nIn this example, instead of rounding and rejecting or enforcing a minimum transfer, it ignores the deduction\
  \ from the sender and credits the receiver.\n\n## References\n\n* [Business Logic Vulnerabilities - PortSwigger - March\
  \ 5, 2026](https://web.archive.org/web/20260305155804/https://portswigger.net/web-security/logic-flaws)\n* [Business Logic\
  \ Vulnerability - OWASP - April 22, 2020](https://web.archive.org/web/20200422002600/https://owasp.org/www-community/vulnerabilities/Business_logic_vulnerability)\n\
  * [CWE-840: Business Logic Errors - CWE - March 24, 2011](https://web.archive.org/web/20260304013031/https://cwe.mitre.org/data/definitions/840.html)\n\
  * [Examples of Business Logic Vulnerabilities - PortSwigger - September 22, 2020](https://web.archive.org/web/20200922175829/https://portswigger.net/web-security/logic-flaws/examples)"
_relative_path: Business Logic Errors/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Business Logic Errors/README.md
```
