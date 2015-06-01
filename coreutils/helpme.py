#!/usr/bin/env python3
import os
from coreutils import setvar

def helpme(*command):
    if command and len(command) == 1:
        filename = command[0]
        docPath = os.path.join(setvar.variables['executableDir'], 'MetaSH-Beta.wiki')
        try:
            with open('{0}/{1}.md'.format(docPath, filename), 'r') as f:
                for line in f.readlines():
                    print(line)
        except IOError:
            print('No documentation for ' + filename + ' was found. Either there '
            'is no such command ' + filename + ', or there is no documentation for it '
            'in this version of the shell.')
    else:
        print('This is the helpme command! To use it, simply enter `helpme [command]` \n'
        'The shell will then print information on the command you are looking for\n. If '
        ' you ever need information about anything, refer to this command.')
