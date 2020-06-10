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

        table = [["Name:", func.__name__], ['Type:', str(type(func))], [
            'Sign:', str(sig)], ['Args:', str({
                k: v.default
                for k, v in sig.parameters.items()
                if v.default is not inspect.Parameter.empty
            })], ['Doc:', inspect.getdoc(func)], ['Source:', lines], ['Output:', f.getvalue()]]
        print()
        print(tabulate(table))

    return helper


@reflect
def foo(bar1, bar2=""):
    """This function does nothing useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


if __name__ == "__main__":
    foo(None, bar2="")
    # The decorator cannot invoke itself because the decorator method has not been initialized
    # on calling the decorator on it
    reflect = reflect(reflect)
    reflect(reflect)
