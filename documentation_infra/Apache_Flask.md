# Apache and Flask configuration and usage

AlvoHive web home directory: 
* Apache container: `/var/www/html`
* WSL mapping: `$HOME/AlvoHive/web`

Apache configuration file: **default file, unchanged**
* WSL mapping: `$HOME/AlvoHive/apache2/apache2.conf`
* Apache container: `/etc/apache2/apache2.conf`



## AlvoWeb Apache configuration file
Apache AlvoWeb configuration file:
* Apache container: `/etc/apache2/sites-enabled/000-default.conf`
* WSL mapping: `$HOME/AlvoHive/apache2/000-default.conf`

```apache
<VirtualHost *:443>
    DocumentRoot /var/www/html
    ErrorDocument 404 /alvo/flask/templates/404.html 

    WSGIDaemonProcess alvoprocgroup user=www-data group=www-data threads=5 python-home=/var/www/html/alvo/flask/flask-venv
    WSGIProcessGroup alvoprocgroup

    SSLEngine on
    SSLCertificateFile      /etc/ssl/certs/ssl-cert-snakeoil.pem
    SSLCertificateKeyFile   /etc/ssl/private/ssl-cert-snakeoil.key

     <FilesMatch "\.(?:cgi|shtml|phtml|php)$">
         SSLOptions +StdEnvVars
     </FilesMatch>
     <Directory /usr/lib/cgi-bin>
         SSLOptions +StdEnvVars
     </Directory>

    <IfModule mod_dbd.c>
        DBDriver pgsql
        DBDParams "host=postgres port=5432 dbname=alvo_db user=alvo password=alvo"
        DBDPrepareSQL "SELECT passwd FROM auth WHERE username = %s" authn_query
        DBDMin 4
        DBDKeep 8
        DBDMax 20
        DBDExptime 300
    </IfModule>

    <Directory "/var/www/html/alvo">
        AuthType Basic
        AuthName "AlvoHive"
        AuthBasicProvider socache dbd
        AuthnCacheProvideFor dbd
        AuthnCacheContext alvo-hive
        Require valid-user
        AuthDBDUserPWQuery "SELECT passwd FROM auth WHERE username = %s"
    </Directory>
    
    WSGIScriptAlias /company_list /var/www/html/alvo/flask/company_list.wsgi
    <Directory /var/www/html/alvo/flask>
        Require valid-user
    </Directory>

    WSGIScriptAlias /contact_list /var/www/html/alvo/flask/contact_list.wsgi
    <Directory /var/www/html/alvo/flask>
        Require valid-user
    </Directory>

    WSGIScriptAlias /docker_status /var/www/html/alvo/flask/docker_status.wsgi
    <Directory /var/www/html/alvo/flask>
        Require valid-user
    </Directory>
</VirtualHost>
```

## Apache authentication with PostgreSQL

`000-default.conf` snippet:
```bash
    <IfModule mod_dbd.c>
        DBDriver pgsql
        DBDParams "host=postgres port=5432 dbname=alvo_db user=alvo password=alvo"
        DBDMin 4
        DBDKeep 8
        DBDMax 20
        DBDExptime 300
    </IfModule>

    <Directory "/var/www/html/alvo">
        AuthType Basic
        AuthName "AlvoHive"
        AuthBasicProvider socache dbd
        AuthnCacheProvideFor dbd
        AuthnCacheContext alvo-hive
        Require valid-user
        AuthDBDUserPWQuery "SELECT passwd FROM auth WHERE username = %s"
    </Directory>
```

## Apache configuration for Flask

`000-default.conf` snippet, global section:
```bash
     WSGIDaemonProcess alvoprocgroup user=www-data group=www-data threads=5 python-home=/var/www/html/alvo/flask/flask-venv
    WSGIProcessGroup alvoprocgroup
```

`000-default.conf` snippet, entries for each Flask applciation:
```apache
    WSGIScriptAlias /company_list /var/www/html/alvo/flask/company_list.wsgi
    <Directory /var/www/html/alvo/flask>
        Require valid-user
    </Directory>

    WSGIScriptAlias /contact_list /var/www/html/alvo/flask/contact_list.wsgi
    <Directory /var/www/html/alvo/flask>
        Require valid-user
    </Directory>

    WSGIScriptAlias /docker_status /var/www/html/alvo/flask/docker_status.wsgi
    <Directory /var/www/html/alvo/flask>
        Require valid-user
    </Directory>
```

## Flask wsgi files
Apache wsgi allows to run Python code.

Exemple for docker_status:
```python
import sys
sys.path.insert(0,'/var/www/html/alvo/flask')
sys.path.insert(0, '/usr/lib/python3/dist-packages')
from docker_status import docker_status as application
```

Route example:
```python
@docker_status.route('/top/<container_id>')
def top(container_id):
    top_info = get_container_top(container_id)
    return jsonify(top_info)
```

When running `python3 docker_status.py`, this works:
```python
fetch('/top/' + containerId)
```

But when served by Apache: provide the complete path
```python
fetch('/docker_status/top/' + containerId)
```




