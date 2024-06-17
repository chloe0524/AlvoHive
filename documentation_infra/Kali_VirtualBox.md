# Kali VM installation and configuration / Postgres configuration

## VM download and configuration
Kali VirtualBox VM download: https://www.kali.org/get-kali/#kali-virtual-machines

Provides a ready-to-use vbox configuration file and vdi disk.

Changed network configuration from NAT to Host-only adapter.

## SSH activation and start
Allow to connect through SSH from Windows or WSL.

```bash
$ sudo systemctl start ssh
$ sudo systemctl enable ssh
$ sudo systemctl status ssh
● ssh.service - OpenBSD Secure Shell server
Loaded: loaded (/usr/lib/systemd/system/ssh.service; enabled; preset: disabled)
Active: active (running) since Thu 2024-05-30 08:14:32 EDT; 1h 52min ago
```

## Postgres configuration

### Add Kali IP to the listener:

```bash
$ sudo vi /etc/postgresql/16/main/postgresql.conf
```

Add line: `listen_addresses = 'localhost,IP_ADDRESS' # what IP address(es) to listen on;`

Postgres listener now will also "listen" to connections issued to IP_ADDRESS.

### Allow connections from any IP

```bash
$ sudo vi /etc/postgresql/16/main/pg_hba.conf
```
Add line: `host    all             all             all            scram-sha-256`

### Restart Postgres

```bash
$ sudo /etc/init.d/postgresql restart
```

### Identify Postgres password

Metasploit uses the Postgres user **msf**.

Identify the password for the user msf (your password will likely be different):
```bash
$ sudo grep -i pa /usr/share/metasploit-framework/config/database.yml
  password: jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=
  password: jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=
  password: jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=
```

### Connect to Postgres
With OS user kali:
```bash
kali$ psql -U msf -h IP_ADDRESS
```
This will prompt for the previously identified password.
