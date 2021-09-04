"""
Michael Patel
September 2021

Project description:

File description:

"""
################################################################################
# Imports
from datetime import datetime

# from other modules
from db import DB

from flask import Flask
server = Flask(__name__)


################################################################################
# ----- ROUTES ----- #
@server.route("/")
def index():
    response = datetime.now()
    response = str(response)
    return response


@server.route("/summary/")
def summary():
    db = DB()
    response = f'Databases: {db.client.list_database_names()}<br>' \
               f'Collections: {db.get_db().list_collection_names()}'
    return response
