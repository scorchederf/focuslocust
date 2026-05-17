---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Wide Source Code Search

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-external-recon-methodology-wide-source-code-search` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/external-recon-methodology/wide-source-code-search.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The goal of this page is to enumerate platforms that allow to search for code (literal or regex) in across thousands/millions of repos in one or more platforms.

## Preserved Body

```markdown
The goal of this page is to enumerate **platforms that allow to search for code** (literal or regex) in across thousands/millions of repos in one or more platforms.

This helps in several occasions to **search for leaked information** or for **vulnerabilities** patterns.

- [**Sourcebot**](https://www.sourcebot.dev/): Open source code search tool. Index and search across thousands of your repos through a modern web interface.
- [**SourceGraph**](https://sourcegraph.com/search): Search in millions of repos. There is a free version and an enterprise version (with 15 days free). It supports regexes. 
- [**Github Search**](https://github.com/search): Search across Github. It supports regexes.
  - Maybe it's also useful to check also [**Github Code Search**](https://cs.github.com/).
- [**Gitlab Advanced Search**](https://docs.gitlab.com/ee/user/search/advanced_search.html): Search across Gitlab projects. Support regexes.
- [**SearchCode**](https://searchcode.com/): Search code in millions of projects.

> [!WARNING]
> When you look for leaks in a repo and run something like `git log -p` don't forget there might be **other branches with other commits** containing secrets!
```

## Source Verification

[source record](../../sources/hacktricks/wide-source-code-search.md)

## Evidence Excerpt

```text
_body: "# Wide Source Code Search\n\n{{#include ../../banners/hacktricks-training.md}}\n\nThe goal of this page is to enumerate\
\ **platforms that allow to search for code** (literal or regex) in across thousands/millions of repos in one or more platforms.\n\
\nThis helps in several occasions to **search for leaked information** or for **vulnerabilities** patterns.\n\n- [**Sourcebot**](https://www.sourcebot.dev/):\
\ Open source code search tool. Index and search across thousands of your repos through a modern web interface.\n- [**SourceGraph**](https://sourcegraph.com/search):\
\ Search in millions of repos. There is a free version and an enterprise version (with 15 days free). It supports regexes.\
\ \n- [**Github Search**](https://github.com/search): Search across Github. It supports regexes.\n  - Maybe it's also useful\
\ to check also [**Github Code Search**](https://cs.github.com/).\n- [**Gitlab Advanced Search**](https://docs.gitlab.com/ee/user/search/advanced_search.html):\
\ Search across Gitlab projects. Support regexes.\n- [**SearchCode**](https://searchcode.com/): Search code in millions\
```
