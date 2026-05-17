---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# SMTP Forwarders / Relays

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-red-team-infrastructure-smtp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/red-team-infrastructure/smtp.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SMTP Forwarders / Relays](../../topics/offensive-security/smtp-forwarders-relays.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-red-team-infrastructure-smtp |
| name | SMTP Forwarders / Relays |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/red-team-infrastructure/smtp.md |

## Preserved Source Material

````yaml
_asset_filenames:
- smtp-relay-droplet.png
- smtp-relay-first-email.png
- smtp-relay-gmail-phish.png
- smtp-relay-header-checks.png
- smtp-relay-headers-relayed.png
- smtp-relay-maila.png
- smtp-relay-mx.png
- smtp-relay-relay-access-denied.png
- smtp-relay-removed-traces.png
- smtp-relay-removed-traces2.png
- smtp-relay-send-phish-like-a-sir.png
- smtp-relay-setting-relay.png
- smtp-relay-test-mail.png
_body: "---\ndescription: SMTP Redirector + Stripping Email Headers\n---\n\n# SMTP Forwarders / Relays\n\n## Setting up Relay\
  \ Mail Server\n\nI am going to set up a mail server that will be later used as an SMTP relay server. First off, a new Ubuntu\
  \ droplet was created in Digital Ocean:\n\n![](../../.gitbook/assets/smtp-relay-droplet.png)\n\nPostfix MTA was installed\
  \ on the droplet with:\n\n```\napt-get install postfix\n```\n\nDuring postfix installation, I set `nodspot.com` as the mail\
  \ name. After the installation, this can be checked/changed here:\n\n```csharp\nroot@ubuntu-s-1vcpu-1gb-sfo2-01:~# cat /etc/mailname\n\
  nodspot.com\n```\n\n## DNS Records\n\nDNS records for nodspot.com has to be updated like so:\n\n![A record pointing to the\
  \ droplet IP](../../.gitbook/assets/smtp-relay-maila.png)\n\n![](../../.gitbook/assets/smtp-relay-mx.png)\n\n## Testing\
  \ Mail Server\n\nOnce postfix is installed and the DNS records are configured, we can test if the mail server is running\
  \ by:\n\n```csharp\ntelnet mail.nodspot.com 25\n```\n\nIf successful, you should see something like this:\n\n![](../../.gitbook/assets/smtp-relay-test-mail.png)\n\
  \nWe can further test if the mail server works by trying to send an actual email like so:\n\n```csharp\nroot@ubuntu-s-1vcpu-1gb-sfo2-01:~#\
  \ sendmail mantvydo@gmail.com\nyolo\n,\n.\n```\n\nSoon enough, the email comes to my gmail:\n\n![](../../.gitbook/assets/smtp-relay-first-email.png)\n\
  \n...with the following headers - all as expected. Note that at this point the originating IP seen in headers is my droplet\
  \ IP 206.189.221.162:\n\n```csharp\nDelivered-To: mantvydo@gmail.com\nReceived: by 2002:a81:1157:0:0:0:0:0 with SMTP id\
  \ 84-v6csp5026946ywr;\n        Tue, 2 Oct 2018 12:22:38 -0700 (PDT)\nX-Google-Smtp-Source: ACcGV62oH69fwYnfV1zg+o+jbTpjQIzIzASmjoIsXbbfvdevE0LlkY32jflNS/acOtNBXiwzxYxP\n\
  X-Received: by 2002:a62:6547:: with SMTP id z68-v6mr17716388pfb.20.1538508158395;\n        Tue, 02 Oct 2018 12:22:38 -0700\
  \ (PDT)\nARC-Seal: i=1; a=rsa-sha256; t=1538508158; cv=none;\n        d=google.com; s=arc-20160816;\n        b=FpEgLAICLn66cI+DDvpIsStUrReQ8fArcreT7FyS8SYcFQXFiK44HDcxwVHXCA8Xxb\n\
  \         fUl+3HcerQEznHZMttZ4pZIMbN18pJS08wzuZdOlhGKAA2JSTkxGd+1PhJwDe1SFTYZc\n         NoARSHL9opemJKg5YqZNjSTDSTfk/QqaCbq7mQL9LAwCKzanGSNR/R/28WymYrdRACOR\n\
  \         GSmDCVvPaUaoemIP8+GwXkfU5Gkk49+F7t9Jbg23HKKq/YOhwF3ryeOEVfn74bhtZIkM\n         QcUzWn5WSL0lIm0nbd2t7677/wcabOg0TCoZj1IHg+I7yLXE7+QZOYX1TguKu16oZeqt\n\
  \         mTIA==\nARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;\n        h=from:date:message-id;\n\
  \        bh=VSFU9fKoMQMmtQzPFdmefDuA+phTpwZXd9k5xGRzwRs=;\n        b=VZ2vHjhPUSs17PXAUDyjYzm0w5sdQYqFx7h9iirh/BF1krrl3MQg4QAgfeo0py9qZH\n\
  \         Xf8/9HmNe1pIgxnZiiZJeVijXeSHCIB4XkG4HYFJY2m/gQ9oZ4JSMfX/Kiw/CXEmbt71\n         YP5S7yQKQNkHw24XnP3WUeDDQ7XvENEfPIS+LlCVtQOPT8fM9TAWQReKz06idynolfhR\n\
  \         7P73wH8igwPea7586wdhSOtDYCURSMKTNVb8yP2eEPNBlP2u2jUrFImG2D2/lke4O6Iu\n         7zu96tCYEY9FVG11dPFheKlMjvMoL4rqPSAQ3zty4Cbi4Vy2Is6f/VF8AYZ34i0FJooj\n\
  \         eEkw==\nARC-Authentication-Results: i=1; mx.google.com;\n       spf=pass (google.com: domain of root@nodspot.com\
  \ designates 206.189.221.162 as permitted sender) smtp.mailfrom=root@nodspot.com\nReturn-Path: <root@nodspot.com>\nReceived:\
  \ from ubuntu-s-1vcpu-1gb-sfo2-01 ([206.189.221.162])\n        by mx.google.com with ESMTP id 38-v6si3160283pgr.237.2018.10.02.12.22.38\n\
  \        for <mantvydo@gmail.com>;\n        Tue, 02 Oct 2018 12:22:38 -0700 (PDT)\nReceived-SPF: pass (google.com: domain\
  \ of root@nodspot.com designates 206.189.221.162 as permitted sender) client-ip=206.189.221.162;\nAuthentication-Results:\
  \ mx.google.com;\n       spf=pass (google.com: domain of root@nodspot.com designates 206.189.221.162 as permitted sender)\
  \ smtp.mailfrom=root@nodspot.com\nReceived: by ubuntu-s-1vcpu-1gb-sfo2-01 (Postfix, from userid 0) id DC6DD3F156; Tue,\n\
  \  2 Oct 2018 19:22:37 +0000 (UTC)\nMessage-Id: <20181002192237.DC6DD3F156@ubuntu-s-1vcpu-1gb-sfo2-01>\nDate: Tue,\n  2\
  \ Oct 2018 19:22:31 +0000 (UTC)\nFrom: root <root@nodspot.com>\n\nyolo\n,\n```\n\n## Setting up Originating Mail Server\n\
  \nWe need to set up the originating mail server that will use the server we set up earlier as a relay server. To achieve\
  \ this, on my attacking machine, I installed postfix mail server.\n\nThe next thing to do is to amend the `/etc/postfix/main.cf`\
  \ and set the `relayhost=nodspot.com`which will make the outgoing emails from the attacking system travel to the nodspot.com\
  \ mail server (the server we set up above) first:\n\n![](../../.gitbook/assets/smtp-relay-setting-relay.png)\n\nOnce the\
  \ change is made and the postfix server is rebooted, we can try sending a test email from the attacking server:\n\n![](../../.gitbook/assets/smtp-relay-send-phish-like-a-sir.png)\n\
  \nIf you do not receive the email, make sure that the relay server is not denying access for the attacking machine. If you\
  \ see your emails getting deferred (on your attacking machine) with the below message, it is exactly what is happening:\n\
  \n![](../../.gitbook/assets/smtp-relay-relay-access-denied.png)\n\nOnce the relay issue is solved, we can repeat the test\
  \ and see a successful relay:\n\n![](../../.gitbook/assets/smtp-relay-gmail-phish.png)\n\nThis time the headers look like\
  \ so:\n\n![](../../.gitbook/assets/smtp-relay-headers-relayed.png)\n\nNote how this time we are observing the originating\
  \ host's details such as a host name and an IP address - this is unwanted and we want to redact that information out.\n\n\
  {% file src=\"../../.gitbook/assets/original_msg (1) (1) (1).txt\" %}\nEmail Headers\n{% endfile %}\n\n## Removing Sensitive\
  \ Headers in Postfix\n\nWe need to make some configuration changes in the relay server in order to redact the headers for\
  \ outgoing emails.\n\nFirst off, let's create a file on the server that contains regular expressions that will hunt for\
  \ the headers that we want removed:\n\n{% code title=\"/etc/postfix/header_checks\" %}\n```csharp\n/^Received:.*/      \
  \        IGNORE\n/^X-Originating-IP:/    IGNORE\n/^X-Mailer:/            IGNORE\n/^Mime-Version:/        IGNORE\n```\n{%\
  \ endcode %}\n\nNext we need to amend the `/etc/postfix/master.cf` to include the following line: `-o header_checks=regexp:/etc/postfix/header_checks`:\n\
  \n![](../../.gitbook/assets/smtp-relay-header-checks.png)\n\nThis will tell the postfix server to remove headers from outgoing\
  \ emails that match regular expressions found in the file we created above.\n\nSave the changes and reload the postfix server:\n\
  \n```\npostmap /etc/postfix/header_checks\npostfix reload\n```\n\nNow send a test email from the attacking machine again\
  \ and inspect the headers of that email:&#x20;\n\n![](../../.gitbook/assets/smtp-relay-removed-traces.png)\n\n![](../../.gitbook/assets/smtp-relay-removed-traces2.png)\n\
  \nNote how the `Received` headers exposing the originating (the attacking) machine were removed, which is exactly what we\
  \ wanted to achieve:\n\n```\nDelivered-To: mantvydo@gmail.com\nReceived: by 2002:a81:1157:0:0:0:0:0 with SMTP id 84-v6csp5668508ywr;\n\
  \        Wed, 3 Oct 2018 03:47:35 -0700 (PDT)\nX-Google-Smtp-Source: ACcGV614wuffoVOsvFkTPPxCiRj0hgFwTIH7y3B4ziIaXfogLFjsoiFyYOdNVChhr+oRcL1axO+a\n\
  X-Received: by 2002:a17:902:a9cc:: with SMTP id b12-v6mr988630plr.198.1538563655360;\n        Wed, 03 Oct 2018 03:47:35\
  \ -0700 (PDT)\nARC-Seal: i=1; a=rsa-sha256; t=1538563655; cv=none;\n        d=google.com; s=arc-20160816;\n        b=qhbzI+R3vHbkqwp2ALOEQ0ItUXU/fA1kEmYln1dBe0CmLELuIfourst4gZVYiU0tAf\n\
  \         sRx20Z5Vcqvv9w6s6f2gVp6crlOuoX2cSKJCn/HyRYKiDB5aVKpEYTDjQtGEBRLoL9xm\n         /T8+3PgV6CHy/KowoPeLugKg3t5mIh9pq+Ig8gG+VVKZcFyvUBJa9YEgBgVKcMwew8H6\n\
  \         x8WzIB2zyavpZLnbIi6SrtheYZAeSTMTwXRutqxZl0n4O/iZS4Y+ZVdRlYeXFXFNdtMK\n         JFaS1XVLR4hYXOzlQT1IC2yeQlqf+Q3FJukmkDlDTgw91ImfZa0HtQYQoo3LwKotp92Q\n\
  \         1HiQ==\nARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;\n        h=from:date:message-id;\n\
  \        bh=hZH42YPrA1C1YyKkQ/LM0S6pyh9p5LGmoqE/s4CGGts=;\n        b=Squ71HtAuuwYHfX+4z63WcgBMoiKbcX5KAQLKwfvlnXuF5QEJNHjfX0GwekViXJIZ5\n\
  \         D2v03648ni6W3/b6uXVoecrtX0MZ9Z/Ck+LxcJRi16toE4QfjR6fhX5l9OSKFjgqkst3\n         Exk9yB1iiX8IAoIvnSaT0pQ5UzOov5Yneti3HO8QbzeCnT1/HieLwIhB/d+znryw1mTQ\n\
  \         jj/VBlNEGFEJhpXjS7cbQFHQEz3yGl1YTSNB3Kxp9T5a7+ncsW3pOAlfKqNYpVywSlBe\n         s6OUSTZ/bEwVYP3dv9aHmbpOIV6rC8uPgUlm+SKYtlj9xiR9uXTtj21IbA0F1esFx+Up\n\
  \         jAQw==\nARC-Authentication-Results: i=1; mx.google.com;\n       spf=pass (google.com: domain of root@nodspot.com\
  \ designates 206.189.221.162 as permitted sender) smtp.mailfrom=root@nodspot.com\nReturn-Path: <root@nodspot.com>\nReceived:\
  \ from ubuntu-s-1vcpu-1gb-sfo2-01 ([206.189.221.162])\n        by mx.google.com with ESMTP id y11-v6si1190446plg.237.2018.10.03.03.47.35\n\
  \        for <mantvydo@gmail.com>;\n        Wed, 03 Oct 2018 03:47:35 -0700 (PDT)\nReceived-SPF: pass (google.com: domain\
  \ of root@nodspot.com designates 206.189.221.162 as permitted sender) client-ip=206.189.221.162;\nAuthentication-Results:\
  \ mx.google.com;\n       spf=pass (google.com: domain of root@nodspot.com designates 206.189.221.162 as permitted sender)\
  \ smtp.mailfrom=root@nodspot.com\nMessage-Id: <20181003104734.1871F42006E@kali>\nDate: Wed,  3 Oct 2018 11:47:28 +0100 (BST)\n\
  From: root <root@nodspot.com>\n\nremoving traces like a sir\n```\n\n{% file src=\"../../.gitbook/assets/headers-removed.txt\"\
  \ %}\nHeaders Removed\n{% endfile %}\n\nThis lab is not going to deal with the emails being marked as phishing by gmail.\
  \ This, however, is related to setting up DKIM, PTR records and the likes, see below for more references.\n\n## References\n\
  \n{% embed url=\"https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-dkim-with-postfix-on-debian-wheezy\"\
  \ %}\n\n{% embed url=\"https://serverfault.com/questions/91954/how-do-i-remove-these-junk-mail-headers\" %}\n\n{% embed\
  \ url=\"https://major.io/2013/04/14/remove-sensitive-information-from-email-headers-with-postfix/\" %}\n\n{% embed url=\"\
  https://www.youtube.com/watch?v=mRUGEygkDEQ\" %}"
_relative_path: offensive-security/red-team-infrastructure/smtp.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/red-team-infrastructure/smtp.md
````
