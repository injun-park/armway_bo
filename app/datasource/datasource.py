import pymongo
import pymongo.errors
from pymongo import MongoClient

class MongoDataSource :
    def __init__(self, dbname = ""):
        self.client = MongoClient()
        self.db = self.client.mongodb_tutorial

    def getCollection(self, collectionName):
        return self.db[collectionName]