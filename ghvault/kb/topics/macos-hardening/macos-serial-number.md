---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# macOS Serial Number

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-macos-hardening-macos-red-teaming-macos-mdm-macos-serial-number` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-red-teaming/macos-mdm/macos-serial-number.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Apple devices post-2010 have serial numbers consisting of 12 alphanumeric characters, each segment conveying specific information:

## Preserved Body

```markdown
## Basic Information

Apple devices post-2010 have serial numbers consisting of **12 alphanumeric characters**, each segment conveying specific information:

- **First 3 Characters**: Indicate the **manufacturing location**.
- **Characters 4 & 5**: Denote the **year and week of manufacture**.
- **Characters 6 to 8**: Serve as a **unique identifier** for each device.
- **Last 4 Characters**: Specify the **model number**.

For instance, the serial number **C02L13ECF8J2** follows this structure.

### **Manufacturing Locations (First 3 Characters)**

Certain codes represent specific factories:

- **FC, F, XA/XB/QP/G8**: Various locations in the USA.
- **RN**: Mexico.
- **CK**: Cork, Ireland.
- **VM**: Foxconn, Czech Republic.
- **SG/E**: Singapore.
- **MB**: Malaysia.
- **PT/CY**: Korea.
- **EE/QT/UV**: Taiwan.
- **FK/F1/F2, W8, DL/DM, DN, YM/7J, 1C/4H/WQ/F7**: Different locations in China.
- **C0, C3, C7**: Specific cities in China.
- **RM**: Refurbished devices.

### **Year of Manufacturing (4th Character)**

This character varies from 'C' (representing the first half of 2010) to 'Z' (second half of 2019), with different letters indicating different half-year periods.

### **Week of Manufacturing (5th Character)**

Digits 1-9 correspond to weeks 1-9. Letters C-Y (excluding vowels and 'S') represent weeks 10-27. For the second half of the year, 26 is added to this number.
```

## Source Verification

[source record](../../sources/hacktricks/macos-serial-number.md)

## Evidence Excerpt

```text
_body: '# macOS Serial Number
{{#include ../../../banners/hacktricks-training.md}}
## Basic Information
Apple devices post-2010 have serial numbers consisting of **12 alphanumeric characters**, each segment conveying specific
information:
- **First 3 Characters**: Indicate the **manufacturing location**.
- **Characters 4 & 5**: Denote the **year and week of manufacture**.
- **Characters 6 to 8**: Serve as a **unique identifier** for each device.
```
