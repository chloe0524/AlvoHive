from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

postgres_hostname="localhost"
if os.uname()[1] == "apache":
    postgres_hostname="postgres"

test_items = Flask(__name__)
CORS(test_items)

# Database configuration
test_items.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://alvo:alvo@'+postgres_hostname+':5432/alvo_db'
test_items.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(test_items)

# Model definition
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


@test_items.errorhandler(404) 
# inbuilt function which takes error as parameter 
def not_found(e): 
    return render_template("404.html") 

# Routes
@test_items.route('/')
def index():
    print ("route / -----------------------------------------")
    return render_template('test_items.html')

@test_items.route('/items', methods=['GET'])
def get_items():
    print ("GET -----------------------------------------")
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

@test_items.route('/items', methods=['POST'])
def add_item():
    print ("POST -----------------------------------------")
    data = request.json
    new_item = Item(name=data['name'], description=data['description'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

@test_items.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    print ("PUT -----------------------------------------")
    data = request.json
    item = Item.query.get(id)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404

    item.name = data['name']
    item.description = data['description']
    db.session.commit()
    return jsonify(item.to_dict())

@test_items.route('/items/bulk_update', methods=['PUT'])
def bulk_update_items():
    print ("BULK -----------------------------------------")
    data = request.json
    print("***************************************************************************************")
    print (data)
    print("***************************************************************************************")
    for item_data in data:
        item = Item.query.get(item_data['id'])
        if item:
            try:
                item.name = item_data['name']
            except:
                pass
            try:
                item.description = item_data['description']
            except:
                pass
    db.session.commit()
    return jsonify({'message': 'Items updated successfully'}), 200

@test_items.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    print ("route /items -----------------------------------------")
    item = Item.query.get(id)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404

    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    db.create_all()
    test_items.run(debug=True)