# Python version 3.7.6
from reflect import reflect


@reflect
def myfunction():
    print("nothing\nuseful")


myfunction()
reflect = reflect(reflect)
reflect(reflect)
