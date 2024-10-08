from flask import Flask, jsonify, request
from pymongo import MongoClient
# importing os module for environment variables
import os

try:
    client = MongoClient(os.getenv("MONGODB_URI"))
    db = client['ratings_db']
except Exception as e:
    print(f"Error connecting to db: {e}")
    db = None

app = Flask(__name__)

@app.route('/')
def home():
    return "yo"

@app.route('/data')
def get_data():
    if db is None:
        return jsonify({"error": "Database connection failed"})
    
    name = request.args.get('name')
    data_cursor = db['rating'].find({"username": name})

    data_list = list(data_cursor)

    if data_list:
        return jsonify(data_list)
    else:
        return jsonify({"error": "No data found"})
    