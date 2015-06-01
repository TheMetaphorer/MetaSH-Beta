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
                filename = string[tokenIndex + 1]
                newString = string[:tokenIndex]
        outputToFile = True
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
                if realVarName in setvar.variables:
                    item = item.replace(item, str(setvar.variables[realVarName]))
                else:
                    item = item.replace(item, '')
                nonQuotedString.append(item)
                pass
            else:
                nonQuotedString.append(item)
        print(' '.join(nonQuotedString))
        return ' '.join(nonQuotedString)
    if outputToFile:
        try:
            with open(filename, 'w') as f:
                if newString[0][0] == '"':
                    if newString[len(newString)-1][len(newString[len(newString)-1]) - 1] == '"':
                        quotedString = ' '.join(args)
                        print(quotedString)
                        return quotedString
                if newString[0][0] == "'":
                    if newString[len(string)-1][len(newString[len(newString)-1]) - 1] == "'":
                        quotedString = ' '.join(args)
                        f.write(quotedString)
                        f.close()
                        return quotedString
                nonQuotedString = []
                for item in newString:
                    if item[0] == '@':
                        realVarName = item.replace('@', '')
                        if realVarName in setvar.variables:
                            item = item.replace(item, str(setvar.variables[realVarName]))
                        else:
                            item = item.replace(item, '')
                        nonQuotedString.append(item)
                        pass
                    else:
                        nonQuotedString.append(item)
                f.write(' '.join(nonQuotedString))
                f.close()
            return ' '.join(nonQuotedString)
        except IOError as e:
            print('Write failed: ' + str(e))
