---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# CI/CD - CircleCI

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-devops-cicd-circle-ci` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-circle-ci.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The configuration files for CircleCI builds are located in .circleci/config.yml\

## Preserved Body

````markdown
The configuration files for CircleCI builds are located in `.circleci/config.yml`\
By default - CircleCI pipelines don't build forked pull requests. It's an opt-in feature that should be enabled by the pipeline owners.

In order to run an OS command in a workflow that builds pull requests - simply add a `run` instruction to the step.

```yaml
jobs:
  build:
    docker:
     - image: cimg/base:2022.05
    steps:
        - run: echo "Say hello to YAML!"
```
````

## Source Verification

[source record](../../sources/internalallthethings/ci-cd-circleci.md)

## Evidence Excerpt

````text
_body: "# CI/CD - CircleCI\n\nThe configuration files for CircleCI builds are located in `.circleci/config.yml`\\\nBy default\
\ - CircleCI pipelines don't build forked pull requests. It's an opt-in feature that should be enabled by the pipeline owners.\n\
\nIn order to run an OS command in a workflow that builds pull requests - simply add a `run` instruction to the step.\n\n\
```yaml\njobs:\n  build:\n    docker:\n     - image: cimg/base:2022.05\n    steps:\n        - run: echo \"Say hello to YAML!\"\
\n```"
_relative_path: devops/cicd-circle-ci.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-circle-ci.md
````
