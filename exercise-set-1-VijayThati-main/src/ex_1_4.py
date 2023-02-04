"""
ex_1_4.py
"""


def get_username(email):
    """
    Your docstring here.  Note: replace the pass keyword below with your code.
    """
    if type('str')!=type(email):
        raise TypeError
    elif '@'==email[0] or '@'==email[-1]:
        raise ValueError
    elif '@' not in email:
        raise ValueError
    else:
        return email.split('@')[0].lower()
