import pymongo
import json

from flask import Flask
from flask.ext import restful
from bson import json_util

app = Flask(__name__)
api = restful.Api(app)

class Gosugamersapi(restful.Resource):
    def get(self, test):
        connection = pymongo.MongoClient('localhost', 27017)
        collection = connection['gosugamers']['matches']
        results = collection.find({"game": test}).sort([("time", 1)])
        
        matches = []
        for item in results:
            del item['_id']
            matches.append(item)
        
        return matches
    
api.add_resource(Gosugamersapi, '/<string:test>')

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=8080)
