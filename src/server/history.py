from pymongo import MongoClient

"""
    A class for handling fetching and storing of build history in a MongoDB database.
"""
class History:

    """
     A method for initiate contact with the database.
     Input: database name, database ip, database port, username and password.
    """
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

    """
    A method for inserting build information in the database.
    Input: serialized build information.
    """
    def insert_build(self, document):
        builds = self.db['builds']
        builds.insert_one(document)

    """
    A method for fetching a specific builds information.
    Input: id of the build that is needed.
    """
    def fetch(self, build_id):
        return self.db['builds'].find_one({"buildID": float(build_id)})

    """
    A method for fetching the last n builds information.
    Input: the amount n of builds which information is needed.
    """
    def fetch_n_last(self, n):
        nr_documents = self.db['builds'].count()
        if(nr_documents < n):
            return self.db['builds'].find()
        return self.db['builds'].find().skip(nr_documents - n)
    
    """
    A method for fetching information of all the builds in the database.
    """
    def fetch_all(self):
        return self.db['builds'].find()

    """
    A method for serializeing build information to prepare it for database insertion.
    Input: id of build, date of commit, CI status, url of commit and error message.
    """
    @staticmethod
    def serialize(build_id, date_rec, status, commit_url, stderr):
        return {
            "ID": build_id,
            "date": date_rec,
            "status": status,
            "url": commit_url,
            "message": stderr
            }