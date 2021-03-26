
import re
from utils import typeOfOperation
from db import import_balance_from_db
def parseText(text):
    newStr = text.split(' ')
    operation =  newStr[0]

    if len(newStr[0]) > 1 and newStr[0] != 'salary':
        if len(newStr) == 3:
            symbl = re.split('(\d+)', newStr[0])

            new_var_def = [symbl[0], symbl[1], newStr[1], newStr[2]]
            answer = typeOfOperation(new_var_def, new_var_def[0])
        return answer

    else:
        answer = typeOfOperation(newStr, operation)
        return answer


def get_current_balance():
    balance = import_balance_from_db()
    return balance


