from flask import Flask, render_template, jsonify
import requests
import os
import psutil

# Instruction
# WSL/Windows: all containers are reachable with hostname "localhost"
# Inside Apache container: use WSL host IP
#
# Docker REST API activation: add "-H tcp://0.0.0.0:2375" to startup command
# $> vi /etc/systemd/system/multi-user.target.wants/docker.service
# ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
#
# Restart: $> sudo systemctl daemon-reload; sudo systemctl restart docker.service

docker_host="localhost"
if os.uname()[1] == "apache":
    docker_host="172.17.246.188" # To be found with "ip a show eth0" from wsl

DOCKER_API_URL = 'http://'+docker_host+':2375' # Docker REST API endpoint

docker_status = Flask(__name__)

# debug
######################################################################
# Processes information for a container id: route /processes/
######################################################################

# Processes information for a container id: route /processes/
# Calling Docker REST API endpoint
def get_container_processes(container_id):
    # response = requests.get(f'{DOCKER_API_URL}/containers/{container_id}/top?ps_args=-eo user,pid,ppid,command,stime,%mem,%cpu')
    response = requests.get(f'{DOCKER_API_URL}/containers/{container_id}/top?ps_args=-ef --sort=-c')
    #response = requests.get(f'{DOCKER_API_URL}/containers/{container_id}/top')
    print(f'{DOCKER_API_URL}/containers/{container_id}/top/')
    return response.json()

@docker_status.route('/processes/<container_id>')
def processes(container_id):
    all_processes = get_container_processes(container_id)
    return jsonify(all_processes)

# debug
######################################################################
# List of all running containers: startup route /
######################################################################

# Containers list: 
# Calling Docker REST API endpoint
def get_containers():
    response = requests.get(f'{DOCKER_API_URL}/containers/json')
    print(f'{DOCKER_API_URL}/containers/json')
    return response.json()

# Startup root
@docker_status.route('/')
def home():
    containers = get_containers()
    return render_template('docker_status.html', containers=containers)

if __name__ == '__main__':
    docker_status.run()
