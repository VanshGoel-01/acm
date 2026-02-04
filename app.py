from flask import Flask, request, jsonify
from Data_setup import create_table
import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
create_table()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

if not supabase_url or not supabase_key:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")

db = create_client(supabase_url, supabase_key)

@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

@app.route('/items', methods=['GET'])
def get_items():
    response = db.table('items').select('*').order('id', desc=True).execute()
    return jsonify(response.data)

@app.route('/items', methods=['POST', 'OPTIONS'])
def add_item():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.json
    
    new_item = {
        'title': data['title'],
        'category': data['category'],
        'price': float(data['price']),
        'location': data['location'],
        'seller_name': data['seller_name'],
        'contact': data['contact'],
        'description': data.get('description', '')
    }
    
    db.table('items').insert(new_item).execute()
    
    return jsonify({"message": "Item posted!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)