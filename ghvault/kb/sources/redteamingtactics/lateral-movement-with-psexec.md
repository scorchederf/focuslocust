---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Lateral Movement with Psexec

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-lateral-movement-with-psexec` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/lateral-movement-with-psexec.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Lateral Movement with Psexec](../../topics/offensive-security/lateral-movement-with-psexec.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-lateral-movement-with-psexec |
| name | Lateral Movement with Psexec |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/lateral-movement-with-psexec.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Annotation 2019-05-20 210729.png
- Annotation 2019-05-20 211216.png
- Annotation 2019-05-20 211401.png
- Annotation 2019-05-20 211654 (1) (1).png
- Annotation 2019-05-20 212123.png
_body: '# Lateral Movement with Psexec


  A very old and noisy lateral movement technique can be performed using psexec by SysInternals.


  ## Execution


  Let''s connect from workstation `ws01` to the domain controller `dc01` with domain administractor credentials:


  {% code title="attacker@victim" %}

  ```

  .\PsExec.exe -u administrator -p 123456 \\dc01 cmd

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Annotation 2019-05-20 210729.png>)


  ## Observations


  The technique is noisy for at least a couple of reasons. Upon code execution, these are some well known artefacts that are
  left behind which will most likely get you flagged in an environment where SOC is present.


  A `psexesvc` service gets created on the remote system and below shows the process ancestry of your command shell:


  ![](<../../.gitbook/assets/Annotation 2019-05-20 211216.png>)


  Proving that `psexec` is actually running as a service:


  ![](<../../.gitbook/assets/Annotation 2019-05-20 211401.png>)


  ![](<../../.gitbook/assets/Annotation 2019-05-20 211654 (1) (1).png>)


  Additionally, there is quite a bit of SMB network traffic generated when connecting to a remote machine which could be signatured:


  ![](<../../.gitbook/assets/Annotation 2019-05-20 212123.png>)'
_relative_path: offensive-security/lateral-movement/lateral-movement-with-psexec.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/lateral-movement-with-psexec.md
````
