from db import getCurrentState, insertNewOperation, updateCurrentState

from utils import typeOfOperation
def parseText(text):
    newStr = text.split(' ')
    operation =  newStr[0]
    answer = typeOfOperation(newStr,operation)
    return answer




#
# def refillOperation(operation,value,dest,source):
#     getCurrentState()
#     updateCurrentState()
#     insertNewOperation()
#     pass
#
#
#
# def  costsOperation(operation, sum_value, category, money_source):
#     getCurrentState()
#     updateCurrentState()
#     insertNewOperation()
#     pass