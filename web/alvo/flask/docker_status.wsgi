import sys
sys.path.insert(0,'/var/www/html/alvo/flask')
sys.path.insert(0, '/usr/lib/python3/dist-packages')
from docker_status import docker_status as application
