# Python version 3.7.6
import uncompyle6
import os
import dis
import marshal
import types
import py_compile


def only_upper(s):
    return "".join(c for c in s if c.isupper())

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

# If user wants to compare bytecode this method is triggered


def comparebyte():
    # Input to determine if users wants to compare
    # pyc fil, python script or code snippet
    accInput = input(
        'Press 1 to compare py file, Press 2 to compare pyc file and Press 3 to compare code snippet ')
# If user enter 1 the method comparepy() is called
    if accInput == '1':
        comparepy()
# If user enter 2 the method comparepyc() is called
    elif accInput == '2':
        comparepyc()
# If user enter 3 the method comparecodesnippet() is called
    elif accInput == '3':
        comparecodesnippet()
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

# Method to compare bytecode for python script


def comparepy():
    # Input to receive files from user
    command = input('Enter the python scripts seperated by a comma ')
# files are splitted into an array using comma
    com = command.split(',')
# for loop to generate bytecode for each file
    for c in com:
        # Condition to determine if the particular file
        # in the loop is valid a python file by checking the last 3 characters
        if c[-3:] != '.py':
            print('Not a valid py file')
            exit()
        try:
            # python script is read and stored in variable
            with open(c) as f_source:
                source_code = f_source.read()
# method to compile python script and execute
            byte_code = compile(source_code, c, "exec")
# storing the result of the bytecode
            s = dis.Bytecode(byte_code).dis()
#array is created
            arr = []
# loop to get bytecode instruction and store them in array
            for line in s.split('\n'):
                arr.append(only_upper(line))
            i = 0
# removing empty space from the array
            for empt in arr:
                if len(empt) == 0:
                    arr.pop(i)
                i += 1
# deriving filename
            getfilename = os.path.basename(
                c)
# dictionary is created to store the occurrence of each instruction
            dt = dict((x, arr.count(x)) for x in set(arr))
# details of byte instruction for each file is printed
            result = "| ".join(str(key) + ' ' + str(value)
                               for key, value in dt.items())
            print(
                '----------------------------------------------------------------------------------')
            print(getfilename+' |' + ' '+result)
            print(
                '----------------------------------------------------------------------------------')
        except IOError:
            print('File not accessible!')

# Method to compare bytecode for pyc file


def comparepyc():
   # Input to receive files from user
    command = input('Enter the pyc file seperated by a comma ')
# files are splitted into an array using comma
    com = command.split(',')
# for loop to generate bytecode for each file
    for c in com:
     # Condition to determine if the particular file
        # in the loop is valid a pyc file by checking the last 4 characters
        if c[-4:] != '.pyc':
            print('Not a valid pyc file')
            exit()
        try:
            # pyc file is read and stored in variable, bytecode is generated and stored
            with open(c, 'rb') as f:
                f.seek(16)
                s = dis.Bytecode(marshal.load(f)).dis()
#array is created
            arr = []
# loop to get bytecode instruction and store them in array
            for line in s.split('\n'):
                arr.append(only_upper(line))
            i = 0
# removing empty space from the array
            for empt in arr:
                if len(empt) == 0:
                    arr.pop(i)
                i += 1
# deriving filename
            getfilename = os.path.basename(
                c)
# dictionary is created to store the occurrence of each instruction
            dt = dict((x, arr.count(x)) for x in set(arr))
            result = "| ".join(str(key) + ' ' + str(value)
                               for key, value in dt.items())
# details of byte instruction for each file is printed
            print(
                '----------------------------------------------------------------------------------')
            print(getfilename+' |' + ' '+result)
            print(
                '----------------------------------------------------------------------------------')

        except IOError:
            print('File not accessible!')

# Method to compare bytecode for code snippet


def comparecodesnippet():
    # Input to receive code snippet from user
    command = input('Enter code snippet seperated by comma!')
# files are splitted into an array using comma
    com = command.split(',')
# for loop to generate bytecode for each file
    for c in com:
        #bytecode is generated and stored
        s = dis.Bytecode(c).dis()
#array is created
        arr = []
# loop to get bytecode instruction and store them in arr
        for line in s.split('\n'):
            arr.append(only_upper(line))
        i = 0
# removing empty space from the array
        for empt in arr:
            if len(empt) == 0:
                arr.pop(i)
            i += 1
# dictionary is created to store the occurrence of each instruction
        dt = dict((x, arr.count(x)) for x in set(arr))
        result = "| ".join(str(key) + ' ' + str(value)
                           for key, value in dt.items())
# details of byte instruction for each file is printed
        print('----------------------------------------------------------------------------------')
        print(c + ' |' + ' '+result)
        print('----------------------------------------------------------------------------------')


# Input to determine if users wants to generate
# bytecode or generate pyc file or compare bytecode
comorprint = input(
    'Enter C to compile or B to get bytecode or CO to compare bytecode')
# If user enters B the method bytecod() is called
if comorprint == 'B':
    bytecod()
# If user enters C the method bytecod() is called
elif comorprint == 'C':
    compiles()
 # If user enters CO the method comparebyte() is called
elif comorprint == 'CO':
    comparebyte()
# If user provides invalid input, program throws error
else:
    print('Invalid selection')
    exit()
