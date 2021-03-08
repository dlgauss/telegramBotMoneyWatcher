from db import getCurrentState, insertNewOperation, updateCurrentState

def parseText(text):
    newStr = text.split(' ')
    operation =  newStr[0]
    if operation == "+":
        operation = "refillCard"
        value = newStr[1]
        dest = newStr[2]
        source = newStr[3]

        refillOperation(operation,value,dest,source)

    elif operation == "-":
        operation = "costs"
        sum_value = newStr[1]
        category = newStr[2]
        money_source = newStr[3]

        costsOperation(operation, sum_value, category, money_source)



def refillOperation(operation,value,dest,source):
    getCurrentState()
    updateCurrentState()
    insertNewOperation()
    pass



def  costsOperation(operation, sum_value, category, money_source):
    getCurrentState()
    updateCurrentState()
    insertNewOperation()
    pass