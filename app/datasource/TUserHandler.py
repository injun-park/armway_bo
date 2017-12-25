import datasource
import pymongo.errors as pymerr
import sys, traceback

class TUserHandler :
    __DB_NAME = "mongodb_tutorial"
    __COLLECTION_NAME = "user"

    def __init__(self):
        self.ds = datasource.MongoDataSource(TUserHandler.__DB_NAME)
        self.collection = self.ds.getCollection(TUserHandler.__COLLECTION_NAME)

    def getNextSequence(self, name):
        db = self.ds.db
        collection = db.counters
        return collection.find_and_modify(query={'_id': name}, update={'$inc': {'seq': 1}}, new=True).get('seq')

    def insertUser(self, cid, cname):
        query = {
            "_id" : self.getNextSequence("userid"),
            "cid" : cid,
            "name" :cname
        }

        try :
            post_id = self.collection.insert(query)
        except pymerr.DuplicateKeyError as e :
            traceback.print_exc(file=sys.stderr)
            post_id = -1

        return post_id

    def selectAll(self):
        result = self.collection.find()
        return result

    def selectByCID(self, cid):
        query = {
            "cid" : cid
        }

        result = self.collection.find_one(query)
        return result

