from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import base64
import os

postgres_hostname="localhost"
if os.uname()[1] == "apache":
    postgres_hostname="postgres"

contact_list = Flask(__name__)
contact_list.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://alvo:alvo@'+postgres_hostname+':5432/alvo_db'
contact_list.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(contact_list)

#    id_company = db.Column(db.Integer, primary_key=True)

# define type of data content
class Company_contact(db.Model):
    id_company = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100))
    id_contact = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    url = db.Column(db.String(512))
    logo = db.Column(db.LargeBinary)

# define main route
@contact_list.route('/')
def index():
    company_contact = Company_contact.query.all()
    company_contact_data = [
        {
            "id_company": company_contact.id_company,
            "company_name": company_contact.company_name,
            "id_contact": company_contact.id_contact,
            "first_name": company_contact.first_name,
            "last_name": company_contact.last_name,
            "email": company_contact.email,
            "phone": company_contact.phone,
            "city": company_contact.city,
            "country": company_contact.country,
            "url": company_contact.url,
            "logo": base64.b64encode(company_contact.logo).decode('utf-8') if company_contact.logo else None
        }
        for company_contact in company_contact
    ]
    return render_template('contact_list.html', company_contact=company_contact_data)


if __name__ == '__main__':
    contact_list.run()
