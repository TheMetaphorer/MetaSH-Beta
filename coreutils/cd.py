#!/usr/bin/env python3
import os
from coreutils import setvar

def cd(*dirPath):
    if dirPath:
        try:
            location = []
            location_ = dirPath[0].split('/')
            for item in location_:
                if item[0] == '@':
                    realVarName = item.replace('@', '')
                    item = item.replace(item, setvar.variables[realVarName])
                    print(item)
                    location.append(item)
                    location.append('/')
                else:
                    location.append(item)
                    location.append('/')
                    pass
            location = ''.join(location)
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
        except Exception as e:
            print('Unable to change to directory {0}: {1}'.format(location, e))
