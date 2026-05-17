---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Dependency Confusion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-dependency-confusion-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Dependency Confusion/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

A dependency confusion attack or supply chain substitution attack occurs when a software installer script is tricked into pulling a malicious code file from a public repository instead of the intended file of the same name from an internal

## Preserved Body

```markdown
> A dependency confusion attack or supply chain substitution attack occurs when a software installer script is tricked into pulling a malicious code file from a public repository instead of the intended file of the same name from an internal repository.

## Tools

* [visma-prodsec/confused](https://github.com/visma-prodsec/confused) - Tool to check for dependency confusion vulnerabilities in multiple package management systems
* [synacktiv/DepFuzzer](https://github.com/synacktiv/DepFuzzer) - Tool used to find dependency confusion or project where owner's email can be takeover.

## Methodology

Look for `npm`, `pip`, `gem` packages, the methodology is the same : you register a public package with the same name of private one used by the company and then you wait for it to be used.

* **DockerHub**: Dockerfile image
* **JavaScript** (npm): package.json
* **MVN** (maven): pom.xml
* **PHP** (composer): composer.json
* **Python** (pypi): requirements.txt

### NPM Example

* List all the packages (ie: package.json, composer.json, ...)
* Find the package missing from [www.npmjs.com](https://www.npmjs.com/)
* Register and create a **public** package with the same name
    * Package example : [0xsapra/dependency-confusion-expoit](https://github.com/0xsapra/dependency-confusion-expoit)

## References

* [Exploiting Dependency Confusion - Aman Sapra (0xsapra) - July 2, 2021](https://web.archive.org/web/20251107024922/https://0xsapra.github.io/website/Exploiting-Dependency-Confusion)
* [Dependency Confusion: How I Hacked Into Apple, Microsoft and Dozens of Other Companies - Alex Birsan - February 9, 2021](https://web.archive.org/web/20210209181139/https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)
* [3 Ways to Mitigate Risk When Using Private Package Feeds - Microsoft - March 29, 2021](https://web.archive.org/web/20210210121930/https://azure.microsoft.com/en-gb/resources/3-ways-to-mitigate-risk-using-private-package-feeds/)
* [$130,000+ Learn New Hacking Technique in 2021 - Dependency Confusion - Bug Bounty Reports Explained - February 22, 2021](https://web.archive.org/web/20210223060107/https://www.youtube.com/watch?v=zFHJwehpBrU)
```

## Source Verification

[source record](../../sources/payloadsallthethings/dependency-confusion.md)

## Evidence Excerpt

```text
_body: "# Dependency Confusion\n\n> A dependency confusion attack or supply chain substitution attack occurs when a software\
\ installer script is tricked into pulling a malicious code file from a public repository instead of the intended file of\
\ the same name from an internal repository.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [NPM\
\ Example](#npm-example)\n* [References](#references)\n\n## Tools\n\n* [visma-prodsec/confused](https://github.com/visma-prodsec/confused)\
\ - Tool to check for dependency confusion vulnerabilities in multiple package management systems\n* [synacktiv/DepFuzzer](https://github.com/synacktiv/DepFuzzer)\
\ - Tool used to find dependency confusion or project where owner's email can be takeover.\n\n## Methodology\n\nLook for\
\ `npm`, `pip`, `gem` packages, the methodology is the same : you register a public package with the same name of private\
\ one used by the company and then you wait for it to be used.\n\n* **DockerHub**: Dockerfile image\n* **JavaScript** (npm):\
```
