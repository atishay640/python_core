# use of name variable

from module_to_be_import import func3

print('call function at indentation level 0')


def func1():
    print('Inside func1')

def func2():
    print('Inside func2')

if __name__ == '__main__':
    print("When file exceute __name__ variable initialized by value = '__main__' ")
    func1()
    func2()
    func3()


