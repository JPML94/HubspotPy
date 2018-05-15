import json
import os
import pprint
from flask import Flask, request, render_template, redirect, url_for, jsonify, current_app

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

direc = './data'
ext = '.json'

file_dict = {}

# Select only files with the ext extension
json_files = [i for i in os.listdir(direc) if os.path.splitext(i)[1] == ext]

# Iterate over your json files
for f in json_files:
    # Open them and assign them to file_dict
    with open(os.path.join(direc, f)) as file_object:
        file_dict[f] = file_object.read()

# Iterate over your dict and print the key/val pairs.
# for i in file_dict:
#     print (i, file_dict[i])


@app.route('/file_dict')
def contact():
    pprint.pprint(file_dict)
    return jsonify(file_dict)

@app.route('/file_object')
def contact2():
    return str(file_object)
