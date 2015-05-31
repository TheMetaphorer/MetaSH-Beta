#!/usr/bin/env python3
import os
from coreutils import setvar

def echo(*args):
    string = list(args)
    outputToFile = False
    if ">>" in string:
        for item in string:
            if item == ">>":
                tokenIndex = string.index(item)
                newString = string[tokenIndex - 1:]
    if not outputToFile:
        if string[0][0] == '"':
            if string[len(string)-1][len(string[len(string)-1]) - 1] == '"':
                quotedString = ' '.join(args)
                print(quotedString)
                return quotedString
        if string[0][0] == "'":
            if string[len(string)-1][len(string[len(string)-1]) - 1] == "'":
                quotedString = ' '.join(args)
                print(quotedString)
                return quotedString
        nonQuotedString = []
        for item in string:
            if item[0] == '@':
                realVarName = item.replace('@', '')
                item = item.replace(item, str(setvar.variables[realVarName]))
                nonQuotedString.append(item)
                pass
            else:
                nonQuotedString.append(item)
        print(' '.join(nonQuotedString))
        return ' '.join(nonQuotedString)
