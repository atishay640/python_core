
'''
Assigning function to another function

'''
def function1():
    print('i am function1')


def function2(anyfunction):
    anyfunction()
    print('i am function2')


function2(function1)

print('-----------------------------------')
'''
returning function from a function
'''

def function3():
    print('i am function3')
    return function1

new_function = function3()
new_function()

print('-----------------------------------')

'''
creating function inside a function
'''

def outer_func():
    print('i am outer function')

    def inner_func():
        print('i am inner function')

    inner_func()

outer_func()

print('-----------------------------------')

'''
creating a function takes another function as aurgument (internal structure follow by decorator)
'''

def my_decorator(any_function):
    print('some code')
    any_function()
    print('some code ends')

def func_istobe_wrapped():
    print('please decorate me...')

my_decorator(func_istobe_wrapped)

print('----------------decorator-------------------')

'''
use of decorator with @ annotation 
'''
def my_decorator(any_function):
    print('some code')
    any_function()
    print('some code ends')

@my_decorator
def func_istobe_wrapped():
    print('please decorate me...')


