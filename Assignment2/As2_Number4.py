# Python version 3.7.6
import uncompyle6
import os
import dis
import marshal
import types
import py_compile

# If user wants to generate bytecode this method is triggered


def bytecod():
    # Input to determine if users wants to generate
    # bytecode for python script or pyc file or code snippet
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

# If user wants to generate pyc file this method is triggered


def compiles():
    # Input to determine if users wants to generate
    # pyc file for python script or code snippet
    accInput = input(
        'Press 1 to compile py file, Press 2 to compile code snippet ')
# If user enter 1 the method compilepy() is called
    if accInput == '1':
        compilepy()
# If user enter 2 the method compilecodesnippet() is called
    elif accInput == '2':
        compilecodesnippet()
# If user provides invalid input, program throws error
    else:
        print('Wrong input, try again with valid input')
        exit()

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
    # Input to receive code snippet from user
    source_py = input('Enter code snippet!')
    # Method to generate bytecode
    print(dis.Bytecode(source_py).dis())

# Method to generate pyc file for python script


def compilepy():
   # Input to receive python file from user
    fileloc = input('Enter file name ')
# Condition to determine if the particular file
# in the loop is valid a python file by
# checking the last 3 characters
    if fileloc[-3:] != '.py':
        print('Not a valid python file')
        exit()

    try:
        # opening and closing file
        f = open(fileloc)
        f.close()
# method to generate pyc file for python script
        py_compile.compile(fileloc)
# getting directory of the python file that was provided
        path = os.path.dirname(
            fileloc)
# getting file name of the file that was provided
        getfilename = os.path.basename(
            fileloc)
# removing the .py extension from the filename
        getfilename = getfilename[:-3]
# appending the directory name to the __pycache__ to get to the pyc file that was generated
        path = os.path.join(path, '__pycache__')
# looping over files in that directory to look for the pyc file that was just generated
        for file in os.listdir(path):
            # condition to check if the newly created pyc file exists in that folder
            if file.startswith(getfilename):
                # renaming the pyc file to the one specified
                newname = 'file'+file[-4:]
                os.rename(os.path.join(path, file),
                          os.path.join(path, newname))

    except FileNotFoundError:
        print('File does not exist')

# Method to generate pyc file for code snippet


def compilecodesnippet():
    # Input to receive code snippet from user
    codesnip = input('Enter Code Snippet ')
# Name is assigned for new python file
    filename = 'myshell.py'
# File is created and opened in the current working directory
# Code snippet from user is written to file and file is closed
    f = open(filename, "w+")
    f.write(codesnip)
    f.close()
# method to generate pyc file for python script
    py_compile.compile('myshell.py')
# method to get current working directory
    path = os.getcwd()
# appending the directory name to the __pycache__ to get to the pyc file that was generated
    path = os.path.join(path, '__pycache__')
# file name is derived
    getfilename = os.path.basename(
        filename)
# removing the .py extension from the filename
    getfilename = getfilename[:-3]
# looping over files in that directory to look for the pyc file that was just generated
    for file in os.listdir(path):
        # condition to check if the newly created pyc file exists in that folder
        if file.startswith(getfilename):
            # renaming the pyc file to the one specified
            newname = 'out'+file[-4:]
            os.rename(os.path.join(path, file),
                      os.path.join(path, newname))
# Method to remove python file that was created
    os.remove(filename)


# Input to determine if users wants to generate
# bytecode or generate pyc file
comorprint = input('Enter C to compile or B to get bytecode ')
# If user enters B the method bytecod() is called
if comorprint == 'B':
    bytecod()
# If user enters C the method bytecod() is called
elif comorprint == 'C':
    compiles()
# If user provides invalid input, program throws error
else:
    print('Invalid selection')
    exit()
