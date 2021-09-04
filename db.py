"""
Michael Patel
September 2021

Project description:

File description:

"""
################################################################################
# Imports
import pymongo

# from other modules
import config


################################################################################
class DB:
    def __init__(self):
        # create a client-side connection to db
        url = "mongodb+srv://" + config.username + ":" + config.password + "@cluster0.34mdn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.client = pymongo.MongoClient(url)

    def get_client(self):
        return self.client

    def get_collection(self):
        return self.get_db()["players"]

    def get_db(self):
        return self.client["nba"]
