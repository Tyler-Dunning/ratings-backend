from flask import Flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 



app = Flask(__name__)

@app.route('/')
def home():
    return os.getenv("MY_KEY")

uri = f'mongodb+srv://tdunning111:{ os.getenv("MY_KEY") }@ratings-cluster.1rltz.mongodb.net/?retryWrites=true&w=majority&appName=Ratings-Cluster'

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)