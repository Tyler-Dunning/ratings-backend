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
    data = db['rating'].find({"username": name})

    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "No data found"})
    

if __name__ == '__main__':
    app.run()