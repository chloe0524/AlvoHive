# Metasploitable2 installation

## Download

Link: https://sourceforge.net/projects/metasploitable\
There are other releases of Metasploitable.

## Installation

Zip file contains a pre-vuild VmWare VM including a disk: `Metasploitable.vmdk`

Step 1: uncompress vmdk file.

Step 2: create a VM that will use this file
- Type: linux
- Version: any 64bit
- Memory: 1 GB is enough
- Processor: 1 or 2
- Storage: Metasploitable.vmdk
- Network: Host-only

User/pwd: msfadmin/msfadmin

## Set French keyboard layout

Once connected:
```bash
$> sudo /bin/loadkeys fr
$> vi /etc/rc.local
```
Add: `nohup /bin/loadkeys fr &`\
Or simply: `/bin/loadkeys fr`

## Configure SSH and access by name on other Kali VM and WSL

``` bash
$> sudo /etc/hosts
```
Add Metasploitable chosen and and IP.
Ex:
```
192.168.56.128   victim
```
Configure SSH to be able to connect to Metasploitable VM "victim":
```bash
$> vi $HOME/.ssh/config
```
Add:
```	
host victim
    HostKeyAlgorithms +ssh-rsa		
``` 





