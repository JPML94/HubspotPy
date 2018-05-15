import json
import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient
from flask import Flask, request, render_template, redirect, url_for, jsonify, current_app
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

from models import User, Admin

app = Flask(__name__)

# KEYS
load_dotenv()
HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")

# DB
app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
client = MongoClient(app)
db = client.database_name

@app.route('/')
def index():
    return 'Hello, World!'
