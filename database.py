import pymongo


class DB:
    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb+srv://dropex777:oM6JF2dJvSPs8r0B@cluster0-iipk4.mongodb.net/test?retryWrites=true&w=majority")

    def addPost(self, id, request):
        db = self.client.users
        collection = db.requests
        post = {"userID": id, "Запрос": request}
        db.requests.insert_one(post)
