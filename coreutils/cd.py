#!/usr/bin/env python3
import os

def cd(*dirPath):
    if dirPath:
        try:
            location = dirPath[0]
            if location[0] == '/':
                os.chdir(location)
            elif location[0] != '/':
                os.chdir(os.path.join(os.getcwd(), location))
        except FileNotFoundError:
            print('Directory {} not found.'.format(location))
        except NotADirectoryError:
            print('{} is not a directory.'.format(location))
        except PermissionError:
            print('You don\'t have permission to directory {}'.format(location))
    helpme()

def helpme():
    info = ("""\
    Usage: cd [directory]
    This will not work if the
    directory does not exist.
    """)
    return info
