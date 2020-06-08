# Python version 3.7.6
import uncompyle6
import os
import dis
import marshal
import types

# Method to generate bytecode for python script


def bytecodepy():
    # Input to receive python script from user
    source_py = input('Enter file! ')
# Condition to determine if the particular file
# in the loop is valid a python file by checking the last 3 characters
    if source_py[-3:] != '.py':
        print('Not a valid python file')
        exit()

    try:
     # python script is read and stored in variable
        with open(source_py) as f_source:
            source_code = f_source.read()
# method to compile python script and execute
        byte_code = compile(source_code, source_py, "exec")
 # Bytecode for the script is generated and printed  by passing the compiled code to the function
        print(dis.Bytecode(byte_code).dis())

    except IOError:
        print('File not accessible!')

# Method to generate bytecode for pyc file


def bytecodepyc():
    # Input to receive pyc file from user
    source_py = input('Enter file ')
# Condition to determine if the particular file
# in the loop is valid a python file by checking the last 4 characters
    if source_py[-4:] != '.pyc':
        print('Not a valid pyc file')
        exit()

    try:
        # pyc file is read and stored in variable, bytecode is generated and printed
        with open(source_py, 'rb') as f:
            f.seek(16)
            print(dis.Bytecode(marshal.load(f)).dis())
    except IOError:
        print('File not accessible!')

# Method to generate bytecode for code snippet


def bytecodesnippet():
    source_py = input('Enter code snippet! ')
    print(dis.Bytecode(source_py).dis())


# Input to determine if users wants to generate
# bytecode for python script, or
# pyc file or code snippet
accInput = input(
    'Press 1 to get bytecode for py file, Press 2 for pyc file and Press 3 for code snippet ')

# If user enter 1 the method bytecodepy() is called
if accInput == '1':
    bytecodepy()
# If user enter 2 the method bytecodepyc() is called
elif accInput == '2':
    bytecodepyc()
# If user enter 3 the method bytecodesnippet() is called
elif accInput == '3':
    bytecodesnippet()
# If user provides invalid input, program throws error
else:
    print('Wrong input, try again with valid input')
    exit()
