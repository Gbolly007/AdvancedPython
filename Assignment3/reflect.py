import inspect
from inspect import signature
from tabulate import tabulate
import sys
import io
from contextlib import redirect_stdout


def reflect(func):
    '''This method takes in a function as arguments
    passes to the function below which reads the content
    of the function argument and prints out the content
    '''
    def helper(*args, **kwargs):
        lines = inspect.getsource(func)
        sig = signature(func)
        f = io.StringIO()
        with redirect_stdout(f):
            str(func(*args, **kwargs))

        i = 0
        for line in lines.split('\n'):
            if 'print(' in line:
                i += 1
        i -= 1
        i = str(i)
        compl = '{print: ' + i + '}'

        table = [["Name:", func.__name__], ['Type:', str(type(func))], [
            'Sign:', str(sig)], ['Args:', str({
                k: v.default
                for k, v in sig.parameters.items()
                if v.default is not inspect.Parameter.empty
            })], ['Doc:', inspect.getdoc(func)], ['Complx:', compl],  ['Source:', lines], ['Output:', f.getvalue()]]
        print(tabulate(table))

    return helper

