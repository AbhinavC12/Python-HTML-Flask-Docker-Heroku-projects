"""
ex_1_3.py
"""
# The following import statement imports your last_user_login function from ex_1_2.py
from . ex_1_2 import last_user_login
# DO NOT REMOVE OR EDIT THE LINE ABOVE


#this code
def last_logins(nested): #input a nested list
    """ Takes input a nested list and returns a Dictionary
        with key as name
        value as last login date"""
    output=dict()
    for i in nested: #outer loop outer iterations
        output[get_username(i[2])]=last_user_login(i)[1]

    return output
