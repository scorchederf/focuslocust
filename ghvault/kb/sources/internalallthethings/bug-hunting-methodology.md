---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Bug Hunting Methodology

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-methodology-bug-hunting-methodology` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/methodology/bug-hunting-methodology.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bug Hunting Methodology](../../topics/methodology/bug-hunting-methodology.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-methodology-bug-hunting-methodology |
| name | Bug Hunting Methodology |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/methodology/bug-hunting-methodology.md |

## Preserved Source Material

````yaml
_body: "# Bug Hunting Methodology\n\n## Passive Recon\n\n* Using [shodan.io](https://www.shodan.io/), [fofa.info](https://en.fofa.info/),\
  \ [zoomeye.ai](https://www.zoomeye.ai/) or [odin.io](https://search.odin.io/hosts) to detect similar app\n\n  ```ps1\n \
  \ # https://github.com/glennzw/shodan-hq-nse\n  nmap --script shodan-hq.nse --script-args 'apikey=<yourShodanAPIKey>,target=<hackme>'\n\
  \  ```\n\n* Search for similar websites using the same favicon: [pielco11/fav-up](https://github.com/pielco11/fav-up) or\
  \ slightly different icon: [profundis.io/favicon-matcher](https://profundis.io/tools/favicon-matcher)\n\n  ```ps1\n  python3\
  \ favUp.py --favicon-file favicon.ico -sc\n  python3 favUp.py --favicon-url https://domain.behind.cloudflare/assets/favicon.ico\
  \ -sc\n  python3 favUp.py --web domain.behind.cloudflare -s\n  ```\n\n* Search inside Shortener URLs: [shorteners.grayhatwarfare.com](https://shorteners.grayhatwarfare.com/),\
  \ [utkusen/urlhunter](https://github.com/utkusen/urlhunter)\n\n  ```ps1\n  urlhunter --keywords keywords.txt --date 2020-11-20\n\
  \  ```\n\n* Search inside Buckets: [buckets.grayhatwarfare.com](https://buckets.grayhatwarfare.com/)\n\n* Using [The Wayback\
  \ Machine](https://archive.org/web/) to detect forgotten endpoints\n\n  ```powershell\n  # Look for JS files, old links\n\
  \  curl -sX GET \"http://web.archive.org/cdx/search/cdx?url=<targetDomain.com>&output=text&fl=original&collapse=urlkey&matchType=prefix\"\
  \n  ```\n\n* Using [laramies/theHarvester](https://github.com/laramies/theHarvester)\n\n  ```python\n  python theHarvester.py\
  \ -b all -d domain.com\n  ```\n\n* Look for private information in [GitHub](https://github.com) repositories with [michenriksen/GitRob](https://github.com/michenriksen/gitrob.git)\n\
  \n  ```bash\n  gitrob analyze johndoe --site=https://github.acme.com --endpoint=https://github.acme.com/api/v3 --access-tokens=token1,token2\n\
  \  ```\n\n* Perform Google Dorks search: [ikuamike/GoogleDorking.md](https://gist.github.com/ikuamike/c2611b171d64b823c1c1956129cbc055)\n\
  \n  ```ps1\n  site: *.example.com -www\n  intext:\"dhcpd.conf\" \"index of\"\n  intitle:\"SSL Network Extender Login\" -checkpoint.com\n\
  \  ```\n\n* Enumerate subdomains using HackerTarget\n\n  ```ps1\n  curl --silent 'https://api.hackertarget.com/hostsearch/?q=targetdomain.com'\
  \ | grep -o '\\w.*targetdomain.com'\n  ```\n\n* Enumerate endpoints using CommonCrawl\n\n  ```ps1\n  echo \"targetdomain.com\"\
  \ | xargs -I domain curl -s \"http://index.commoncrawl.org/CC-MAIN-2018-22-index?url=*.targetdomain.com&output=json\" |\
  \ jq -r .url | sort -u\n  ```\n\n## Active Recon\n\n### Network Discovery\n\n* Subdomains enumeration\n    * Enumerate already\
  \ found subdomains: [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder), [OWASP/Amass](https://github.com/OWASP/Amass)\n\
  \n    ```ps1\n    subfinder -d hackerone.com\n    amass enum -passive -dir /tmp/amass_output/ -d example.com -o dir/example.com\n\
  \    ```\n\n    * Permutate subdomains: [infosec-au/altdns](https://github.com/infosec-au/altdns)\n    * Bruteforce subdomains:\
  \ [Josue87/gotator](https://github.com/Josue87/gotator)\n    * Resolve subdomains to IP with [blechschmidt/massdns](https://github.com/blechschmidt/massdns),\
  \ remember to use a good list of resolvers like [trickest/resolvers](https://github.com/trickest/resolvers)\n\n    ```ps1\n\
  \    massdns -r resolvers.txt -o S -w massdns.out subdomains.txt\n    ```\n\n    * Subdomain takeovers: [EdOverflow/can-i-take-over-xyz](https://github.com/EdOverflow/can-i-take-over-xyz)\n\
  \n* Network discovery\n    * Scan IP ranges with `nmap`, [robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan)\
  \ and [projectdiscovery/naabu](https://github.com/projectdiscovery/naabu)\n    * Discover services, version and banners\n\
  \n* Review latest acquisitions\n\n* ASN enumeration\n    * [projectdiscovery/asnmap](https://github.com/projectdiscovery/asnmap):\
  \ `asnmap -a AS45596 -silent`\n    * [asnlookup.com](http://www.asnlookup.com)\n\n* DNS Zone Transfer\n\n  ```ps1\n  host\
  \ -t ns domain.local\n  domain.local name server master.domain.local.\n\n  host master.domain.local        \n  master.domain.local\
  \ has address 192.168.1.1\n \n  dig axfr domain.local @192.168.1.1\n  ```\n\n### Web Discovery\n\n#### Common Files\n\n\
  * `security.txt`: A file that provides contact info for reporting security issues with your site (like an email or PGP key).\n\
  \n  ```ps1\n  Contact: mailto:security@example.com\n  ```\n\n* `sitemap.xml`: Lists all the important URLs of your site\
  \ so search engines can index them efficiently.\n\n  ```ps1\n  <urlset>\n    <url><loc>https://example.com/</loc></url>\n\
  \    <url><loc>https://example.com/about</loc></url>\n  </urlset>\n  ```\n\n* `robots.txt`: Tells search engine crawlers\
  \ which pages or files they can or cannot access on your site.\n\n  ```ps1\n  User-agent: *\n  Disallow: /admin/\n  ```\n\
  \n#### Enumerate Files and Folders\n\nEnumerate all accessible files and subdirectories. Once the underlying technology\
  \ has been identified, prioritize the use of targeted wordlists rather than generic ones. Technology specific wordlists\
  \ such as those provided by Assetnote ([https://wordlists.assetnote.io](https://wordlists.assetnote.io)), significantly\
  \ improve coverage and efficiency. Examples include `httparchive_parameters_top_1m_2026_01_27.txt`, `httparchive_directories_1m_2026_01_27.txt`,\
  \ and `httparchive_php_2026_01_27.txt`.\n\n* [OJ/gobuster](https://github.com/OJ/gobuster)\n* [ffuf/ffuf](https://github.com/ffuf/ffuf)\n\
  * [bitquark/shortscan](https://github.com/bitquark/shortscan)\n\n  ```ps1\n  ffuf -H 'User-Agent: Mozilla' -v -t 30 -w mydirfilelist.txt\
  \ -b 'NAME1=VALUE1; NAME2=VALUE2' -u 'https://example.com/FUZZ'\n  gobuster dir -a 'Mozilla' -e -k -l -t 30 -w mydirfilelist.txt\
  \ -c 'NAME1=VALUE1; NAME2=VALUE2' -u 'https://example.com/'\n  ```\n\nIdentify and enumerate backup and temporary files\
  \ that may have been unintentionally exposed. These files often contain source code, credentials, or sensitive configuration\
  \ data and are commonly created by editors, deployment processes, or manual backups.\n\n* [mazen160/bfac](https://github.com/mazen160/bfac)\n\
  \n```bash\nbfac --url http://example.com/test.php --level 4\nbfac --list testing_list.txt\n```\n\nCrawl the website's pages\
  \ and resources to identify additional attack surface and expand the assessment perimeter.\n\n* [hakluke/hakrawler](https://github.com/hakluke/hakrawler)\n\
  * [projectdiscovery/katana](https://github.com/projectdiscovery/katana)\n\n```ps1\nkatana -u https://tesla.com\necho https://google.com\
  \ | hakrawler\n```\n\n#### Next.js Endpoints\n\nIn Next.js, `window.__BUILD_MANIFEST` is a runtime global variable that\
  \ the framework automatically injects into the client-side JavaScript bundle.\n\nGo to `DevTools->Console` and execute this\
  \ JavaScript code:\n\n```js\nconsole.log(window.__BUILD_MANIFEST)\nconsole.log(__BUILD_MANIFEST.sortedPages)\n```\n\nIf\
  \ you inspect your app in the browser console (for a production build), you might see something like this:\n\n```js\n{__rewrites:\
  \ {…}, /: Array(10), /404: Array(8), /500: Array(4), /_error: Array(1), …}\n/: (10) ['static/chunks/2852872c-b605aca0298c2109.js',\
  \ 'static/chunks/3748-2a8cf394c7270ee0.js']\n/404: (8) ['static/chunks/2852872c-b605aca0298c2109.js', 'static/chunks/3748-2a8cf394c7270ee0.js']\n\
  /500: (4) ['static/chunks/3748-2a8cf394c7270ee0.js', 'static/chunks/1221-b44c330d41258365.js']\n/[slug]: (30) ['static/chunks/2852872c-b605aca0298c2109.js',\
  \ 'static/chunks/29107295-4cc022cea922dbb4.js']\n/_error: ['static/chunks/pages/_error-6ddff449d199572c.js']\n/about/[slug]:\
  \ (31) ['static/chunks/2852872c-b605aca0298c2109.js']\n```\n\n#### JS and HTML Comments\n\nRetrieve comments in source code.\n\
  \n```html\n<!-- HTML Comment -->\n// JS Comment\n```\n\n#### Internet Archive\n\nIdentify historical URLs and endpoints\
  \ by reviewing archived content from sources such as the Wayback Machine and the Internet Archive.\n\n* [tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls)\n\
  * [lc/gau](https://github.com/lc/gau)\n\n```ps1\ngau --o example-urls.txt example.com\ngau --blacklist png,jpg,gif example.com\n\
  ```\n\n#### Hidden Parameters\n\nSearch for `hidden` parameters:\n\n* [PortSwigger/param-miner](https://github.com/PortSwigger/param-miner)\n\
  * [s0md3v/Arjun](https://github.com/s0md3v/Arjun)\n* [Sh1Yo/x8](https://github.com/Sh1Yo/x8)\n\n  ```ps1\n  x8 -u \"https://example.com/?something=1\"\
  \ -w <wordlist>\n  ```\n\n#### Map Technologies\n\n* Web service enumeration using [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx)\
  \ or [projectdiscovery/wappalyzergo](https://github.com/projectdiscovery/wappalyzergo)\n    * Favicon hash\n    * JARM fingerprint\n\
  \    * ASN\n    * Status code\n    * Services\n    * Technologies (Github Pages, Cloudflare, Ruby, Nginx,...)\n\n    ```ps1\n\
  \    httpx -title -tech-detect -status-code -follow-redirects -jarm -asn -json -silent -ports 80,443 -l urls.txt\n    ```\n\
  \n* Look for WAF with [projectdiscovery/cdncheck](https://github.com/projectdiscovery/cdncheck) and identify the real IP\
  \ with [christophetd/CloudFlair](https://github.com/christophetd/CloudFlair)\n\n  ```ps1\n  echo www.hackerone.com | cdncheck\
  \ -resp\n  www.hackerone.com [waf] [cloudflare]\n  ```\n\n* Take screenshots for every websites using [sensepost/gowitness](https://github.com/sensepost/gowitness)\n\
  \n#### Manual Testing\n\nExplore the website with a proxy:\n\n* [Caido - A lightweight web security auditing toolkit](https://caido.io/)\n\
  * [ZAP - OWASP Zed Attack Proxy](https://www.zaproxy.org/)\n* [Burp Suite - Community Edition](https://portswigger.net/burp/communitydownload)\n\
  \n#### Automated vulnerability scanners\n\n* [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei):\n\n\
  \  ```ps1\n  nuclei -u https://example.com\n  ```\n\n* [Burp Suite's web vulnerability scanner](https://portswigger.net/burp/vulnerability-scanner)\n\
  * [sullo/nikto](https://github.com/sullo/nikto)\n\n  ```ps1\n  ./nikto.pl -h http://www.example.com\n  ```\n\n## Looking\
  \ for Web Vulnerabilities\n\n* Explore the website and look for vulnerabilities listed in this repository: SQL injection,\
  \ XSS, CRLF, Cookies, ....\n* Test for Business Logic weaknesses\n    * High or negative numerical values\n    * Try all\
  \ the features and click all the buttons\n* [The Web Application Hacker's Handbook Checklist](https://web.archive.org/web/20210126221152/https://gist.github.com/gbedoya/10935137)\n\
  \n* Subscribe to the site and pay for the additional functionality to test\n\n* Inspect Payment functionality - [@gwendallecoguic](https://twitter.com/gwendallecoguic/status/988138794686779392)\n\
  \  > If the webapp you're testing uses an external payment gateway, check the doc to find the test credit numbers, purchase\
  \ something and if the webapp didn't disable the test mode, it will be free\n\n  From [https://stripe.com/docs/testing](https://stripe.com/docs/testing#cards)\
  \ : \"Use any of the following test card numbers, a valid expiration date in the future, and any random CVC number, to create\
  \ a successful payment. Each test card's billing country is set to U.S.\"\n\n  Test card numbers and tokens  \n\n  | NUMBER\
  \           | BRAND          | TOKEN          |\n  | :-------------   | :------------- | :------------- |\n  | 4242424242424242\
  \ | Visa           | tok_visa       |\n  | 4000056655665556 | Visa (debit)   | tok_visa_debit |\n  | 5555555555554444 |\
  \ Mastercard     | tok_mastercard |\n\n  International test card numbers and tokens\n\n  | NUMBER           | TOKEN    \
  \      | COUNTRY        | BRAND          |\n  | :-------------   | :------------- | :------------- | :------------- |\n\
  \  | 4000000400000008 | tok_at         | Austria (AT)   | Visa           |\n  | 4000000560000004 | tok_be         | Belgium\
  \ (BE)   | Visa           |\n  | 4000002080000001 | tok_dk         | Denmark (DK)   | Visa           |\n  | 4000002460000001\
  \ | tok_fi         | Finland (FI)   | Visa           |\n  | 4000002500000003 | tok_fr         | France (FR)    | Visa  \
  \         |\n\n## References\n\n* [Nmap CheatSheet - HackerTarget](https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/)\n\
  * [Yahoo phpinfo.php disclosure - Patrik Fehrenbach - January 20, 2013](https://blog.wss.sh/bugbounty-yahoo-phpinfo-php-disclosure/)\n\
  * [Bug Bounty Masterclass - Wiz, Gal Nagli](https://www.wiz.io/bug-bounty-masterclass)"
_relative_path: methodology/bug-hunting-methodology.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/methodology/bug-hunting-methodology.md
````
