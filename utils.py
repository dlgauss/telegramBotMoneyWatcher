from categories import find_typeOfCategory
from db import getCurrentState, insertOneRefill, send_newOperation, getCurrentSourceBalance
from db import updateBalance, insertOutcameOP

from datetime import datetime
from datetime import date

date_today = date.today()
str_date = date_today.strftime("%d-%m-%Y")
time_now1 = datetime.now()
time_now = time_now1.strftime("%H:%M:%S")


def typeOfOperation(newStr, operation):
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
        insertOneRefill(refillData["source"], refillData["dest"], result_for_source, result_for_destination)
        new_state = getCurrentState(refillData["source"], refillData["dest"])
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
            "DATE": str_date,
            "TIME": time_now
        }
        source_balance = getCurrentSourceBalance(outcame_data["money_source"])
        source_balance["SUM"] = float(source_balance["SUM"]) - float(outcame_data["sum"])
        updateBalance(source_balance)
        insertOutcameOP(outcame_data)
        response = f'A new operation has been registered.\nOutcame category:{outcame_data["category"]}\nSUM: {outcame_data["sum"]}\nBalance on {outcame_data["money_source"]} is {source_balance["SUM"]}'
        return response

    elif operation.lower() == "salary":
        income_data = {
            "operation":"salary",
            "sum": newStr[1],
            "dest":newStr[2],
            "DATE": str_date,
            "TIME": time_now

        }
        source_balance = getCurrentSourceBalance(income_data["dest"])
        source_balance["SUM"] = float(source_balance["SUM"]) + float(income_data["sum"])
        updateBalance(source_balance)
        insertOutcameOP(income_data)
        response = f'Your account {source_balance["name"]} has been recharged with {income_data["sum"]} MDL.\nCurrent balance is {source_balance["SUM"]} MDL'
        return response