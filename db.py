import pymongo
from pymongo import  MongoClient

from dotenv import load_dotenv
import os


load_dotenv()
cluster = MongoClient(f"{os.getenv('URL_MONG')}")
db = cluster["currencies"]
collection = db["moneywatcher"]


myData = {"_id":1,
          "name":"Test"
 }
collection.insert_one(
    myData
)


def getCurrentState():
    pass
def updateCurrentState():
    pass
def insertNewOperation():
    pass

