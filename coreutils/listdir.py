#!/usr/bin/env python3
import os
import math

def listdir(*dirPath):
    if dirPath:
        directoryContents = os.listdir(dirPath[0])
        for item in directoryContents:
            print(item)
    elif not dirPath:
        for item in os.listdir(os.getcwd()):
            print(item)

if __name__ == '__main__':
    exit()
