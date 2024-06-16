## Docker: Apache and Postgres installation

Base image used: ubuntu/apache2:latest (https://hub.docker.com/r/ubuntu/apache2)\
Additional packages added:
* python3
* python3-requests
* pip
* iproute2
* net-tools
* inetutils-ping
* openssh-client
* postgresql-client
* vim
* curl

Project home directory: `$HOME/AlvoHive`

### Adding storage persistance
Creation of local directories:
```bash
$ mkdir $HOME/AlvoHive/apache2
$ mkdir $HOME/AlvoHive/web
$ mkdir $HOME/AlvoHive/pgdata
```
All are mapped as a volume in docker-compose.yml.
- $HOME/AlvoHive/apache2 : Apache configuration files.
- $HOME/AlvoHive/web : AlvoHive web.
- $HOME/AlvoHive/pgdata : PostgreSQL data

### Creating docker build files and docker-compose.yml

Docker Postgresql image creation will be added later.

```bash
$ mkdir -p $HOME/AlvoHive/docker-compose/docker/images/apache/
$ cd $HOME/AlvoHive/docker-compose
$ vi docker/images/apache/dockerfile-apache
```
Add into docker/images/apache/dockerfile-apache:
```docker
FROM ubuntu/apache2:latest
RUN apt-get update
RUN apt-get install -y python3 python3-requests pip iproute2 net-tools inetutils-ping openssh-client postgresql-client vim curl
# Enable Apache SSL
RUN set -eux; \
    apt-get update; \
    apt-get install ssl-cert; \
    a2enmod ssl; \
    a2ensite default-ssl
EXPOSE 80
EXPOSE 443
```
More Python packages will be added later to the image

```bash
$ vi docker-compose.yml
```
Add into docker-compose.yml: **mapping of apache2.conf is disabled at this step**.
```yaml
services:
  apache:
    image: apache
    container_name: apache-AlvoHive
    build:
      context: .
      dockerfile: docker/images/apache/dockerfile-apache
    hostname: apache
    restart: unless-stopped
    environment:
      - TZ=Europe/Paris
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - "$HOME/AlvoHive/web:/var/www/html"
    #- "$HOME/AlvoHive/apache2/apache2.conf:/etc/apache2/apache2.conf"
    networks:
      - postgres
      - cverest

  postgres:
    image: ubuntu/postgres:14-22.04_beta
    container_name: postgres-AlvoHive
    hostname: postgres
    restart: unless-stopped
    environment:
      - POSTGRES_PASSWORD=alvo
      - POSTGRES_USER=alvo
      - POSTGRES_DB=alvo_db
      - TZ=Europe/Paris
    ports:
      - '5432:5432'
    volumes:
      - "$HOME/AlvoHive/pgdata:/var/lib/postgresql/data"
    networks:
      - postgres

networks:
  postgres:
  cverest:
    name: cve-search-docker_frontend
    external: true
```

### Docker images creation and container start up
```bash
$ cd ~/AlvoHive/docker-compose
$ docker compose up
```
To start start de containers in background: `docker compose up -d`

Checking the containers are running:

```bash
$ docker compose ps
NAME                IMAGE                           COMMAND                  SERVICE    CREATED              STATUS              PORTS
apache-AlvoHive     docker-compose-apache           "apache2-foreground"     apache     About a minute ago   Up About a minute   0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp
postgres-AlvoHive   ubuntu/postgres:14-22.04_beta   "docker-entrypoint.s…"   postgres   About a minute ago   Up About a minute   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp
```
Or : `docker ps`

Cheking the Docker networks automacally created:
```bash
$ docker network ls
NETWORK ID     NAME                         DRIVER    SCOPE
90c8f5139e7f   bridge                       bridge    local
8be5053732a1   cve-search-docker_backend    bridge    local
15411c8cb213   cve-search-docker_frontend   bridge    local
7b877a816e6d   docker-compose_cverest       bridge    local
1ef6b217b20b   docker-compose_postgres      bridge    local
45586c5f8e55   host                         host      local
aa4b66e26820   none                         null      local
```

### Apache: configuration files

To be done when Apache container is up.
```bash
$ docker container cp apache-AlvoHive:/etc/apache2/apache2.conf $HOME/AlvoHive/apache2
Successfully copied 255kB to /home/chloe/AlvoHive
```

Apache default configuration file is now in `$HOME/AlvoHive/apache2`.
Remove comments and empty lines for readability:
```bash
    $ sed -i '/^#/d;/^$/d' $HOME/AlvoHive/apache2/apache2.conf
```

In docker-compose.yml, comment out volume mapping:
```yaml
      - "$HOME/AlvoHive/apache2/apache2.conf:/etc/apache2/apache2.conf"
```

Remove and recreate Suppression Apache container: **stop and start, or restart is not enough.**
```bash
$ docker compose down apache
$ docker compose up apache
```

The container apache-AlvoHive now uses `$HOME/AlvoHive/apache2/apache2.conf` as configuration file.


For restarting Apache from the container:
```bash
$ docker exec -it apache-AlvoHive bash
root@apache:/# /etc/init.d/apache2 reload
```


### Postgres configuration
Directory /home/chloe/AlvoHive/pgdata belongs by default to UID 999 an user root.

```bash
$ sudo -i
root$ cd /home/chloe/AlvoHive/pgdata
root$ vi postgresql.conf
```

If listen_addresses=127.0.0.1 or localhost, change it to: `listen_addresses = '*'`

Leave root: `exit`
```bash
$ cd ~/AlvoHive/docker-compose
$ docker compose restart postgres
```


### Stopping containers
Warning: will hang if there is any active `docker exec -it xxxxx bash`.
```bash
$ cd ~/AlvoHive/docker-compose
$ docker compose stop
```

To stop only one container: `docker compose stop service_name`\
service_name: apache or postgres

### Connecting into the containers

```bash
~/AlvoHive/docker-compose$ docker exec -it apache-AlvoHive bash
root@apache:/#
```
```bash
~/AlvoHive/docker-compose$ docker exec -it postgres-AlvoHive bash
root@postgres:/#
```

### Cleaning all up

IE: useful when changing the custom image created.

```bash
~/AlvoHive/docker-compose$ cd /home/$HOME/AlvoHive/docker-compose

~/AlvoHive/docker-compose$ docker compose stop

~/AlvoHive/docker-compose$ docker compose rm apache postgres

~/AlvoHive/docker-compose$ docker images
REPOSITORY         TAG             IMAGE ID       CREATED         SIZE
apache             latest          24d397d8d246   5 days ago      702MB
ubuntu/postgres    14-22.04_beta   21b9b7760873   8 days ago      416MB
cve_search         latest          4e7d3a4a2cfc   2 weeks ago     1.21GB
cve_search-mongo   latest          30a9ec3ed096   2 weeks ago     1.48GB
cve_search-redis   latest          28b83ce9a8a0   2 weeks ago     135MB

~/AlvoHive/docker-compose$ docker rmi 24d397d8d246 21b9b7760873 --force
```

Checking that the image is deleted

```bash
~/AlvoHive/docker-compose$ docker compose images
CONTAINER        REPOSITORY        TAG              IMAGE ID          SIZE
```

### Accessing the container

```bash
~/AlvoHive/docker-compose$ docker exec -it apache-AlvoHive bash
root@apache:/#
```
```bash
~/AlvoHive/docker-compose$ docker exec -it postgres-AlvoHive bash
root@postgres:/#
```


### Backup/restore

**Important**: 
- Using `tar` allows to keep the existing owner/group and rights.
- Needs to executed as root because `~/AlvoHive/pgdata` is not owned by WSL user.

#### Backup
```bash
$ sudo -i tar -cvzf $HOME/Backup_AlvoHive_$(date +%Y-%m-%d_%H-%M).tgz -C $HOME AlvoHive CVE-Search-Docker/docker-compose.yml
```
&rArr; Copy the backup file to a secure remote location.

#### Restore

Untar in a temporary directory and restore the relevant files:
```bash
$ cd $HOME
$ mkdir restauration
$ cd restauration
$ sudo tar xvfz <chemin accès>/Backup_AlvoHive_YYYY-MM-DD_HH_MI.tgz
```

### Connection tests

#### Testing Apache index.html with a browser

Ignore the security alert: the certificate used is not sign by a known authority.\
https://localhost or https://localhost:443, 443 is the default https port.

#### Testing CVE-Search REST API in Python from Apache container
```bash
$> docker exec -it apache-AlvoHive bash
$> vi /tmp/t.py
```
Paste code:
```python
import requests
 
url = "https://cve_search:5000/api/cve/CVE-2016-3333"
 
payload={}
headers = {
  'X-Api-Key': 'API_KEY'
}
 
response = requests.request("GET", url, headers=headers, data=payload, verify=False)
 
print(response.text)
```
Test:
```bash
docker exec -it apache-AlvoHive python3 /tmp/t.py
```

#### Testing Postgres DB connection from Apache
```bash
$> docker exec -it apache-AlvoHive psql -U alvo -p 5432 -h postgres -d alvo_db
```

#### Testing Postgres DB connection from HeidiSQL on Windows

Download : https://www.heidisql.com/download.php

Créer une nouvelle connexion :
- Network type: **PostgreSQL (TCP/IP)**
- Library: **libpq-15.dll** (default)
- IP: **127.0.0.1**
- Port: **5432** (default)
