from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from Data_setup import create_table

app = Flask(__name__)
create_table()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campus_cart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = 'items'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String, nullable=False)
    seller_name = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "price": self.price,
            "location": self.location,
            "seller_name": self.seller_name,
            "contact": self.contact,
            "description": self.description
        }

@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.order_by(Item.id.desc()).all()
    return jsonify([item.to_dict() for item in items])

@app.route('/items', methods=['POST', 'OPTIONS'])
def add_item():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.json
    
    new_item = Item(
        title=data['title'],
        category=data['category'],
        price=float(data['price']),
        location=data['location'],
        seller_name=data['seller_name'],
        contact=data['contact'],
        description=data.get('description', '')
    )
    
    db.session.add(new_item)
    db.session.commit()
    
    return jsonify({"message": "Item posted!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)