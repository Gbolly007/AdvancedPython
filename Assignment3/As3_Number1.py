# Python version 3.7.6
import inspect


def reflect(func):
    '''This method takes in a function as arguments'''
    '''passes to the function below which reads the content'''
    '''of the function argument and prints out the content'''
    def helper():
        lines = inspect.getsource(func)
        print(lines)
    return helper


@reflect
def foo():
    print("bar")


if __name__ == '__main__':
    foo()
