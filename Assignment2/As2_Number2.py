# Python version 3.7.6
import types
import dis

# Method to generate bytecodes for python scripts


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
# Bytecode for that script is generated by passing the compiled code to the function
        print(dis.Bytecode(byte_code).dis())

    except IOError:
        print('File not accessible!')


# call to the method
bytecodepy()