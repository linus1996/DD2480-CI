import pkg_resources
pkg_resources.require("pymongo==4.1.1")
from pymongo import MongoClient
from urllib.parse import quote_plus

class History:
    def __init__(self, mongo_name,
                 mongo_ip,
                 mongo_port,
                 mongo_user,
                 mongo_pass):
        
        self.mongo_client = MongoClient("mongodb+srv://group17:dd2480group17@cluster0.undpmzo.mongodb.net/?retryWrites=true&w=majority")

        # self.mongo_client = MongoClient(
        #     # 'mongodo://group17:130.229.177.245/32'
        #     'mongodb+srv://%s:%s@%s:%s/%s' % 
        #         (
        #             mongo_user,
        #             mongo_pass,
        #             mongo_ip,
        #             mongo_port,
        #             mongo_name
        #             # quote_plus(mongo_user),
        #             # quote_plus(mongo_pass),
        #             # quote_plus(mongo_ip),
        #             # quote_plus(mongo_port),
        #             # quote_plus(mongo_name)
        #             )
        #     )

        self.db = self.mongo_client[mongo_name]

    def insert_build(self, document):
        builds = self.db['builds']
        builds.insert_one(document)

    def fetch(self, build_id):
        return self.db['builds'].find_one({"_id": float(build_id)})

    def fetch_n_last(self, n):
        nr_documents = self.db['builds'].count()
        if(nr_documents < n):
            return self.db['builds'].find()
        return self.db['builds'].find().skip(nr_documents - n)
    
    def fetch_all(self):
        return self.db['builds'].find()

    @staticmethod
    def serialize(build_id, date_rec, status, commit_url, stderr):
        return {
            "_id": build_id,
            "date": date_rec,
            "status": status,
            "url": commit_url,
            "message": stderr
            }