---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# CI/CD - BuildKite

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-devops-cicd-buildkite` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-buildkite.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The configuration files for BuildKite builds are located in .buildkite/.yml\

## Preserved Body

````markdown
The configuration files for BuildKite builds are located in `.buildkite/*.yml`\
BuildKite build are often self-hosted, this means that you may gain excessive privileges to the kubernetes cluster that runs the runners, or to the hosting cloud environment.

In order to run an OS command in a workflow that builds pull requests - simply add a `command` instruction to the step.

```yaml
steps:
  - label: "Example Test"
    command: echo "Hello!"
```
````

## Source Verification

[source record](../../sources/internalallthethings/ci-cd-buildkite.md)

## Evidence Excerpt

````text
_body: "# CI/CD - BuildKite\n\nThe configuration files for BuildKite builds are located in `.buildkite/*.yml`\\\nBuildKite\
\ build are often self-hosted, this means that you may gain excessive privileges to the kubernetes cluster that runs the\
\ runners, or to the hosting cloud environment.\n\nIn order to run an OS command in a workflow that builds pull requests\
\ - simply add a `command` instruction to the step.\n\n```yaml\nsteps:\n  - label: \"Example Test\"\n    command: echo \"\
Hello!\"\n```"
_relative_path: devops/cicd-buildkite.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-buildkite.md
````
