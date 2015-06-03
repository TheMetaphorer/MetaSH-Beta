# echo #

The echo command is the basic text manipulation command of the shell. It
allows you to write text out to files, or, you can print them to the console.
It also allows you to print variables to the console, and you can write
variables out to the console too. Here's how you use it:

`echo [text] >> [filename]`

Now, there's several important things to note about this command. The first is
that you don't always have to write out text to a file, so if you just want to
print something to the console, you can simply input

`echo [text]`

This also supports printing out variables. As noted in the documentation for
the setvar command, if you want to print out a variable, simply do

`echo @variablename`

Now, you can escape echoing the variable, and literally echo "@variablename" by
enclosing your text in quotes:

`echo "@variablename"`

Now, if you want to write information out to a file, you can simply do the command
noted above. However, if the file you are trying to write to already exists, then
an IOError will be raised.
