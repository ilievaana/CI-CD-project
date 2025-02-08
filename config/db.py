import os

from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017/mydatabase")
conn = MongoClient(mongo_uri)

db = conn["mydatabase"]

customer_collection = db["customer"]
article_collection = db["article"]
category_collection = db["category"]

try:
    conn.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)