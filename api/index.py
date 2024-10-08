from flask import Flask, jsonify, request
from pymongo import MongoClient
# importing os module for environment variables
import os

client = MongoClient("mongodb+srv://tdunning111:M4VgeWhq5uu6aUJ0@ratings-cluster.1rltz.mongodb.net/?retryWrites=true&w=majority&appName=Ratings-Cluster'"
)
db = client['ratings_db']


app = Flask(__name__)

@app.route('/')
def home():
    return "yo"

@app.route('/data')
def get_data():
    name = request.args.get('name')
    data = db['rating'].find_one({"username:": name}, {"_id": 0})

    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "No data found"})
    

if __name__ == '__main__':
    app.run()