from categories import find_typeOfCategory
from db import getCurrentState, insertOneRefill, send_newOperation, getCurrentSourceBalance
from db import updateBalance, insertOutcameOP

from datetime import datetime
from datetime import date
from gsheets import insert_gsheet_refcard,insert_gsheet_outcame,insert_gsheet_salary




def typeOfOperation(newStr, operation):
    date_today = date.today()
    str_date = date_today.strftime("%d-%m-%Y")
    time_now1 = datetime.now()
    time_now = time_now1.strftime("%H:%M:%S")
    if operation == "+":
        refillData = {
            "operation": "refillCard",
            "SUM": newStr[1],
            "dest": newStr[2],
            "source": newStr[3],
            "Type": "Operations",
            "DATE": str_date,
            "TIME": time_now}

        state = getCurrentState(refillData["source"], refillData["dest"])

        # state[0] == dest_operation ;  state[1] == source
        result_for_source = float(state[1]["SUM"]) - float(refillData["SUM"])
        result_for_destination = float(state[0]["SUM"]) + float(refillData["SUM"])
        #DB insert operation
        insertOneRefill(refillData["source"], refillData["dest"], result_for_source, result_for_destination)
        #DB update balance
        new_state = getCurrentState(refillData["source"], refillData["dest"])
        #Inert operations to gsheet
        insert_gsheet_refcard(refillData)
        #Return respone
        str_response = f''' You have successfully added to the {refillData["dest"]} {refillData["SUM"]}. 
Your current balance on {new_state[0]["name"]} is: {new_state[0]["SUM"]} 
And on {new_state[1]["name"]}: {new_state[1]["SUM"]}'''
        send_newOperation(refillData)
        return str_response
    elif operation == "-":
        outcame_data = {
            "operation": "outcame",
            "sum": newStr[1],
            "category": find_typeOfCategory(newStr[2]),
            "money_source": newStr[3],
            "Type": "Operations",
            "DATE": str_date,
            "TIME": time_now
        }
        source_balance = getCurrentSourceBalance(outcame_data["money_source"])
        source_balance["SUM"] = float(source_balance["SUM"]) - float(outcame_data["sum"])

        # Update current balance:
        updateBalance(source_balance)

        # insert operations into Mongo DB:
        insertOutcameOP(outcame_data)

        # Insert data to the google sheet:
        insert_gsheet_outcame(outcame_data)

        # return response
        response = f'A new operation has been registered.\nOutcame category:{outcame_data["category"]}\nSUM: {outcame_data["sum"]}\nBalance on {outcame_data["money_source"]} is {source_balance["SUM"]}'


        return response

    elif operation.lower() == "salary":
        date_today = date.today()
        str_date = date_today.strftime("%d-%m-%Y")
        time_now1 = datetime.now()
        time_now = time_now1.strftime("%H:%M:%S")
        income_data = {
            "operation":"salary",
            "sum": newStr[1],
            "dest":newStr[2],
            "Type": "Operations",
            "DATE": str_date,
            "TIME": time_now

        }
        source_balance = getCurrentSourceBalance(income_data["dest"])
        source_balance["SUM"] = float(source_balance["SUM"]) + float(income_data["sum"])
        # Update current balance:
        updateBalance(source_balance)
        # insert operations into Mongo DB:
        insertOutcameOP(income_data)
        # Insert data to the google sheet:
        insert_gsheet_salary(income_data)
        # return response
        response = f'Your account {source_balance["name"]} has been recharged with {income_data["sum"]} MDL.\nCurrent balance is {source_balance["SUM"]} MDL'
        return response