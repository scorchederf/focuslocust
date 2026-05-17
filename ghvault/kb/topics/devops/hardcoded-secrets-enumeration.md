---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Hardcoded Secrets Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-devops-secrets-enumeration` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/secrets-enumeration.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

synacktiv/nord-stream - List the secrets stored inside CI/CD environments and extract them by deploying malicious pipelines

## Preserved Body

````markdown
## Tools

* [synacktiv/nord-stream](https://github.com/synacktiv/nord-stream) - List the secrets stored inside CI/CD environments and extract them by deploying malicious pipelines
* [xforcered/SCMKit](https://github.com/xforcered/SCMKit) - Source Code Management Attack Toolkit

## Search inside Repositories, Files and Codes

* Discover repositories being used in a particular SCM system

    ```ps1
    SCMKit.exe -s gitlab -m listrepo -c userName:password -u https://gitlab.something.local
    SCMKit.exe -s gitlab -m listrepo -c apiKey -u https://gitlab.something.local
    ```

* Search for repositories by repository name in a particular SCM system

    ```ps1
    SCMKit.exe -s github -m searchrepo -c userName:password -u https://github.something.local -o "some search term"
    SCMKit.exe -s gitlab -m searchrepo -c apikey -u https://gitlab.something.local -o "some search term"
    ```

* Search for code containing a given keyword in a particular SCM system

    ```ps1
    SCMKit.exe -s github -m searchcode -c userName:password -u https://github.something.local -o "some search term"
    SCMKit.exe -s github -m searchcode -c apikey -u https://github.something.local -o "some search term"
    ```

* Search for files in repositories containing a given keyword in the file name in a particular SCM system

    ```ps1
    SCMKit.exe -s gitlab -m searchfile -c userName:password -u https://gitlab.something.local -o "some search term"
    SCMKit.exe -s gitlab -m searchfile -c apikey -u https://gitlab.something.local -o "some search term"
    ```

* List snippets owned by the current user in GitLab

    ```ps1
    SCMKit.exe -s gitlab -m listsnippet -c userName:password -u https://gitlab.something.local
    SCMKit.exe -s gitlab -m listsnippet -c apikey -u https://gitlab.something.local
    ```

## References

* [CI/CD SECRETS EXTRACTION, TIPS AND TRICKS - Hugo Vincent, Théo Louis-Tisserand - 01/03/2023](https://www.synacktiv.com/publications/cicd-secrets-extraction-tips-and-tricks.html)
````

## Source Verification

[source record](../../sources/internalallthethings/hardcoded-secrets-enumeration.md)

## Evidence Excerpt

````text
_body: "# Hardcoded Secrets Enumeration\n\n## Tools\n\n* [synacktiv/nord-stream](https://github.com/synacktiv/nord-stream)\
\ - List the secrets stored inside CI/CD environments and extract them by deploying malicious pipelines\n* [xforcered/SCMKit](https://github.com/xforcered/SCMKit)\
\ - Source Code Management Attack Toolkit\n\n## Search inside Repositories, Files and Codes\n\n* Discover repositories being\
\ used in a particular SCM system\n\n    ```ps1\n    SCMKit.exe -s gitlab -m listrepo -c userName:password -u https://gitlab.something.local\n\
\    SCMKit.exe -s gitlab -m listrepo -c apiKey -u https://gitlab.something.local\n    ```\n\n* Search for repositories\
\ by repository name in a particular SCM system\n\n    ```ps1\n    SCMKit.exe -s github -m searchrepo -c userName:password\
\ -u https://github.something.local -o \"some search term\"\n    SCMKit.exe -s gitlab -m searchrepo -c apikey -u https://gitlab.something.local\
\ -o \"some search term\"\n    ```\n\n* Search for code containing a given keyword in a particular SCM system\n\n    ```ps1\n\
````
