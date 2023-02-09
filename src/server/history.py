import pkg_resources
pkg_resources.require("pymongo==4.1.1")
from pymongo import MongoClient
from urllib.parse import quote

class History:
    """
    A class for handling fetching and storing of build history in a MongoDB database.
    """

    def __init__(self, mongo_name, mongo_url):
        """
        A method for initiating contact with the database.
        Input: database name and API url.
        """ 
        
        self.mongo_client = MongoClient(mongo_url)

        self.db = self.mongo_client[mongo_name]


    def insert_build(self, document):
        """
        A method for inserting build information in the database.
        Input: serialized build information.
        """
        builds = self.db['builds']
        builds.insert_one(document)

    def fetch(self, id):
        """
        A method for retrieving build information about a particular build.
        Input: build ID, which is the identifier.
        """
        return self.db['builds'].find_one({"_id": id})


    def fetch_n_last(self, n):
        """
        A method for fetching the last n builds information.
        Input: n, which is the number of builds which information is to be fetched.
        """
        nr_documents = self.db['builds'].count()
        if(nr_documents < n):
            return self.db['builds'].find()
        return self.db['builds'].find().skip(nr_documents - n)
    

    def fetch_all(self):
        """
        A method for fetching information of all the builds in the database.
        """
        return self.db['builds'].find()


    @staticmethod
    def serialize(id, date, status, commit_url, stderr):
        """
        A method for serializeing build information to prepare it for database insertion.
        Input: id of build, date of commit, CI status, url of commit and error message.
        """
        return {
            "_id": id,
            "date": date,
            "status": status,
            "url": commit_url,
            "message": stderr
            }