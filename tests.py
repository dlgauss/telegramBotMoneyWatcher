import re

new_var = str.split()
if len(new_var[0]) > 1:
    if len(new_var) == 3:
        symbl = re.split('(\d+)', new_var[0])

        new_var_def = [symbl[0], symbl[1], new_var[1], new_var[2]]


# if  len(new_var) == 4:
#     if new_var[0].startswith("+") | new_var[0].startswith("-") and:
#         print('Everythin is ok')
#
# else:
#     if new_var[0].startswith("+") | new_var[0].startswith("-"):
#         symbl = re.split('(\d+)',new_var[0])
#         print(symbl)
#         new_var_def = [symbl[0], symbl[1], new_var[1], new_var[2]]
#         print(new_var_def)
#     else:
#         print("Something was worng. Please try again")