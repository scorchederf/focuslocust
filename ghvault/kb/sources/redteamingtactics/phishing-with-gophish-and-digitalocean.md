---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Phishing with GoPhish and DigitalOcean

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-initial-access-phishing-with-gophish-and-digitalocean` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-gophish-and-digitalocean.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Phishing with GoPhish and DigitalOcean](../../topics/offensive-security/phishing-with-gophish-and-digitalocean.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-initial-access-phishing-with-gophish-and-digitalocean |
| name | Phishing with GoPhish and DigitalOcean |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/initial-access/phishing-with-gophish-and-digitalocean.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2019-01-08 22-47.gif
- Screenshot from 2019-01-08 22-37-41.png
- Screenshot from 2019-01-08 22-40-21.png
- Screenshot from 2019-01-08 22-41-09.png
- Screenshot from 2019-01-08 22-45-34.png
- Screenshot from 2019-01-08 22-50-47.png
- Screenshot from 2019-01-08 22-51-21.png
- Screenshot from 2019-01-08 22-56-12.png
- Screenshot from 2019-01-08 23-11-32.png
- Screenshot from 2019-01-09 21-12-51.png
_body: "# Phishing with GoPhish and DigitalOcean\n\nThis lab is dedicated to exploring one of the phishing frameworks GoPhish.\
  \ I will be installing and configuring GoPhish on a DigitalOcean VPS running Ubuntu Linux distribution.\n\n## Configuring\
  \ Environment\n\n### DigitalOcean VPS\n\nThe dropled that I have created got assigned an IP address `68.183.113.176`\n\n\
  Let's login to the VPS and install the mail delivery agent:\n\n{% code title=\"attacker@kali\" %}\n```csharp\nssh root@68.183.113.176\n\
  apt-get install postfix\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-01-09 21-12-51.png>)\n\n\
  Point `mynetworks` variable in postfix config to the IP we got assigned in DigitalOcean:\n\n{% code title=\"attacker@vps\"\
  \ %}\n```csharp\nnano /etc/postfix/main.cf\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-01-08\
  \ 22-37-41.png>)\n\n### Configure DNS Zones\n\nCreate an `A` record `mail` that points to the VPS IP and an `MX` record\
  \ that points to `mail.yourdomain`:\n\n![](<../../.gitbook/assets/Screenshot from 2019-01-08 22-56-12.png>)\n\n### Install\
  \ GoPhish\n\n{% code title=\"attacker@vps\" %}\n```csharp\nwget https://github.com/gophish/gophish/releases/download/0.7.1/gophish-v0.7.1-linux-64bit.zip\n\
  apt install unzip\nunzip gophish-v0.7.1-linux-64bit.zip \nchmod +x gophish\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-01-08 22-40-21.png>)\n\n## Execution\n\nLaunching GoPhish is simple:\n\n{% code title=\"attacker@vps\" %}\n\
  ```csharp\n./gophish\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-01-08 22-41-09.png>)\n\nGoPhish\
  \ admininistration panel is bound to 127.0.0.1:3333 by default, so we can either modify the config and change it to listen\
  \ on 0.0.0.0 (all interfaces) if we want to access the admin panel from the Internet or create a local SSH tunnel if we\
  \ want to restrict access to local network only. Let's do an SSH tunnel:\n\n{% code title=\"attacker@kali\" %}\n```csharp\n\
  ssh root@68.183.113.176 -L3333:localhost:3333 -N -f\n```\n{% endcode %}\n\nWe can now access the GoPhish admin panel via\
  \ `https://127.0.0.1:3333` from our Kali box. After creating user groups (phish targets), landing pages (phishing pages\
  \ victims will see if they click on our phishing links), etc, we can create an email template - the email that will be sent\
  \ to the unsuspecting victims as part of a phishing campaign that we will create in the next step:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-01-08 22-45-34.png>)\n\nBelow is a quick demo of how a new campaign is put together once all the other pieces\
  \ mentioned above are in place (users, templates, landing pages):\n\n![](<../../.gitbook/assets/Peek 2019-01-08 22-47.gif>)\n\
  \n## Receiving the Phish\n\nBelow is the actual end result of our mock phish campaign:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-01-08 22-50-47.png>)\n\nThe URL found in the above phish email takes the user to our mock phishing page:\n\n\
  ![](<../../.gitbook/assets/Screenshot from 2019-01-08 22-51-21.png>)\n\n## Campaign Results\n\nSwitching to `Campaigns`\
  \ section of the admin panel, we can see how many emails were sent as part of the campaign, how many of them were opened\
  \ and how many times the phishing URL was clicked:\n\n![](<../../.gitbook/assets/Screenshot from 2019-01-08 23-11-32.png>)\n\
  \n## References\n\n{% embed url=\"https://docs.getgophish.com/user-guide/building-your-first-campaign/creating-the-template\"\
  \ %}\n\n{% embed url=\"http://www.postfix.org/BASIC_CONFIGURATION_README.html\" %}"
_relative_path: offensive-security/initial-access/phishing-with-gophish-and-digitalocean.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-gophish-and-digitalocean.md
````
