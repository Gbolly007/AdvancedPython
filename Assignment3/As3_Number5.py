from reflect import reflect


@reflect
def myfunction():
    print("nothing\nuseful")


myfunction()
reflect = reflect(reflect)
reflect(reflect)
