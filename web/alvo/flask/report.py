#!/usr/bin/python3

from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import base64
import os 
import subprocess

# Configure Flask application
report = Flask(__name__)

postgres_hostname = "localhost"
if os.uname()[1] == "apache":
    postgres_hostname = "postgres"

report.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://alvo:alvo@'+postgres_hostname+':5432/alvo_db'
report.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(report)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    report_date = db.Column(db.String(512))
    pdf = db.Column(db.String(100))
    zip = db.Column(db.String(100))

@report.route('/execute', methods=['POST'])
def execute():
    data = request.json
    row_value = data.get('row_value')
    
    base_path = os.path.dirname(__file__)
    # debug: visible with 'docker logs'
    print ("***************************************************************")
    print ('Execute: ' + base_path + '/back/generate_report.py , host id='+row_value)
    print ("***************************************************************") 
    result = subprocess.run([base_path + '/back/generate_report.py', row_value])
    
    return jsonify({'output': result.stdout})


@report.route('/')
def index():
    try:
        reports = Report.query.all()

        report_data = [
            {
                "id": report.id,
                "company_name": report.company_name,
                "first_name": report.first_name,
                "last_name": report.last_name,
                "name": report.name,
                "report_date": report.report_date,
                "pdf": report.pdf,
                "zip": report.zip
            }
            for report in reports
        ]

        return render_template('report.html', report=report_data)

    except Exception as e:
        return f"Error fetching reports: {str(e)}"

if __name__ == '__main__':
    report.run(debug=True)