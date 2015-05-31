#!/usr/bin/env python3
import os

def cd(*dirPath):
    if dirPath:
        location = dirPath[0]
        if location[0] == '/':
            os.chdir(location)
        elif location[0] != '/':
            os.chdir(os.path.join(os.getcwd(), '/{}'.format(location)))
    helpme()

def helpme():
    info = ("""\
    Usage: cd [directory]
    This will not work if the
    directory does not exist.
    """)
    return info
