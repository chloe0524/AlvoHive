# Apache and Flask configuration and usage <!-- omit in toc -->

- [AlvoWeb Apache configuration file](#alvoweb-apache-configuration-file)
- [Apache authentication with PostgreSQL](#apache-authentication-with-postgresql)
- [Apache configuration for Flask](#apache-configuration-for-flask)
- [Flask WSGI files](#flask-wsgi-files)
- [Debug](#debug)
	- [Python: Apache logs](#python-apache-logs)
	- [HTML/JavaScript](#htmljavascript)
		- [Alert](#alert)
		- [Browser console](#browser-console)


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
<VirtualHost *:443>  # HTTPS port
    DocumentRoot /var/www/html
    ErrorDocument 404 /alvo/flask/templates/404.html 

    # Web Server Gateway Interface configuration: executing Python with Apache
    WSGIDaemonProcess alvoprocgroup user=www-data group=www-data threads=5 python-home=/var/www/html/alvo/flask/flask-venv
    WSGIProcessGroup alvoprocgroup

    # HTTPS configuration
    SSLEngine on
    SSLCertificateFile      /etc/ssl/certs/ssl-cert-snakeoil.pem
    SSLCertificateKeyFile   /etc/ssl/private/ssl-cert-snakeoil.key

     <FilesMatch "\.(?:cgi|shtml|phtml|php)$">
         SSLOptions +StdEnvVars
     </FilesMatch>
     <Directory /usr/lib/cgi-bin>
         SSLOptions +StdEnvVars
     </Directory>

    # Authtentication with Postgres
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
        AuthnCacheTimeout 60
        AuthDBDUserPWQuery "SELECT passwd FROM auth WHERE username = %s"
    </Directory>
    
    # # Web Server Gateway Interface aliases
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

    WSGIScriptAlias /report /var/www/html/alvo/flask/report.wsgi
    <Directory /var/www/html/alvo/flask>
        Require valid-user
    </Directory>

    # Alias for the reports directory
    <IfModule alias_module>
        Alias /reports/ /var/www/html/alvo/flask/back/reports/
        <Directory "/var/www/html/alvo/flask/back/reports/">
            Options +Indexes
            Require valid-user
        </Directory>
    </IfModule>

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

    WSGIScriptAlias /report /var/www/html/alvo/flask/report.wsgi
    <Directory /var/www/html/alvo/flask>
        Require valid-user
    </Directory>
```

## Flask WSGI files
Apache WSGI allows to run Python code.

Exemple for docker_status: `docker_status.wsgi`
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

But when served by Apache: providing the complete route path is mandatory
```python
fetch('/docker_status/top/' + containerId)
```

## Debug

### Python: Apache logs
	
Python `print` commands are logged to Apache logs.

To monitor Apache log: `docker logs -f apache_AlvoHive`

Example: `print` in a WSGI module
``` python
print ("***************************************************************")
print ('Execute: ' + base_path + '/back/generate_report.py , host id='+row_value)
print ("***************************************************************") 
```

In Apache log:
```
[Wed Jul 10 08:40:49.835732 2024] [wsgi:error] [pid 86:tid 140390309721792] [remote 172.19.0.1:54440] ***************************************************************
[Wed Jul 10 08:40:49.835784 2024] [wsgi:error] [pid 86:tid 140390309721792] [remote 172.19.0.1:54440] Execute: /var/www/html/alvo/flask/back/generate_report.py , host id=6
[Wed Jul 10 08:40:49.835791 2024] [wsgi:error] [pid 86:tid 140390309721792] [remote 172.19.0.1:54440] *************************************************************** 
```

Example: `print` in Python code, not WSGI
``` python
print("**************************************")
print("update hosts set report_date='" + str(dt.now()) + "', pdf='" + report_name + ".pdf', zip='" + report_name + ".zip' where id=" + str(host_id))
print("**************************************")
```
In Apache log:
``` postgres
**************************************
update hosts set report_date='2024-07-10 08:40:57.445838', pdf='report_006_2024-07-10_0840.pdf', zip='report_006_2024-07-10_0840.zip' where id=6
**************************************
```

### HTML/JavaScript
	
#### Alert

Simple messages like:
``` JavaScript
alert ('Here I am.')
```

#### Browser console

Example:

``` JavaScript
console.log('TTY: tty_position=', tty_position );
```

In Browser console:
```
TTY: tty_position= 6
```
