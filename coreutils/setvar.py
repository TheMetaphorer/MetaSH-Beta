#!/usr/bin/env python3
import os
import getpass
import datetime
import sys
from decimal import Decimal
variables = {'platform' : sys.platform, 'user' : getpass.getuser(),
 'executableDirectory' : os.path.dirname(os.path.abspath(__file__)),
  'date' : datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"),
  'home' : os.path.expanduser('~')
 }

def setvar(*varInfo):
    if varInfo and len(varInfo) == 3:
        name = varInfo[0]
        value = varInfo[2]
        if value.isdigit() == False and value.isalpha() == False:
            variables[name] = Decimal(value)
        elif value.isdigit() == False and value.isalpha() == True:
            variables[name] = str(value)
        elif value.isdigit() == True:
            variables[name] = int(value)
    else:
        print("""\
        Usage: setvar [name] = [value]
        It automatically be determined whether this variable
        is a string, integer, or a floating point number""")
