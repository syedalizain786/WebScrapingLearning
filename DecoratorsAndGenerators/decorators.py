#Decorators in Python
#it allows programmers to modify the behaviour of a function or class.
# Decorators allow us to wrap another function in order to
# extend the behaviour of the wrapped function,
# without permanently modifying it.


def div(a, b):
    print(a / b)

#We always want the bigger element to be numerator and
# we don't want to change internal logic of div func
div(2, 4)


#So python introduced here Decorators

def new_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner

@new_div
def div(a, b):
    print(a / b)

div(2,4)

