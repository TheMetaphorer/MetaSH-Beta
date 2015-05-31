#!/usr/bin/env python3
import os

def mkdir(*dirPath):
    if dirPath:
        for location in dirPath:
            if location[0] != '/':
                os.makedirs(os.path.join(os.getcwd(), location))
            elif location[0] == '/':
                os.makedirs(location)
    if len(dirPath) == 0:
        print("""\
        Usage: mkdir [path/to/dir]
        """)
def helpme():
    info = ("""\
    Usage: mkdir [path/to/dir]
    """)
    return info
if __name__ == '__main__':
    exit()
