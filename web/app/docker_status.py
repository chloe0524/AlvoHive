#!/usr/bin/python3

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

DOCKER_API_URL = 'http://localhost:2375' # Docker REST API endpoint

def get_containers():
    response = requests.get(f'{DOCKER_API_URL}/containers/json')
    return response.json()

def get_container_top(container_id):
    response = requests.get(f'{DOCKER_API_URL}/containers/{container_id}/top')
    return response.json()

@app.route('/top/<container_id>')
def top(container_id):
    top_info = get_container_top(container_id)
    return jsonify(top_info)

@app.route('/')
def home():
    containers = get_containers()
    return render_template('docker_status.html', containers=containers)

if __name__ == '__main__':
    app.run(debug=True)