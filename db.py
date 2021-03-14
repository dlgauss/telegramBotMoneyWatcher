import pymongo
from pymongo import  MongoClient
from datetime import datetime
from datetime import date
from dotenv import load_dotenv
import os



load_dotenv()
cluster = MongoClient(f"{os.getenv('URL_MONG')}")
db = cluster["currencies"]
collection_balance = db["balance"]
collection_opeartions = db["moneywatcher"]

date_today = date.today()
str_date = date_today.strftime("%d-%m-%Y")
time_now1 = datetime.now()
time_now = time_now1.strftime("%H:%M:%S")



def getCurrentState(source,dest):
    source_op = collection_balance.find_one({"name":source})
    dest_op = collection_balance.find_one({"name":dest})

    source_operation = {
        "name":source_op["name"],
        "SUM":source_op["SUM"]}

    dest_operation = {
        "name": dest_op["name"],
        "SUM": dest_op["SUM"]}

    return  dest_operation, source_operation,





def getListOfBalanceSources():
    name_sources = collection_balance.find()
    list_of_source = []
    for i in name_sources:
        list_of_source.append(i["name"])
    return list_of_source



def refillCardOperation():
    pass



def updateCurrentState():
    pass


def insertNewOperation():
    pass

def insertOneRefill(source_name,dest_name,result_for_source,result_for_destination):

    query_source = {"name":source_name}
    value_source = {"$set":{"SUM":result_for_source,"LAST TIME UPDATED":time_now,"LAST DATE UPDATED":str_date}}
    query_dest = {"name":dest_name}
    value_dest = {"$set":{"SUM":result_for_destination ,"LAST TIME UPDATED":time_now,"LAST DATE UPDATED":str_date}}
    collection_balance.update_one(query_source,value_source)
    collection_balance.update_one(query_dest, value_dest)

def send_newOperation(dataset):
    collection_opeartions.insert_one(dataset)

def getCurrentSourceBalance(name):
    source_name = collection_balance.find_one({"name":name})
    return source_name


def updateBalance(source_balance):
    query_source = {"name": source_balance["name"]}
    value_source = {"$set":{"SUM":source_balance["SUM"],"LAST TIME UPDATED":time_now,"LAST DATE UPDATED":str_date}}
    collection_balance.update_one(query_source,value_source)


def insertOutcameOP(outcameData):
    collection_opeartions.insert_one(outcameData)


def import_balance_from_db():
    balance = collection_balance.find()
    list_of_sources = []
    for i in balance:
        list_of_sources.append({
            "name":i["name"],
            "sum":i["SUM"]
        })

    return list_of_sources
    # micb_balance = {
    #     "name":
    # }
    # mobias_balance =
    # up_moldova balance =
    # cash_balance =


