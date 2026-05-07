---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0028
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0028-image-metadata
---

## Description

contextual information associated with a virtual machine image, such as its name, resource group, status (active or inactive), type (custom or prebuilt), size, creation date, and permissions. This metadata is critical for understanding the state and configuration of virtual machine images in cloud environments. Examples: <br><br>- Azure Compute Service Image Metadata Example:<br>    - Name: MyCustomImage<br>    - Resource Group: MyResourceGroup<br>    - State: Available<br>    - Type: Managed Image<br>- AWS EC2 AMI Metadata Example:<br>    - Image ID: ami-1234567890abcdef0<br>    - Name: ProdImage<br>    - State: Available<br>    - Platform: Windows<br>- Google Cloud Compute Engine Image Metadata Example:<br>    - Image Name: webserver-image<br>    - Project: my-project-id<br>    - Family: webserver<br>    - Source Disk: my-disk-id<br>- VMware vSphere Template Metadata Example:<br>    - Name: LinuxTemplate<br>    - Disk Size: 40GB<br>    - Network Adapter: VM Network
