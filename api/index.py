from flask import Flask, jsonify, request
from pymongo import MongoClient
# importing os module for environment variables
import os

client = MongoClient(os.getenv("MONGODB_URI"))
db = client['ratings_db']


app = Flask(__name__)

@app.route('/')
def home():
    return os.getenv("MY_KEY")

@app.route('/data')
def get_data():
    name = request.args.get('name')
    data = db['rating'].find_one({"username:": name}, {"_id": 0})

    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "No data found"})
    
