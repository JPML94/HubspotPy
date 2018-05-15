import json
import os

from flask import Flask, request, render_template, redirect, url_for, jsonify, current_app

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


class AttrDict(dict):
    """A dictionary with attribute-style access. It maps attribute access to
    the real dictionary.  """

    def __init__(self, init={}):
        dict.__init__(self, init)

    def __getstate__(self):
        return self.__dict__.items()

    def __setstate__(self, items):
        for key, val in items:
            self.__dict__[key] = val

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, dict.__repr__(self))

    def __setitem__(self, key, value):
        return super(AttrDict, self).__setitem__(key, value)

    def __getitem__(self, name):
        return super(AttrDict, self).__getitem__(name)

    def __delitem__(self, name):
        return super(AttrDict, self).__delitem__(name)

    __getattr__ = __getitem__
    __setattr__ = __setitem__

    def copy(self):
        ch = AttrDict(self)
        return ch


direc = 'data'
ext = '.json'

file_dict = AttrDict()
contacts_dict = AttrDict()

# Select only files with the ext extension
json_files = [i for i in os.listdir(direc) if os.path.splitext(i)[1] == ext]

# Iterate over your json files
for f in json_files:
    # Open them and assign them to file_dict
    with open(os.path.join(direc, f)) as file_object:
        jsonFile = json.load(file_object)
        file_dict[f] = jsonFile
    contacts_dict[f] = file_dict

print(contacts_dict)