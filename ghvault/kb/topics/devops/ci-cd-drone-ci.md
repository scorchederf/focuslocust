---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# CI/CD - Drone CI

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-devops-cicd-drone-ci` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-drone-ci.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The configuration files for Drone builds are located in .drone.yml\

## Preserved Body

````markdown
The configuration files for Drone builds are located in `.drone.yml`\
Drone build are often self-hosted, this means that you may gain excessive privileges to the kubernetes cluster that runs the runners, or to the hosting cloud environment.

In order to run an OS command in a workflow that builds pull requests - simply add a `commands` instruction to the step.

```yaml
steps:
  - name: do-something
    image: some-image:3.9
    commands:
      - {Payload}
```
````

## Source Verification

[source record](../../sources/internalallthethings/ci-cd-drone-ci.md)

## Evidence Excerpt

````text
_body: "# CI/CD - Drone CI\n\nThe configuration files for Drone builds are located in `.drone.yml`\\\nDrone build are often\
\ self-hosted, this means that you may gain excessive privileges to the kubernetes cluster that runs the runners, or to\
\ the hosting cloud environment.\n\nIn order to run an OS command in a workflow that builds pull requests - simply add a\
\ `commands` instruction to the step.\n\n```yaml\nsteps:\n  - name: do-something\n    image: some-image:3.9\n    commands:\n\
\      - {Payload}\n```"
_relative_path: devops/cicd-drone-ci.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-drone-ci.md
````
