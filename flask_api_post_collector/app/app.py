#!/usr/bin/env python3

import ast
import uuid
import os
from flask_pymongo import PyMongo
from flask import Flask, request, jsonify

application = Flask(__name__)
MONGODB_USERNAME = os.environ['MONGODB_USERNAME']
MONGODB_PASSWORD = os.environ['MONGODB_PASSWORD']
MONGODB_HOSTNAME = os.environ['MONGODB_HOSTNAME']
MONGODB_DATABASE = os.environ['MONGODB_DATABASE']

# initialize some settings for the database connection
application.config["MONGO_URI"] = f'mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOSTNAME}:27017/{MONGODB_DATABASE}'

mongo = PyMongo(application)
db = mongo.db


@application.route('/', methods=["GET"])
def home():
    endpoint_id = str(uuid.uuid4())

    item = {
        'endpoint_id': endpoint_id,
        'endpoint_post_data': ''
    }

    db.flaskdb.insert_one(item)

    return jsonify(endpoint_uid=endpoint_id)


@application.route('/<uid>', methods=["GET", "POST"])
def check_uid(uid):
    if request.method == "GET":
        return get_data(uid)
    elif request.method == "POST":
        return put_data(uid, request.json)

@application.route('/list', methods=["GET"])
def list_ids():
    cursor = db.flaskdb.find()
    return jsonify([id['endpoint_id'] for id in cursor])

@application.route('/health')
def health_check():
    try:
        db.flaskdb.find_one()
        return jsonify(status=200)
    except:
        return jsonify(status=424)


def get_data(uid):
    id = db.flaskdb.find_one({'endpoint_id': uid})
    return jsonify(endpoint_id=id['endpoint_id'], content=id['endpoint_post_data'])



def put_data(uid, data):
    data_id = db.flaskdb.find_one_and_update(
        {"endpoint_id": uid}, {"$set": {"endpoint_post_data": data}}, new=True)
    return jsonify(endpoint_id=data_id['endpoint_id'], content=data_id['endpoint_post_data'])


if __name__ == '__main__':
    ENVIRONMENT_DEBUG = ast.literal_eval(os.environ.get("APP_DEBUG"))
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT,
                    debug=ENVIRONMENT_DEBUG)
