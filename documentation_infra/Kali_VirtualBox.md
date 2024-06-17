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
$> sudo vi /etc/postgresql/16/main/postgresql.conf
```

Add line: `listen_addresses = 'localhost,IP_ADDRESS' # what IP address(es) to listen on;`

Postgres listener now will also "listens" connexions issue to IP IP_ADDRESS.


### Allow connections from any IP

``` bash
$> vi /etc/postgresql/16/main/pg_hba.conf
```
Add line: `host    all             all             all            scram-sha-256`



### Restart Postgres

```bash
$> sudo /etc/init.d/postgresql restart
```

### Identify Postgres password

Metaexploit uses Postgres user **msf**.

Identifier le password du user msf : le tien sera différent sans doute
``` bash
$> sudo grep -i pa /usr/share/metasploit-framework/config/database.yml
  password: jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=
  password: jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=
  password: jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=
```

### Connect to Postgres
With OS user OS kali:
```bash
kali$> psql -U msf -h IP_ADDRESS
```
Will prompt for the previously indentified password.

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

Postgres listener now will also "listen" to connections issued to IP IP_ADDRESS.

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

## Data migration with SSH

```bash
$ ssh kali@IP_ADDRESS 'PGPASSWORD="jhu97O5W2IMI9XzpNKD/J50szUSmuh/WAaXB7/Cuad0=" pg_dump -U msf -h IP_ADDRESS --table services --table hosts | PGPASSWORD=alvo psql -U alvo -p 5432 -h postgres -d alvo_db'
```

This command will:

1. SSH into the Kali VM at `IP_ADDRESS`.
2. Set the Postgres password for the msf user using the `PGPASSWORD` environment variable (avoiding manual entry).
3. Use `pg_dump` to export the `services` and `hosts` tables from the `msf` user database.
4. `|` -> Pipe the dumped data to another Postgres instance:
   - Set the Postgres password for the `alvo` user.
   - Use `psql` to import the data into the `alvo_db` database.

### Explanation of components:
- `PGPASSWORD="jhu97O5W2IMI9XzpNKD/J50szUSmuh/WAaXB7/Cuad0="`: Passes the password in a variable to avoid manual input.
- `pg_dump`: Postgres tool for exporting data.
- `-U msf`: Postgres username.
- `-h `IP_ADDRESS`: Host address.
- `--table services --table hosts`: List of tables to dump.
- `|`: Standard pipe to pass output to another command.
- `PGPASSWORD=alvo`: Passes the password for the target database.
- `psql`: Standard Postgres command-line tool.
- `-U alvo`: Target Postgres username.
- `-p 5432`: Port (default is 5432, so this is optional).
- `-h postgres`: Hostname (Docker resolves this to the correct container).
- `-d alvo_db`: Target database name.

This process will transfer the `services` and `hosts` tables from the Metasploit database in Kali to the `alvo_db` database on the target Postgres instance.






