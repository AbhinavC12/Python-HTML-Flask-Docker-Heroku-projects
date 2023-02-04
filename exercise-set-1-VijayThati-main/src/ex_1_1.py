"""
ex_1_1.py
"""


def get_username(email: str):
    """Your docstring here.  Note: replace pass below with your code."""
    if '@' in email:
        if email[0]=="@" or email[-1]=='@':
            return None
        return email.split('@')[0].lower()
    return None

