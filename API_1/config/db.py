from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>.@cluster0.glypb4r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection = db["todo_collection"]
