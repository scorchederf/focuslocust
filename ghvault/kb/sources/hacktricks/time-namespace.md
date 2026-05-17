---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Time Namespace

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-linux-hardening-privilege-escalation-container-security-protections-namespaces-time-namespace` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/linux-hardening/privilege-escalation/container-security/protections/namespaces/time-namespace.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Time Namespace](../../topics/linux-hardening/time-namespace.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-linux-hardening-privilege-escalation-container-security-protections-namespaces-time-namespace |
| name | Time Namespace |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/linux-hardening/privilege-escalation/container-security/protections/namespaces/time-namespace.md |

## Preserved Source Material

````yaml
_body: "# Time Namespace\n\n{{#include ../../../../../banners/hacktricks-training.md}}\n\n## Overview\n\nThe time namespace\
  \ virtualizes selected clocks, especially **`CLOCK_MONOTONIC`** and **`CLOCK_BOOTTIME`**. It is a newer and more specialized\
  \ namespace than mount, PID, network, or user namespaces, and it is rarely the first thing an operator thinks about when\
  \ discussing container hardening. Even so, it is part of the modern namespace family and worth understanding conceptually.\n\
  \nThe main purpose is to let a process observe controlled offsets for certain clocks without changing the host's global\
  \ time view. This is useful for checkpoint/restore workflows, deterministic testing, and some advanced runtime behavior.\
  \ It is not usually a headline isolation control in the same way as mount or user namespaces, but it still contributes to\
  \ making the process environment more self-contained.\n\n## Lab\n\nIf the host kernel and userspace support it, you can\
  \ inspect the namespace with:\n\n```bash\nsudo unshare --time --fork bash\nls -l /proc/self/ns/time /proc/self/ns/time_for_children\n\
  cat /proc/$$/timens_offsets 2>/dev/null\n```\n\nSupport varies by kernel and tool versions, so this page is more about understanding\
  \ the mechanism than expecting it to be visible in every lab environment.\n\n### Time Offsets\n\nLinux time namespaces virtualize\
  \ offsets for `CLOCK_MONOTONIC` and `CLOCK_BOOTTIME`. The current per-namespace offsets are exposed through `/proc/<pid>/timens_offsets`,\
  \ which on supporting kernels can also be modified by a process that holds `CAP_SYS_TIME` inside the relevant namespace:\n\
  \n```bash\nsudo unshare -Tr --mount-proc bash\ncat /proc/$$/timens_offsets\necho \"monotonic 172800000000000\" > /proc/$$/timens_offsets\n\
  cat /proc/uptime\n```\n\nThe file contains nanosecond deltas. Adjusting `monotonic` by two days changes uptime-like observations\
  \ inside that namespace without changing the host wall clock.\n\n### `unshare` Helper Flags\n\nRecent `util-linux` versions\
  \ provide convenience flags that write the offsets automatically:\n\n```bash\nsudo unshare -T --monotonic=\"+24h\" --boottime=\"\
  +7d\" --mount-proc bash\n```\n\nThese flags are mostly a usability improvement, but they also make it easier to recognize\
  \ the feature in documentation and testing.\n\n## Runtime Usage\n\nTime namespaces are newer and less universally exercised\
  \ than mount or PID namespaces. OCI Runtime Specification v1.1 added explicit support for the `time` namespace and the `linux.timeOffsets`\
  \ field, and newer `runc` releases implement that part of the model. A minimal OCI fragment looks like:\n\n```json\n{\n\
  \  \"linux\": {\n    \"namespaces\": [\n      { \"type\": \"time\" }\n    ],\n    \"timeOffsets\": {\n      \"monotonic\"\
  : 86400,\n      \"boottime\": 600\n    }\n  }\n}\n```\n\nThis matters because it turns time namespacing from a niche kernel\
  \ primitive into something that runtimes can request portably.\n\n## Security Impact\n\nThere are fewer classic breakout\
  \ stories centered on the time namespace than on other namespace types. The risk here is usually not that the time namespace\
  \ directly enables escape, but that readers ignore it completely and therefore miss how advanced runtimes may be shaping\
  \ process behavior. In specialized environments, altered clock views can affect checkpoint/restore, observability, or forensic\
  \ assumptions.\n\n## Abuse\n\nThere is usually no direct breakout primitive here, but altered clock behavior can still be\
  \ useful for understanding the execution environment and identifying advanced runtime features:\n\n```bash\nreadlink /proc/self/ns/time\n\
  readlink /proc/self/ns/time_for_children\ndate\ncat /proc/uptime\n```\n\nIf you are comparing two processes, differences\
  \ here can help explain odd timing behavior, checkpoint/restore artifacts, or environment-specific logging mismatches.\n\
  \nImpact:\n\n- almost always reconnaissance or environment understanding\n- useful for explaining logging, uptime, or checkpoint/restore\
  \ anomalies\n- not normally a direct container-escape mechanism by itself\n\nThe important abuse nuance is that time namespaces\
  \ do not virtualize `CLOCK_REALTIME`, so they do not by themselves let an attacker falsify the host wall clock or directly\
  \ break certificate-expiry checks system-wide. Their value is mostly in confusing monotonic-time-based logic, reproducing\
  \ environment-specific bugs, or understanding advanced runtime behavior.\n\n## Checks\n\nThese checks are mostly about confirming\
  \ whether the runtime is using a private time namespace at all.\n\n```bash\nreadlink /proc/self/ns/time                \
  \ # Current time namespace identifier\nreadlink /proc/self/ns/time_for_children    # Time namespace inherited by children\n\
  cat /proc/$$/timens_offsets 2>/dev/null     # Monotonic and boottime offsets when supported\n```\n\nWhat is interesting\
  \ here:\n\n- In many environments these values will not lead to an immediate security finding, but they do tell you whether\
  \ a specialized runtime feature is in play.\n- If you are comparing two processes, differences here may explain confusing\
  \ timing or checkpoint/restore behavior.\n\nFor most container breakouts, the time namespace is not the first control you\
  \ will investigate. Still, a complete container-security section should mention it because it is part of the modern kernel\
  \ model and occasionally matters in advanced runtime scenarios.\n{{#include ../../../../../banners/hacktricks-training.md}}"
_relative_path: linux-hardening/privilege-escalation/container-security/protections/namespaces/time-namespace.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/linux-hardening/privilege-escalation/container-security/protections/namespaces/time-namespace.md
````
