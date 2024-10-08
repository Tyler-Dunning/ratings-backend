from flask import Flask, jsonify, request
from pymongo import MongoClient
# importing os module for environment variables
import os

client = MongoClient(os.getenv("MONGODB_URI"))
db = client['ratings_db']

app = Flask(__name__)

@app.route('/')
def home():
    return "yo"

@app.route('/data')
def get_data():
    name = request.args.get('name')
    data_cursor = db['rating'].find({"username": name}, {"_id": 0})

    data = list(data_cursor)

    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "No data found"})
    
@app.route('/postReview', methods=['POST'])
def post_data():
    data = request.get_json()
    try:
        db['rating'].insert_one(data)
        return jsonify({"message": "Document inserted"})
    except:
        return jsonify({"error": "Failed to insert"}) 



