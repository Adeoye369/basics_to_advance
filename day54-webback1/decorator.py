# Python decorator function

# A decorator function takes in a main function,
# calls with from its wrapper funciton then
# returns its wrapped function
import time

def deco_func(main_func):
    def _func():
        # do any operation on main function
        time.sleep(2)
        print(main_func() * 3)

    return _func


@deco_func
def hello_world():
    return "Ghello Deco!\n"

@deco_func
def ghello_you():
    return "ghello Python\n"

hello_world()
ghello_you()