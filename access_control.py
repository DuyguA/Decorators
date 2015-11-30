#!/usr/bin/python

class LoginCheck:
    '''
    This class checks whether a user
    has logged in properly via
    the global "check_function". If so,
    the requested routine is called.
    Otherwise, an alternative page is
    displayed via the global "alt_function"
    '''
    def __init__(self, f):
        self._f = f

    def __call__(self, *args):
        Status = check_function()
        if Status is 1:
            return self._f(*args)
        else:
            return alt_function()

def check_function():
    return test

def alt_function():
    return 'Sorry - this is the forced behaviour'

@LoginCheck
def display_members_page():
    print 'This is the members page'
