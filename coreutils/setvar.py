#!/usr/bin/env python3
import os
import getpass
import datetime
import sys
from decimal import Decimal
import coreutils
variables = {'platform' : sys.platform, 'user' : getpass.getuser(),
 'executableDirectory' : os.path.dirname(os.path.abspath(__file__)),
  'date' : datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"),
  'home' : os.path.expanduser('~'),
  'executableDir' : os.path.dirname(coreutils.__file__).replace('coreutils', '')
 }

def setvar(*varInfo):
    if varInfo and len(varInfo) == 3:
        name = varInfo[0]
        value = varInfo[2]
        if value.isdigit() == True:
            try:
                variables[name] = Decimal(value)
            except:
                return False
        else:
            variables[name] = str(value)


    else:
        print("""\
        Usage: setvar [name] = [value]
        It automatically be determined whether this variable
        is a string, integer, or a floating point number""")
