#!/usr/bin/env python3
import os
import math
from coreutils import setvar

def listdir(*dirPath):
    if dirPath:
        if dirPath[0][0] == '@':
            try:
                newDirPath = dirPath[0].replace(dirPath[0], setvar.variables[dirPath[0].replace('@', '')])
            except KeyError:
                return
        else:
            newDirPath = dirPath[0]
        try:
            directoryContents = os.listdir(newDirPath)
            for item in directoryContents:
                print(item)
        except FileNotFoundError:
            print('Directory ' + newDirPath + ' not found.')
        except PermissionError:
            print('You don\'t have permission to directory {}'.format(newDirPath))
    elif not dirPath:
        for item in os.listdir(os.getcwd()):
            print(item)
