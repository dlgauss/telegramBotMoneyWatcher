import pymongo
from pymongo import  MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
cluster = MongoClient(f"{os.getenv('URL_MONG')}")

db = cluster["currencies"]
collection_categories = db["categories"]


def find_typeOfCategory(name):
    all_cat = collection_categories.find()
    prod_category = ''
    for i in all_cat:
        if name in i["Aliases"]:
            prod_category = i["Category Name"]
            break
        else :
            prod_category = "Other"
    return prod_category

        # else:
        #     print("Nu such category")
        # for j in i["Aliases"]:
        #     if j == name:
        #         print(i["Category name"])


