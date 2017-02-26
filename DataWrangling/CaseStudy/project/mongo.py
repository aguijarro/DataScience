# -*- coding: utf-8 -*-
import pprint


def getDocuments(db):
    data = db.sfsample.find()
    return data.count()


def getAllTypes(db):
    data = db.sfsample.group(["type"], {}, {"count":0},"function(o, p){p.count++}" )
    return data


def getNodes(db):
    data = db.sfsample.find({"type": "node"}).count()
    return data


def getWays(db):
    data = db.sfsample.find({"type": "way"}).count()
    return data


def getCountUniqueUsers(db):
    data = len(db.sfsample.distinct("created.user"))
    return data

def getSampleUniqueUsers(db):
    data = db.sfsample.distinct("created.user")
    return data[:10]


def getTopUniqueUsers(db):
    data = db.sfsample.aggregate([{"$group":{"_id" : "$created.user", "count" :{"$sum": 1}}},{"$sort":{"count":-1}}, {"$limit":10}])
    return data

def getCountAmenities(db):
    data = len(db.sfsample.distinct("amenity"))
    return data

def getAmenities(db):
    data = db.sfsample.aggregate([{"$group":{"_id" : "$amenity", "count" :{"$sum": 1}}},{"$sort":{"count":-1}}, {"$limit":10}])
    return data

def getCuisine(db):
    data = db.sfsample.aggregate([{"$group":{"_id" : "$cuisine", "count" :{"$sum": 1}}},{"$sort":{"count":-1}}, {"$limit":10}])
    return data


def get_db():
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.datawrangling
    return db


def main():
    db = get_db()
    pprint.pprint(getDocuments(db))
    #pprint.pprint(getAllTypes(db))
    pprint.pprint(getNodes(db))
    pprint.pprint(getWays(db))
    pprint.pprint(getCountUniqueUsers(db))
    pprint.pprint(getSampleUniqueUsers(db))
    print("**Top Ten**")
    for doc in getTopUniqueUsers(db):
        print doc
    print("**Count Amenities**")
    pprint.pprint(getCountAmenities(db))
    print("**Amenities**")
    for doc in getAmenities(db):
        print doc
    print("**Cuisine**")
    for doc in getCuisine(db):
        print doc

if __name__ == '__main__':
    main()
