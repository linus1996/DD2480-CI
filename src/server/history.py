from pymongo import MongoClient

class History:
    def __init__(self, mongo_name,
                 mongo_ip,
                 mongo_port,
                 mongo_user,
                 mongo_pass):

        self.mongo_client = MongoClient(
            'mongodb://%s:%s@%s:%s/%s' % (mongo_user,
                                          mongo_pass,
                                          mongo_ip,
                                          mongo_port,
                                          mongo_name))

        self.db = self.mongo_client[mongo_name]

    def insert_build(self, document):
        builds = self.db['builds']
        builds.insert_one(document)

    def fetch(self, build_id):
        return self.db['builds'].find_one({"buildID": float(build_id)})

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
            "ID": build_id,
            "date": date_rec,
            "status": status,
            "url": commit_url,
            "message": stderr
            }