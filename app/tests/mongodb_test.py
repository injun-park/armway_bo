import unittest
from pymongo import MongoClient

class TestStringMethods(unittest.TestCase):

    def test_conn(self):
        client = MongoClient()
        client = MongoClient('mongodb://localhost:27017/')
        db = client.mongodb_tutorial
        collection = db.counters
        query = {
            "_id" : "userid"
        }
        cursor = list(collection.find(query))
        for c in cursor :
            print c

    def test_sequence_gen(self):
        def getNextSequence(collection, name):
            return collection.find_and_modify(query={'_id': name}, update={'$inc': {'seq': 1}}, new=True).get('seq')

        client = MongoClient()
        client = MongoClient('mongodb://localhost:27017/')
        db = client['mongodb_tutorial']
        collection = db['counters']
        seq = getNextSequence(collection, "userid")
        print "seq : ", seq

if __name__ == '__main__':
    unittest.main()