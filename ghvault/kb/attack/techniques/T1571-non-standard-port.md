---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1571 - Non-Standard Port

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1571` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may communicate using a protocol and port pairing that are typically not associated. For example, HTTPS over port 8088 or port 587 as opposed to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or muddle analysis/parsing of network data.

Adversaries may also make changes to victim systems to abuse non-standard ports. For example, Registry keys and other configuration settings can be used to modify protocol and port pairings.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Covenant](../../tools/unknown/covenant.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) listeners and controllers can be configured to use non-standard ports.(Citation: Github Covenant) |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can use port 4782 on the compromised host for TCP callbacks.(Citation: CISA AR18-352A Quasar RAT December 2018) |

## Source Verification

[source record](../../sources/mitre/non-standard-port.md)

## Evidence Excerpt

```text
created: '2020-03-14T18:18:32.443Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may communicate using a protocol and port pairing that are typically not associated. For example,
HTTPS over port 8088(Citation: Symantec Elfin Mar 2019) or port 587(Citation: Fortinet Agent Tesla April 2018) as opposed
to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or
muddle analysis/parsing of network data.
Adversaries may also make changes to victim systems to abuse non-standard ports. For example, Registry keys and other configuration
settings can be used to modify protocol and port pairings.(Citation: change_rdp_port_conti)'
```
