#!/usr/bin/python3


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://alvo:alvo@localhost:5432/alvo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Company(db.Model):
    id_company = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100))
    url = db.Column(db.String(512))
    logo = db.Column(db.LargeBinary)

@app.route('/')
#def index():
#    company = Company.query
#    return render_template('basic_table.html', company=company)
#
def index():
    company = Company.query.all()
    company_data = [
        {
            "company_name": company.company_name,
            "url": company.url,
            "logo": base64.b64encode(company.logo).decode('utf-8') if company.logo else None
        }
        for company in company
    ]
    return render_template('company_list.html', company=company_data)


if __name__ == '__main__':
    app.run()
