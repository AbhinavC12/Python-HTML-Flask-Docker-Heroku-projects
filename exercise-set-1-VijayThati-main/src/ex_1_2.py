"""
ex_1_2.py
"""
# The following import statement imports your get_username() function from ex_1_1.py
from . ex_1_1 import get_username
# DO NOT REMOVE OR EDIT THE LINE ABOVE


def last_user_login(x):
    """
    Your docstring here.  Note: replace the pass keyword below with your code.
    """
    username=get_username(x[2])
    last_login=x[3]
    ans=(username,last_login)
    return ans
